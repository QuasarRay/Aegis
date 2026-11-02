from __future__ import annotations

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "infra"))
from agentinfra.roadmap_interfaces import compare_interfaces, observe_interfaces
from agentinfra.roadmap_records import ContractError


class ModuleInterfaceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory();self.root = Path(self.temp.name)
        self.package = self.root / "infra/agentinfra";self.package.mkdir(parents=True)
        (self.package / "__init__.py").write_text('INTERFACE_VERSION = 1\n__version__ = "fixture"\n')
        (self.package / "roadmap_policy.py").write_text("def policy(x, *, bound=3):\n return x < bound\nclass Rules:\n def __enter__(self): return self\n def check(self, x): return x\n")
        shared = self.root / "Roadmaps/Shared";shared.mkdir(parents=True)
        shutil.copyfile(ROOT / "Roadmaps/Shared/records.schema.json", shared / "records.schema.json")
        self.git("init", "--initial-branch=dev");self.git("add", ".");self.git("commit", "-m", "baseline")

    def git(self, *args):
        return subprocess.run(["git", "-c", "user.name=Aegis fixture", "-c", "user.email=fixture@example.invalid",
                               "-c", "commit.gpgsign=false", *args], cwd=self.root,
                              capture_output=True, text=True, check=True, timeout=30).stdout

    def tearDown(self):
        self.temp.cleanup()

    def test_observation_does_not_execute_source_and_retains_lifecycle_methods(self):
        path = self.package / "roadmap_policy.py"
        path.write_text(path.read_text() + '\nraise RuntimeError("must not execute source")\n')
        value = observe_interfaces(self.root)
        policy = next(m for m in value["modules"] if m["module"] == "agentinfra.roadmap_policy")
        self.assertIn("__enter__", policy["exports"]["Rules"][0]["methods"])
        self.assertEqual(compare_interfaces(self.root, "HEAD")["changes"], [])

    def test_changed_default_removed_export_and_lifecycle_break_are_visible(self):
        path = self.package / "roadmap_policy.py";before = path.read_text()
        for after in (before.replace("bound=3", "bound=2"), before.replace("def policy", "def renamed"),
                      before.replace("def __enter__(self)", "def __enter__(self, mode)")):
            path.write_text(after)
            result = compare_interfaces(self.root, "HEAD")
            self.assertFalse(result["structural_compatible"])
            self.assertFalse(result["domain_proof"])

    def test_added_public_method_is_structurally_additive(self):
        path = self.package / "roadmap_policy.py";path.write_text(path.read_text() + " def additional(self): return True\n")
        self.assertTrue(compare_interfaces(self.root, "HEAD")["structural_compatible"])

    def test_shadowed_declarations_do_not_hide_an_earlier_signature_change(self):
        path = self.package / "roadmap_policy.py"
        path.write_text("def same(x=1): return x\ndef same(x=2): return x\n")
        self.git("add", ".");self.git("commit", "-m", "shadowed exports")
        path.write_text(path.read_text().replace("same(x=1)", "same(x=9)"))
        self.assertFalse(compare_interfaces(self.root, "HEAD")["structural_compatible"])

    def test_unknown_module_or_record_version_fails_without_importing_it(self):
        (self.package / "unowned.py").write_text("def hidden(): return 1\n")
        with self.assertRaisesRegex(ContractError, "responsibility"):
            observe_interfaces(self.root)
        (self.package / "unowned.py").unlink()
        path = self.root / "Roadmaps/Shared/records.schema.json";value = json.loads(path.read_text())
        value["$defs"]["WorkUnit"]["properties"]["schema"]["const"] = True;path.write_text(json.dumps(value))
        with self.assertRaisesRegex(ContractError, "record interface version"):
            observe_interfaces(self.root)

    def test_nested_unowned_module_is_part_of_the_denominator(self):
        nested = self.package / "extra";nested.mkdir()
        (nested / "hidden.py").write_text("def exported(): return 1\n")
        with self.assertRaisesRegex(ContractError, "responsibility"):
            observe_interfaces(self.root)

    def test_conditional_declaration_guards_are_part_of_the_interface(self):
        path = self.package / "roadmap_policy.py"
        path.write_text("if mode == 'original':\n def selected(x): return x\n")
        self.git("add", ".");self.git("commit", "-m", "conditional API")
        path.write_text(path.read_text().replace("'original'", "'changed'"))
        self.assertFalse(compare_interfaces(self.root, "HEAD")["structural_compatible"])


if __name__ == "__main__":
    unittest.main()
