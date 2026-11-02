from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "infra"))
from agentinfra.roadmap_portability import artifacts, check, inventory, markdown, publish, shards
from agentinfra.roadmap_records import ContractError, canonical, digest, read_json
from agentinfra.transaction import FileTransaction


class PortabilityPublicationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.root = Path(self.temp.name)
        (self.root / "infra").mkdir()
        (self.root / "infra/a.py").write_text("def first(x):\n    return x + 1\n")
        (self.root / "infra/b.py").write_text("def second(x):\n    return [n for n in range(x)]\n")
        self.base = self.root / "Roadmaps/Shared/python-rust"

    def tearDown(self):
        self.temp.cleanup()

    def test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged(self):
        first = inventory(self.root); publish(self.root, first)
        old_index = read_json(self.base / "inventory.json")
        old_document = self.base / "infra__b.py.md"
        before = old_document.read_bytes(); stamp = old_document.stat().st_mtime_ns
        owned = {part["path"]: (self.base / part["path"]).read_bytes() for part in old_index["shards"]
                 if all(u["file"] == "infra/b.py" for u in read_json(self.base / part["path"])["units"])}
        (self.root / "infra/a.py").write_text("def first(x):\n    return x + 2\n")
        second = inventory(self.root); result = publish(self.root, second)
        self.assertEqual(old_document.read_bytes(), before)
        self.assertEqual(old_document.stat().st_mtime_ns, stamp)
        for relative, raw in owned.items(): self.assertEqual((self.base / relative).read_bytes(), raw)
        self.assertEqual(check(self.root, second)["status"], "CURRENT")
        self.assertLessEqual(result["artifacts_changed"], 3)
        self.assertEqual(publish(self.root, second)["status"], "REUSED")

    def test_source_additions_deletions_and_override_edits_invalidate_captured_generation(self):
        for change in ("add", "delete", "override"):
            with self.subTest(change=change):
                record = inventory(self.root)
                if change == "add": (self.root / "infra/added.py").write_text("added = 1\n")
                elif change == "delete": (self.root / "infra/a.py").unlink()
                else:
                    path = self.root / "Roadmaps/Shared/python-rust-overrides.json";path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_text('{"schema":1,"units":{}}')
                with self.assertRaisesRegex(ContractError, "changed during generation"):
                    publish(self.root, record)

    def test_physical_utf8_shard_bound_includes_envelope_and_final_newline(self):
        units = [dict(id=str(i), file="infra/a.py", body="λ" * 22) for i in range(12)]
        record = dict(files=[], units=units, coverage="fixture", digest="fixture")
        index, parts = shards(record, max_bytes=250)
        self.assertEqual([u for p in parts.values() for u in p["units"]], units)
        self.assertTrue(all(len(canonical(p)) + 1 <= 250 for p in parts.values()))
        self.assertTrue(all(s["bytes"] <= 250 for s in index["shards"]))
        with self.assertRaisesRegex(ContractError, "single behavioral entry"):
            shards(record, max_bytes=30)

    def test_edits_to_owned_artifacts_are_preserved_and_block_regeneration(self):
        record = inventory(self.root);publish(self.root, record)
        path = self.base / "infra__a.py.md";path.write_bytes(path.read_bytes() + b"\nuser review\n")
        before = path.read_bytes()
        with self.assertRaises(ContractError): publish(self.root, record)
        self.assertEqual(path.read_bytes(), before)
        with self.assertRaises(ContractError): check(self.root, record)

    def test_legacy_layout_migration_preserves_every_unit_and_unowned_file(self):
        record = inventory(self.root)
        # Reproduce the old generated owner's exact bytes, independently of the new publisher.
        old = {"schema": 1, "units": record["units"]}
        self.base.joinpath("units").mkdir(parents=True)
        self.base.joinpath("units/units-0000.json").write_text(json.dumps(old, indent=2, sort_keys=True) + "\n")
        index = {"schema": 1, "kind": "sharded_python_rust_inventory", "coverage": record["coverage"],
                 "files": record["files"], "unit_count": len(record["units"]), "digest": record["digest"],
                 "shards": [{"path": "units/units-0000.json", "digest": digest(old), "count": len(record["units"])}]}
        (self.base / "inventory.json").write_text(json.dumps(index, indent=2, sort_keys=True) + "\n")
        for source in record["files"]:
            local = dict(record, files=[source], units=[u for u in record["units"] if u["file"] == source["path"]])
            (self.base / (source["path"].replace("/", "__") + ".md")).write_text(markdown(local))
        (self.base / "user-notes.txt").write_text("retain")
        publish(self.root, record)
        current = read_json(self.base / "inventory.json")
        resolved = [u for shard in current["shards"] for u in read_json(self.base / shard["path"])["units"]]
        self.assertEqual(resolved, record["units"])
        self.assertFalse((self.base / "units/units-0000.json").exists())
        self.assertEqual((self.base / "user-notes.txt").read_text(), "retain")
        self.assertEqual(check(self.root, record)["status"], "CURRENT")

    def test_deleted_source_retires_only_its_owned_generated_artifacts(self):
        publish(self.root, inventory(self.root))
        (self.root / "infra/a.py").unlink()
        record = inventory(self.root);publish(self.root, record)
        self.assertFalse((self.base / "infra__a.py.md").exists())
        self.assertTrue((self.base / "infra__b.py.md").exists())
        self.assertEqual(check(self.root, record)["status"], "CURRENT")

    def test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery(self):
        publish(self.root, inventory(self.root))
        before = {p.relative_to(self.base).as_posix(): p.read_bytes() for p in self.base.rglob("*") if p.is_file()}
        (self.root / "infra/a.py").write_text("def first(x):\n    return x + 4\n")
        record = inventory(self.root)

        def fail(stage, _journal):
            if stage == "after_destination": raise OSError("seeded interruption")

        def transaction(*args, **kwargs):
            return FileTransaction(*args, **kwargs, fault=fail)

        with patch("agentinfra.roadmap_portability.FileTransaction", side_effect=transaction):
            with self.assertRaisesRegex(OSError, "seeded interruption"):
                publish(self.root, record)
        after = {p.relative_to(self.base).as_posix(): p.read_bytes() for p in self.base.rglob("*") if p.is_file()}
        self.assertEqual(after, before)
        publish(self.root, record)
        self.assertEqual(check(self.root, record)["status"], "CURRENT")

    def test_document_path_collision_cannot_merge_two_source_owners(self):
        (self.root / "infra/x").mkdir()
        (self.root / "infra/x/y.py").write_text("first = 1\n")
        (self.root / "infra/x__y.py").write_text("second = 2\n")
        record = inventory(self.root)
        with self.assertRaisesRegex(ContractError, "path collision"):
            artifacts(record)
        self.assertFalse((self.base / "inventory.json").exists())


if __name__ == "__main__":
    unittest.main()
