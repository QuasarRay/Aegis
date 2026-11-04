"""AM20 on the owned managed-turn fixture; no live native inference is run."""
from __future__ import annotations

import json
from pathlib import Path
import shutil
import time
import unittest
from unittest.mock import patch

from agentinfra.roadmap_persistence import POLICY_PATH
from agentinfra.roadmap_records import ContractError, file_binding
from agentinfra.roadmap_runtime import BudgetLedger


ROOT = Path(__file__).resolve().parents[2]


class ManagedPersistenceTests(unittest.TestCase):
    def setUp(self):
        from test_roadmap_managed_turn import ManagedTurnTests
        self.fixture = ManagedTurnTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.root = self.fixture.root
        shutil.copyfile(ROOT / POLICY_PATH, self.root / POLICY_PATH)
        self.fixture.compiled["policy"] = {"execution_policy": POLICY_PATH}
        self.fixture.compiled["milestones"]["A04"]["budget_policy"].update(max_seconds_per_recipe=None, max_attempts=None)
        self.ledger = BudgetLedger(self.root)

    def test_persistent_prepare_has_explicit_unlimited_allocation_and_refuses_hidden_caps(self):
        with self.fixture.fixture():
            spec = self.fixture.runner.prepare("same owned work", role="executor", authorization_id="owned-work")
            self.assertEqual(spec["execution_mode"], "persistent_unlimited")
            self.assertEqual([spec[k] for k in ("max_seconds", "max_attempts", "total_seconds")], [None, None, None])
            self.assertEqual(spec["execution_policy"]["path"], POLICY_PATH)
            with self.assertRaisesRegex(ContractError, "cannot carry"):
                self.fixture.runner.prepare("same owned work", role="executor", authorization_id="owned-work", seconds=1)

    def test_elapsed_time_does_not_interrupt_a_persistent_live_native_handle(self):
        with self.fixture.fixture():
            result = self.fixture.start()
            self.fixture.runner.started_monotonic = time.monotonic() - 1000000
            result = self.fixture.runner.poll(0)
            self.assertEqual(result["state"], "RUNNING")
            self.assertEqual(self.ledger.read()["attempts"][0]["status"], "RESERVED")
            self.assertIsNone(self.ledger.read()["attempts"][0]["reserved_seconds"])
            self.assertFalse(any(x["method"] == "turn/interrupt" for x in self.fixture.state()["traffic"]))
            self.fixture.runner.interrupt(user_authorized=True, authorization_id="fixture-cleanup")
            self.assertEqual(self.fixture.observe(self.fixture.runner.poll(0))["state"], "INTERRUPTED")

    def test_failed_persistent_start_requires_evidenced_recovery_and_retains_attempt_and_unit_history(self):
        self.fixture.configure(reject_start=True)
        with self.fixture.fixture():
            spec = self.fixture.runner.prepare("same owned work", role="executor", authorization_id="owned-work")
            failed = self.fixture.runner.start(spec, user_authorized=True)
            self.assertEqual(failed["state"], "FAILED")
            original = self.ledger.read()["attempts"][0]
            with self.assertRaisesRegex(ContractError, "recovery record"):
                self.fixture.runner.start(spec, user_authorized=True)
            self.fixture.configure(reject_start=False, complete=True)
            # Native readback journals new traffic. Bind an immutable snapshot
            # rather than that live mutable service-state file.
            (self.root / "readiness-observation.json").write_text(json.dumps(self.fixture.state()))
            plan = failed["recovery_required"]
            plan.update(trigger="native request rejected", diagnosis="The fixture native service now accepts this unchanged request",
                        strategy="wait_for_capacity", action="Retry the same owned request after verified service readiness",
                        alternatives=[{"strategy": "wait_for_capacity", "reason": "The original native service reports readiness"},
                                      {"strategy": "reconnect_reobserve", "reason": "The original connection and terminal rejection remain known"}],
                        evidence=[file_binding(self.root, "readiness-observation.json")])
            (self.root / "recovery.json").write_text(json.dumps(plan))
            result = self.fixture.observe(self.fixture.runner.start(spec, user_authorized=True,
                                          recovery=file_binding(self.root, "recovery.json")))
            self.assertEqual(result["state"], "SUCCESS")
            rows = self.ledger.read()["attempts"]
            self.assertEqual(len(rows), 2)
            self.assertEqual(rows[0], original)
            self.assertTrue(all(a["reserved_seconds"] is None for a in rows))
            unit = self.fixture.adapter.read()["work_units"][spec["work_id"]]
            self.assertEqual(unit["continuation"]["history"][0]["continuation"]["attempt"], original["id"])
            self.assertEqual(sum(x["method"] == "turn/start" for x in self.fixture.state()["traffic"]), 2)

    def test_many_external_action_requests_are_retained_without_an_internal_count_stop(self):
        with self.fixture.fixture():
            self.fixture.start()
            for number in range(250):
                self.fixture.runner._consume({"id": "request-" + str(number),
                    "method": "item/commandExecution/requestApproval", "params": {"private": "not copied"}})
            requests = self.fixture.runner.operation["user_action_requests"]
            self.assertEqual(len(requests), 250)
            self.assertFalse(any("private" in x for x in requests))
            self.fixture.runner.interrupt(user_authorized=True, authorization_id="fixture-cleanup")
            self.assertEqual(self.fixture.observe(self.fixture.runner.poll(0))["state"], "INTERRUPTED")

    def test_model_capability_after_more_than_twenty_pages_can_start_the_owned_turn(self):
        from agentinfra.roadmap_managed import _TurnClient
        original_call = _TurnClient.call
        cursors = []

        def catalog(client, method, params):
            if method != "model/list":
                return original_call(client, method, params)
            page = int(params.get("cursor", "0"))
            cursors.append(page)
            return {"data": [] if page < 24 else [{"model": "M", "supportedReasoningEfforts": [{"reasoningEffort": "max"}]}],
                    "nextCursor": str(page + 1) if page < 24 else None}

        self.fixture.configure(complete=True)
        with self.fixture.fixture(), patch.object(_TurnClient, "call", new=catalog):
            result = self.fixture.observe(self.fixture.start())
        self.assertEqual(result["state"], "SUCCESS")
        self.assertEqual(cursors, list(range(25)))
        self.assertEqual(sum(x["method"] == "turn/start" for x in self.fixture.state()["traffic"]), 1)

    def test_cyclic_model_catalog_is_invalid_data_and_never_dispatches_a_model(self):
        from agentinfra.roadmap_managed import _TurnClient
        original_call = _TurnClient.call
        cursors = []

        def catalog(client, method, params):
            if method != "model/list":
                return original_call(client, method, params)
            cursors.append(params.get("cursor"))
            return {"data": [], "nextCursor": "cycle"}

        with self.fixture.fixture(), patch.object(_TurnClient, "call", new=catalog):
            result = self.fixture.start()
        self.assertEqual(result["state"], "FAILED")
        self.assertEqual(cursors, [None, "cycle"])
        self.assertFalse(any(x["method"] == "turn/start" for x in self.fixture.state()["traffic"]))
        self.assertEqual(self.ledger.read()["attempts"][0]["operation"]["start_observation_error"], "ContractError")
        self.assertIsNotNone(result["recovery_required"]["prior_attempt"])
