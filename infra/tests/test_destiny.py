"""Acceptance tests exercise the public command boundary in real Git fixtures."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import patch

FRAMEWORK = Path(__file__).resolve().parents[2]
CLI = FRAMEWORK / "bin/destinyctl.py"


class DestinyFixture(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / "destiny"
        self.root.mkdir()
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        self.write(".gitignore", "target/\nbuild/\n.aegis/\n*.pyc\n")
        self.write("Cargo.toml", '[package]\nname = "destiny-bevy-compat"\nversion = "0.4.0"\n')
        self.write("rust-toolchain.toml", '[toolchain]\nchannel = "1.95.0"\n')
        self.write("src/runtime.rs", "pub fn tick() {}\n")
        self.write("verification/spec/src/catalog.rs", "// original obligations\n")
        self.write("verification/tools/proof_coverage.py", "print('original obligations: 2')\n")
        self.write("verification/tools/pattern_scan.py", "print('[]')\n")

    def write(self, relative, data):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(data, encoding="utf-8")
        return path

    def call(self, *args, ok=True):
        result = subprocess.run([sys.executable, "-B", str(CLI), "--project", str(self.root), *args],
                                capture_output=True, text=True, timeout=20)
        if ok:
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        return json.loads(result.stdout)


class TestDestiny(DestinyFixture):
    def test_actual_queue_keeps_fixture_identities_and_independent_lanes(self):
        sys.path.insert(0,str(FRAMEWORK/"infra"))
        from agentinfra.catalog import work_queue
        from agentinfra.destiny import load_profile
        source="python/test_case.py"
        first=source+"::FirstFixture::test_a"
        second=source+"::SecondFixture::test_a"
        self.write("verification/kani/src/proofs.rs",
            f"// original-test: {source}::test_a\n// original-case: {first}\nfn scenario() {{ assert!(true); }}\n")
        rows=[{"id":identity,"source":source,"fixture":fixture,"test":"test_a",
               "line":1,"original_commit":"0"*40,"original_source_sha256":"1"*64,
               "legacy_marker":source+"::test_a", "legacy_multiplicity":2}
              for identity,fixture in ((first,"FirstFixture"),(second,"SecondFixture"))]
        with patch("agentinfra.catalog.qualified_index",return_value=rows):
            result=work_queue(self.root,load_profile(),SimpleNamespace(original=None,differential=None,output=None))
        self.assertEqual(result["qualified_identities"],2)
        document=json.loads(Path(result["path"]).read_text())
        entries={r["id"]:r for r in document["obligations"]}
        self.assertTrue(entries[first]["assurance"]["mapped_or_marked"])
        self.assertFalse(entries[second]["assurance"]["mapped_or_marked"])
        for row in entries.values():
            self.assertFalse(row["assurance"]["spec_proved"])
            self.assertFalse(row["assurance"]["production_rust_refinement_proved"])
            self.assertFalse(row["assurance"]["runtime_differential_evidence"])

    def test_runtime_plan_is_ordered_and_deduplicated(self):
        plan = self.call("plan", "--changed", "src/runtime.rs", "--changed", "src/runtime.rs")
        ids = [row["id"] for row in plan["checks"]]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertTrue({"rust-test", "python-contract", "native-differential", "kani", "verus"} <= set(ids))
        self.assertLess(ids.index("native-build"), ids.index("native-differential"))
        self.assertEqual(plan["status"], "PLANNED")
        self.assertTrue(all(row["status"] == "NOT_RUN" for row in plan["checks"]))

    def test_python_geometry_routes_to_cross_language_contracts(self):
        ids = {x["id"] for x in self.call("plan", "--changed", "python/destiny/_geometry.py")["checks"]}
        self.assertTrue({"python-contract", "spec-test", "native-differential", "kani", "verus"} <= ids)

    def test_unknown_paths_fail_conservatively_and_empty_is_not_pass(self):
        plan = self.call("plan", "--changed", "new-system/config.txt")
        self.assertIn("new-system/config.txt", plan["unmapped"])
        self.assertTrue(plan["manual_gates"])
        self.assertIn("kani", {x["id"] for x in plan["checks"]})

    def test_release_includes_external_and_platform_gates(self):
        plan = self.call("plan", "--release")
        self.assertTrue({"rust-test", "kani", "verus", "dependency-audit"} <= {x["id"] for x in plan["checks"]})
        self.assertGreaterEqual(len(plan["manual_gates"]), 3)

    def test_changed_paths_cannot_escape(self):
        for path in ("../secret", "/tmp/secret", "src/../../secret", "C:\\outside\\secret"):
            with self.subTest(path=path):
                self.assertEqual(self.call("plan", "--changed", path, ok=False)["status"], "ERROR")

    def test_marker_success_is_an_observation_and_reuse_is_explicit(self):
        first = self.call("run", "proof-markers")
        self.assertEqual(first["status"], "OBSERVED_SUCCESS")
        self.assertEqual(first["claim"], "marker-inventory-only")
        second = self.call("run", "proof-markers")
        self.assertEqual(second["status"], "REUSED")
        self.assertEqual(second["receipt"], first["receipt"])
        self.assertFalse(second["executed"])
        fresh = self.call("run", "proof-markers", "--fresh", "--reason", "release observation")
        self.assertNotEqual(fresh["receipt"], first["receipt"])

    def test_edit_add_delete_and_ignored_cargo_configuration_invalidate(self):
        previous = self.call("run", "proof-markers")["key"]
        for relative, contents in (("src/runtime.rs", "pub fn tick() { panic!() }\n"),
                                   ("src/new.rs", "// new\n"), (".cargo/config.toml", "[net]\noffline=true\n")):
            self.write(relative, contents)
            result = self.call("run", "proof-markers")
            self.assertEqual(result["status"], "OBSERVED_SUCCESS")
            self.assertNotEqual(result["key"], previous)
            previous = result["key"]
        (self.root / "src/new.rs").unlink()
        self.assertNotEqual(self.call("run", "proof-markers")["key"], previous)

    def test_failure_is_not_retried_implicitly_or_promoted(self):
        self.write("verification/tools/proof_coverage.py", "raise SystemExit(3)\n")
        first = self.call("run", "proof-markers", ok=False)
        self.assertEqual(first["status"], "FAILED")
        second = self.call("run", "proof-markers", ok=False)
        self.assertEqual(second["status"], "PREVIOUS_FAILURE")
        self.assertFalse(second["executed"])
        retried = self.call("run", "proof-markers", "--fresh", "--reason", "diagnostic retry", ok=False)
        self.assertEqual(retried["status"], "FAILED")
        self.assertNotEqual(retried["receipt"], first["receipt"])

    def test_generated_outputs_do_not_invalidate_untracked_but_tracked_do(self):
        first = self.call("run", "proof-markers")
        self.write("target/report.log", "new output")
        self.assertEqual(self.call("run", "proof-markers")["key"], first["key"])
        subprocess.run(["git", "add", "-f", "target/report.log"], cwd=self.root, check=True)
        self.assertNotEqual(self.call("run", "proof-markers")["key"], first["key"])

    def test_cache_tampering_is_rejected(self):
        report = self.call("run", "proof-markers")
        path = self.root / report["receipt"]
        data = json.loads(path.read_text())
        data["returncode"] = 123
        path.write_text(json.dumps(data))
        self.assertEqual(self.call("run", "proof-markers", ok=False)["status"], "ERROR")

    def test_redirected_state_and_sources_fail_closed(self):
        outside = Path(self.tmp.name) / "outside"
        outside.mkdir()
        (self.root / ".aegis").symlink_to(outside, target_is_directory=True)
        self.call("run", "proof-markers", ok=False)
        self.assertEqual(list(outside.iterdir()), [])
        (self.root / ".aegis").unlink()
        (self.root / "src/runtime.rs").unlink()
        (self.root / "src/runtime.rs").symlink_to(outside / "secret")
        self.call("run", "proof-markers", ok=False)

    def test_context_is_bounded_and_freshness_does_not_depend_on_mtime(self):
        path = self.write("src/runtime.rs", "λ" * 4000 + "\n")
        first = self.call("context", "src/runtime.rs", "--max-bytes", "1000")
        self.assertLessEqual(len(first["text"].encode()), 1000)
        self.assertTrue(first["truncated"])
        self.assertEqual(first["sha256"], hashlib.sha256(path.read_bytes()).hexdigest())
        self.assertEqual(self.call("context", "src/runtime.rs", "--max-bytes", "1000")["status"], "UNCHANGED")
        before = path.stat()
        path.write_text("μ" * 4000 + "\n")
        os.utime(path, ns=(before.st_atime_ns, before.st_mtime_ns))
        self.assertEqual(self.call("context", "src/runtime.rs", "--max-bytes", "1000")["status"], "READ")
        self.assertEqual(self.call("context", "src/runtime.rs", "--start", "2")["status"], "READ")

    def test_source_mutation_during_check_cannot_be_reused(self):
        self.write("verification/tools/proof_coverage.py", "from pathlib import Path\nPath('src/runtime.rs').write_text('changed')\n")
        result = self.call("run", "proof-markers", ok=False)
        self.assertEqual(result["status"], "INPUTS_CHANGED")

    def test_unknown_check_and_unreasoned_rerun_rejected(self):
        self.call("run", "arbitrary-command", ok=False)
        self.call("run", "proof-markers", "--fresh", ok=False)

    def test_budget_and_native_prerequisite_are_not_pass(self):
        self.assertEqual(self.call("run", "kani", "--budget-seconds", "1", ok=False)["status"], "BUDGET_EXCEEDED")
        self.assertEqual(self.call("run", "native-differential", ok=False)["status"], "UNAVAILABLE")


if __name__ == "__main__":
    unittest.main()
