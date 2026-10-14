"""Focused evidence-reader checks. Synthetic output is never Destiny proof evidence."""
import copy
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from agentinfra.destiny import load_profile, matches_version
from agentinfra.destiny_reuse import digest
from agentinfra.evidence import classified, current_receipt, differential_cases, kani_properties, proof_identity, proof_output, property_name, property_location
from agentinfra.formal import AUTHORITY, validate_plan

CASE = "case.py::OriginalFixture::test_value"
OUTPUT = """Checking harness proofs::formation...
RESULTS:
Check 1: proofs::formation.assertion.1
 - Status: SUCCESS
 - Description: "relation holds"
Check 2: runtime::step.cover.1
 - Status: SATISFIED
 - Location: src/runtime.rs:1:1 in function runtime::step
SUMMARY:
VERIFICATION:- SUCCESSFUL
Complete - 1 successfully verified harnesses, 0 failures, 1 total.
"""


class TestEvidence(unittest.TestCase):
    def test_exact_helper_and_trait_property_names_preserve_spaces(self):
        for name in ("proofs::compare::<f64, 8>.assertion.1", "<f64 as std::cmp::PartialEq>::eq.assertion.1"):
            self.assertTrue(property_name(name,"assertion"))
        for name in ("x.assertion.1\n", " x.assertion.1", "x\t.assertion.1", "x.cover.1"):
            self.assertFalse(property_name(name,"assertion"))

    def test_assertion_location_is_bound_to_the_actual_manifest_source(self):
        (self.root/"verification/kani/src/proofs.rs").write_text("assert!(true);\n")
        self.assertEqual(property_location(self.root,"verification/kani/Cargo.toml",
            {"location":"src/proofs.rs:1:5 in function proofs::compare::<f64, 8>"}),
            {"file":"verification/kani/src/proofs.rs","line":1})
        self.assertIsNone(property_location(self.root,"verification/kani/Cargo.toml",
            {"location":"src/proofs.rs:2:5 in function proofs::compare::<f64, 8>"}))

    def test_property_names_with_rust_type_spaces_are_never_dropped(self):
        name = "std::cmp::<impl PartialEq for i8>::eq.pointer_dereference.1"
        output = OUTPUT.replace("SUMMARY:", f"Check 3: {name}\n - Status: FAILURE\nSUMMARY:")
        self.assertEqual(kani_properties(output)[name]["status"], "FAILURE")
        self.assertFalse(proof_output(self.obligation, self.output(output)))

    def test_incomplete_property_inventory_is_rejected(self):
        for output in (OUTPUT.replace("Check 2:", "Check 3:"),
                       OUTPUT.replace(" - Status: SATISFIED\n", "")):
            self.assertFalse(proof_output(self.obligation, self.output(output)))

    def test_manifest_relative_cover_locations_resolve_to_the_bound_source(self):
        self.obligation["evidence"] = self.scope
        receipt = {"commands": [{"stdout": OUTPUT.replace("src/runtime.rs:1:1", "src/../../../src/runtime.rs:1:1"), "stderr": ""}]}
        self.assertEqual(classified(self.root, self.obligation, receipt), "production_rust_refinement_proved")
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ("src/runtime.rs", "verification/spec/src/spec.rs", "verification/kani/src/proofs.rs", "verification/kani/Cargo.toml"):
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("// source fixture\n")
        self.obligation = {"id": "formation", "method": "kani", "entry": "proofs::formation", "expected_checks": 1,
                           "invariant": "Declared original behavior", "specification": ["verification/spec/src/spec.rs"],
                           "implementation": ["src/runtime.rs"], "proof_inputs": ["verification/kani/src/proofs.rs"],
                           "assumptions": "Synthetic output only", "limits": "No actual Destiny proof"}
        self.scope = {"kind": "production_rust_refinement_proved", "original_cases": [CASE],
                      "assertion_properties": ["proofs::formation.assertion.1"],
                      "reachability": [{"property": "runtime::step.cover.1", "file": "src/runtime.rs", "line": 1}],
                      "relation": "Production output equals the declared specification within the reviewed domain",
                      "review": "Fixture represents a reviewed source correspondence, not an actual proof"}

    def output(self, text):
        return SimpleNamespace(stdout=text, stderr="", returncode=0, timed_out=False, stdout_truncated=False, stderr_truncated=False)

    def plan(self):
        return {"schema": 1, "objective": "Evidence classification fixture", "authority_sha256": digest(AUTHORITY.read_bytes()),
                "reference_review": "Synthetic fixture only", "reuse": {"strategy": "handwrite", "sources": [], "license": "fixture",
                "reason": "Exercise classification boundary", "generator": []}, "obligations": [self.obligation]}

    def test_exact_pinned_version_has_no_prefix_or_prerelease_alias(self):
        self.assertTrue(matches_version("0.68.0", "cargo-kani 0.68.0\n"))
        for version in ("0.68.01", "0.68.0-dev", "0.67.0", "v0.68.0"):
            self.assertFalse(matches_version("0.68.0", version))

    def test_exact_harness_needs_behavioral_assertion_and_reachable_cover(self):
        self.assertTrue(proof_output(self.obligation, self.output(OUTPUT)))
        mutations = [OUTPUT.replace("proofs::formation...", "other::formation..."), OUTPUT * 2,
                     OUTPUT.replace("SATISFIED", "UNSATISFIABLE"), OUTPUT.replace("SATISFIED", "UNREACHABLE"),
                     OUTPUT.replace("SUCCESS\n", "UNDETERMINED\n"), OUTPUT.replace(".assertion.", ".overflow."),
                     OUTPUT.replace(".cover.", ".overflow."), OUTPUT.replace("RESULTS:", "RESULTS:\n - Status: FAILURE"),
                     "Checking harness proofs::formation...\n - Status: SUCCESS\nVERIFICATION:- SUCCESSFUL\nComplete - 1 successfully verified harnesses, 0 failures, 1 total.\n"]
        for text in mutations:
            with self.subTest(text=text):
                self.assertFalse(proof_output(self.obligation, self.output(text)))

    def test_mapping_and_spec_success_do_not_promote_to_production(self):
        receipt = {"commands": [{"stdout": OUTPUT, "stderr": ""}]}
        self.assertEqual(classified(self.root, self.obligation, receipt), "unclassified")
        self.obligation["evidence"] = {**self.scope, "kind": "spec_proved"}
        self.assertEqual(classified(self.root, self.obligation, receipt), "spec_proved")
        self.obligation["evidence"] = self.scope
        self.assertEqual(classified(self.root, self.obligation, receipt), "production_rust_refinement_proved")
        for bad in (OUTPUT.replace("src/runtime.rs", "verification/spec/src/spec.rs"), OUTPUT.replace("SATISFIED", "UNREACHABLE")):
            with self.assertRaises(ValueError):
                classified(self.root, self.obligation, {"commands": [{"stdout": bad, "stderr": ""}]})

    def test_classification_requires_catalog_identity_and_production_witness(self):
        self.obligation["evidence"] = copy.deepcopy(self.scope)
        with patch("agentinfra.catalog.qualified_index", return_value=[{"id": CASE}]):
            validate_plan(self.root, load_profile(), self.plan())
            self.obligation["evidence"]["reachability"][0]["file"] = "verification/spec/src/spec.rs"
            with self.assertRaisesRegex(ValueError, "production"):
                validate_plan(self.root, load_profile(), self.plan())
            self.obligation["evidence"] = {**self.scope, "original_cases": ["case.py::test_value"]}
            with self.assertRaisesRegex(ValueError, "fixture-qualified"):
                validate_plan(self.root, load_profile(), self.plan())

    def test_harness_digest_changes_even_without_a_git_commit(self):
        before = proof_identity(self.root, self.obligation)
        (self.root / "verification/kani/src/proofs.rs").write_text("// changed harness\n")
        self.assertNotEqual(before, proof_identity(self.root, self.obligation))

    def test_cached_or_missing_execution_is_not_evidence(self):
        for result in ({"executed": False, "status": "REUSED"}, {"status": "OBSERVED_SUCCESS"}, {"executed": True, "status": "UNAVAILABLE"}):
            with self.assertRaisesRegex(ValueError, "fresh"):
                current_receipt(self.root, load_profile(), result)

    def test_differential_evidence_requires_real_executed_scenario_inventory(self):
        scenario = "test_value (runtime.Fixture.test_value)"
        mapping = {"schema": 1, "records": [{"case": CASE, "observation": {"receipt": "synthetic.json"},
                   "scenarios": [scenario], "rationale": "Explicit reviewed scenario correspondence"}]}
        (self.root / "mapping.json").write_text(json.dumps(mapping))
        receipt = {"id": "native-differential", "identity": {"external": {"library": "digest"}, "source": {"digest": "source"}},
                   "commands": [{"stdout": "", "stderr": scenario + " ... ok\nRan 1 test in 0.01s\nOK\n"}]}
        with patch("agentinfra.evidence.current_receipt", return_value=receipt):
            self.assertEqual(len(differential_cases(self.root, load_profile(), "mapping.json")), 1)
            receipt["commands"][0]["stderr"] = scenario + " ... skipped 'no library'\nRan 1 test in 0.01s\nOK (skipped=1)\n"
            with self.assertRaisesRegex(ValueError, "skipped"):
                differential_cases(self.root, load_profile(), "mapping.json")


if __name__ == "__main__":
    unittest.main()
