"""Backend receipt/diagnostic controls using explicit test-only ledger fixtures.

No backend runs here, and these fabricated process records grant no proof credit.
The real fixed producer is exercised separately through named roadmap recipes.
"""
from __future__ import annotations

import ast
import copy
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

from agentinfra.roadmap_python import source_closure
from agentinfra.roadmap_python_catalog import qualification_reports, qualification_receipt_dependencies
from agentinfra.roadmap_records import ContractError, digest, file_binding


ROOT = Path(__file__).resolve().parents[2]


class QualificationObservationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        for name in ("Roadmaps/Shared/registry.json", "Roadmaps/Shared/records.schema.json",
                     "infra/agentinfra/__init__.py", "infra/agentinfra/roadmap_policy.py",
                     "infra/agentinfra/roadmap_records.py", "infra/agentinfra/security.py",
                     "verification/roadmap/python/policy_positive.py", "verification/roadmap/python/policy_negative.py"):
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, path)
        self.write("infra/tests/test_roadmap.py", "class DomainPolicyTests:\n def test_budgets_and_completion(self):\n  pass\n")
        self.write(".aegis/test-tool-binary", "TEST ONLY: this is not an executable")
        self.write(".aegis/unrelated-config", "first")
        self.original = self.bind("infra/tests/test_roadmap.py")
        self.tool = {"status": "INSTALLED_NOT_QUALIFIED", "python": "/fixture/python", "nagini": "/fixture/nagini",
                     "files": [self.bind(".aegis/test-tool-binary")]}
        self.save(".aegis/toolchain.json", self.tool)
        tool_binding = self.bind(".aegis/toolchain.json")
        self.production = source_closure(self.root, "agentinfra.roadmap_policy:may_reserve")
        self.spec = {"schema": 1, "project": "Aegis", "recipe": "python.qualify", "candidate": "producer-candidate",
                     "selection": {"kind": "actual_python_source_qualification", "action": "qualify", "domain_proof": False,
                                   "toolchain": tool_binding}, "toolchain": {"executable": str(Path(sys.executable).resolve())},
                     "inputs": [self.original, *self.production["files"], self.bind(".aegis/unrelated-config")],
                     "target": {"output": ".aegis/work/producer-candidate/python.qualify"}}
        self.spec["argv"] = [sys.executable, "-B", "scripts/roadmap_python.py", "qualify", "--output",
                             self.spec["target"]["output"] + "/details.json", "--candidate", self.spec["candidate"],
                             "--toolchain", tool_binding["path"]]
        self.spec["digest"] = digest(self.spec)
        directory = self.spec["target"]["output"] + "/" + self.spec["digest"]
        self.spec_path = directory + "/spec.json"
        self.details_path = directory + "/details.json"
        self.save(self.spec_path, self.spec)
        self.details = {"schema": 1, "action": "qualify", "backend": "nagini", "candidate": self.spec["candidate"],
                        "domain_proof": False, "production": self.production, "original": self.original,
                        "toolchain": tool_binding, "status": "UNSUPPORTED_OR_UNQUALIFIED", "runs": [], "artifacts": []}
        for name, intent in (("policy_positive.py", "positive"), ("policy_negative.py", "deliberately_wrong_assertion")):
            fixture = self.bind("verification/roadmap/python/" + name)
            raw = {"argv": [self.tool["python"], "-B", self.tool["nagini"], "--mypy-path", str(self.root / "infra"), str(self.root / fixture["path"])],
                   "cwd": str(self.root), "returncode": 1, "timed_out": False, "stdout_truncated": False, "stderr_truncated": False,
                   "stdout": "Translation failed\nType error: Encountered Any type. Type annotation missing? (agentinfra.roadmap_policy@80.0)\n", "stderr": ""}
            result_path = directory + "/" + name + ".result.json"
            self.save(result_path, raw)
            result = self.bind(result_path)
            self.details["runs"].append({"fixture": fixture, "result": result, "intent": intent,
                                         "classification": {"outcome": "UNSUPPORTED_OR_ERROR", "reason": "recorded fixture"}})
            self.details["artifacts"].extend([fixture, result])
        self.outer_path = directory + "/result.json"
        self.outer = {"argv": self.spec["argv"], "cwd": str(self.root), "returncode": 0, "timed_out": False,
                      "stdout": "test-only producer completed", "stderr": "", "stdout_truncated": False,
                      "stderr_truncated": False, "duration_seconds": 0.001}
        self.save(self.outer_path, self.outer)
        self.persist()
        policy = self.bind("infra/agentinfra/roadmap_policy.py")
        node = next(n for n in ast.parse((self.root / policy["path"]).read_bytes()).body if isinstance(n, ast.FunctionDef) and n.name == "proof_errors")
        self.catalog = {"fixture_semantics": {"fixture-id": {"location": {"source": self.original,
                        "fixture": "DomainPolicyTests", "test": "test_budgets_and_completion"}}},
                        "production_targets": {"declaration-id": {"id": "declaration-id", "source": policy,
                                                "span": [node.lineno, node.end_lineno]}},
                        "obligations": [{"id": "A09-O01", "source_bindings": [policy], "original_fixture_ids": ["fixture-id"]},
                                        {"id": "A13-O03", "source_bindings": [policy], "original_fixture_ids": ["fixture-id"]},
                                        {"id": "unattempted", "source_bindings": [], "original_fixture_ids": []}]}

    def write(self, relative, content):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)

    def save(self, relative, value):
        self.write(relative, json.dumps(value))

    def bind(self, relative):
        return file_binding(self.root, relative)

    def persist(self):
        self.save(self.details_path, self.details)
        binding = self.bind(self.details_path)
        receipt = {"schema": 1, "recipe": "python.qualify", "inputs": self.spec["digest"], "candidate": self.spec["candidate"],
                   "argv": self.spec["argv"], "domain_proof": False, "installed_artifact_acceptance": False,
                   "returncode": 0, "timed_out": False, "truncated": False, "stdout": self.outer["stdout"], "stderr": "",
                   "tool_microseconds": 1000,
                   "artifacts": [self.bind(self.spec_path), self.bind(self.outer_path), binding, *self.details["artifacts"]]}
        self.attempt = {"id": "1" * 64, "work_id": "test-only-qualification", "status": "SUCCESS", "inputs": self.spec["digest"],
                        "operation": {"spec": self.bind(self.spec_path)}, "receipt": receipt}
        self.save(".aegis/roadmaps/reservations.json", {"schema": 1, "attempts": [self.attempt], "usage": {}})
        self.save(".aegis/project.json", {"schema": 1, "project": "Aegis", "python_qualification_observation": binding})

    def reports(self, candidate="route-candidate"):
        return qualification_reports(self.root, candidate, self.catalog)

    def test_actual_unsupported_controls_join_originals_and_exact_production_location(self):
        report = self.reports()
        observation = report["qualification_observations"][0]
        self.assertTrue(observation["production_closure_current"])
        self.assertFalse(observation["same_code_candidate"])
        self.assertEqual(len(report["qualification_interventions"]), 2)
        self.assertEqual([len(r["assertion_source_nodes"]) for r in observation["runs"]], [6, 1])
        for packet in report["qualification_interventions"]:
            self.assertEqual(packet["original_fixture_ids"], ["fixture-id"])
            self.assertEqual(packet["potentially_affected_obligation_ids"], ["A09-O01", "A13-O03"])
            self.assertEqual(packet["diagnostics"][0]["containing_declaration_ids"], ["declaration-id"])
            self.assertEqual(packet["diagnostics"][0]["line"], 80)
            self.assertEqual(packet["control"]["assertion_reachability"], "NOT_ESTABLISHED")
            self.assertFalse(packet["backend_qualified"] or packet["domain_proof"] or packet["semantic_translation_approved"])

    def test_missing_observation_remains_not_attempted(self):
        self.save(".aegis/project.json", {"schema": 1, "project": "Aegis"})
        self.assertEqual(qualification_receipt_dependencies(self.root), [])
        self.assertEqual(self.reports()["qualification_observations"][0]["status"], "NOT_ATTEMPTED")

    def test_convenient_json_and_duplicate_producers_are_rejected(self):
        self.save(".aegis/roadmaps/reservations.json", {"schema": 1, "attempts": [], "usage": {}})
        with self.assertRaisesRegex(ContractError, "unique actual ledger"):
            self.reports()
        self.save(".aegis/roadmaps/reservations.json", {"schema": 1, "attempts": [self.attempt, copy.deepcopy(self.attempt)], "usage": {}})
        with self.assertRaisesRegex(ContractError, "unique actual ledger"):
            self.reports()

    def test_supervisor_contradiction_is_rejected_even_with_new_artifact_hash(self):
        self.outer["stdout"] = "changed supervisor output"
        self.save(self.outer_path, self.outer)
        self.persist()
        ledger = json.loads((self.root / ".aegis/roadmaps/reservations.json").read_text())
        ledger["attempts"][0]["receipt"]["stdout"] = "contradicted receipt output"
        self.save(".aegis/roadmaps/reservations.json", ledger)
        with self.assertRaisesRegex(ContractError, "contradicts"):
            self.reports()

    def test_changed_production_or_missing_tool_bytes_remain_stale_without_location_credit(self):
        dependency_before = qualification_receipt_dependencies(self.root)
        self.write("infra/agentinfra/roadmap_policy.py", (self.root / "infra/agentinfra/roadmap_policy.py").read_text() + "\nCHANGED = True\n")
        report = self.reports()
        self.assertNotEqual(report["qualification_dependencies"], dependency_before)
        self.assertEqual(report["qualification_interventions"], [])
        self.assertEqual(report["qualification_observations"][0]["status"], "STALE_QUALIFICATION_ARTIFACTS_NO_CURRENT_CREDIT")
        (self.root / ".aegis/test-tool-binary").unlink()
        report = self.reports()
        self.assertTrue(any(x["expected"]["path"] == ".aegis/test-tool-binary" and x["observed"] is None for x in report["qualification_observations"][0]["stale_bindings"]))

    def test_unchanged_closure_does_not_turn_historical_candidate_into_current_qualification(self):
        self.write(".aegis/unrelated-config", "second")
        observation = self.reports()["qualification_observations"][0]
        self.assertFalse(observation["producer_inputs_current"])
        self.assertTrue(observation["production_closure_current"])
        self.assertFalse(observation["same_code_candidate"] or observation["backend_qualified"] or observation["domain_proof"])

    def test_missing_negative_control_and_forged_console_arguments_are_rejected(self):
        original = copy.deepcopy(self.details)
        self.details["runs"] = self.details["runs"][:1]
        self.persist()
        with self.assertRaisesRegex(ContractError, "positive/negative"):
            self.reports()
        self.details = original
        result = self.details["runs"][0]["result"]
        raw = json.loads((self.root / result["path"]).read_text())
        raw["argv"] = ["unrelated-verifier", "toy-model.py"]
        self.save(result["path"], raw)
        replacement = self.bind(result["path"])
        self.details["runs"][0]["result"] = replacement
        self.details["artifacts"] = [replacement if b == result else b for b in self.details["artifacts"]]
        self.persist()
        with self.assertRaisesRegex(ContractError, "pinned console"):
            self.reports()

    def test_diagnostic_outside_the_bound_closure_remains_unresolved(self):
        result = self.details["runs"][0]["result"]
        raw = json.loads((self.root / result["path"]).read_text())
        raw["stdout"] = "Type error: unsupported (unrelated.module@80.0)\n"
        self.save(result["path"], raw)
        replacement = self.bind(result["path"])
        self.details["runs"][0]["result"] = replacement
        self.details["artifacts"] = [replacement if b == result else b for b in self.details["artifacts"]]
        self.persist()
        diagnostic = self.reports()["qualification_interventions"][0]["diagnostics"][0]
        self.assertEqual(diagnostic["source_identity_status"], "UNRESOLVED_LOCATION")
        self.assertEqual(diagnostic["containing_declaration_ids"], [])

    def test_new_backend_witness_changes_route_spec_without_changing_code_candidate(self):
        from agentinfra.roadmap import compile_roadmaps
        from agentinfra.roadmap_work import materialize
        compiled = compile_roadmaps(ROOT)
        dependency = {"path": ".aegis/fixture-only/backend-result.json", "sha256": "a" * 64}
        with patch("agentinfra.roadmap_work.ProjectAdapter") as adapter, \
             patch("agentinfra.roadmap_protocol.native_executable", return_value={"path": "/fixture/codex", "sha256": "b" * 64, "version": "fixture"}), \
             patch("agentinfra.roadmap_python_catalog.test_receipt_dependencies", return_value=[]):
            adapter.return_value.read.return_value = {"execution": {"native_turn_configuration": {"model": "fixture", "effort": "max", "mode": "default"}}}
            with patch("agentinfra.roadmap_python_catalog.qualification_receipt_dependencies", return_value=[]):
                before = materialize(ROOT, compiled, "A09", "python.route")
            with patch("agentinfra.roadmap_python_catalog.qualification_receipt_dependencies", return_value=[dependency]):
                after = materialize(ROOT, compiled, "A09", "python.route")
        self.assertEqual(before["candidate"], after["candidate"])
        self.assertNotEqual(before["digest"], after["digest"])
        self.assertEqual(after["selection"]["qualification_dependencies"], [dependency])
        self.assertIn(dependency, after["inputs"])


if __name__ == "__main__":
    unittest.main()
