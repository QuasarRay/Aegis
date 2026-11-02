"""Runtime qualification of durable execution; these are not domain proofs."""
from __future__ import annotations

import copy
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "infra"))
from agentinfra.atomic import atomic_write_json
from agentinfra.process import observe_process, run_process
from agentinfra.roadmap_lease import WorkspaceLease
from agentinfra.roadmap_native import inspect_process, process_handle, read_session_metadata
from agentinfra.roadmap_project import ProjectAdapter
from agentinfra.roadmap_records import ContractError, digest, file_binding, read_json
from agentinfra.roadmap_runtime import BudgetLedger
from agentinfra.roadmap_work import materialize, operation_state, qualify_execution, recover_operation, run_work


class DurableExecutionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        shared = self.root / "Roadmaps/Shared"
        shared.mkdir(parents=True)
        for name in ("registry.json", "records.schema.json"):
            shutil.copyfile(ROOT / "Roadmaps/Shared" / name, shared / name)
        self.ledger = BudgetLedger(self.root)

    def tearDown(self):
        self.temp.cleanup()

    def operation(self, identity="S", child=None):
        return {"state": "PREPARED", "spec_digest": identity, "owner": {"session": "fixture"},
                "runner": process_handle(os.getpid()), "child": child}

    def canonical(self):
        owner = WorkspaceLease(self.root).acquire("native-fixture", "A03 fixture")
        execution = {"scope": ["A03"], "workspace_lease": owner, "binding_history": [],
                     "native_turn_configuration": {"model": "selected-model", "effort": "max", "mode": "default"},
                     "native_binding": {"thread_id": owner["session"], "objective": "complete roadmap", "contract_digest": "a" * 64,
                                        "observation": {"threadId": owner["session"], "objective": "complete roadmap",
                                                        "status": "active", "createdAt": 1, "tokensUsed": 10, "timeUsedSeconds": 2}}}
        adapter = ProjectAdapter(self.root)
        adapter.update({"execution": execution, "continuation": {"milestone": "A03", "started_ns": 1_000_000_000}},
                       expected_digest=None, allow_create=True)
        compiled = {"milestones": {"A03": {"project": "Aegis"}}, "projects": {"Aegis": {"canonical_record": ".aegis/project.json"}}}
        return adapter, owner, compiled

    def test_observer_records_actual_creation_before_supervisor_returns(self):
        observed = []
        with observe_process(lambda proc: observed.append(process_handle(proc.pid))):
            result = run_process([sys.executable, "-B", "-c", "print('real child')"], cwd=self.root)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "real child")
        self.assertEqual(len(observed), 1)
        self.assertEqual(inspect_process(observed[0]), "GONE")

    def test_observer_failure_kills_and_reaps_owned_child(self):
        observed = []

        def reject(proc):
            observed.append(process_handle(proc.pid))
            raise RuntimeError("journal storage failed")

        with observe_process(reject), self.assertRaisesRegex(RuntimeError, "journal storage"):
            run_process([sys.executable, "-B", "-c", "import time; time.sleep(20)"], cwd=self.root)
        self.assertEqual(inspect_process(observed[0]), "GONE")

    def test_supervisor_timeout_has_actual_terminal_handle(self):
        observed = []
        with observe_process(lambda proc: observed.append(process_handle(proc.pid))):
            result = run_process([sys.executable, "-B", "-c", "import time; time.sleep(20)"], cwd=self.root, timeout=.1)
        self.assertTrue(result.timed_out)
        self.assertEqual(inspect_process(observed[0]), "GONE")

    def test_other_work_id_cannot_bypass_workspace_reservation(self):
        first = self.ledger.reserve_operation("first", "S", 30, operation=self.operation())
        with self.assertRaisesRegex(ContractError, "workspace operation"):
            self.ledger.reserve("renamed", "different", 30)
        self.assertEqual(len(self.ledger.read()["attempts"]), 1)
        self.ledger.close(first["id"], "INTERRUPTED", {"unknown_usage": True})
        self.assertEqual(self.ledger.metrics()["reserved_seconds"], 30)

    def test_reuse_checks_current_artifacts_and_does_not_charge_again(self):
        artifact = self.root / "result.txt"; artifact.write_text("actual output")
        first = self.ledger.reserve_operation("W", "S", 30, operation=self.operation())
        self.ledger.close(first["id"], "SUCCESS", {"artifacts": [file_binding(self.root, "result.txt")], "tool_microseconds": 42})
        second = self.ledger.reserve_operation("consumer", "S", 30, operation=self.operation())
        self.assertTrue(second["reused"])
        again = self.ledger.reserve_operation("consumer", "S", 30, operation=self.operation())
        self.assertTrue(again["reused"])
        self.assertEqual(self.ledger.metrics()["reuse_consumers"], 1)
        self.assertEqual(self.ledger.metrics()["attempts"], 1)
        artifact.write_text("changed output")
        with self.assertRaises(ContractError):
            self.ledger.reserve_operation("W", "S", 30, operation=self.operation())

    def test_failures_and_unknown_usage_survive_renaming_and_corrected_retry(self):
        first = self.ledger.reserve("W", "source-v1", 20)
        self.ledger.close(first["id"], "FAILED", {"unknown_usage": True})
        with self.assertRaisesRegex(ContractError, "diagnosis"):
            self.ledger.reserve("renamed", "source-v2", 20, inherited_attempt_ids=(first["id"],))
        second = self.ledger.reserve("renamed", "source-v2", 20, diagnosis="corrected exact input",
                                     inherited_attempt_ids=(first["id"],))
        self.ledger.close(second["id"], "FAILED", {})
        with self.assertRaisesRegex(ContractError, "attempt limit"):
            BudgetLedger(self.root).reserve("third-name", "source-v3", 20, diagnosis="another correction",
                                            inherited_attempt_ids=(second["id"],))
        self.assertEqual(self.ledger.metrics()["outcomes"]["FAILED"], 2)
        self.assertIsNone(self.ledger.metrics()["observed_tool_microseconds"])

    def test_missing_child_handle_and_live_runner_remain_unresolved(self):
        first = self.ledger.reserve_operation("W", "S", 20, operation=self.operation())
        observed = recover_operation(self.root, first["id"])
        self.assertEqual(observed["status"], "UNRESOLVED")
        self.assertEqual(observed["observed"]["runner"], "LIVE")
        self.assertEqual(observed["observed"]["child"], "UNKNOWN")
        self.assertEqual(self.ledger.read()["attempts"][0]["status"], "RESERVED")

    def test_recovery_closes_only_proven_gone_runner_child_and_group(self):
        processes = [subprocess.Popen([sys.executable, "-B", "-c", "import time; time.sleep(20)"], start_new_session=True)
                     for _ in range(2)]
        try:
            runner, child = [process_handle(proc.pid) for proc in processes]
            operation = self.operation(child=child); operation["runner"] = runner
            first = self.ledger.reserve_operation("W", "S", 20, operation=operation)
            self.assertEqual(recover_operation(self.root, first["id"])["status"], "UNRESOLVED")
            for proc in processes:
                proc.kill(); proc.wait(timeout=5)
            observed = recover_operation(self.root, first["id"])
            self.assertEqual(observed["status"], "INTERRUPTED")
            self.assertEqual(recover_operation(self.root, first["id"])["status"], "INTERRUPTED")
            self.assertEqual(self.ledger.read()["attempts"][0]["reserved_seconds"], 20)
        finally:
            for proc in processes:
                if proc.poll() is None:
                    proc.kill(); proc.wait(timeout=5)

    def test_surviving_descendant_blocks_recovery_after_leader_exits(self):
        proc = subprocess.Popen([sys.executable, "-B", "-c",
            "import subprocess,sys,time; p=subprocess.Popen([sys.executable,'-c','import time; time.sleep(20)']); print(p.pid,flush=True); time.sleep(.2)"],
            stdout=subprocess.PIPE, text=True, start_new_session=True)
        try:
            child = process_handle(proc.pid)
            descendant_pid = int(proc.stdout.readline())
            descendant = process_handle(descendant_pid)
            proc.wait(timeout=5)
            operation = self.operation(child=child)
            self.assertEqual(inspect_process(descendant), "LIVE")
            state = operation_state(operation)
            self.assertEqual(state["child"], "GONE")
            self.assertEqual(state["process_group"], "LIVE")
            self.assertFalse(state["safe_interruption"])
        finally:
            os.killpg(proc.pid, signal.SIGKILL)
            proc.wait(timeout=5); proc.stdout.close()

    def test_foreign_or_creation_mismatched_process_is_not_owned_live_work(self):
        handle = process_handle(os.getpid())
        self.assertEqual(inspect_process(dict(handle, host="different-host")), "UNKNOWN")
        self.assertEqual(inspect_process(dict(handle, process_identity="different-creation")), "REUSED_PID")
        self.assertEqual(inspect_process(dict(handle, boot_identity="different-boot")), "PREVIOUS_BOOT")

    def test_previous_boot_processes_are_terminal_without_signalling_reused_group_ids(self):
        handle = dict(process_handle(os.getpid()), boot_identity="recorded-previous-boot")
        operation = self.operation(child=handle); operation["runner"] = handle
        attempt = self.ledger.reserve_operation("W", "S", 20, operation=operation)
        with patch("agentinfra.roadmap_work.os.killpg", side_effect=AssertionError("must not signal a previous boot's group")):
            self.assertEqual(recover_operation(self.root, attempt["id"])["status"], "INTERRUPTED")

    def test_operation_cannot_replace_runner_child_or_owner(self):
        operation = self.operation(child=process_handle(os.getpid()))
        attempt = self.ledger.reserve_operation("W", "S", 30, operation=operation)
        for field in ("runner", "child", "owner"):
            changed = copy.deepcopy(operation); changed[field] = {"different": True}
            with self.assertRaises(ContractError):
                self.ledger.journal(attempt["id"], changed)
        self.assertEqual(self.ledger.read()["attempts"][0]["operation"], operation)

    def test_category_snapshots_are_cumulative_and_separate_from_goal_tokens(self):
        huge = 2 ** 100
        totals = {"input_tokens": huge, "cached_input_tokens": 7, "output_tokens": 9, "reasoning_output_tokens": 4}
        self.ledger.observe_usage("T", "G", 100)
        self.ledger.observe_categories("T", "E", totals, {"journal": "offset"})
        self.ledger.observe_categories("T", "E", totals, {"journal": "offset"})
        self.ledger.observe_categories("T", "unknown", {}, {"journal": "unknown"})
        series = self.ledger.metrics()["native_series"]
        self.assertEqual(series["T"]["total"], 100)
        self.assertEqual(series["native-session:T"]["totals"]["input_tokens"], huge)
        self.assertIsNone(series["native-session:T"]["totals"]["total_tokens"])
        with self.assertRaisesRegex(ContractError, "duplicate"):
            self.ledger.observe_categories("T", "E", dict(totals, output_tokens=10), {"journal": "offset"})
        with self.assertRaisesRegex(ContractError, "decreasing"):
            self.ledger.observe_categories("T", "later", {"input_tokens": 1}, {"journal": "offset2"})
        for value in (-1, True, 1.5):
            with self.assertRaises(ContractError):
                self.ledger.observe_categories("T", "invalid", {"output_tokens": value}, {"journal": "offset"})

    def test_journal_retains_metadata_provenance_without_message_content(self):
        journal = self.root / "session.jsonl"
        events = [{"type": "session_meta", "payload": {"id": "T", "private": "not retained"}},
                  {"type": "turn_context", "payload": {"model": "M", "effort": "max", "collaboration_mode": {"mode": "default"}, "cwd": str(self.root)}},
                  {"type": "event_msg", "payload": {"type": "task_started", "turn_id": "turn"}},
                  {"type": "response_item", "payload": {"content": "secret conversation"}},
                  {"type": "event_msg", "payload": {"type": "token_count", "info": {"total_token_usage": {"input_tokens": 9}}}}]
        raw = b"".join(json.dumps(e).encode() + b"\n" for e in events); journal.write_bytes(raw)
        metadata = read_session_metadata(journal, "T")
        self.assertNotIn("secret conversation", json.dumps(metadata))
        self.assertNotIn("not retained", json.dumps(metadata))
        origin = metadata["usage"]["origin"]
        self.assertEqual(digest(raw[origin["offset"]:origin["offset"] + origin["bytes"]]), origin["sha256"])
        with self.assertRaisesRegex(ContractError, "another chat"):
            read_session_metadata(journal, "other")
        journal.write_bytes(raw + b'{"incomplete"')
        with self.assertRaisesRegex(ContractError, "incomplete"):
            read_session_metadata(journal, "T")

    def test_native_mode_goal_reasoning_model_and_cap_are_dispatch_gates(self):
        adapter, owner, compiled = self.canonical()
        execution = adapter.read()["execution"]
        observation = {"goal": execution["native_binding"]["observation"], "caller_is_descendant": True,
                       "status": "active", "mode": "default", "effort": "max", "model": "selected-model",
                       "metadata": {"usage": None}}
        for field, value in (("mode", "plan"), ("effort", "high"), ("model", "routed-model"),
                             ("caller_is_descendant", False), ("status", "idle")):
            with patch.object(WorkspaceLease, "qualify", return_value=dict(observation, **{field: value})), self.assertRaises(ContractError):
                qualify_execution(self.root, compiled, "A03", "roadmap.validate")
        execution["monetary_cap"] = {"currency": "USD", "amount": "5"}
        adapter.update({"execution": execution}, expected_digest=digest(adapter.profile.path().read_bytes()))
        with patch.object(WorkspaceLease, "qualify", return_value=observation), self.assertRaisesRegex(ContractError, "monetary cap"):
            qualify_execution(self.root, compiled, "A03", "roadmap.validate")
        self.assertEqual(self.ledger.read()["attempts"], [])

    def test_live_native_owner_cannot_be_rebound(self):
        adapter, owner, _ = self.canonical()
        before = adapter.profile.path().read_bytes()
        with self.assertRaisesRegex(ContractError, "live or unknown"):
            adapter.rebind_native_process(os.getpid())
        self.assertEqual(before, adapter.profile.path().read_bytes())
        self.assertEqual(WorkspaceLease(self.root).read()["active"], owner)

    def test_qualified_goal_cannot_release_using_a_caller_supplied_terminal_label(self):
        adapter, owner, _ = self.canonical()
        execution = adapter.read()["execution"]
        execution["native_binding"]["native_accounting_preserved"] = True
        adapter.update({"execution": execution}, expected_digest=digest(adapter.profile.path().read_bytes()))
        with patch("agentinfra.roadmap_native.observe_native_owner", return_value={"status": "idle", "goal": {"status": "active"}}):
            with self.assertRaisesRegex(ContractError, "auto-continuing"):
                WorkspaceLease(self.root).release(owner, {"session": owner["session"], "status": "completed",
                                                          "producer": "qualified_codex_transport"})
        self.assertEqual(WorkspaceLease(self.root).read()["active"], owner)

    def test_completed_receipt_recovers_without_reexecuting_the_operation(self):
        from dataclasses import asdict
        result = run_process([sys.executable, "-B", "-c", "print('completed before runner interruption')"], cwd=self.root)
        source = self.root / "input.txt"; source.write_text("bound input")
        spec = {"candidate": "fixture-candidate", "argv": list(result.argv), "inputs": [file_binding(self.root, "input.txt")]}
        spec["digest"] = digest(spec)
        atomic_write_json(self.root / "spec.json", spec, root=self.root)
        (self.root / "logs").mkdir()
        atomic_write_json(self.root / "logs/result.json", asdict(result), root=self.root)
        previous = dict(process_handle(os.getpid()), boot_identity="previous-boot")
        operation = self.operation(spec["digest"], child=previous)
        operation.update(runner=previous, spec=file_binding(self.root, "spec.json"), receipt_path="receipt.json")
        attempt = self.ledger.reserve_operation("W", spec["digest"], 20, operation)
        receipt = {"inputs": spec["digest"], "candidate": spec["candidate"], "argv": list(result.argv),
                   "domain_proof": False, "installed_artifact_acceptance": False, "returncode": 0,
                   "timed_out": False, "truncated": False, "stdout": result.stdout, "stderr": result.stderr,
                   "tool_microseconds": int(result.duration_seconds * 1_000_000),
                   "artifacts": [file_binding(self.root, "spec.json"), file_binding(self.root, "logs/result.json")]}
        atomic_write_json(self.root / "receipt.json", receipt, root=self.root)
        recovered = recover_operation(self.root, attempt["id"])
        self.assertTrue(recovered["completed_result_recovered"])
        self.assertEqual(recovered["status"], "SUCCESS")
        self.assertEqual(self.ledger.reservation_record(attempt["id"])["consumed"], 20)
        self.assertEqual(len(self.ledger.read()["attempts"]), 1)

    def test_recipe_materialization_owns_argv_namespace_and_all_semantic_inputs(self):
        (self.root / "framework.toml").write_text("version = 'fixture'\n")
        (self.root / "infra/agentinfra").mkdir(parents=True)
        source = self.root / "infra/agentinfra/kernel.py"; source.write_text("value = 1\n")
        compiled = {"digest": "C", "inputs": [file_binding(self.root, "infra/agentinfra/kernel.py")],
                    "milestones": {"A03": {"project": "Aegis", "checks": ["production.build", "proof.kani"],
                    "budget_policy": {"max_attempts": 2, "max_seconds_per_recipe": 900}}},
                    "recipes": {"production.build": {"max_seconds": 900, "max_attempts": 2}, "proof.kani": {}}}
        with patch("agentinfra.roadmap_work.compile_roadmaps", return_value=compiled), patch.dict(os.environ, {}, clear=True):
            first = materialize(self.root, compiled, "A03", "production.build")
            self.assertEqual(first, materialize(self.root, compiled, "A03", "production.build"))
            self.assertIn("--invalidation-mode=checked-hash", first["argv"])
            (source.parent / "new.py").write_text("def unused(): return 2\n")
            added = materialize(self.root, compiled, "A03", "production.build")
            self.assertNotEqual(first["digest"], added["digest"])
            self.assertIn("infra/agentinfra/new.py", [b["path"] for b in added["inputs"]])
            with self.assertRaisesRegex(ContractError, "qualified implementation"):
                materialize(self.root, compiled, "A03", "proof.kani")
            with patch.dict(os.environ, {"PYTHONPATH": "/unowned/package"}), self.assertRaisesRegex(ContractError, "ambient Python"):
                materialize(self.root, compiled, "A03", "production.build")

    def test_materialized_build_runs_actual_supervisor_then_reuses_without_new_process(self):
        adapter, owner, _ = self.canonical()
        (self.root / "framework.toml").write_text("version = 'fixture'\n")
        for name in ("infra/agentinfra", "bin", "scripts", "verification/roadmap", "Roadmaps/Shared/ci"):
            (self.root / name).mkdir(parents=True, exist_ok=True)
        (self.root / "infra/agentinfra/kernel.py").write_text("def unused(value):\n    return value + 1\n")
        compiled = {"digest": "C", "inputs": [file_binding(self.root, "infra/agentinfra/kernel.py")],
                    "milestones": {"A03": {"project": "Aegis", "requirements": ["ROOT-03"], "checks": ["production.build"],
                        "budget_policy": {"max_attempts": 2, "max_seconds_per_recipe": 900}}},
                    "recipes": {"production.build": {"max_seconds": 900, "max_attempts": 2}}}
        observation = {"digest": "native-fixture", "turn_id": "fixture-turn"}
        with patch("agentinfra.roadmap_work.compile_roadmaps", return_value=compiled), \
             patch("agentinfra.roadmap_work.qualify_execution", return_value=(owner, observation, "build-work", ())), \
             patch.dict(os.environ, {}, clear=True):
            first = run_work(self.root, compiled, "A03", "production.build")
            self.assertEqual(first["returncode"], 0)
            self.assertFalse(first["reused"])
            pyc = [b for b in first["artifacts"] if b["path"].endswith(".pyc")]
            self.assertEqual(len(pyc), 1)
            with patch("agentinfra.roadmap_work.run_process", side_effect=AssertionError("duplicate process")):
                second = run_work(self.root, compiled, "A03", "production.build")
            self.assertTrue(second["reused"])
            self.assertEqual(first["attempt"], second["attempt"])
        self.assertEqual(len(self.ledger.read()["attempts"]), 1)
        self.assertEqual(adapter.read()["work_units"]["build-work"]["continuation"]["status"], "REUSED")


if __name__ == "__main__":
    unittest.main()
