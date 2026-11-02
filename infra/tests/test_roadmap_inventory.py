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

from agentinfra.roadmap_inventory import authority_inventory, inspect_python, reconcile_inventory, save_inventory
from agentinfra.roadmap_records import ContractError, canonical, read_json


class AuthorityInventoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base_temp = tempfile.TemporaryDirectory()
        cls.base = Path(cls.base_temp.name)
        shutil.copytree(ROOT / "Roadmaps", cls.base / "Roadmaps", ignore=shutil.ignore_patterns("python-rust"))
        sources = read_json(ROOT / "Roadmaps/Shared/sources.json")
        sources["files"] = [s for s in sources["files"] if s["path"].lower().endswith(".md")]
        for source in sources["files"]:
            path = cls.base / source["path"]
            path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / source["path"], path)
        (cls.base / "Roadmaps/Shared/sources.json").write_bytes(canonical(sources))
        (cls.base / ".gitignore").write_text(".aegis/\n")
        (cls.base / "example.py").write_text("def retained(x):\n    return x + 1\n")
        cls.git(cls.base, "init", "--initial-branch=dev")
        cls.git(cls.base, "add", ".")
        cls.git(cls.base, "commit", "-m", "authority fixture")

    @staticmethod
    def git(root, *args):
        return subprocess.run(["git", "-c", "user.name=Aegis fixture", "-c", "user.email=fixture@example.invalid",
                               "-c", "commit.gpgsign=false", *args], cwd=root,
                              capture_output=True, text=True, check=True, timeout=30).stdout

    @classmethod
    def tearDownClass(cls):
        cls.base_temp.cleanup()

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "repo"
        self.git(Path(self.temp.name), "clone", "--shared", str(self.base), str(self.root))

    def tearDown(self):
        self.temp.cleanup()

    def test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection(self):
        self.git(self.root, "branch", "same-body")
        self.git(self.root, "switch", "-c", "different-body")
        (self.root / "example.py").write_text("def retained(x):\n    return x + 2\n")
        self.git(self.root, "commit", "-am", "different component")
        self.git(self.root, "switch", "dev")
        record = authority_inventory(self.root)
        self.assertEqual(record, authority_inventory(self.root))
        self.assertTrue({"refs/heads/dev", "refs/heads/same-body", "refs/heads/different-body"} <=
                        {r["ref"] for r in record["refs"]})
        components = [c for c in record["components"] if "example.py" in c["paths"]]
        self.assertEqual(len(components), 2)
        self.assertEqual({c["disposition"] for c in components},
                         {"PRESERVE_CURRENT_IMPLEMENTATION", "RETAIN_PENDING_SEMANTIC_REVIEW_BEFORE_REUSE"})
        self.assertTrue(all(not c["inspection"]["semantic_acceptance"] for c in components))
        self.assertEqual(reconcile_inventory(self.root, record)["status"], "RECONCILED")
        record["requirements"].pop()
        with self.assertRaisesRegex(ContractError, "differs from current"):
            reconcile_inventory(self.root, record)

    def test_dirty_addition_deletion_and_binary_bytes_survive_recording(self):
        (self.root / "example.py").unlink()
        (self.root / "user work.bin").write_bytes(b"\x00\xff\x80dirty")
        record = authority_inventory(self.root)
        files = {f["path"]: f for f in record["worktree"]["files"]}
        self.assertEqual(files["example.py"]["kind"], "missing")
        self.assertEqual(files["user work.bin"]["kind"], "file")
        path = self.root / ".aegis/project.json"
        path.parent.mkdir()
        path.write_text(json.dumps({"schema": 1, "project": "Aegis", "existing_queue": ["keep"]}))
        result = save_inventory(self.root, record)
        self.assertEqual(result["status"], "RECORDED")
        self.assertEqual(read_json(path)["existing_queue"], ["keep"])
        self.assertEqual(save_inventory(self.root, record)["status"], "REUSED")
        self.assertEqual((self.root / "user work.bin").read_bytes(), b"\x00\xff\x80dirty")
        self.assertFalse((self.root / "example.py").exists())

    def test_content_edits_with_same_status_invalidate_publication(self):
        path = self.root / "example.py"
        path.write_text("def retained(x):\n    return x + 2\n")
        record = authority_inventory(self.root)
        path.write_text("def retained(x):\n    return x + 3\n")
        with self.assertRaisesRegex(ContractError, "source or branches changed"):
            save_inventory(self.root, record)

    def test_new_ref_invalidates_snapshot_even_when_tree_is_identical(self):
        record = authority_inventory(self.root)
        self.git(self.root, "branch", "new-preservation-obligation")
        with self.assertRaisesRegex(ContractError, "source or branches changed"):
            save_inventory(self.root, record)

    def test_unknown_canonical_record_is_not_overwritten(self):
        record = authority_inventory(self.root)
        path = self.root / ".aegis/project.json"
        path.parent.mkdir()
        path.write_text('{"schema":99,"project":"Aegis","user":"keep"}')
        before = path.read_bytes()
        with self.assertRaisesRegex(ContractError, "explicit migration"):
            save_inventory(self.root, record)
        self.assertEqual(path.read_bytes(), before)

    def test_reference_symlink_preserves_link_bytes_without_following_destination(self):
        destination = Path(self.temp.name) / "external.txt"
        destination.write_text("first")
        (self.root / "link").symlink_to(destination)
        first = authority_inventory(self.root)
        destination.write_text("different external bytes")
        second = authority_inventory(self.root)
        self.assertEqual(first, second)
        link = next(f for f in first["worktree"]["files"] if f["path"] == "link")
        self.assertEqual(link["kind"], "symlink")

    def test_unparseable_historical_source_remains_an_explicit_obligation(self):
        self.git(self.root, "switch", "-c", "old-interpreter")
        (self.root / "old.py").write_bytes(b"print 'Python 2'\n")
        self.git(self.root, "add", "old.py")
        self.git(self.root, "commit", "-m", "retained historical source")
        self.git(self.root, "switch", "dev")
        record = authority_inventory(self.root)
        component = next(c for c in record["components"] if "old.py" in c["paths"])
        self.assertEqual(component["inspection"]["status"], "UNSUPPORTED_BY_CURRENT_INTERPRETER")
        self.assertEqual(component["disposition"], "RETAIN_PENDING_SEMANTIC_REVIEW_BEFORE_REUSE")

    def test_gitlink_untracked_content_changes_invalidate_inventory(self):
        reference = Path(self.temp.name) / "reference"
        reference.mkdir()
        self.git(reference, "init", "--initial-branch=reference-dev")
        (reference / "kept.py").write_text("original = True\n")
        self.git(reference, "add", ".")
        self.git(reference, "commit", "-m", "reference source")
        self.git(self.root, "-c", "protocol.file.allow=always", "submodule", "add", str(reference), "reference")
        self.git(self.root, "commit", "-am", "retained gitlink")
        nested = self.root / "reference"
        self.git(nested, "checkout", "--detach")
        (nested / "user.py").write_text("user = 1\n")
        first = authority_inventory(self.root)
        (nested / "user.py").write_text("user = 2\n")
        second = authority_inventory(self.root)
        self.assertEqual(first["worktree"]["status"], second["worktree"]["status"])
        self.assertNotEqual(first["digest"], second["digest"])
        link = next(f for f in second["worktree"]["files"] if f["path"] == "reference")
        self.assertIsNone(link["checkout"]["branch"])
        self.assertEqual([f["path"] for f in link["checkout"]["files"]], ["user.py"])
        with self.assertRaisesRegex(ContractError, "source or branches changed"):
            save_inventory(self.root, first)
        (nested / "kept.py").write_text("original = 2\n")
        self.git(nested, "add", "kept.py")
        (nested / "kept.py").write_text("original = True\n")
        staged_first = authority_inventory(self.root)
        (nested / "kept.py").write_text("original = 3\n")
        self.git(nested, "add", "kept.py")
        (nested / "kept.py").write_text("original = True\n")
        staged_second = authority_inventory(self.root)
        self.assertEqual(staged_first["worktree"]["status"], staged_second["worktree"]["status"])
        self.assertNotEqual(staged_first["digest"], staged_second["digest"])

    def test_remote_heads_are_live_and_unfetched_work_is_visible(self):
        remote = Path(self.temp.name) / "remote.git"
        self.git(Path(self.temp.name), "init", "--bare", str(remote))
        self.git(self.root, "remote", "set-url", "origin", str(remote))
        self.git(self.root, "push", "origin", "dev")
        self.git(remote, "branch", "not-fetched", "dev")
        record = authority_inventory(self.root, remote=True)
        self.assertEqual({h["ref"] for h in record["remote_heads"]},
                         {"refs/heads/dev", "refs/heads/not-fetched"})
        self.assertEqual([h["ref"] for h in record["unreconciled_remote_heads"]], ["refs/heads/not-fetched"])

    def test_nested_and_shadowed_definitions_have_distinct_body_identities(self):
        raw = b"class Original:\n def same(self):\n  def nested(): return 1\n  return nested()\n def same(self): return 2\n"
        result = inspect_python(raw, "original.py")
        definitions = result["definitions"]
        self.assertEqual(len(definitions), 4)
        same = [d for d in definitions if d["owner"] == "module::Original::same"]
        self.assertEqual(len(same), 2)
        self.assertNotEqual(same[0]["route"], same[1]["route"])
        self.assertNotEqual(same[0]["ast_sha256"], same[1]["ast_sha256"])


if __name__ == "__main__":
    unittest.main()
