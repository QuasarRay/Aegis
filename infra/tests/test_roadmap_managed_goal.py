"""Managed Goal controls through an actual owned stdio fixture, not live Codex.

The fixture uses the Python executable as its pinned server. It cannot perform
inference or mutate a real chat. Existing policy/host tests remain unchanged.
"""
from __future__ import annotations

import contextlib
import copy
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "infra"))

from agentinfra.atomic import atomic_write_json
from agentinfra.roadmap_codex import CodexReader, CodexRpcError, bind_goal
from agentinfra.roadmap_lease import WorkspaceLease
from agentinfra.roadmap_native_adapter import NativeGoalAdapter, _ManagedGoalClient
from agentinfra.roadmap_project import ProjectAdapter
from agentinfra.roadmap_protocol import REQUIRED_SCHEMAS, export_manifest
from agentinfra.roadmap_records import ContractError, digest, read_json
from agentinfra.roadmap_runtime import BudgetLedger


SERVER = r'''
import json,os,sys
from pathlib import Path
state_path=Path('fixture-state.json')
def save(state): state_path.write_text(json.dumps(state))
for line in sys.stdin:
    message=json.loads(line)
    if 'id' not in message: continue
    state=json.loads(state_path.read_text())
    method,params=message['method'],message['params']
    state['traffic'].append({'method':method,'params':params,'pid':os.getpid()})
    save(state)
    response={'id':message['id']}
    if method=='initialize':
        if state['mode']=='initialization-reject':
            response['error']={'code':-32600,'message':'fixture initialization rejected'}
        else:
            response['result']={}
    elif method=='thread/goal/get':
        if state['writes']:
            canonical=json.loads(Path('.aegis/project.json').read_text())
            transition=canonical['execution']['native_transition']
            assert transition['state'] in {'PREPARED','AWAITING_READBACK','UNKNOWN'}
            attempts=json.loads(Path('.aegis/roadmaps/reservations.json').read_text())['attempts']
            attempt=next(a for a in attempts if a['id']==transition['attempt'])
            reply_binding=transition.get('reply') or attempt['operation']['reply']
            reply=json.loads(Path(reply_binding['path']).read_text())
            state['reply_saved_before_readback']=reply
            save(state)
        if state.get('block_reads') and state['writes']:
            response['error']={'code':-32000,'message':'fixture readback unavailable'}
        else:
            response['result']={'goal':state['goal']}
    elif method in {'thread/goal/set','thread/goal/clear'}:
        canonical=json.loads(Path('.aegis/project.json').read_text())
        transition=canonical['execution']['native_transition']
        assert transition['state']=='PREPARED'
        attempts=json.loads(Path('.aegis/roadmaps/reservations.json').read_text())['attempts']
        attempt=next(a for a in attempts if a['id']==transition['attempt'])
        assert attempt['status']=='RESERVED' and attempt['operation']['state']=='RUNNING'
        assert attempt['operation']['child']['pid']==os.getpid()
        assert 'objective' not in params and params['threadId']=='T'
        state['writes']+=1
        if state['mode']=='reject':
            response['error']={'code':-32602,'message':'token=fixture-sensitive-value'}
        else:
            if method=='thread/goal/clear':
                state['goal']=None
                response['result']={}
            else:
                for key in ['status','tokenBudget']:
                    if key in params: state['goal'][key]=params[key]
                if state['mode']=='reset':
                    state['goal']['createdAt']+=1
                    state['goal']['tokensUsed']=0
                response['result']={'goal':state['goal']}
        save(state)
        if state['mode']=='disconnect-applied': break
        if state['mode']=='malformed':
            print('{bad-json}',flush=True)
            continue
        if state['mode']=='invalid-reply': response['result']={'unqualified':True}
    else:
        response['error']={'code':-32601,'message':'fixture refuses method'}
    print(json.dumps(response),flush=True)
'''


class ManagedGoalTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        shared = self.root / "Roadmaps/Shared"; shared.mkdir(parents=True)
        for name in ("registry.json", "records.schema.json"):
            shutil.copyfile(ROOT / "Roadmaps/Shared" / name, shared / name)
        self.executable = {"path": str(Path(sys.executable).resolve()),
                           "sha256": digest(Path(sys.executable).read_bytes())}
        export = self.root / "export/v2"; export.mkdir(parents=True)
        for name in REQUIRED_SCHEMAS:
            value = {"type": "object", "properties": {}, "required": []}
            if name == "ThreadGoalSetParams.json":
                value.update(properties={k: {} for k in ["threadId", "origin", "status", "tokenBudget"]}, required=["threadId"])
                value["properties"]["tokenBudget"] = {"format": "int64", "type": ["integer", "null"]}
            if name == "ThreadGoalClearParams.json":
                value.update(properties={"threadId": {}, "origin": {}}, required=["threadId"])
            if name in {"ThreadGoalGetParams.json", "ThreadReadParams.json"}:
                value.update(properties={"threadId": {}, "includeTurns": {}}, required=["threadId"])
            if name in {"ThreadGoalSetResponse.json", "ThreadGoalGetResponse.json"}:
                value.update(properties={"goal": {}}, required=["goal"])
            if name in {"ThreadItemsListResponse.json", "ThreadTurnsListResponse.json"}:
                value["definitions"] = {"ThreadItem": {"oneOf": []}, "Turn": {"type": "object"}}
            atomic_write_json(export / name, value, root=self.root)
        with patch("agentinfra.roadmap_protocol.native_executable", return_value=self.executable):
            self.protocol = export_manifest(self.root, "export", self.executable)
        (self.root / "app-server").write_text(SERVER)
        self.owner = WorkspaceLease(self.root).acquire("T", "owned managed fixture")
        self.goal = {"threadId": "T", "objective": "complete objective", "createdAt": 1, "status": "active",
                     "tokensUsed": 100, "timeUsedSeconds": 10, "tokenBudget": None}
        self.binding = bind_goal(self.goal, thread_id="T", objective=self.goal["objective"], contract_hash="c" * 64)
        self.adapter = ProjectAdapter(self.root)
        self.adapter.update({"execution": {"workspace_lease": self.owner, "native_binding": self.binding,
                             "scope": ["A04"], "native_turn_configuration": {"model": "M", "effort": "max", "mode": "default"}},
                             "pending_proof_obligations": []}, expected_digest=None, allow_create=True)
        self.state_path = self.root / "fixture-state.json"
        self.save_state({"goal": self.goal, "mode": "ok", "writes": 0, "traffic": []})
        self.native = NativeGoalAdapter(self.root, self.protocol)

    def tearDown(self): self.temp.cleanup()

    def save_state(self, state): self.state_path.write_text(json.dumps(state))
    def state(self): return read_json(self.state_path)

    def prepare(self, action="pause", budget=None):
        params = {"threadId": "T", "origin": "automatic" if action == "complete" else "user"}
        if action == "budget": params["tokenBudget"] = budget
        elif action != "clear": params["status"] = {"pause": "paused", "resume": "active", "complete": "complete"}[action]
        value = {"schema": 1, "action": action, "binding": self.binding, "owner": self.owner,
                 "contract_digest": "c" * 64, "evidence": None,
                 "request": {"method": "thread/goal/clear" if action == "clear" else "thread/goal/set", "params": params}}
        value["digest"] = digest(value)
        return value

    def controls(self, prepared):
        stack = contextlib.ExitStack()
        stack.enter_context(contextlib.chdir(self.root))
        stack.enter_context(patch("agentinfra.roadmap_protocol.native_executable", return_value=self.executable))
        stack.enter_context(patch.object(self.native, "prepare", return_value=copy.deepcopy(prepared)))
        return stack

    def dispatch(self, prepared, authorization="user-control-1"):
        return self.native.dispatch_managed(prepared, user_authorized=True, authorization_id=authorization)

    def test_stdio_control_is_reserved_and_journaled_before_write_and_reply_precedes_readback(self):
        prepared = self.prepare()
        with self.controls(prepared): result = self.dispatch(prepared)
        self.assertEqual(result["state"], "SUCCESS")
        state = self.state(); self.assertEqual(state["writes"], 1)
        self.assertEqual(state["goal"]["objective"], self.goal["objective"])
        self.assertEqual((state["goal"]["createdAt"], state["goal"]["tokensUsed"]), (1, 100))
        self.assertEqual(state["reply_saved_before_readback"]["response"]["goal"]["status"], "paused")
        attempt = BudgetLedger(self.root).read()["attempts"][0]
        self.assertEqual(attempt["operation"]["transport"], "managed_app_server_stdio_goal")
        wire = next(t for t in state["traffic"] if t["method"] == "thread/goal/set")
        self.assertEqual(wire["pid"], attempt["operation"]["child"]["pid"])
        self.assertEqual(result["reconciliation"]["transport_process_state"], "GONE")
        self.assertEqual(attempt["status"], "SUCCESS")
        self.assertTrue(all(t["method"] in {"initialize", "thread/goal/get", "thread/goal/set"} for t in state["traffic"]))

    def test_managed_clear_preserves_prior_accounting_in_durable_preparation(self):
        prepared = self.prepare("clear")
        with self.controls(prepared): result = self.dispatch(prepared)
        self.assertEqual(result["state"], "SUCCESS"); self.assertIsNone(self.state()["goal"])
        transition = self.adapter.read()["execution"]["native_transition"]
        prior = read_json(self.root / transition["preparation"]["path"])
        self.assertEqual(prior["binding"]["observation"]["tokensUsed"], 100)
        self.assertEqual(self.adapter.read()["execution"]["native_binding"], self.binding)

    def test_managed_budget_keeps_native_int64_and_does_not_reset_identity_or_usage(self):
        prepared = self.prepare("budget", 2 ** 63 - 1)
        with self.controls(prepared): result = self.dispatch(prepared)
        self.assertEqual(result["state"], "SUCCESS")
        self.assertEqual(self.state()["goal"], dict(self.goal, tokenBudget=2 ** 63 - 1))
        self.assertEqual(self.state()["traffic"][2]["params"]["tokenBudget"], 2 ** 63 - 1)

    def test_managed_resume_uses_existing_goal_without_sending_objective(self):
        self.binding["observation"]["status"] = "paused"
        state = self.state(); state["goal"]["status"] = "paused"; self.save_state(state)
        prepared = self.prepare("resume")
        with self.controls(prepared): result = self.dispatch(prepared)
        self.assertEqual(result["state"], "SUCCESS")
        wire = next(t for t in self.state()["traffic"] if t["method"] == "thread/goal/set")
        self.assertEqual(wire["params"], {"threadId": "T", "origin": "user", "status": "active"})
        self.assertEqual(self.state()["goal"]["tokensUsed"], 100)

    def test_explicit_rpc_rejection_is_failed_and_redacted_even_when_readback_fails(self):
        state = self.state(); state.update(mode="reject", block_reads=True); self.save_state(state)
        prepared = self.prepare()
        with self.controls(prepared): result = self.dispatch(prepared)
        self.assertEqual(result["state"], "FAILED")
        self.assertEqual(result["response"]["error"]["code"], -32602)
        self.assertEqual(result["reconciliation"]["readback_error"], "CodexRpcError")
        self.assertNotIn("fixture-sensitive-value", json.dumps(result))
        self.assertEqual(BudgetLedger(self.root).read()["attempts"][0]["status"], "FAILED")
        self.assertEqual(self.state()["goal"], self.goal)

    def test_disconnect_after_apply_reconciles_same_goal_without_another_write(self):
        state = self.state(); state["mode"] = "disconnect-applied"; self.save_state(state)
        prepared = self.prepare()
        with self.controls(prepared): result = self.dispatch(prepared)
        self.assertEqual(result["state"], "SUCCESS")
        self.assertEqual(result["observation_error"], "ContractError")
        self.assertEqual(self.state()["writes"], 1)

    def test_invalid_reply_is_recorded_but_only_actual_readback_can_confirm_mutation(self):
        state = self.state(); state["mode"] = "invalid-reply"; self.save_state(state)
        prepared = self.prepare()
        with self.controls(prepared): result = self.dispatch(prepared)
        reply = read_json(self.root / result["reply"]["path"])
        self.assertEqual(reply["transport_observations"][0]["status"], "INVALID_NATIVE_REPLY")
        self.assertEqual(result["observation_error"], "ContractError")
        self.assertEqual(result["state"], "SUCCESS"); self.assertEqual(self.state()["writes"], 1)

    def test_malformed_wire_reply_preserves_unknown_then_recovers_without_redispatch(self):
        state = self.state(); state.update(mode="malformed", block_reads=True); self.save_state(state)
        prepared = self.prepare()
        with self.controls(prepared):
            result = self.dispatch(prepared)
            self.assertEqual(result["state"], "UNKNOWN")
            self.assertEqual(result["observation_error"], "ContractError")
            reply = read_json(self.root / result["reply"]["path"])
            self.assertIsNone(reply["response"])
            self.assertEqual(reply["transport_observations"][0]["status"], "UNKNOWN")
            self.assertEqual(BudgetLedger(self.root).read()["attempts"][0]["status"], "RESERVED")
            with self.assertRaisesRegex(ContractError, "requires read-back"):
                self.dispatch(prepared)
            state = self.state(); state["block_reads"] = False; self.save_state(state)
            recovered = self.native.recover()
        self.assertEqual(recovered["state"], "SUCCESS")
        self.assertEqual(len(BudgetLedger(self.root).read()["attempts"]), 1)
        self.assertEqual(self.state()["writes"], 1)

    def test_recreated_goal_cannot_confirm_control_or_be_redispatched(self):
        state = self.state(); state["mode"] = "reset"; self.save_state(state)
        prepared = self.prepare()
        with self.controls(prepared):
            result = self.dispatch(prepared)
            recovered = self.native.recover()
        self.assertEqual(result["state"], "UNKNOWN"); self.assertEqual(recovered["state"], "UNKNOWN")
        self.assertEqual(self.state()["writes"], 1)
        self.assertEqual(BudgetLedger(self.root).read()["attempts"][0]["status"], "RESERVED")

    def test_changed_prewrite_goal_refuses_wire_mutation_and_does_not_hold_a_false_unknown(self):
        state = self.state(); state["goal"]["status"] = "paused"; self.save_state(state)
        prepared = self.prepare()
        with self.controls(prepared): result = self.dispatch(prepared)
        self.assertEqual(result["state"], "FAILED")
        self.assertTrue(result["reconciliation"]["request_not_dispatched"])
        self.assertEqual(self.state()["writes"], 0)

    def test_unauthorized_or_changed_preparation_is_refused_before_reservation_or_process(self):
        prepared = self.prepare()
        with self.controls(prepared):
            with self.assertRaises(ContractError):
                self.native.dispatch_managed(prepared, user_authorized=False, authorization_id="user")
            prepared["request"]["params"]["objective"] = "replacement"
            with self.assertRaisesRegex(ContractError, "prepared native request was changed"):
                self.dispatch(prepared)
        self.assertEqual(BudgetLedger(self.root).read()["attempts"], [])
        self.assertEqual(self.state()["traffic"], [])

    def test_fresh_shared_policy_refusal_cannot_be_bypassed_by_managed_transport(self):
        prepared = self.prepare("complete")
        with contextlib.chdir(self.root), \
             patch("agentinfra.roadmap_protocol.native_executable", return_value=self.executable), \
             patch.object(self.native, "prepare", side_effect=ContractError("full objective incomplete")):
            with self.assertRaisesRegex(ContractError, "full objective incomplete"):
                self.dispatch(prepared)
        self.assertEqual(self.state()["traffic"], [])
        self.assertEqual(BudgetLedger(self.root).read()["attempts"], [])

    def test_matching_success_is_reused_without_second_managed_server_or_goal_write(self):
        prepared = self.prepare()
        with self.controls(prepared):
            self.assertEqual(self.dispatch(prepared)["state"], "SUCCESS")
            traffic = copy.deepcopy(self.state()["traffic"])
            with self.assertRaisesRegex(ContractError, "already successful"):
                self.dispatch(prepared)
        self.assertEqual(self.state()["traffic"], traffic)
        self.assertEqual(len(BudgetLedger(self.root).read()["attempts"]), 1)

    def test_read_only_client_still_refuses_all_managed_goal_and_turn_methods(self):
        reader = CodexReader(self.executable["path"])
        for method in ["thread/goal/set", "thread/goal/clear", "thread/resume", "turn/start", "turn/steer", "turn/interrupt"]:
            with self.assertRaisesRegex(ContractError, "read-only"):
                reader.call(method, {"threadId": "T"})
        self.assertNotIn("turn/start", _ManagedGoalClient.ALLOWED)

    def test_managed_transport_keeps_live_or_unknown_child_reserved_after_goal_readback(self):
        prepared = self.prepare()
        with self.controls(prepared), patch("agentinfra.roadmap_native.inspect_process", return_value="UNKNOWN"):
            result = self.dispatch(prepared)
            self.assertEqual(result["state"], "UNKNOWN")
            self.assertTrue(result["reconciliation"]["confirmed"])
            self.assertEqual(BudgetLedger(self.root).read()["attempts"][0]["status"], "RESERVED")
        with self.controls(prepared): recovered = self.native.recover()
        self.assertEqual(recovered["state"], "SUCCESS")
        self.assertEqual(self.state()["writes"], 1)

    def test_corrupt_reply_binding_cannot_be_recovered_as_a_success(self):
        prepared = self.prepare(); state = self.state(); state["block_reads"] = True; self.save_state(state)
        with self.controls(prepared):
            result = self.dispatch(prepared)
            self.assertEqual(result["state"], "UNKNOWN")
            (self.root / result["reply"]["path"]).write_text('{}')
            with self.assertRaisesRegex(ContractError, "reply evidence changed"):
                self.native.recover()
        self.assertEqual(BudgetLedger(self.root).read()["attempts"][0]["status"], "RESERVED")

    def test_initialization_rejection_is_recorded_without_sending_a_goal_control(self):
        prepared = self.prepare(); state = self.state(); state['mode'] = 'initialization-reject'; self.save_state(state)
        with self.controls(prepared): result = self.dispatch(prepared)
        self.assertEqual(result["state"], "FAILED")
        self.assertTrue(result["reconciliation"]["request_not_dispatched"])
        self.assertEqual(result["response"]["method"], "initialize")
        self.assertEqual(self.state()["writes"], 0)

    def test_interruption_after_reply_persistence_recovers_without_another_native_write(self):
        prepared = self.prepare()
        with self.controls(prepared):
            with patch.object(self.native, "_readback", side_effect=KeyboardInterrupt):
                with self.assertRaises(KeyboardInterrupt): self.dispatch(prepared)
            transition = self.adapter.read()["execution"]["native_transition"]
            self.assertEqual(transition["state"], "AWAITING_READBACK")
            self.assertTrue((self.root / transition["reply"]["path"]).is_file())
            self.assertEqual(BudgetLedger(self.root).read()["attempts"][0]["status"], "RESERVED")
            recovered = self.native.recover()
        self.assertEqual(recovered["state"], "SUCCESS")
        self.assertEqual(self.state()["writes"], 1)

    def test_host_callback_rejection_uses_the_same_durable_failed_outcome(self):
        prepared = self.prepare()
        def rejected(_):
            raise CodexRpcError("thread/goal/set", {"code": -32602, "message": "token=fixture-sensitive-value"})
        with self.controls(prepared):
            result = self.native.dispatch(prepared, rejected, user_authorized=True, authorization_id="host-control",
                                          host_identity={"provider": "codex", "transport": "fixture", "identity": "fixture-host"})
        self.assertEqual(result["state"], "FAILED")
        self.assertEqual(result["response"]["error"]["code"], -32602)
        self.assertNotIn("fixture-sensitive-value", json.dumps(result))
        self.assertEqual(BudgetLedger(self.root).read()["attempts"][0]["status"], "FAILED")

    def test_wire_budget_domain_rejects_bool_negative_and_overflow_before_dispatch(self):
        for value in [True, 0, -1, 2 ** 63, 1.5]:
            with self.subTest(value=value):
                request = self.prepare("budget", value)["request"]
                client = _ManagedGoalClient(self.root, self.protocol, request, lambda _: self.fail("must not spawn"))
                with patch("agentinfra.roadmap_protocol.native_executable", return_value=self.executable):
                    with self.assertRaisesRegex(ContractError, "int64"):
                        client.call(request["method"], request["params"])
                self.assertFalse(client.sent)

    def test_reply_in_ledger_recovers_when_canonical_projection_was_not_advanced(self):
        prepared = self.prepare()
        original_update = self.adapter.update
        def interrupted(adapter, fields, **kwargs):
            if fields.get("execution", {}).get("native_transition", {}).get("state") == "AWAITING_READBACK":
                raise KeyboardInterrupt
            return original_update(fields, **kwargs)
        with self.controls(prepared):
            with patch.object(ProjectAdapter, "update", new=interrupted):
                with self.assertRaises(KeyboardInterrupt): self.dispatch(prepared)
            transition = self.adapter.read()["execution"]["native_transition"]
            self.assertEqual(transition["state"], "PREPARED")
            self.assertNotIn("reply", transition)
            attempt = BudgetLedger(self.root).read()["attempts"][0]
            self.assertIn("reply", attempt["operation"])
            recovered = self.native.recover()
        self.assertEqual(recovered["state"], "SUCCESS")
        self.assertEqual(self.adapter.read()["execution"]["native_transition"]["reply"], attempt["operation"]["reply"])
        self.assertEqual(self.state()["writes"], 1)
        self.assertEqual(len([t for t in self.state()["traffic"] if t["method"] == "thread/goal/set"]), 1)

    def test_terminal_ledger_reconciles_projection_without_closing_or_dispatching_twice(self):
        prepared = self.prepare()
        original_update = self.adapter.update
        def interrupted(adapter, fields, **kwargs):
            if fields.get("execution", {}).get("native_transition", {}).get("state") == "SUCCESS":
                raise KeyboardInterrupt
            return original_update(fields, **kwargs)
        with self.controls(prepared):
            with patch.object(ProjectAdapter, "update", new=interrupted):
                with self.assertRaises(KeyboardInterrupt): self.dispatch(prepared)
            self.assertEqual(BudgetLedger(self.root).read()["attempts"][0]["status"], "SUCCESS")
            self.assertEqual(self.adapter.read()["execution"]["native_transition"]["state"], "AWAITING_READBACK")
            recovered = self.native.recover()
        self.assertEqual(recovered["state"], "SUCCESS")
        self.assertTrue(recovered["ledger_already_terminal"])
        self.assertEqual(self.adapter.read()["execution"]["native_transition"]["state"], "SUCCESS")
        self.assertEqual(self.state()["writes"], 1)


if __name__ == "__main__": unittest.main()
