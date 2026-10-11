"""Recovery regressions: missing cache indexes do not erase consumed attempts."""
import json
from pathlib import Path
import sys
import subprocess
import unittest
from unittest.mock import patch

from test_destiny import DestinyFixture

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from agentinfra.context_cache import ContextLedger
from agentinfra.destiny import context, load_profile
from types import SimpleNamespace


class TestDestinyRecovery(DestinyFixture):
    def test_original_reference_is_pinned_before_execution(self):
        self.write("verification/tools/run_original_formation_tests.py", "print('wrong reference would run')\n")
        subprocess.run(["git", "add", "."], cwd=self.root, check=True, capture_output=True)
        subprocess.run(["git", "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                        "commit", "-qm", "fixture"], cwd=self.root, check=True, capture_output=True)
        library = Path(self.tmp.name) / "native-library"
        library.write_bytes(b"fixture")
        result = self.call("run", "original-formations", "--original", str(self.root), "--library", str(library), ok=False)
        self.assertEqual(result["status"], "ERROR")
        self.assertFalse(result["executed"])
        self.assertIn("reference revision", result["reason"])

    def test_interrupted_attempt_needs_diagnosis_before_retry(self):
        result = self.call("run", "proof-markers")
        (self.root / ".aegis/destiny/cache" / (result["key"] + ".json")).unlink()
        denied = self.call("run", "proof-markers", ok=False)
        self.assertEqual(denied["status"], "ERROR")
        self.assertIn("diagnosis", denied["reason"])
        attempts = json.loads(next((self.root / ".aegis/destiny/attempts").glob("*.json")).read_text())
        self.assertEqual(len(attempts["attempts"]), 1)

    def test_no_unchanged_claim_after_a_context_read_race(self):
        original = ContextLedger.record_file
        changed = False

        def race(ledger, path, conclusion="", dependencies=()):
            nonlocal changed
            if not changed:
                path.write_text("new source\n")
                changed = True
            return original(ledger, path, conclusion, dependencies)

        args = SimpleNamespace(path="src/runtime.rs", start=1, lines=100, max_bytes=1000, fresh=False)
        with patch.object(ContextLedger, "record_file", race):
            with self.assertRaisesRegex(RuntimeError, "changed while reading"):
                context(self.root, load_profile(), args)
        self.assertEqual(context(self.root, load_profile(), args)["status"], "READ")


if __name__ == "__main__":
    unittest.main()
