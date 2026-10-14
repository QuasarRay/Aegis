"""Operational boundaries identified during branch reuse and adversarial review."""
from dataclasses import replace
import json
import io
import tarfile
import hashlib
from pathlib import Path
import subprocess
import sys
import unittest

from test_destiny import DestinyFixture

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from agentinfra.destiny_reuse import checked_output
from agentinfra.process import run_process
from agentinfra.destiny import source_snapshot, registry_source_files
from agentinfra.context_cache import sha256_file


class TestBranchVerifierReuse(unittest.TestCase):
    def test_scoped_kani_preserves_features_contracts_and_exact_selection(self):
        from agentinfra.destiny import scoped_kani_commands
        commands=[["cargo","kani","-Z","function-contracts","--features","production-kernels",
            "--manifest-path","old/Cargo.toml","--output-format=terse"]]
        self.assertEqual(scoped_kani_commands(commands,"verification/kani/Cargo.toml","module::contract"),
            [["cargo","kani","-Z","function-contracts","--features","production-kernels",
              "--manifest-path","verification/kani/Cargo.toml","--harness","module::contract",
              "--exact","--force-build","--output-format","regular"]])
        for invalid in ([],commands+commands,[["kani"]],[["cargo","kani","--harness","other"]],
                        [["cargo","kani","--output-format"]]):
            with self.assertRaises(ValueError):scoped_kani_commands(invalid,"Cargo.toml","module::contract")

    def test_scoped_verus_preserves_registered_configuration_and_exact_entry(self):
        from agentinfra.destiny import scoped_verus_commands
        entry="verification/verus/concurrent.rs"
        configured=["{verus}","--crate-type=lib","--cfg","checked_model","--log","vir",entry]
        commands=[configured,["{verus}","--crate-type=lib","other.rs"]]
        self.assertEqual(scoped_verus_commands(commands,entry,{"verus":"/verified/verus"}),
                         [["/verified/verus",*configured[1:]]])
        for invalid in ([],[configured,configured]):
            with self.assertRaises(ValueError):scoped_verus_commands(invalid,entry,{"verus":"/verified/verus"})

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
    def test_proof_registry_payload_binds_actual_math_source_and_build_script(self):
        self.write("verification/kani/Cargo.toml", "[package]\nname='proof'\nversion='0.1.0'\n")
        home = self.root / "cargo-home"
        tree = home / "registry/src/fixture-index/libm-0.2.16"
        tree.mkdir(parents=True)
        implementation = tree / "exp.rs"
        implementation.write_text("original math\n")
        (tree / "build.rs").write_text("original build\n")
        archive = home / "registry/cache/fixture-index/libm-0.2.16.crate"
        archive.parent.mkdir(parents=True)
        with tarfile.open(archive, "w:gz") as release:
            for source in (implementation, tree / "build.rs"):
                data = source.read_bytes()
                member = tarfile.TarInfo("libm-0.2.16/" + source.name)
                member.size = len(data)
                release.addfile(member, io.BytesIO(data))
        checksum = hashlib.sha256(archive.read_bytes()).hexdigest()
        self.write("verification/kani/Cargo.lock", "version=4\n[[package]]\nname='libm'\nversion='0.2.16'\nsource='registry+https://github.com/rust-lang/crates.io-index'\nchecksum='" + checksum + "'\n")
        env = {"CARGO_HOME": str(home)}
        files = registry_source_files(self.root, "verification/kani/Cargo.toml", env)
        self.assertIn(implementation, files)
        self.assertIn(tree / "build.rs", files)
        implementation.write_text("changed math\n")
        with self.assertRaisesRegex(ValueError, "source differs from locked archive"):
            registry_source_files(self.root, "verification/kani/Cargo.toml", env)
        archive.write_bytes(b"wrong release")
        with self.assertRaisesRegex(ValueError, "release checksum differs"):
            registry_source_files(self.root, "verification/kani/Cargo.toml", env)

    def test_embedded_repositories_bind_controller_and_vendor_source_separately(self):
        for name in (".agents", "vendor/dependency"):
            directory = self.root / name
            directory.mkdir(parents=True)
            subprocess.run(["git", "init", "-q", str(directory)], check=True)
            (directory / "source.rs").write_text("original source\n")
            (directory / ".gitignore").write_text(".aegis/\n.cargo/\n")
            subprocess.run(["git", "-C", str(directory), "add", "."], check=True)
            subprocess.run(["git", "-C", str(directory), "-c", "user.name=Fixture",
                            "-c", "user.email=fixture@example.invalid", "commit", "-qm", "fixture"], check=True)
        before = source_snapshot(self.root)
        self.assertEqual(set(before["repositories"]), {".agents", "vendor/dependency"})
        for name in (".agents", "vendor/dependency"):
            directory = self.root / name
            (directory / "source.rs").write_text("edited source\n")
            edited = source_snapshot(self.root)
            self.assertNotEqual(edited["digest"], before["digest"])
            self.assertNotEqual(edited["repositories"][name]["source"], before["repositories"][name]["source"])
            before = edited
            (directory / "untracked.rs").write_text("new source\n")
            self.assertNotEqual(source_snapshot(self.root)["digest"], before["digest"])
            before = source_snapshot(self.root)
            (directory / ".cargo").mkdir()
            (directory / ".cargo/config.toml").write_text("[net]\noffline = true\n")
            self.assertNotEqual(source_snapshot(self.root)["digest"], before["digest"])
            before = source_snapshot(self.root)
            (directory / ".aegis").mkdir()
            (directory / ".aegis/receipt.json").write_text("{}\n")
            self.assertEqual(source_snapshot(self.root), before)

    def test_directory_glob_is_not_silently_ignored(self):
        (self.root / "ordinary").mkdir()
        with self.assertRaisesRegex(ValueError, "not a separate Git repository"):
            source_snapshot(self.root, ["ordinary"])

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
