"""Native adapter runtime controls; real service acceptance uses its named recipe."""
from __future__ import annotations

import copy
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from dataclasses import asdict
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "infra"))
from agentinfra.atomic import atomic_write_json
from agentinfra.process import run_process
from agentinfra.roadmap_codex import CodexReader, CodexRpcError, bind_goal
from agentinfra.roadmap_lease import WorkspaceLease
from agentinfra.roadmap_native import process_handle
from agentinfra.roadmap_native_adapter import NativeEventState, NativeGoalAdapter, NativeRpc, observe_goal, observe_plan
from agentinfra.roadmap_project import ProjectAdapter
from agentinfra.roadmap_protocol import REQUIRED_SCHEMAS, assert_protocol, export_manifest
from agentinfra.roadmap_records import ContractError, digest, file_binding, read_json
from agentinfra.roadmap_runtime import BudgetLedger
from agentinfra.roadmap_verification import reconcile_native_transition
from agentinfra.roadmap_work import selected_work_milestones


class ReplyClient:
    def __init__(self, reply):
        self.reply = reply
        self.calls = []
        self.events = []
        self.initialization = {}

    def call(self, method, params):
        self.calls.append((method, params))
        if isinstance(self.reply, Exception):
            raise self.reply
        return copy.deepcopy(self.reply)

    def __enter__(self): return self
    def __exit__(self, *_): pass
    def watch(self, *_): pass


class PlanRpc:
    def __init__(self, root, text):
        self.root = root
        self.item = {"type": "plan", "id": "P", "text": text}
        self.turn_status = "completed"
        self.entry_turn = "T"

    def turns(self, _): return [{"id": "T", "status": self.turn_status}]
    def call(self, method, _):
        if method == "thread/read": return {"thread": {"id": "source", "cwd": str(self.root)}}
        return {"data": [{"turnId": self.entry_turn, "item": self.item}], "nextCursor": None}


class NativeAdapterTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        shared = self.root / "Roadmaps/Shared"; shared.mkdir(parents=True)
        for name in ("registry.json", "records.schema.json"):
            shutil.copyfile(ROOT / "Roadmaps/Shared" / name, shared / name)
        self.executable = {"path": "/fixture/codex", "sha256": "b" * 64}

    def tearDown(self): self.temp.cleanup()

    def schemas(self):
        export = self.root / "export/v2"; export.mkdir(parents=True)
        for name in REQUIRED_SCHEMAS:
            value = {"title": name, "type": "object", "properties": {}, "required": []}
            if name == "ThreadReadParams.json":
                value.update(properties={"threadId": {}, "includeTurns": {}}, required=["threadId"])
            elif name == "ThreadReadResponse.json":
                value.update(properties={"thread": {}}, required=["thread"])
            elif name in {"ThreadTurnsListParams.json", "ThreadItemsListParams.json"}:
                value.update(properties={k: {} for k in ["threadId", "turnId", "limit", "cursor", "itemsView", "sortDirection"]}, required=["threadId"])
            elif name == "ThreadGoalSetParams.json":
                value["properties"] = {"tokenBudget": {"format": "int64", "type": ["integer", "null"]}}
            if name in {"ThreadItemsListResponse.json", "ThreadTurnsListResponse.json"}:
                value["definitions"] = {"ThreadItem": {"oneOf": []}, "Turn": {"type": "object"}}
            atomic_write_json(export / name, value, root=self.root)
        atomic_write_json(export / "UnselectedButRequiredForFreshness.json", {"description": "fixture"}, root=self.root)
        with patch("agentinfra.roadmap_protocol.native_executable", return_value=self.executable):
            return export_manifest(self.root, "export", self.executable)

    def canonical(self):
        owner = WorkspaceLease(self.root).acquire("T", "native fixture")
        goal = {"threadId": "T", "objective": "whole roadmap", "status": "active", "createdAt": 1,
                "tokensUsed": 100, "timeUsedSeconds": 10, "tokenBudget": None}
        binding = bind_goal(goal, thread_id="T", objective=goal["objective"], contract_hash="c" * 64)
        adapter = ProjectAdapter(self.root)
        adapter.update({"execution": {"workspace_lease": owner, "native_binding": binding, "scope": ["A04"],
                        "native_turn_configuration": {"model": "M", "effort": "max", "mode": "default"}},
                        "pending_proof_obligations": []}, expected_digest=None, allow_create=True)
        return adapter, owner, binding

    def prepared(self, owner, binding):
        value = {"schema": 1, "action": "pause", "binding": binding, "owner": owner, "contract_digest": "c" * 64,
                 "evidence": None, "request": {"method": "thread/goal/set", "params": {"threadId": "T", "status": "paused", "origin": "user"}}}
        value["digest"] = digest(value)
        return value

    def test_complete_protocol_manifest_includes_unselected_bytes_and_embedded_types(self):
        manifest = self.schemas()
        self.assertEqual(len(manifest["files"]), len(REQUIRED_SCHEMAS) + 1)
        self.assertEqual(manifest["definitions"]["ThreadItem"]["pointer"], "/definitions/ThreadItem")
        with patch("agentinfra.roadmap_protocol.native_executable", return_value=self.executable):
            assert_protocol(self.root, manifest)
            added = self.root / "export/v2/AddedSchema.json"; added.write_text('{}')
            with self.assertRaisesRegex(ContractError, "namespace changed"):
                assert_protocol(self.root, manifest)
            added.unlink()
            (self.root / "export/v2/UnselectedButRequiredForFreshness.json").write_text('{"changed":true}')
            with self.assertRaisesRegex(ContractError, "contracts changed"):
                assert_protocol(self.root, manifest)

    def test_exported_method_and_embedded_definition_denominators_cannot_be_omitted(self):
        self.schemas()
        path = self.root / "export/v2/ThreadItemsListResponse.json"
        value = read_json(path); value["definitions"].pop("ThreadItem"); atomic_write_json(path, value, root=self.root)
        with patch("agentinfra.roadmap_protocol.native_executable", return_value=self.executable):
            with self.assertRaisesRegex(ContractError, "definition missing"):
                export_manifest(self.root, "export", self.executable)
            path.unlink()
            with self.assertRaisesRegex(ContractError, "schema missing"):
                export_manifest(self.root, "export", self.executable)

    def test_changed_executable_and_unknown_manifest_are_not_accepted(self):
        manifest = self.schemas()
        with patch("agentinfra.roadmap_protocol.native_executable", return_value=dict(self.executable, sha256="d" * 64)):
            with self.assertRaises(ContractError): assert_protocol(self.root, manifest)
        manifest["schema"] = 99
        with self.assertRaises(ContractError): assert_protocol(self.root, manifest)

    def test_rpc_profile_rejects_mutations_full_history_unknown_fields_and_unbounded_pages(self):
        manifest = self.schemas(); client = ReplyClient({"thread": {"id": "T"}})
        with patch("agentinfra.roadmap_protocol.native_executable", return_value=self.executable), \
             patch("agentinfra.roadmap_native_adapter.CodexReader", return_value=client):
            with NativeRpc(self.root, manifest) as rpc:
                for method, params in [("thread/goal/set", {"threadId": "T"}),
                                       ("thread/read", {"threadId": "T", "includeTurns": True}),
                                       ("thread/read", {"threadId": "T", "includeTurns": False, "argv": ["unowned"]})]:
                    with self.assertRaises(ContractError): rpc.call(method, params)
                self.assertEqual(client.calls, [])
                with self.assertRaisesRegex(ContractError, "must be bounded"):
                    rpc.call("thread/turns/list", {"threadId": "T", "itemsView": "notLoaded", "limit": 21})
                reply = rpc.call("thread/read", {"threadId": "T", "includeTurns": False})
                self.assertEqual(reply["thread"]["id"], "T")
                self.assertEqual(rpc.calls[-1]["status"], "OBSERVED")
                self.assertNotIn("thread", rpc.calls[-1])

    def test_explicit_native_rejection_is_distinct_from_an_unknown_transport_outcome(self):
        manifest = self.schemas()
        for failure, outcome in [(CodexRpcError("thread/read", {"code": -32602, "message": "invalid params"}), "REJECTED"),
                                 (TimeoutError("unobserved"), "UNKNOWN")]:
            client = ReplyClient(failure)
            with patch("agentinfra.roadmap_protocol.native_executable", return_value=self.executable), \
                 patch("agentinfra.roadmap_native_adapter.CodexReader", return_value=client):
                with NativeRpc(self.root, manifest) as rpc:
                    with self.assertRaises(type(failure)): rpc.call("thread/read", {"threadId": "T", "includeTurns": False})
                    self.assertEqual(rpc.calls[-1]["status"], outcome)

    def test_actual_stdio_error_reply_is_typed_and_redacted(self):
        server = self.root / "codex-fixture"
        server.write_text("#!" + sys.executable + "\nimport sys,json\nfor line in sys.stdin:\n p=json.loads(line)\n if 'id' not in p: continue\n r={'id':p['id']}\n if p['method']=='initialize': r['result']={}\n else: r['error']={'code':-32602,'message':'token=fixture-sensitive-value'}\n print(json.dumps(r),flush=True)\n")
        server.chmod(0o700)
        with CodexReader(str(server), timeout=1) as client:
            with self.assertRaises(CodexRpcError) as caught: client.call("thread/read", {"threadId": "T"})
            self.assertEqual(caught.exception.code, -32602)
            self.assertNotIn("fixture-sensitive-value", str(caught.exception))

    def test_rpc_policy_retains_actual_reply_identity_before_rejecting_model_routing(self):
        manifest = self.schemas(); client = ReplyClient({"thread": {"id": "T"}})
        client.events.append({"method": "model/rerouted", "params": {"threadId": "T", "turnId": "U", "fromModel": "M", "toModel": "other"}})
        with patch("agentinfra.roadmap_protocol.native_executable", return_value=self.executable), \
             patch("agentinfra.roadmap_native_adapter.CodexReader", return_value=client):
            with NativeRpc(self.root, manifest) as rpc:
                rpc.watch({"session": "T", "model": "M", "turn_id": "U", "status": "active"})
                with self.assertRaisesRegex(ContractError, "rerouting"):
                    rpc.call("thread/read", {"threadId": "T", "includeTurns": False})
                self.assertEqual(rpc.calls[-1]["status"], "OBSERVED_POLICY_REFUSED")
                self.assertEqual(rpc.calls[-1]["response_digest"], digest(client.reply))

    def test_goal_binding_rejects_replaced_cleared_and_decreasing_native_state(self):
        _, _, previous = self.canonical()
        compiled = {"digest": "d" * 64}
        valid = previous["observation"]
        cases = [None, dict(valid, objective="smaller"), dict(valid, threadId="other"), dict(valid, tokensUsed=99),
                 dict(valid, timeUsedSeconds=9), dict(valid, tokensUsed=None), dict(valid, createdAt=2), dict(valid, createdAt=True)]
        for goal in cases:
            with self.subTest(goal=goal), self.assertRaises(ContractError):
                observe_goal(self.root, ReplyClient({"goal": goal}), compiled, previous)
        observed = observe_goal(self.root, ReplyClient({"goal": dict(valid, tokensUsed=2 ** 100)}), compiled, previous)
        self.assertEqual(observed["observation"]["tokensUsed"], 2 ** 100)
        self.assertEqual(observed["contract_digest"], compiled["digest"])

    def plan(self):
        path = self.root / "adopted.md"; path.write_text("exact adopted native Plan\n")
        source = {"thread_id": "source", "turn_id": "T", "item_id": "P", "adopted_source": file_binding(self.root, "adopted.md"),
                  "text_sha256": digest(path.read_bytes())}
        return source, PlanRpc(self.root, path.read_text()), {"digest": "e" * 64, "milestones": {"A04": {}}}

    def test_plan_binding_requires_exact_completed_native_item_and_adopted_source_bytes(self):
        source, rpc, compiled = self.plan()
        observation = observe_plan(self.root, rpc, source, compiled, ["A04"])
        self.assertEqual(observation["binding"]["native_item_id"], "P")
        self.assertEqual(observation["binding"]["native_item_digest"], digest(rpc.item))
        for field, value in [("type", "agentMessage"), ("text", "almost equivalent plan")]:
            before = dict(rpc.item); rpc.item[field] = value
            with self.assertRaises(ContractError): observe_plan(self.root, rpc, source, compiled, ["A04"])
            rpc.item = before
        (self.root / "adopted.md").write_text("changed authority")
        with self.assertRaises(ContractError): observe_plan(self.root, rpc, source, compiled, ["A04"])

    def test_incomplete_interrupted_wrong_workspace_or_wrong_turn_plan_cannot_bind(self):
        source, rpc, compiled = self.plan()
        for status in ("inProgress", "failed", "interrupted"):
            rpc.turn_status = status
            with self.assertRaisesRegex(ContractError, "not completed"): observe_plan(self.root, rpc, source, compiled, ["A04"])
        rpc.turn_status = "completed"; rpc.entry_turn = "other"
        with self.assertRaisesRegex(ContractError, "escaped"): observe_plan(self.root, rpc, source, compiled, ["A04"])
        rpc.entry_turn = "T"; rpc.root = self.root / "different"
        with self.assertRaisesRegex(ContractError, "another workspace"): observe_plan(self.root, rpc, source, compiled, ["A04"])

    def events(self):
        state = NativeEventState("T", "M")
        started = {"method": "turn/started", "params": {"threadId": "T", "turn": {"id": "U", "status": "inProgress"}}}
        state.consume(started)
        return state, started

    def test_plan_deltas_and_completed_step_lists_never_replace_final_native_plan(self):
        state, started = self.events(); state.consume(started)
        self.assertEqual(len(state.observed), 1)
        state.consume({"method": "item/plan/delta", "params": {"threadId": "T", "turnId": "U", "itemId": "P", "delta": "partial"}})
        state.consume({"method": "turn/plan/updated", "params": {"threadId": "T", "turnId": "U", "plan": [{"step": "done", "status": "completed"}]}})
        self.assertEqual(state.plans, {})
        self.assertEqual(state.status, "inProgress")
        item = {"type": "plan", "id": "P", "text": "authoritative final text"}
        completed = {"method": "item/completed", "params": {"threadId": "T", "turnId": "U", "item": item}}
        state.consume(completed); state.consume(completed)
        self.assertEqual(state.plans["P"], item)
        changed = copy.deepcopy(completed); changed["params"]["item"]["text"] = "changed final"
        with self.assertRaises(ContractError): state.consume(changed)

    def test_stream_refuses_overlapping_turns_rerouting_and_foreign_observations(self):
        state, _ = self.events()
        with self.assertRaisesRegex(ContractError, "overlapping"):
            state.consume({"method": "turn/started", "params": {"threadId": "T", "turn": {"id": "other"}}})
        with self.assertRaisesRegex(ContractError, "another chat"):
            state.consume({"method": "turn/completed", "params": {"threadId": "other", "turn": {"id": "U", "status": "completed"}}})
        state.consume({"method": "model/rerouted", "params": {"threadId": "T", "turnId": "U", "fromModel": "M", "toModel": "different"}})
        self.assertEqual(state.selected_model, "M")
        self.assertTrue(state.blockers)

    def test_interrupted_and_failed_turns_remain_terminal_without_completion_credit(self):
        for outcome in ("interrupted", "failed", "completed"):
            state, _ = self.events()
            state.consume({"method": "turn/completed", "params": {"threadId": "T", "turn": {"id": "U", "status": outcome}}})
            self.assertEqual(state.status, outcome)
            self.assertEqual(state.plans, {})

    def test_native_cumulative_usage_deduplicates_and_rejects_decrease_and_boolean_tokens(self):
        state, _ = self.events()
        event = {"method": "thread/tokenUsage/updated", "params": {"threadId": "T", "turnId": "U", "tokenUsage": {"total": {"inputTokens": 2 ** 100, "outputTokens": 10}}}}
        state.consume(event); state.consume(event)
        self.assertEqual(state.usage, event["params"]["tokenUsage"]["total"])
        for value in (-1, True, 2):
            changed = copy.deepcopy(event); changed["params"]["tokenUsage"]["total"]["inputTokens"] = value
            with self.assertRaises(ContractError): state.consume(changed)

    def test_readback_cannot_confirm_recreated_goal_or_missing_accounting(self):
        _, _, binding = self.canonical(); before = binding["observation"]
        for after in (dict(before, status="paused", createdAt=2), dict(before, status="paused", tokensUsed=None)):
            self.assertFalse(reconcile_native_transition(before, None, after, "paused")["confirmed"])
        self.assertTrue(reconcile_native_transition(before, None, dict(before, status="paused"), "paused")["confirmed"])

    def test_native_budget_domain_and_user_pause_do_not_depend_on_plan_execution_permission(self):
        _, _, binding = self.canonical(); manifest = self.schemas()
        native = NativeGoalAdapter(self.root, manifest)
        observed = {"caller_is_descendant": True, "effort": None, "mode": "plan", "model": "M"}
        reads = ReplyClient({"goal": binding["observation"]})
        compiled = {"digest": "c" * 64}
        with patch.object(WorkspaceLease, "qualify", return_value=observed), \
             patch("agentinfra.roadmap_native_adapter.compile_roadmaps", return_value=compiled), \
             patch("agentinfra.roadmap_native_adapter.NativeRpc", return_value=reads):
            pause = native.prepare("pause", user_authorized=True)
            self.assertEqual(pause["request"]["params"]["status"], "paused")
            self.assertNotIn("objective", pause["request"]["params"])
            with self.assertRaises(ContractError): native.prepare("resume", user_authorized=True)
            with self.assertRaises(ContractError): native.prepare("pause", user_authorized=False)
            for value in (True, 0, -1, 2 ** 63, 1.5):
                with self.assertRaises(ContractError): native.prepare("budget", user_authorized=True, token_budget=value)
            for value in (1, 2 ** 63 - 1):
                budget = native.prepare("budget", user_authorized=True, token_budget=value)
                self.assertEqual(budget["request"]["params"]["tokenBudget"], value)
        self.assertEqual(BudgetLedger(self.root).read()["attempts"], [])

    def test_green_gate_projection_cannot_omit_required_domain_obligation_at_native_completion(self):
        adapter, _, binding = self.canonical(); manifest = self.schemas()
        path = self.root / "evidence.json"; atomic_write_json(path, {"receipts": []}, root=self.root)
        adapter.update({"roadmap_evidence": file_binding(self.root, "evidence.json"),
                        "pending_proof_obligations": [{"id": "A04-O01", "status": "PROVED"}]},
                       expected_digest=digest(adapter.profile.path().read_bytes()))
        native = NativeGoalAdapter(self.root, manifest)
        observed = {"caller_is_descendant": True, "effort": "max", "mode": "default", "model": "M"}
        compiled = {"digest": "c" * 64, "milestones": {"A04": {"gates": ["full_domain_proof"]}}}
        with patch.object(WorkspaceLease, "qualify", return_value=observed), \
             patch("agentinfra.roadmap_native_adapter.compile_roadmaps", return_value=compiled), \
             patch("agentinfra.roadmap_native_adapter.NativeRpc", return_value=ReplyClient({"goal": binding["observation"]})), \
             patch("agentinfra.roadmap_native_adapter.audit_evidence", return_value={"milestones": {"A04": {"state": "SATISFIED"}}}):
            with self.assertRaisesRegex(ContractError, "domain obligations"):
                native.prepare("complete", user_authorized=True)
        self.assertEqual(adapter.read()["execution"]["native_binding"]["observation"]["status"], "active")

    def test_explicit_user_control_can_pause_during_existing_tool_work(self):
        adapter, owner, binding = self.canonical(); ledger = BudgetLedger(self.root)
        model = ledger.reserve("tool-work", "inputs", 30)
        prepared = self.prepared(owner, binding); native = NativeGoalAdapter(self.root, {"digest": "p"})
        goal = dict(binding["observation"])
        reads = ReplyClient({"goal": goal})

        def host(request):
            current = adapter.read()["execution"]["native_transition"]
            self.assertEqual(current["state"], "PREPARED")
            self.assertEqual(sum(a["status"] == "RESERVED" for a in ledger.read()["attempts"]), 2)
            goal["status"] = "paused"; reads.reply = {"goal": goal}
            return {"goal": goal}

        with patch.object(native, "prepare", return_value=prepared), patch("agentinfra.roadmap_native_adapter.NativeRpc", return_value=reads):
            result = native.dispatch(prepared, host, user_authorized=True, authorization_id="user-message-1",
                                     host_identity={"provider": "codex", "transport": "fixture", "identity": "fixture-code"})
        self.assertEqual(result["state"], "SUCCESS")
        self.assertEqual(ledger.read()["attempts"][0]["status"], "RESERVED")
        ledger.close(model["id"], "INTERRUPTED", {"reason": "fixture cleanup"})

    def test_unknown_native_callback_is_retained_then_recovered_from_same_goal_without_redispatch(self):
        adapter, owner, binding = self.canonical(); ledger = BudgetLedger(self.root)
        prepared = self.prepared(owner, binding); native = NativeGoalAdapter(self.root, {"digest": "p"})
        reads = ReplyClient({"goal": binding["observation"]})
        identity = {"provider": "codex", "transport": "fixture", "identity": "fixture-code"}
        with patch.object(native, "prepare", return_value=prepared), patch("agentinfra.roadmap_native_adapter.NativeRpc", return_value=reads):
            result = native.dispatch(prepared, lambda _: (_ for _ in ()).throw(TimeoutError("unknown")),
                                     user_authorized=True, authorization_id="user-message-2", host_identity=identity)
            self.assertEqual(result["state"], "UNKNOWN")
            self.assertEqual(ledger.read()["attempts"][0]["status"], "RESERVED")
            with self.assertRaisesRegex(ContractError, "requires read-back"):
                native.dispatch(prepared, lambda _: self.fail("must not redispatch"), user_authorized=True,
                                authorization_id="user-message-2", host_identity=identity)
            reads.reply = {"goal": dict(binding["observation"], status="paused")}
            recovered = native.recover()
        self.assertEqual(recovered["state"], "SUCCESS")
        self.assertEqual(len(ledger.read()["attempts"]), 1)
        self.assertEqual(adapter.read()["execution"]["native_transition"]["state"], "SUCCESS")

    def test_unidentified_or_unauthorized_host_control_cannot_receive_a_reservation(self):
        _, owner, binding = self.canonical(); prepared = self.prepared(owner, binding)
        native = NativeGoalAdapter(self.root, {"digest": "p"})
        for authorization, host in [(False, {"provider": "codex", "transport": "fixture", "identity": "x"}), (True, {}),
                                    (True, {"provider": "other", "transport": "fixture", "identity": "x"})]:
            with self.assertRaises(ContractError):
                native.dispatch(prepared, lambda _: self.fail("unauthorized callback"), user_authorized=authorization,
                                authorization_id="user-message", host_identity=host)
        self.assertEqual(BudgetLedger(self.root).read()["attempts"], [])

    def test_acceptance_selection_keeps_ready_independent_work_and_all_retained_accepted_responsibilities(self):
        compiled = {"order": ["A00", "A02", "A03", "A04", "A09"], "milestones": {
            "A00": {"dependencies": []}, "A02": {"dependencies": ["A00"]}, "A03": {"dependencies": ["A02"]},
            "A04": {"dependencies": ["A03"]}, "A09": {"dependencies": ["A02"]}}}
        record = {"execution": {"scope": list(compiled["order"])}, "aegis_roadmap_projection": {"milestones": {
            "A00": {"state": "SATISFIED"}, "A02": {"state": "SATISFIED"}, "A03": {"state": "SATISFIED"}, "A04": {"state": "READY"}}}}
        self.assertEqual(selected_work_milestones(compiled, record, "A09"), ["A00", "A02", "A03", "A09"])
        self.assertEqual(selected_work_milestones(compiled, record, "A04"), ["A00", "A02", "A03", "A04"])

    def test_new_successful_target_generation_retains_failed_ancestry_and_cannot_reset_failed_retries(self):
        ledger = BudgetLedger(self.root)

        def operation(identity, spec=None, supersedes=None):
            value = {"state": "PREPARED", "spec_digest": identity, "runner": process_handle(os.getpid()),
                     "owner": {"session": "generation-fixture"}, "child": None}
            if spec: value["spec"] = spec
            if supersedes: value["supersedes_success"] = supersedes
            return value

        def actual_result(label):
            directory = self.root / label; directory.mkdir()
            result = run_process([sys.executable, "-B", "-c", f"print({label!r})"], cwd=self.root)
            spec = {"candidate": label, "argv": list(result.argv), "inputs": [file_binding(self.root, "Roadmaps/Shared/records.schema.json")]}
            spec["digest"] = digest(spec)
            atomic_write_json(directory / "spec.json", spec, root=self.root)
            atomic_write_json(directory / "result.json", asdict(result), root=self.root)
            spec_binding = file_binding(self.root, label + "/spec.json")
            receipt = {"inputs": spec["digest"], "candidate": label, "argv": list(result.argv),
                       "returncode": 0, "timed_out": False, "truncated": False,
                       "stdout": result.stdout, "stderr": result.stderr,
                       "tool_microseconds": int(result.duration_seconds * 1_000_000),
                       "domain_proof": False, "installed_artifact_acceptance": False,
                       "artifacts": [spec_binding, file_binding(self.root, label + "/result.json")]}
            return spec, spec_binding, receipt

        failed = ledger.reserve_operation("responsibility", "broken-source", 10, operation("broken-source"))
        ledger.close(failed["id"], "FAILED", {"failure": "retain"})
        old, old_binding, receipt = actual_result("validated-old-target")
        passed = ledger.reserve_operation("responsibility", old["digest"], 10, operation(old["digest"], old_binding), diagnosis="corrected relevant source")
        ledger.close(passed["id"], "SUCCESS", receipt)
        new, new_binding, _ = actual_result("new-authorized-source-target")
        with self.assertRaisesRegex(ContractError, "generation lineage"):
            ledger.reserve_operation("responsibility", new["digest"], 10, operation(new["digest"], new_binding), diagnosis="new source")
        with self.assertRaisesRegex(ContractError, "latest successful"):
            ledger.reserve_operation("responsibility", new["digest"], 10, operation(new["digest"], new_binding, failed["id"]))
        next_target = ledger.reserve_operation("responsibility", new["digest"], 10, operation(new["digest"], new_binding, passed["id"]))
        self.assertEqual(next_target["generation"], 2)
        self.assertEqual(next_target["attempt_in_generation"], 1)
        self.assertEqual(set(next_target["inherited_attempt_ids"]), {failed["id"], passed["id"]})
        ledger.close(next_target["id"], "FAILED", {})
        with self.assertRaisesRegex(ContractError, "latest successful"):
            ledger.reserve_operation("responsibility", "another-source", 10, operation("another-source", supersedes=passed["id"]))
        corrected = ledger.reserve_operation("responsibility", "corrected-new-source", 10, operation("corrected-new-source"), diagnosis="corrected this generation's failure")
        self.assertEqual(corrected["generation"], 2)
        self.assertEqual(corrected["attempt_in_generation"], 2)
        ledger.close(corrected["id"], "FAILED", {})
        with self.assertRaisesRegex(ContractError, "attempt limit exhausted"):
            ledger.reserve_operation("responsibility", "third-source", 10, operation("third-source"), diagnosis="cannot reset")
        self.assertEqual(len(ledger.read()["attempts"]), 4)
        self.assertEqual(ledger.metrics()["reserved_seconds"], 40)


if __name__ == "__main__": unittest.main()
