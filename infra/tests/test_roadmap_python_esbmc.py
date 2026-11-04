"""ESBMC archive, source-selection and evidence boundaries; no verifier runs."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import stat
import tempfile
import unittest
import zipfile

from agentinfra.roadmap_python import classify_esbmc, esbmc_arguments, esbmc_link_state
from agentinfra.roadmap_records import ContractError
from agentinfra.roadmap_runtime import retry_limits
import test_roadmap_mirrors as mirror_support


ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("_aegis_esbmc_test_support", ROOT / "scripts/roadmap_esbmc.py")
SUPPORT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SUPPORT)


class EsbmcQualificationTests(unittest.TestCase):
    def test_fixed_command_selects_original_function_and_keeps_assertion_and_domain_checks(self):
        tool = {"backend": "esbmc-python", "executable": "/pinned/esbmc", "python": "/pinned/python"}
        fixture = "verification/roadmap/python/policy_deal_positive.py"
        argv = esbmc_arguments(ROOT, tool, fixture)
        self.assertEqual(argv[:2], [tool["executable"], str(ROOT / fixture)])
        self.assertEqual(argv[argv.index("--function") + 1], "original_budget_and_completion")
        self.assertEqual(argv[argv.index("--python") + 1], tool["python"])
        self.assertIn("--ir", argv)
        self.assertIn("--multi-property", argv)
        self.assertFalse(set(argv) & {"--unwind", "--no-assertions", "--python-ignore-assertions", "--no-unwinding-assertions", "--strict-types"})
        negative = esbmc_arguments(ROOT, tool, "verification/roadmap/python/policy_deal_negative.py")
        self.assertEqual(negative[negative.index("--function") + 1], "deliberately_wrong_budget_assertion")
        self.assertEqual(esbmc_arguments(ROOT, tool, fixture, claims=True)[-1], "--show-claims")
        with self.assertRaises(ContractError):
            esbmc_arguments(ROOT, tool, "unrelated-model.py")

    def test_cli_success_without_property_model_review_cannot_become_proof(self):
        run = {"returncode": 0, "stdout": "VERIFICATION SUCCESSFUL", "stderr": ""}
        self.assertEqual(classify_esbmc(run)["outcome"], "TOOL_VERDICT_PROPERTIES_UNQUALIFIED")
        self.assertEqual(classify_esbmc(dict(run, stdout="VERIFICATION SUCCESSFUL\nERROR: unsupported import"))["outcome"], "UNSUPPORTED_OR_ERROR")
        self.assertEqual(classify_esbmc(dict(run, stdout="nothing happened"))["outcome"], "UNSUPPORTED_OR_ERROR")

    def test_negative_verdict_timeout_and_truncation_cannot_claim_original_assertion_detection(self):
        run = {"returncode": 10, "stdout": "VERIFICATION FAILED", "stderr": ""}
        self.assertEqual(classify_esbmc(run)["outcome"], "FAILURE_PROPERTY_UNREVIEWED")
        for update in ({"timed_out": True}, {"stdout_truncated": True}, {"stderr_truncated": True}, {"stdout": "Timed out"}):
            self.assertEqual(classify_esbmc(dict(run, **update))["outcome"], "INDETERMINATE")

    def test_consumed_amendment_preserves_failed_history_without_freezing_later_policy(self):
        fixture = mirror_support.RetryScopeTests()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        fixture.bind()
        (fixture.root / "pin.json").write_text("new reviewed mirror policy")
        with fixture.state(), self.assertRaisesRegex(ContractError, "inputs changed"):
            retry_limits(fixture.root, "A09", "python.toolchain", 2, 1800)
        consumed = dict(fixture.prior[-1], id="consumed", status="SUCCESS")
        later = dict(consumed, id="later", generation=2)
        with fixture.state([*fixture.prior, consumed, later]):
            self.assertEqual(retry_limits(fixture.root, "A09", "python.toolchain", 2, 1800, candidate="new-target"),
                             {"max_attempts": 2, "total_seconds": 1800})
        self.assertEqual(fixture.amendment["prior_attempts"], fixture.prior)


class EsbmcArchiveTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.archive = self.root / "release.zip"
        self.destination = self.root / "release"

    def archive_entries(self, entries):
        with zipfile.ZipFile(self.archive, "w") as archive:
            for name, content, mode in entries:
                entry = zipfile.ZipInfo(name)
                entry.create_system = 3
                entry.external_attr = mode << 16
                archive.writestr(entry, content)

    def test_regular_bytes_exec_permissions_and_internal_link_identity_are_preserved(self):
        self.archive_entries([("pkg/bin/esbmc", b"test-only-binary", stat.S_IFREG | 0o755),
                              ("pkg/lib/data", b"test model", stat.S_IFREG | 0o644),
                              ("pkg/lib/alias", b"data", stat.S_IFLNK | 0o777)])
        SUPPORT.extract_release(self.root, self.archive, self.destination)
        self.assertEqual((self.destination / "pkg/bin/esbmc").read_bytes(), b"test-only-binary")
        self.assertTrue((self.destination / "pkg/bin/esbmc").stat().st_mode & stat.S_IXUSR)
        marker = json.loads((self.destination / "aegis-release-identity.json").read_text())
        tool = {"release_root": "release", "symlinks": marker["symlinks"]}
        self.assertTrue(all(x["safe"] and x["observed"] == x["expected"] for x in esbmc_link_state(self.root, tool)))
        SUPPORT.extract_release(self.root, self.archive, self.destination)
        link = self.destination / "pkg/lib/alias"
        link.unlink()
        link.symlink_to("../bin/esbmc")
        self.assertNotEqual(esbmc_link_state(self.root, tool)[0]["observed"], esbmc_link_state(self.root, tool)[0]["expected"])
        with self.assertRaisesRegex(ContractError, "symlinks changed"):
            SUPPORT.extract_release(self.root, self.archive, self.destination)

    def test_traversal_special_files_and_duplicates_are_rejected(self):
        for entries in ([('../outside', b'x', stat.S_IFREG | 0o644)],
                        [('device', b'x', stat.S_IFCHR | 0o600)],
                        [('same', b'x', stat.S_IFREG | 0o644), ('same', b'y', stat.S_IFREG | 0o644)]):
            with self.subTest(entries=entries):
                self.archive_entries(entries)
                with self.assertRaises(ContractError):
                    SUPPORT.extract_release(self.root, self.archive, self.destination)
                self.assertFalse(self.destination.exists())

    def test_escaping_link_and_interrupted_staging_require_recovery(self):
        self.archive_entries([('escape', b'../../outside', stat.S_IFLNK | 0o777)])
        with self.assertRaisesRegex(ContractError, "escapes"):
            SUPPORT.extract_release(self.root, self.archive, self.destination)
        self.assertTrue(self.destination.with_name("release.staging").exists())
        with self.assertRaisesRegex(ContractError, "interrupted"):
            SUPPORT.extract_release(self.root, self.archive, self.destination)
