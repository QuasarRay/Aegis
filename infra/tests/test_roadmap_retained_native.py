"""Pinned active-host recovery across an atomic native package replacement."""
from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
import socket
import tempfile
import unittest
from unittest.mock import patch

from agentinfra.roadmap_native import _reader_executable, observe_native_owner
from agentinfra.roadmap_records import ContractError, digest, file_binding
from agentinfra.roadmap_persistence import POLICY_PATH
from agentinfra.roadmap_work import materialize


ROOT = Path(__file__).resolve().parents[2]


class RetainedNativeExecutableTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        shared = self.root / "Roadmaps/Shared"
        shared.mkdir(parents=True)
        for name in ("registry.json", "records.schema.json"):
            shutil.copyfile(ROOT / "Roadmaps/Shared" / name, shared / name)
        self.installed_path = self.root / "installed/codex"
        self.installed_path.parent.mkdir()
        self.installed_path.write_bytes(b"new installed native executable fixture")
        self.installed = {"path": str(self.installed_path), "sha256": digest(self.installed_path.read_bytes())}
        self.old_sha = digest(b"prior pinned active native fixture")
        self.schema = self.root / "protocol-schema.json"
        self.schema.write_text('{"fixture":"retained protocol"}\n')
        self.manifest = {"schema": 1, "kind": "installed_codex_protocol_export",
                         "executable": {"path": str(self.installed_path), "sha256": self.old_sha},
                         "files": [file_binding(self.root, "protocol-schema.json")]}
        self.save_manifest()

    def save_manifest(self, *, recompute=True):
        if recompute:
            self.manifest["digest"] = digest({k: v for k, v in self.manifest.items() if k != "digest"})
        (self.root / "protocol.json").write_text(json.dumps(self.manifest))
        record = {"schema": 1, "project": "Aegis", "native_protocol": file_binding(self.root, "protocol.json")}
        (self.root / ".aegis").mkdir(exist_ok=True)
        (self.root / ".aegis/project.json").write_text(json.dumps(record))

    def retained(self, sha=None, path=None):
        return _reader_executable(self.root, self.installed, path or str(self.installed_path) + " (deleted)",
                                  sha or self.old_sha, "/proc/123/exe")

    def test_installed_active_bytes_need_no_historical_protocol_fallback(self):
        (self.root / ".aegis/project.json").unlink()
        result = _reader_executable(self.root, self.installed, str(self.installed_path),
                                    self.installed["sha256"], "/proc/123/exe")
        self.assertEqual(result["path"], str(self.installed_path))
        self.assertEqual(result["route"], "installed_active_host")

    def test_retained_route_uses_exact_prior_pin_without_changing_project_or_goal(self):
        before = (self.root / ".aegis/project.json").read_bytes()
        result = self.retained()
        self.assertEqual(result["path"], "/proc/123/exe")
        self.assertEqual(result["sha256"], self.old_sha)
        self.assertEqual(result["route"], "kernel_retained_pinned_active_host")
        self.assertNotEqual(result["sha256"], self.installed["sha256"])
        self.assertEqual((self.root / ".aegis/project.json").read_bytes(), before)

    def test_unpinned_bytes_unrelated_paths_and_nondeleted_mismatch_are_rejected(self):
        with self.assertRaisesRegex(ContractError, "prior exact native authority"):
            self.retained(sha=digest(b"unknown binary"))
        with self.assertRaisesRegex(ContractError, "path differs"):
            self.retained(path=str(self.root / "unrelated/codex") + " (deleted)")
        with self.assertRaisesRegex(ContractError, "bytes differ"):
            self.retained(path=str(self.installed_path))
        record = json.loads((self.root / ".aegis/project.json").read_text())
        record["native_protocol"]["sha256"] = "0" * 64
        (self.root / ".aegis/project.json").write_text(json.dumps(record))
        with self.assertRaisesRegex(ContractError, "unchanged prior protocol"):
            self.retained()

    def test_rebound_but_tampered_manifest_digest_or_schema_bytes_are_rejected(self):
        self.manifest["digest"] = "0" * 64
        self.save_manifest(recompute=False)
        with self.assertRaisesRegex(ContractError, "prior exact native authority"):
            self.retained()
        self.save_manifest()
        self.schema.write_text("changed schema bytes")
        with self.assertRaisesRegex(ContractError, "prior exact native authority"):
            self.retained()

    def test_other_protocol_kind_cannot_supply_native_executable_authority(self):
        self.manifest["kind"] = "unreviewed_export"
        self.save_manifest()
        with self.assertRaisesRegex(ContractError, "prior exact native authority"):
            self.retained()

    def test_later_installed_protocol_pin_keeps_the_running_prior_pin_available(self):
        (self.root / "retained-protocol.json").write_bytes((self.root / "protocol.json").read_bytes())
        prior = file_binding(self.root, "retained-protocol.json")
        self.manifest["executable"] = self.installed
        self.save_manifest()
        path = self.root / ".aegis/project.json"
        record = json.loads(path.read_text())
        record["native_protocol_history"] = [prior]
        path.write_text(json.dumps(record))
        result = self.retained()
        self.assertEqual(result["prior_protocol"], prior)
        self.assertEqual(result["sha256"], self.old_sha)

    def test_protocol_exports_for_different_binaries_cannot_overwrite_a_retained_schema_pin(self):
        shutil.copyfile(ROOT / POLICY_PATH, self.root / POLICY_PATH)
        (self.root / "framework.toml").write_text("version = 'fixture'\n")
        path = self.root / ".aegis/project.json"
        record = json.loads(path.read_text())
        record["execution"] = {"native_turn_configuration": {"model": "fixture-model"}}
        path.write_text(json.dumps(record))
        compiled = {"digest": "C", "inputs": [], "policy": {"execution_policy": POLICY_PATH},
                    "milestones": {"A04": {"project": "Aegis", "checks": ["native.protocol"],
                                            "budget_policy": {"max_attempts": None, "max_seconds_per_recipe": None}}},
                    "recipes": {"native.protocol": {"max_seconds": None, "max_attempts": None}}}
        first_tool = dict(self.installed, sha256=self.old_sha)
        with patch("agentinfra.roadmap_work.compile_roadmaps", return_value=compiled), \
             patch("agentinfra.roadmap_protocol.native_executable", side_effect=[first_tool, self.installed]), \
             patch.dict(os.environ, {}, clear=True):
            first = materialize(self.root, compiled, "A04", "native.protocol")
            second = materialize(self.root, compiled, "A04", "native.protocol")
        self.assertNotEqual(first["candidate"], second["candidate"])
        self.assertNotEqual(first["argv"][-1], second["argv"][-1])
        self.assertTrue(first["argv"][-1].startswith(first["target"]["output"] + "/"))
        self.assertTrue(second["argv"][-1].startswith(second["target"]["output"] + "/"))

    def test_changed_process_creation_identity_stops_before_native_reader_dispatch(self):
        owner = {"host": socket.gethostname(), "pid": os.getpid(), "process_identity": "fixture-identity", "session": "fixture"}
        route = {"path": "/never/execute", "sha256": self.old_sha}
        with patch("agentinfra.roadmap_native._pid_alive", side_effect=[True, False]), \
             patch("agentinfra.roadmap_protocol.native_executable", return_value=self.installed), \
             patch("agentinfra.roadmap_native._reader_executable", return_value=route), \
             patch("agentinfra.roadmap_native.CodexReader") as reader:
            with self.assertRaisesRegex(ContractError, "creation identity changed"):
                observe_native_owner(self.root, owner)
        reader.assert_not_called()
