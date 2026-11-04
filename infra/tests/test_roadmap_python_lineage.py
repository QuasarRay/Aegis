"""Attempt-history cache regression; no verifier/process execution or proof."""
from pathlib import Path
import unittest
from unittest.mock import patch

from agentinfra.roadmap import compile_roadmaps
from agentinfra.roadmap_python_catalog import qualification_lineage_digest
from agentinfra.roadmap_work import materialize


class QualificationLineageTests(unittest.TestCase):
    def test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged(self):
        root = Path(__file__).resolve().parents[2]
        compiled = compile_roadmaps(root)
        with patch("agentinfra.roadmap_python_catalog._qualification_evidence", return_value=({"retained_attempt_ids": ["selected"]}, None, [])):
            before_lineage = qualification_lineage_digest(root)
        with patch("agentinfra.roadmap_python_catalog._qualification_evidence", return_value=({"retained_attempt_ids": ["selected", "later-failed"]}, None, [])):
            after_lineage = qualification_lineage_digest(root)
        self.assertNotEqual(before_lineage, after_lineage)
        with patch("agentinfra.roadmap_work.ProjectAdapter") as adapter, \
             patch("agentinfra.roadmap_protocol.native_executable", return_value={"path": "/fixture/codex", "sha256": "b" * 64, "version": "fixture"}), \
             patch("agentinfra.roadmap_python_catalog.test_receipt_dependencies", return_value=[]), \
             patch("agentinfra.roadmap_python_catalog.qualification_receipt_dependencies", return_value=[]):
            adapter.return_value.read.return_value = {"execution": {"native_turn_configuration": {"model": "fixture", "effort": "max", "mode": "default"}}}
            with patch("agentinfra.roadmap_python_catalog.qualification_lineage_digest", return_value=before_lineage):
                before = materialize(root, compiled, "A09", "python.route")
            with patch("agentinfra.roadmap_python_catalog.qualification_lineage_digest", return_value=after_lineage):
                after = materialize(root, compiled, "A09", "python.route")
        self.assertEqual(before["candidate"], after["candidate"])
        self.assertEqual(before["inputs"], after["inputs"])
        self.assertNotEqual(before["digest"], after["digest"])
        self.assertEqual(after["selection"]["qualification_lineage_digest"], after_lineage)


if __name__ == "__main__":
    unittest.main()
