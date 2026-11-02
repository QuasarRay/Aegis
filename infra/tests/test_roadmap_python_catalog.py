"""Source/fixture identity regressions; no verifier or model inference is run."""
from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from agentinfra.roadmap_python import original_occurrences
from agentinfra.roadmap_python_catalog import fixture_catalog, runtime_bindings
from agentinfra.roadmap_records import ContractError


class OriginalFixtureCatalogTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        package = self.root / "infra/agentinfra"
        package.mkdir(parents=True)
        (package / "__init__.py").write_text("PACKAGE_STATE = {'enabled': True}\n")
        self.helper = package / "helper.py"
        self.helper.write_text("def real(x: int) -> int:\n    return x + 1\ndef unused():\n    return 1\n")
        tests = self.root / "infra/tests"
        tests.mkdir()
        self.test_source = tests / "test_example.py"
        self.test_source.write_text(
            "import unittest\nfrom agentinfra.helper import real\n"
            "def setUpModule():\n    pass\n"
            "def tearDownModule():\n    pass\n"
            "class Base(unittest.TestCase):\n"
            "    def setUp(self):\n        self.value = real(2)\n        self.addCleanup(self.cleanup)\n"
            "    def cleanup(self):\n        self.value = None\n"
            "    def tearDown(self):\n        self.value = None\n"
            "class Example(Base):\n"
            "    def test_rules(self):\n"
            "        with self.assertRaises(ValueError):\n            raise ValueError('expected')\n"
            "        for item in (1, 2):\n"
            "            with self.subTest(item=item):\n                self.assertEqual(real(item), item + 1)\n")

    def catalog(self):
        return fixture_catalog(self.root, original_occurrences(self.root))

    def test_inherited_setup_cleanup_module_hooks_assertions_and_quantification_bound(self):
        fixtures, closures = self.catalog()
        self.assertEqual(len(fixtures), 1)
        record = next(iter(fixtures.values()))
        self.assertEqual({d["declared_name"] for d in record["fixture_definitions"]}, {"Example", "Base"})
        self.assertEqual(record["external_bases"], ["unittest.TestCase"])
        fields = record["semantic_source_fields"]
        self.assertEqual(fields["fixture_setup"]["hooks"][0]["declared_name"], "setUp")
        self.assertEqual(fields["fixture_teardown"]["hooks"][0]["declared_name"], "tearDown")
        self.assertEqual({h["declared_name"] for h in fields["fixture_setup"]["module_hooks"]}, {"setUpModule", "tearDownModule"})
        self.assertEqual(fields["helpers"]["definitions"][0]["declared_name"], "cleanup")
        self.assertEqual(len(fields["assertions"]["nodes"]), 2)
        self.assertEqual(len(fields["exceptions"]["nodes"]), 1)
        self.assertEqual(len(fields["quantification"]["nodes"]), 2)
        self.assertIn("no invented universal", fields["quantification"]["interpretation"])
        self.assertIn("infra/agentinfra/helper.py", {b["path"] for b in closures[record["source_closure"]]["files"]})
        self.assertFalse(record["domain_proof"])

    def test_unused_imported_helper_change_invalidates_full_fixture_semantics(self):
        first, _ = self.catalog()
        self.helper.write_text(self.helper.read_text().replace("return 1", "return 7"))
        second, _ = self.catalog()
        self.assertEqual(set(first), set(second))
        self.assertNotEqual(next(iter(first.values()))["digest"], next(iter(second.values()))["digest"])

    def test_runtime_pass_is_only_a_finite_source_matched_observation(self):
        fixtures, _ = self.catalog()
        key, fixture = next(iter(fixtures.items()))
        details = {"source_files": [fixture["location"]["source"]],
                   "occurrences": [{"id": fixture["runtime_id"], "outcome": "PASS", "subtests": [{"id": "item=1", "outcome": "PASS"}]}]}
        result = runtime_bindings(self.root, fixtures, details)
        self.assertEqual(result["fixtures"][key]["status"], "OBSERVED_PASS_RUNTIME_ONLY")
        self.assertEqual(result["original_test_translation_review"], "NOT_GRANTED")
        self.assertFalse(result["domain_proof"])
        self.test_source.write_text(self.test_source.read_text() + "\nNEW_MODULE_STATE = 1\n")
        stale = runtime_bindings(self.root, fixtures, details)
        self.assertEqual(stale["fixtures"][key]["status"], "MISSING_OR_STALE_EXECUTED_SOURCE")

    def test_shadowed_fixture_name_cannot_collapse_two_source_occurrences(self):
        self.test_source.write_text("import unittest\nclass Example(unittest.TestCase):\n def test_same(self):\n  self.assertTrue(True)\nclass Example(unittest.TestCase):\n def test_same(self):\n  self.assertFalse(False)\n")
        fixtures, _ = self.catalog()
        self.assertEqual(len(fixtures), 2)
        fixture = next(iter(fixtures.values()))
        result = runtime_bindings(self.root, fixtures, {"source_files": [fixture["location"]["source"]],
                                  "occurrences": [{"id": fixture["runtime_id"], "outcome": "PASS"}]})
        self.assertEqual({r["status"] for r in result["fixtures"].values()}, {"AMBIGUOUS_RUNTIME_SOURCE_OCCURRENCE"})

    def test_dynamic_unmatched_and_duplicate_runtime_occurrences_are_not_discarded(self):
        fixtures, _ = self.catalog()
        result = runtime_bindings(self.root, fixtures, {"source_files": [], "occurrences": [{"id": "dynamic.generated.test", "outcome": "PASS"}]})
        self.assertEqual(result["unmatched_runtime_ids"], ["dynamic.generated.test"])
        with self.assertRaises(ContractError):
            runtime_bindings(self.root, fixtures, {"source_files": [], "occurrences": [{"id": "same", "outcome": "PASS"}, {"id": "same", "outcome": "PASS"}]})

    def test_changed_original_method_body_cannot_reuse_a_static_location(self):
        locations = original_occurrences(self.root)
        self.test_source.write_text(self.test_source.read_text().replace("item + 1", "item + 2"))
        with self.assertRaises(ContractError):
            fixture_catalog(self.root, locations)

    def test_new_runtime_witness_changes_route_spec_without_changing_code_candidate(self):
        from agentinfra.roadmap import compile_roadmaps
        from agentinfra.roadmap_work import materialize
        root = Path(__file__).resolve().parents[2]
        compiled = compile_roadmaps(root)
        dependency = {"path": ".aegis/fixture-only/original-test-result.json", "sha256": "a" * 64}
        with patch("agentinfra.roadmap_work.ProjectAdapter") as adapter, patch("agentinfra.roadmap_protocol.native_executable", return_value={"path": "/fixture/codex", "sha256": "b" * 64, "version": "fixture"}):
            adapter.return_value.read.return_value = {"execution": {"native_turn_configuration": {"model": "fixture-selected", "effort": "max", "mode": "default"}}}
            with patch("agentinfra.roadmap_python_catalog.test_receipt_dependencies", return_value=[]):
                before = materialize(root, compiled, "A09", "python.route")
            with patch("agentinfra.roadmap_python_catalog.test_receipt_dependencies", return_value=[dependency]):
                after = materialize(root, compiled, "A09", "python.route")
        self.assertEqual(before["candidate"], after["candidate"])
        self.assertNotEqual(before["digest"], after["digest"])
        self.assertIn(dependency, after["inputs"])
        self.assertEqual(after["selection"]["original_test_dependencies"], [dependency])


if __name__ == "__main__":
    unittest.main()
