"""Scoped retry authorization over preserved generations; fixture-only controls."""
from __future__ import annotations

from contextlib import contextmanager
import copy
import json
import unittest
from unittest.mock import patch

from agentinfra.roadmap_lease import WorkspaceLease
from agentinfra.roadmap_records import ContractError, digest, file_binding
from agentinfra.roadmap_runtime import authorize_single_retry, retry_limits
import test_roadmap_mirrors as mirror_support


FIELDS = ("id", "work_id", "inputs", "status", "reserved_seconds", "generation")


class RetryAuthorizationHistoryTests(unittest.TestCase):
    def setUp(self):
        self.fixture = mirror_support.RetryScopeTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        f = self.fixture
        f.work_id = digest({"recipe": "original.tests", "root": str(f.root), "native_thread": "thread",
                            "project": "Aegis", "milestone": "A04"})
        f.record["execution"]["workspace_lease"] = {"session": "thread"}
        self.current = [dict(a, work_id=f.work_id, generation=3) for a in f.prior]
        self.history = [dict(self.current[0], id="old-success", inputs="old-source-1", generation=1, status="SUCCESS"),
                        dict(self.current[0], id="old-failure", inputs="old-source-2-failed", generation=2, status="FAILED"),
                        dict(self.current[0], id="old-correction", inputs="old-source-2-fixed", generation=2, status="SUCCESS"),
                        *self.current]
        self.source = copy.deepcopy(f.amendment["source"])
        self.source["content"] = "one extra 900-second fixture test run; preserve all history"
        self.goal = {"threadId": "thread", "objective": "objective", "createdAt": 1, "status": "active"}
        self.compiled = {"recipes": {"original.tests": {"max_seconds": 900, "max_attempts": 2}},
                         "milestones": {"A04": {"checks": ["original.tests"],
                             "budget_policy": {"max_seconds_per_recipe": 900, "max_attempts": 2}}}}

    def save_record(self, changes, *, expected_digest):
        f = self.fixture
        path = f.root / ".aegis/project.json"
        self.assertEqual(expected_digest, digest(path.read_bytes()))
        f.record.update(changes)
        path.write_text(json.dumps({"schema": 1, "project": "Aegis", **f.record}))

    @contextmanager
    def state(self, history):
        f = self.fixture
        with f.state(history), \
             patch.object(WorkspaceLease, "qualify", return_value={"turn_id": "turn", "goal": self.goal}), \
             patch("agentinfra.roadmap_runtime.recipe_scope", return_value=(f.work_id, ())), \
             patch("agentinfra.roadmap_project.ProjectAdapter.update", side_effect=self.save_record):
            yield

    def authorize(self, *, user_authorized=True, source=None):
        f = self.fixture
        return authorize_single_retry(f.root, self.compiled, "A04", "original.tests",
                                      user_authorized=user_authorized, source=source or self.source,
                                      dependencies=[file_binding(f.root, "pin.json")])

    def test_latest_exhausted_generation_keeps_all_older_attempts(self):
        unchanged = copy.deepcopy(self.history)
        with self.state(self.history):
            amendment = self.authorize()
            limits = retry_limits(self.fixture.root, "A04", "original.tests", 2, 1800)
        self.assertEqual(amendment["prior_attempts"], [{k: a[k] for k in FIELDS} for a in self.current])
        self.assertEqual(amendment["retained_history"], [{k: a[k] for k in FIELDS} for a in self.history])
        self.assertEqual((limits["max_attempts"], limits["total_seconds"]), (3, 2700))
        self.assertEqual(self.history, unchanged)
        self.assertEqual(self.history[1]["status"], "FAILED")
        self.assertEqual(self.history[1]["reserved_seconds"], 900)

    def test_explicit_user_authority_and_current_native_turn_remain_required(self):
        for kwargs in ({"user_authorized": False},
                       {"source": dict(self.source, role="assistant")},
                       {"source": dict(self.source, observed_native_turn="different-turn")}):
            with self.subTest(kwargs=kwargs), self.state(self.history), self.assertRaises(ContractError):
                self.authorize(**kwargs)
        self.assertEqual(self.fixture.record["execution"]["budget_amendments"], {})

    def test_unspent_successful_or_unresolved_generations_cannot_borrow_failures(self):
        scenarios = [self.history[:-1],
                     [*self.history[:-1], dict(self.history[-1], status="SUCCESS")],
                     [*self.history, dict(self.history[-1], id="new-generation", generation=4)],
                     [dict(self.history[0], status="RESERVED"), *self.history[1:]]]
        for history in scenarios:
            with self.subTest(history=history), self.state(history), self.assertRaises(ContractError):
                self.authorize()
        self.assertEqual(self.fixture.record["execution"]["budget_amendments"], {})

    def test_deleting_changing_or_reordering_older_history_invalidates_amendment(self):
        with self.state(self.history):
            self.authorize()
        scenarios = [self.history[1:],
                     [self.history[0], *self.history[2:]],
                     [self.history[0], dict(self.history[1], reserved_seconds=0), *self.history[2:]],
                     [self.history[1], self.history[0], *self.history[2:]]]
        for history in scenarios:
            with self.subTest(history=history), self.state(history), self.assertRaisesRegex(ContractError, "retained attempt history"):
                retry_limits(self.fixture.root, "A04", "original.tests", 2, 1800)

    def test_consumed_generation_cannot_extend_later_work_or_freeze_old_pins(self):
        f = self.fixture
        with self.state(self.history):
            amendment = self.authorize()
        spec = {"candidate": "authorized-fixture"}
        spec["digest"] = digest(spec)
        (f.root / "spec.json").write_text(json.dumps(spec))
        consumed = dict(self.current[-1], id="consumed", status="SUCCESS", inputs=spec["digest"],
                        operation={"spec": file_binding(f.root, "spec.json")})
        later_spec = {"candidate": "later-fixture"}
        later_spec["digest"] = digest(later_spec)
        (f.root / "later-spec.json").write_text(json.dumps(later_spec))
        later = dict(consumed, id="later", generation=4, inputs=later_spec["digest"],
                     operation={"spec": file_binding(f.root, "later-spec.json")})
        (f.root / "pin.json").write_text("new reviewed fixture pin")
        with self.state([*self.history, consumed, later]):
            self.assertEqual(retry_limits(f.root, "A04", "original.tests", 2, 1800, candidate="later-fixture"),
                             {"max_attempts": 2, "total_seconds": 1800})
        self.assertEqual(amendment["retained_history"], [{k: a[k] for k in FIELDS} for a in self.history])


if __name__ == "__main__":
    unittest.main()
