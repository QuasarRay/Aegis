"""A09 regressions: retained source closure, honest tool strength and ownership."""
from __future__ import annotations

import ast
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest

from agentinfra.process import run_process
from agentinfra.roadmap import compile_roadmaps
from agentinfra.roadmap_python import (classify_nagini, original_occurrences, python_proof_errors,
                                      research_sources, route, source_closure)
from agentinfra.roadmap_portability import maintained_python
from agentinfra.roadmap_records import ContractError, digest


ROOT = Path(__file__).resolve().parents[2]


class PythonSourceClosureTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.package = self.root / "infra/agentinfra"
        self.package.mkdir(parents=True)
        (self.package / "__init__.py").write_text("PACKAGE_STATE = {'active': True}\n")
        (self.package / "dependency.py").write_text("def private_unused():\n    return 3\n")
        (self.package / "policy.py").write_text("from . import dependency\nimport pathlib\ndef policy(x: int) -> int:\n    return x + 1\ndef hidden(x):\n    return getattr(x, 'value')\n")

    def test_whole_imported_modules_and_package_state_remain_bound(self):
        before = source_closure(self.root, "agentinfra.policy:policy")
        self.assertEqual({b["path"] for b in before["files"]}, {"infra/agentinfra/__init__.py", "infra/agentinfra/policy.py", "infra/agentinfra/dependency.py"})
        (self.package / "dependency.py").write_text("def private_unused():\n    return 4\n")
        after = source_closure(self.root, "agentinfra.policy:policy")
        self.assertNotEqual(before["digest"], after["digest"])
        self.assertEqual(before["target_ast_sha256"], after["target_ast_sha256"])

    def test_unreachable_dynamic_code_and_external_effects_are_retained(self):
        record = source_closure(self.root, "agentinfra.policy:policy")
        self.assertFalse(record["semantic_closure_proved"])
        self.assertTrue(record["hazards"])
        self.assertEqual(record["external"][0]["module"], "pathlib")
        self.assertTrue(record["external"][0]["runtime_effect_boundary"])

    def test_shadowed_target_is_not_arbitrarily_selected(self):
        path = self.package / "policy.py"
        path.write_text(path.read_text() + "\ndef policy(x):\n    return 7\n")
        with self.assertRaises(ContractError):
            source_closure(self.root, "agentinfra.policy:policy")


class PythonQualificationTests(unittest.TestCase):
    def test_routes_retain_complete_domain_and_source_denominators(self):
        compiled = compile_roadmaps(ROOT)
        record = route(ROOT, compiled, "regression-candidate")
        expected = {o["id"] for c in compiled["milestones"].values() if c["project"] == "Aegis" and
                    c["phase"] != "modernization" for o in c["proof_obligations"]}
        self.assertEqual({o["id"] for o in record["obligations"]}, expected)
        self.assertEqual({b["path"] for b in record["source_files"]}, {p.relative_to(ROOT).as_posix() for p in maintained_python(ROOT)})
        self.assertTrue(record["source_units"])
        self.assertTrue(all(o["qualified_backend"] is None for o in record["obligations"]))
        self.assertFalse(record["domain_proof"])

    def test_research_archive_denominator_and_original_report_retained(self):
        record = research_sources(ROOT)
        self.assertEqual(len(record["chapters"]), 13)
        self.assertEqual(len(record["recommendations"]), 24)
        self.assertEqual(record["report"]["sha256"], digest((ROOT / record["report"]["path"]).read_bytes()))

    def test_static_original_locations_do_not_claim_dynamic_fixture_closure(self):
        locations = original_occurrences(ROOT)
        original = [r for r in locations if r["fixture"] == "DomainPolicyTests" and r["test"] == "test_budgets_and_completion"]
        self.assertEqual(len(original), 1)
        self.assertEqual(original[0]["status"], "REQUIRES_FULL_FIXTURE_AND_RUNTIME_OCCURRENCE_CLOSURE")
        self.assertEqual(len({r["id"] for r in locations}), len(locations))

    def test_cli_success_text_cannot_hide_unsupported_or_truncated_result(self):
        base = dict(returncode=0, stdout="Verification successful.", stderr="", timed_out=False,
                    stdout_truncated=False, stderr_truncated=False)
        self.assertEqual(classify_nagini(base)["outcome"], "VERIFIED_TOOL_RESULT")
        for field in ("timed_out", "stdout_truncated", "stderr_truncated"):
            self.assertEqual(classify_nagini(dict(base, **{field: True}))["outcome"], "INDETERMINATE")
        self.assertEqual(classify_nagini(dict(base, stderr="Unsupported construct"))["outcome"], "UNSUPPORTED_OR_ERROR")
        self.assertEqual(classify_nagini(dict(base, returncode=1))["outcome"], "UNSUPPORTED_OR_ERROR")

    def test_failed_import_is_not_a_successful_negative_control(self):
        run = dict(returncode=1, stdout="Verification failed. assert.failed", stderr="Traceback: ImportError")
        self.assertEqual(classify_nagini(run)["outcome"], "UNSUPPORTED_OR_ERROR")
        self.assertEqual(classify_nagini(dict(run, stderr=""))["outcome"], "ASSERTION_COUNTEREXAMPLE")

    def test_unqualified_python_backend_rejects_synthetic_proved_claim(self):
        for backend in ("nagini", "esbmc-python", "deal"):
            with self.subTest(backend=backend):
                self.assertTrue(python_proof_errors(ROOT, {"backend": backend}, {"status": "PROVED", "executed": True}))
        self.assertEqual(python_proof_errors(ROOT, {"backend": "kani"}, {}), [])

    def test_merely_editing_matrix_cannot_qualify_an_execution_adapter(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shared = root / "Roadmaps/Shared"
            shared.mkdir(parents=True)
            qualification = shared / "qualification.json"
            qualification.write_text(json.dumps({"toolchain": {"version": "fake"}, "status": "QUALIFIED"}))
            binding = {"path": "Roadmaps/Shared/qualification.json", "sha256": digest(qualification.read_bytes())}
            (shared / "python-backends.json").write_text(json.dumps({"backends": [{"name": "Nagini", "status": "QUALIFIED", "qualified_producer": binding}]}))
            errors = python_proof_errors(root, {"backend": "nagini", "toolchain": {"version": "fake"}}, {"python_qualification": binding})
            self.assertTrue(any("adapter" in error for error in errors))

    @unittest.skipUnless(os.name == "posix", "inherited group qualification is POSIX only")
    def test_outer_timeout_cleans_inherited_nested_stage(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            marker = root / "child.json"
            code = ("import json,os,pathlib,sys; sys.path.insert(0, " + repr(str(ROOT / "infra")) + "); "
                    "from agentinfra.process import run_recipe_stage; "
                    "run_recipe_stage([sys.executable,'-c'," + repr("import json,os,pathlib,time; pathlib.Path(" + repr(str(marker)) + ").write_text(json.dumps({'pid':os.getpid(),'group':os.getpgrp()})); time.sleep(60)") + "],cwd=pathlib.Path(" + repr(str(root)) + "),timeout=60)")
            compile(ast.parse(code), "nested-group-control", "exec")
            result = run_process([sys.executable, "-B", "-c", code], cwd=root, timeout=2)
            self.assertTrue(result.timed_out)
            observed = json.loads(marker.read_text())
            self.assertNotEqual(observed["pid"], observed["group"])
            stat = Path("/proc") / str(observed["pid"]) / "stat"
            if stat.exists():
                self.assertEqual(stat.read_text().rsplit(")", 1)[1].split()[0], "Z")


if __name__ == "__main__":
    unittest.main()
