from __future__ import annotations

import copy
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "infra"))
from agentinfra.atomic import atomic_write_json
from agentinfra.roadmap import project_into_record
from agentinfra.roadmap_lease import WorkspaceLease
from agentinfra.roadmap_project import AEGIS_RECORD_WRITER, ProjectAdapter
from agentinfra.roadmap_records import ContractError, digest, read_json
from agentinfra.roadmap_runtime import BudgetLedger, recipe_scope


class ProjectAdapterTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        shared = self.root / "Roadmaps/Shared"
        shared.mkdir(parents=True)
        for name in ("registry.json", "records.schema.json"):
            shutil.copyfile(ROOT / "Roadmaps/Shared" / name, shared / name)
        self.adapter = ProjectAdapter(self.root)
        self.path = self.adapter.profile.path()

    def tearDown(self):
        self.temp.cleanup()

    def current_hash(self):
        return digest(self.path.read_bytes())

    def test_inventory_projection_and_execution_share_one_recovery_owner(self):
        self.adapter.update({"failures": ["retain"], "foreign_queue": {"items": [1]}},
                            expected_digest=None, allow_create=True)
        self.adapter.update({"authority_inventory": {"generation": 1}}, expected_digest=self.current_hash())
        project_into_record(self.root, "./.aegis/project.json", {"milestones": {"A00": {"state": "READY"}}}, self.current_hash())
        project_into_record(self.root, str(self.path), {"milestones": {"A00": {"state": "SATISFIED"}}}, self.current_hash())
        self.adapter.update({"continuation": {"milestone": "A01"}}, expected_digest=self.current_hash())
        value = self.adapter.read()
        self.assertEqual(value["failures"], ["retain"])
        self.assertEqual(value["foreign_queue"], {"items": [1]})
        self.assertEqual(value["canonical_writer_transaction_name"], AEGIS_RECORD_WRITER)
        self.assertEqual(value["aegis_roadmap_projection"]["milestones"]["A00"]["state"], "SATISFIED")

    def test_stale_update_cannot_replace_concurrent_data(self):
        self.adapter.update({"user": "first"}, expected_digest=None, allow_create=True)
        stale = self.current_hash()
        self.adapter.update({"user": "newer"}, expected_digest=stale)
        with self.assertRaisesRegex(ContractError, "changed"):
            self.adapter.update({"user": "lost"}, expected_digest=stale)
        self.assertEqual(self.adapter.read()["user"], "newer")

    def test_unknown_version_or_changed_writer_requires_explicit_migration(self):
        for record in ({"schema": 99, "project": "Aegis"}, {"schema": True, "project": "Aegis"},
                       {"schema": 1, "project": "Aegis", "canonical_writer_transaction_name": "another-writer"}):
            atomic_write_json(self.path, record, root=self.root)
            before = self.path.read_bytes()
            with self.assertRaises(ContractError):
                self.adapter.update({"ignored": False}, expected_digest=self.current_hash())
            self.assertEqual(before, self.path.read_bytes())

    def test_foreign_profiles_do_not_create_a_competing_carbon_queue(self):
        adapter = ProjectAdapter(self.root, "Destiny")
        self.assertTrue(adapter.describe()["external_writer_adoption_required"])
        with self.assertRaisesRegex(ContractError, "qualified adoption"):
            adapter.update({"source": "do not write"}, expected_digest=None, allow_create=True)
        self.assertFalse(self.path.exists())

    def test_generic_projection_keeps_its_existing_nonproject_contract(self):
        path = self.root / "legacy.json"
        atomic_write_json(path, {"existing": "keep"}, root=self.root)
        project_into_record(self.root, "legacy.json", {"milestones": {}}, digest(path.read_bytes()))
        self.assertEqual(read_json(path)["existing"], "keep")

    def test_native_identity_history_accounting_and_lease_are_not_replaceable(self):
        lease = WorkspaceLease(self.root)
        owner = lease.acquire("native-T", "initial roadmap")
        execution = {"scope": ["A00", "A01", "A02"], "workspace_lease": owner, "binding_history": [{"old": "keep"}],
                     "native_binding": {"thread_id": "native-T", "objective": "whole roadmap",
                                        "observation": {"tokensUsed": 300, "timeUsedSeconds": 40}}}
        self.adapter.update({"execution": execution}, expected_digest=None, allow_create=True)
        cases = []
        changed = copy.deepcopy(execution); changed["native_binding"]["objective"] = "smaller"; cases.append(changed)
        changed = copy.deepcopy(execution); changed["scope"] = ["A02"]; cases.append(changed)
        changed = copy.deepcopy(execution); changed["binding_history"] = []; cases.append(changed)
        changed = copy.deepcopy(execution); changed["native_binding"]["observation"]["tokensUsed"] = 0; cases.append(changed)
        changed = copy.deepcopy(execution); changed["workspace_lease"]["fence"] += 1; cases.append(changed)
        for changed in cases:
            with self.subTest(changed=changed), self.assertRaises(ContractError):
                self.adapter.update({"execution": changed}, expected_digest=self.current_hash())
        self.assertEqual(self.adapter.read()["execution"], execution)
        lease.release(owner, {"producer": "qualified_codex_transport", "session": "native-T", "status": "completed"})
        with self.assertRaisesRegex(ContractError, "stale fencing"):
            self.adapter.update({"continuation": {}}, expected_digest=self.current_hash())

    def test_legacy_attempts_are_attributed_only_to_the_current_unit_lifetime(self):
        ledger = BudgetLedger(self.root)
        legacy = digest({"recipe": "roadmap.validate", "root": str(self.root.resolve())})
        old = ledger.reserve(legacy, "A00 source", 10)
        ledger.close(old["id"], "FAILED", {})
        lease = WorkspaceLease(self.root); owner = lease.acquire("T", "initial roadmap")
        started = old["created_ns"] + 1
        execution = {"scope": ["A02"], "workspace_lease": owner,
                     "native_binding": {"thread_id": "T", "objective": "whole roadmap",
                                        "observation": {"threadId": "T", "objective": "whole roadmap", "status": "active", "createdAt": 1}}}
        self.adapter.update({"execution": execution, "continuation": {"milestone": "A02", "started_ns": started}},
                            expected_digest=None, allow_create=True)
        compiled = {"milestones": {"A02": {"project": "Aegis"}}, "projects": {"Aegis": {"canonical_record": ".aegis/project.json"}}}
        _, inherited = recipe_scope(self.root, compiled, "roadmap.validate", "A02", ledger)
        self.assertEqual(inherited, ())
        current = ledger.reserve(legacy, "A02 source", 10, diagnosis="different owned work")
        ledger.close(current["id"], "FAILED", {})
        _, inherited = recipe_scope(self.root, compiled, "roadmap.validate", "A02", ledger)
        self.assertEqual(inherited, (current["id"],))
        self.adapter.update({"continuation": {"milestone": "A02"}}, expected_digest=self.current_hash())
        with self.assertRaisesRegex(ContractError, "work-unit start"):
            recipe_scope(self.root, compiled, "roadmap.validate", "A02", ledger)
        lease.release(owner, {"producer": "qualified_codex_transport", "session": "T", "status": "completed"})


if __name__ == "__main__":
    unittest.main()
