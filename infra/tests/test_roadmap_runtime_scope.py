from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from agentinfra.atomic import atomic_write_json
from agentinfra.roadmap_lease import WorkspaceLease
from agentinfra.roadmap_records import ContractError, digest
from agentinfra.roadmap_runtime import BudgetLedger, recipe_scope


class ScopedRecipeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.ledger = BudgetLedger(self.root)

    def tearDown(self):
        self.temp.cleanup()

    def test_imported_failure_and_spent_time_survive_restart_and_omitted_aliases(self):
        old = self.ledger.reserve("old", "before", 60)
        self.ledger.close(old["id"], "FAILED", {"failure": "retained"})
        new = self.ledger.reserve("scoped", "corrected", 60, diagnosis="corrected binding",
                                  inherited_attempt_ids=(old["id"],))
        self.ledger.close(new["id"], "FAILED", {})
        restarted = BudgetLedger(self.root)
        with self.assertRaisesRegex(ContractError, "attempt limit exhausted"):
            restarted.reserve("scoped", "another", 60, diagnosis="another correction")
        self.assertEqual(sum(a["reserved_seconds"] for a in restarted.read()["attempts"]), 120)
        self.assertEqual(restarted.read()["attempts"][0]["receipt"], {"failure": "retained"})

    def test_inherited_success_and_unresolved_work_cannot_be_dispatched_again(self):
        old = self.ledger.reserve("old", "same", 10)
        with self.assertRaisesRegex(ContractError, "requires recovery"):
            self.ledger.reserve("scoped", "different", 10, inherited_attempt_ids=(old["id"],))
        self.ledger.close(old["id"], "SUCCESS", {})
        with self.assertRaisesRegex(ContractError, "successful work already exists"):
            self.ledger.reserve("scoped", "same", 10, inherited_attempt_ids=(old["id"],))

    def test_unknown_ancestor_and_unchanged_failed_inputs_are_rejected(self):
        with self.assertRaisesRegex(ContractError, "missing from the durable ledger"):
            self.ledger.reserve("new", "input", 10, inherited_attempt_ids=("invented",))
        old = self.ledger.reserve("old", "same", 10)
        self.ledger.close(old["id"], "FAILED", {})
        with self.assertRaisesRegex(ContractError, "unchanged failed inputs"):
            self.ledger.reserve("new", "same", 10, diagnosis="no actual correction",
                                inherited_attempt_ids=(old["id"],))

    def test_scope_uses_native_lifetime_and_requires_actual_owned_current_unit(self):
        legacy = digest({"recipe": "roadmap.validate", "root": str(self.root.resolve())})
        before = self.ledger.reserve(legacy, "authoring", 10)
        self.ledger.close(before["id"], "SUCCESS", {})
        # Give the historical fixture a distinct observed native lifetime.
        state = self.ledger.read()
        state["attempts"][0]["created_ns"] = 1_000_000_000
        atomic_write_json(self.ledger.path, state, root=self.root)
        current = self.ledger.reserve(legacy, "execution", 10, diagnosis="new execution inputs")
        self.ledger.close(current["id"], "FAILED", {})
        lease = WorkspaceLease(self.root)
        owner = lease.acquire("native-T", "A00")
        record = {"schema": 1, "project": "Aegis", "continuation": {"milestone": "A00"},
                  "execution": {"scope": ["A00", "A01"], "workspace_lease": owner,
                                "native_binding": {"thread_id": "native-T", "objective": "whole objective",
                                                   "observation": {"threadId": "native-T", "objective": "whole objective",
                                                                   "status": "active", "createdAt": 2}}}}
        path = self.root / ".aegis/project.json"
        atomic_write_json(path, record, root=self.root)
        compiled = {"milestones": {"A00": {"project": "Aegis"}, "A01": {"project": "Aegis"}},
                    "projects": {"Aegis": {"canonical_record": ".aegis/project.json"}}}
        work, ancestors = recipe_scope(self.root, compiled, "roadmap.validate", "A00", self.ledger)
        self.assertEqual(ancestors, (current["id"],))
        self.assertNotEqual(work, legacy)
        with self.assertRaisesRegex(ContractError, "outside the current"):
            recipe_scope(self.root, compiled, "roadmap.validate", "A01", self.ledger)
        record["execution"]["native_binding"]["observation"]["status"] = "paused"
        atomic_write_json(path, record, root=self.root)
        with self.assertRaisesRegex(ContractError, "mismatched or inactive"):
            recipe_scope(self.root, compiled, "roadmap.validate", "A00", self.ledger)
        lease.release(owner, {"producer": "qualified_codex_transport", "session": "native-T", "status": "completed"})


if __name__ == "__main__":
    unittest.main()
