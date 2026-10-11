"""Operational boundaries identified during branch reuse and adversarial review."""
from dataclasses import replace
import json
from pathlib import Path
import sys
import unittest

from test_destiny import DestinyFixture

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from agentinfra.destiny_reuse import checked_output
from agentinfra.process import run_process


class TestBranchVerifierReuse(unittest.TestCase):
    def test_exact_nonvacuous_kani_and_verus_inventory(self):
        result = run_process([sys.executable, "-c", "pass"], cwd=Path.cwd())
        obligation = {"method": "kani", "entry": "proofs::formation", "expected_checks": 1}
        good = "Checking harness proofs::formation...\n - Status: SUCCESS\nVERIFICATION:- SUCCESSFUL\nComplete - 1 successfully verified harnesses, 0 failures, 1 total.\n"
        self.assertTrue(checked_output(obligation, replace(result, stdout=good)))
        self.assertTrue(checked_output(obligation, replace(result, stdout=good + "SAT checker: instance is UNSATISFIABLE\n")))
        for text in ("", good * 2, good.replace("proofs::formation", "other"), good + " - Status: UNREACHABLE\n", good + " - Status: FAILURE\n"):
            self.assertFalse(checked_output(obligation, replace(result, stdout=text)))
        for altered in ({"returncode": 1}, {"timed_out": True}, {"stdout_truncated": True}, {"stderr_truncated": True}):
            self.assertFalse(checked_output(obligation, replace(result, stdout=good, **altered)))
        obligation.update(method="verus", expected_checks=2)
        self.assertTrue(checked_output(obligation, replace(result, stdout="verification results:: 2 verified, 0 errors")))
        for text in ("verification results:: 0 verified, 0 errors", "verification results:: 2 verified, 1 errors", "verification results:: 2 verified, 0 errors\n" * 2):
            self.assertFalse(checked_output(obligation, replace(result, stdout=text)))


class TestDestinyHardening(DestinyFixture):
    def test_ignored_marker_inputs_are_fingerprinted(self):
        self.write(".gitignore", ".aegis/\nverification/kani/ignored.rs\n.cargo/\n")
        path = self.write("verification/kani/ignored.rs", "// original-test: example::first\n")
        before = self.call("run", "proof-markers")
        path.write_text("// original-test: example::second\n")
        self.assertNotEqual(self.call("run", "proof-markers")["key"], before["key"])
        before = self.call("run", "proof-markers")
        self.write(".cargo/config.toml", "[net]\noffline=true\n")
        self.assertNotEqual(self.call("run", "proof-markers")["key"], before["key"])

    def test_budget_reservations_prevent_repeated_fresh_runs(self):
        self.call("run", "proof-markers")
        self.call("run", "proof-markers", "--fresh", "--reason", "second observation")
        third = self.call("run", "proof-markers", "--fresh", "--reason", "unbounded rerun", ok=False)
        self.assertEqual(third["status"], "BUDGET_EXCEEDED")
        reservations = list((self.root / ".aegis/destiny/attempts").glob("*.json"))
        self.assertEqual(len(reservations), 1)
        self.assertEqual(len(json.loads(reservations[0].read_text())["attempts"]), 2)

    def test_redaction_still_respects_context_byte_budget(self):
        self.write("src/runtime.rs", "token=x\n")
        response = self.call("context", "src/runtime.rs", "--max-bytes", "7")
        self.assertLessEqual(len(response["text"].encode()), 7)

    def test_context_handles_long_lines_and_out_of_range_selection(self):
        self.write("src/runtime.rs", "x" * 200_000 + "\nselected\n")
        response = self.call("context", "src/runtime.rs", "--max-bytes", "100")
        self.assertEqual(len(response["text"]), 100)
        self.assertTrue(response["truncated"])
        response = self.call("context", "src/runtime.rs", "--start", "2", "--max-bytes", "100")
        self.assertEqual(response["text"], "selected\n")
        response = self.call("context", "src/runtime.rs", "--start", "30", "--max-bytes", "100")
        self.assertEqual(response["text"], "")

    def test_ignore_policy_changes_select_full_matrix(self):
        ids = {row["id"] for row in self.call("plan", "--changed", ".gitignore")["checks"]}
        self.assertIn("kani", ids)

    def test_duplicate_json_keys_do_not_override_receipt_fields(self):
        result = self.call("run", "proof-markers")
        receipt = self.root / result["receipt"]
        text = receipt.read_text()
        receipt.write_text(text.replace('"returncode": 0', '"returncode": 7, "returncode": 0'))
        self.assertEqual(self.call("run", "proof-markers", ok=False)["status"], "ERROR")


if __name__ == "__main__":
    unittest.main()
