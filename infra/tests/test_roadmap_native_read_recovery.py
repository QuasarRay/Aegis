"""Read-acceptance provenance across an atomic native package update.

These fixtures exercise executable bindings, not live native qualification.
"""
from __future__ import annotations

import copy
import unittest
from unittest.mock import patch

from agentinfra.roadmap_native import _read_transport_binding
from agentinfra.roadmap_records import ContractError, digest


class NativeReadRecoveryTests(unittest.TestCase):
    def setUp(self):
        from test_roadmap_retained_native import RetainedNativeExecutableTests
        self.fixture = RetainedNativeExecutableTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.protocol = {"executable": self.fixture.installed}
        route = self.fixture.retained()
        self.native = {"schema": 1, "kind": "codex_active_host_observation",
                       "producer": "agentinfra.roadmap_native.observe_native_owner",
                       "owner_process": {"pid": 123}, "installed_executable": self.fixture.installed,
                       "executable": {"path": route["path"], "sha256": route["sha256"]},
                       "executable_route": route}

    def bind(self, native=None):
        native = copy.deepcopy(self.native if native is None else native)
        native["digest"] = digest({k: v for k, v in native.items() if k != "digest"})
        with patch("agentinfra.roadmap_protocol.assert_protocol") as pin:
            result = _read_transport_binding(self.fixture.root, self.protocol, native)
        pin.assert_called_once_with(self.fixture.root, self.protocol)
        return result

    def test_installed_reader_and_retained_host_keep_both_exact_pins_and_canonical_bytes(self):
        before = (self.fixture.root / ".aegis/project.json").read_bytes()
        binding = self.bind()
        self.assertEqual(binding["installed_transport"], self.fixture.installed)
        self.assertEqual(binding["active_host"]["sha256"], self.fixture.old_sha)
        self.assertNotEqual(binding["active_host"]["sha256"], binding["installed_transport"]["sha256"])
        self.assertEqual(binding["active_host_route"]["prior_protocol"], self.native["executable_route"]["prior_protocol"])
        self.assertEqual((self.fixture.root / ".aegis/project.json").read_bytes(), before)

    def test_same_installed_host_uses_its_exact_identity_without_a_retained_route(self):
        native = dict(self.native, executable=self.fixture.installed)
        native.pop("executable_route")
        binding = self.bind(native)
        self.assertEqual(binding["active_host"], binding["installed_transport"])
        self.assertIsNone(binding["active_host_route"])

    def test_unqualified_different_host_or_unrelated_path_cannot_supply_read_acceptance(self):
        cases = []
        native = copy.deepcopy(self.native); native.pop("executable_route"); cases.append(native)
        native = copy.deepcopy(self.native); native["installed_executable"]["sha256"] = "0" * 64; cases.append(native)
        native = copy.deepcopy(self.native); native["executable_route"]["sha256"] = "0" * 64; cases.append(native)
        native = copy.deepcopy(self.native); native["executable"]["path"] = "/unrelated/codex"; cases.append(native)
        native = copy.deepcopy(self.native); native["kind"] = "untrusted_observation_file"; cases.append(native)
        for native in cases:
            with self.subTest(native=native), self.assertRaisesRegex(ContractError, "verified pinned retained"):
                self.bind(native)

    def test_prior_pin_schema_tampering_and_changed_owned_observation_are_rejected(self):
        native = copy.deepcopy(self.native); native["digest"] = "0" * 64
        with patch("agentinfra.roadmap_protocol.assert_protocol"), self.assertRaisesRegex(ContractError, "observation changed"):
            _read_transport_binding(self.fixture.root, self.protocol, native)
        self.fixture.schema.write_text("changed prior protocol bytes")
        with self.assertRaisesRegex(ContractError, "lost its exact prior"):
            self.bind()
