"""Complementary Deal controls preserve original cases and reject weak results."""
from __future__ import annotations

import ast
import copy
import json
from pathlib import Path
import tempfile
import unittest

from agentinfra.roadmap_python import backend_observation_key, classify_deal, qualification_backend
from agentinfra.roadmap_records import ContractError


ROOT = Path(__file__).resolve().parents[2]


class DealQualificationTests(unittest.TestCase):
    def run_record(self):
        return {"returncode": 0, "timed_out": False, "stdout_truncated": False, "stderr_truncated": False}

    def observation(self):
        return {"status": "OBSERVED_UNQUALIFIED", "proof": {"conclusion": "OK", "description": "assertion"},
                "solver_results": [{"conclusion": "OK", "description": "assertion"}], "skips": []}

    def test_empty_partial_skipped_or_nested_skip_results_never_receive_result_credit(self):
        for update in ({"solver_results": []}, {"proof": {"conclusion": "OK", "description": "nothing to prove"}},
                       {"proof": {"conclusion": "PARTIAL", "description": "assertion"}},
                       {"proof": {"conclusion": "SKIP", "description": "unsupported"}},
                       {"skips": ["unsupported production operation"]}):
            observation = dict(self.observation(), **update)
            with self.subTest(update=update):
                self.assertEqual(classify_deal(self.run_record(), observation)["outcome"], "UNSUPPORTED_OR_ERROR")

    def test_import_error_timeout_truncation_and_failed_process_are_not_negative_control_detection(self):
        for update in ({"timed_out": True}, {"stdout_truncated": True}, {"stderr_truncated": True}):
            self.assertEqual(classify_deal(dict(self.run_record(), **update), self.observation())["outcome"], "INDETERMINATE")
        self.assertEqual(classify_deal(dict(self.run_record(), returncode=1), self.observation())["outcome"], "UNSUPPORTED_OR_ERROR")
        self.assertEqual(classify_deal(self.run_record(), dict(self.observation(), error={"type": "ImportError"}))["outcome"], "UNSUPPORTED_OR_ERROR")

    def test_solver_ok_remains_semantically_unqualified(self):
        result = classify_deal(self.run_record(), self.observation())
        self.assertEqual(result["outcome"], "TOOL_RESULT_SEMANTICS_UNQUALIFIED")
        self.assertIn("review", result["reason"])

    def test_exception_or_unknown_failure_cannot_claim_the_deliberately_wrong_assertion(self):
        observation = self.observation()
        observation["proof"]["conclusion"] = "FAIL"
        observation["solver_results"][0] = {"conclusion": "FAIL", "description": "ValueError"}
        self.assertEqual(classify_deal(self.run_record(), observation)["outcome"], "UNSUPPORTED_OR_ERROR")
        observation["solver_results"][0]["description"] = "assertion"
        result = classify_deal(self.run_record(), observation)
        self.assertEqual(result["outcome"], "ASSERTION_COUNTEREXAMPLE_UNREVIEWED")
        self.assertIn("identity", result["reason"])

    def test_controls_keep_all_original_calls_bool_case_and_assertion_expressions(self):
        old = ast.parse((ROOT / "verification/roadmap/python/policy_positive.py").read_bytes())
        new = ast.parse((ROOT / "verification/roadmap/python/policy_deal_positive.py").read_bytes())
        targets = {"may_reserve", "all_satisfied", "cgp_eligible"}
        calls = lambda tree: [ast.dump(n, include_attributes=False) for n in ast.walk(tree) if isinstance(n, ast.Call) and
                              isinstance(n.func, ast.Name) and n.func.id in targets]
        self.assertEqual(calls(old), calls(new))
        self.assertEqual(len(calls(new)), 6)
        original_assertions = [ast.dump(n.args[0], include_attributes=False) for n in ast.walk(old)
                               if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "Assert"]
        self.assertEqual(original_assertions, [ast.dump(n.test, include_attributes=False) for n in ast.walk(new) if isinstance(n, ast.Assert)])
        negative = ast.parse((ROOT / "verification/roadmap/python/policy_deal_negative.py").read_bytes())
        self.assertEqual(len(calls(negative)), 1)
        self.assertEqual(calls(negative)[0], calls(new)[0])
        assertions = [n for n in ast.walk(negative) if isinstance(n, ast.Assert)]
        self.assertEqual(len(assertions), 1)
        self.assertIsInstance(assertions[0].test, ast.UnaryOp)
        self.assertIsInstance(assertions[0].test.op, ast.Not)

    def test_fixed_backend_selection_preserves_nagini_ownership_and_rejects_unknown_backend(self):
        self.assertEqual(backend_observation_key("nagini", "toolchain"), "python_toolchain_observation")
        self.assertEqual(backend_observation_key("nagini", "qualification"), "python_qualification_observation")
        self.assertEqual(backend_observation_key("deal", "toolchain"), "python_deal_toolchain_observation")
        self.assertEqual(backend_observation_key("deal", "qualification"), "python_deal_qualification_observation")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "Roadmaps/Shared/python-backends.json"
            path.parent.mkdir(parents=True)
            path.write_text(json.dumps({"active_qualification_backend": "arbitrary-command"}))
            with self.assertRaises(ContractError):
                qualification_backend(root)
            path.write_text("{}")
            self.assertEqual(qualification_backend(root), "nagini")


if __name__ == "__main__":
    unittest.main()
