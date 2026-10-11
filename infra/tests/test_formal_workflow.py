"""Controller regressions using explicit verifier fixtures, not mathematical proof evidence."""
import copy
import hashlib
import json
import os
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

from test_destiny import DestinyFixture, FRAMEWORK


class TestFormalWorkflow(DestinyFixture):
    def setUp(self):
        super().setUp()
        self.write("verification/verus/proofs.rs", "// scoped verifier fixture input\n")
        self.contract = {
            "schema": 1, "objective": "Check a declared fixture invariant",
            "authority_sha256": hashlib.sha256((FRAMEWORK / "contracts/destiny.json").read_bytes()).hexdigest(),
            "reference_review": "Fixture only; no actual original parity claimed",
            "reuse": {"strategy": "reuse", "sources": ["fixture source"], "license": "fixture",
                      "reason": "Exercise the controller boundary", "generator": []},
            "obligations": [{"id": "formation-slot", "invariant": "Fixture declared invariant",
                "method": "verus", "entry": "verification/verus/proofs.rs", "expected_checks": 2,
                "specification": ["verification/spec/src/catalog.rs"], "implementation": ["src/runtime.rs"],
                "proof_inputs": ["verification/verus/proofs.rs"], "assumptions": "Fixture output is synthetic",
                "limits": "No mathematical result or actual Destiny result is asserted"}],
        }

    def save(self):
        self.write(".destiny/plan.json", json.dumps(self.contract))

    def bind(self):
        self.save()
        return self.call("bind", ".destiny/plan.json")

    def verifier(self, output="verification results:: 2 verified, 0 errors", version="0.2026.09.20.aef82ed", extra=""):
        if os.name == "nt":
            self.skipTest("POSIX executable fixture; cross-platform process cases run separately")
        path = Path(self.tmp.name) / "fixture-verus"
        path.write_text(f"#!{sys.executable}\nimport sys\nif '--version' in sys.argv:\n print({version!r})\nelse:\n print({output!r})\n" + extra)
        path.chmod(0o755)
        return str(path)

    def test_binding_is_not_completion_and_source_edits_invalidate_it(self):
        self.assertEqual(self.bind()["status"], "BOUND")
        self.assertEqual(self.call("audit", ok=False)["status"], "INCOMPLETE")
        self.write("src/runtime.rs", "pub fn changed() {}\n")
        self.assertIn("STALE", self.call("verify", "formation-slot", ok=False)["reason"])
        self.assertFalse((self.root / ".aegis/destiny/receipts").exists())

    def test_vacuous_duplicate_and_placeholder_contracts_are_rejected(self):
        original = copy.deepcopy(self.contract)
        invalid = [[], [original["obligations"][0]] * 2]
        for obligations in invalid:
            self.contract = copy.deepcopy(original)
            self.contract["obligations"] = obligations
            self.save()
            self.assertEqual(self.call("bind", ".destiny/plan.json", ok=False)["status"], "ERROR")
        self.contract = copy.deepcopy(original)
        self.contract["obligations"][0]["expected_checks"] = 0
        self.save()
        self.call("bind", ".destiny/plan.json", ok=False)
        self.contract = copy.deepcopy(original)
        self.contract["objective"] = "REPLACE_objective"
        self.save()
        self.call("bind", ".destiny/plan.json", ok=False)

    def test_exact_fresh_observation_audits_and_changed_tool_is_stale(self):
        tool = self.verifier()
        self.bind()
        result = self.call("verify", "formation-slot", "--verus", tool)
        self.assertEqual(result["status"], "CHECKED_SCOPED")
        self.assertTrue(result["result"]["executed"])
        self.assertEqual(self.call("audit")["status"], "CHECKED_SCOPED")
        Path(tool).write_text(Path(tool).read_text() + "# tool changed\n")
        self.assertEqual(self.call("audit", ok=False)["obligations"][0]["status"], "STALE_TOOL")

    def test_wrong_count_and_mismatched_version_are_incomplete(self):
        tool = self.verifier(output="verification results:: 0 verified, 0 errors")
        self.bind()
        self.assertEqual(self.call("verify", "formation-slot", "--verus", tool, ok=False)["status"], "FAILED")
        self.assertEqual(self.call("audit", ok=False)["status"], "INCOMPLETE")
        tool = self.verifier(version="0.2026.09.20.aef82ed-unreviewed")
        self.assertEqual(self.call("verify", "formation-slot", "--verus", tool, ok=False)["status"], "UNAVAILABLE")
        tool = self.verifier(version="0.0.0")
        self.assertEqual(self.call("verify", "formation-slot", "--verus", tool, ok=False)["status"], "UNAVAILABLE")
        self.assertEqual(self.call("audit", ok=False)["status"], "INCOMPLETE")

    def test_ignored_declared_proof_changes_invalidate_binding(self):
        self.write(".gitignore", ".aegis/\nverification/verus/proofs.rs\n")
        self.bind()
        self.write("verification/verus/proofs.rs", "// changed ignored input\n")
        self.assertIn("STALE", self.call("audit", ok=False)["reason"])

    def test_changed_compilation_environment_invalidates_observation(self):
        tool = self.verifier()
        self.bind()
        self.call("verify", "formation-slot", "--verus", tool)
        with patch.dict(os.environ, {"RUSTFLAGS": "--cfg changed_environment"}):
            result = self.call("audit", ok=False)
        self.assertEqual(result["obligations"][0]["status"], "STALE_ENVIRONMENT")

    def test_success_output_does_not_hide_input_change_during_execution(self):
        tool = self.verifier(extra=f"if '--version' not in sys.argv:\n from pathlib import Path\n Path({str(self.root / 'src/runtime.rs')!r}).write_text('changed')\n")
        self.bind()
        self.assertIn("STALE", self.call("verify", "formation-slot", "--verus", tool, ok=False)["reason"])
        self.assertIn("STALE", self.call("audit", ok=False)["reason"])

    def test_repeating_proof_needs_diagnosis_and_never_reuses_cache(self):
        tool = self.verifier()
        self.bind()
        first = self.call("verify", "formation-slot", "--verus", tool)
        denied = self.call("verify", "formation-slot", "--verus", tool, ok=False)
        self.assertIn("diagnosis", denied["reason"])
        second = self.call("verify", "formation-slot", "--verus", tool, "--reason", "Confirm fixture replay")
        self.assertNotEqual(first["result"]["receipt"], second["result"]["receipt"])
        exhausted = self.call("verify", "formation-slot", "--verus", tool, "--reason", "Third identical attempt", ok=False)
        self.assertEqual(exhausted["status"], "BUDGET_EXCEEDED")
        self.assertEqual(self.call("audit", ok=False)["status"], "INCOMPLETE")


if __name__ == "__main__":
    unittest.main()
