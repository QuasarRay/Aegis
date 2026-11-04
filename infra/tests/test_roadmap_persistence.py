"""AM20 execution/recovery controls; fixture processes confer no domain proof."""
from __future__ import annotations

import copy
import io
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import MagicMock, patch

from agentinfra.process import run_process
from agentinfra.roadmap import compile_roadmaps
from agentinfra.roadmap_python import esbmc_arguments, esbmc_command_policy
from agentinfra.roadmap_interfaces import compare_interfaces, observe_interfaces, validate_compatibility_disposition
from agentinfra.roadmap_persistence import POLICY_PATH, policy_binding, recovery_packet, retained_history
from agentinfra.roadmap_records import ContractError, bindings_current, digest, file_binding, read_json, validate_record
from agentinfra.roadmap_runtime import BudgetLedger
from agentinfra.roadmap_work import current_success, materialize, run_work
from agentinfra import roadmap_mirrors as mirrors
from agentinfra.roadmap_download import _ResolvedConnection

ROOT = Path(__file__).resolve().parents[2]


class PersistentExecutionTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        for relative in (POLICY_PATH, "Roadmaps/Shared/records.schema.json"):
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative, target)
        self.ledger = BudgetLedger(self.root)
        (self.root / "failure.txt").write_text("observed fixture failure; no live handle")

    def operation(self, inputs):
        return {"state": "PREPARED", "spec_digest": inputs, "runner": {"fixture": True}}

    def plan(self, inputs, *, action="Resume from the verified checkpoint", strategy="resume_checkpoint"):
        history = self.ledger.read()["attempts"]
        record = recovery_packet("work", inputs, history)
        record.update(trigger="external observation timeout", diagnosis="Fixture child is terminal; checkpoint is retained",
                      strategy=strategy, action=action,
                      alternatives=[{"strategy": strategy, "reason": "Checkpoint retains the exact source and completed work"},
                                    {"strategy": "async_poll", "reason": "No live remote handle remains to poll"}],
                      evidence=[file_binding(self.root, "failure.txt")])
        path = "recovery-" + digest(record) + ".json"
        (self.root / path).write_text(json.dumps(record))
        return file_binding(self.root, path)

    def reserve(self, inputs, recovery=None):
        return self.ledger.reserve_operation("work", inputs, None, self.operation(inputs),
                                             max_attempts=None, total_seconds=None,
                                             persistent_policy=policy_binding(self.root), recovery=recovery)

    def test_unlimited_allocations_exceed_old_caps_and_preserve_every_historical_row(self):
        for number in range(2):
            inputs = "finite-" + str(number)
            old = self.ledger.reserve_operation("work", inputs, 900, self.operation(inputs), diagnosis="corrected fixture")
            self.ledger.close(old["id"], "FAILED", {"tool_microseconds": 7})
        historical = copy.deepcopy(self.ledger.read()["attempts"])
        for number in range(6):
            inputs = "persistent-" + str(number)
            attempt = self.reserve(inputs, self.plan(inputs, action="Resume verified checkpoint " + str(number)))
            self.assertIsNone(attempt["reserved_seconds"])
            self.assertIsNone(self.ledger.reservation_record(attempt["id"])["consumed"])
            self.ledger.close(attempt["id"], "FAILED", {"tool_microseconds": 11})
        self.assertEqual(self.ledger.read()["attempts"][:2], historical)
        metrics = self.ledger.metrics()
        self.assertEqual((metrics["attempts"], metrics["reserved_seconds"], metrics["unlimited_allocation_attempts"]), (8, 1800, 6))
        self.assertEqual(metrics["observed_tool_microseconds"], 80)

    def test_unresolved_operation_and_missing_recovery_cannot_redispatch(self):
        first = self.reserve("source")
        with self.assertRaisesRegex(ContractError, "requires recovery"):
            self.reserve("changed")
        self.ledger.close(first["id"], "INTERRUPTED", {})
        with self.assertRaisesRegex(ContractError, "recovery record"):
            self.reserve("changed")
        self.assertEqual(len(self.ledger.read()["attempts"]), 1)

    def test_forged_history_missing_alternatives_and_weakened_invariants_are_rejected(self):
        first = self.reserve("source")
        self.ledger.close(first["id"], "FAILED", {})
        good = self.plan("changed")
        for key, value in (("history_digest", "forged"), ("alternatives", []), ("preserves", []), ("evidence", [])):
            record = read_json(self.root / good["path"])
            record[key] = value
            (self.root / "forged.json").write_text(json.dumps(record))
            with self.subTest(key=key), self.assertRaises(ContractError):
                self.reserve("changed", file_binding(self.root, "forged.json"))
        self.assertEqual(len(self.ledger.read()["attempts"]), 1)

    def test_unchanged_failed_strategy_is_rejected_and_an_evidenced_alternative_can_continue(self):
        first = self.reserve("source")
        self.ledger.close(first["id"], "FAILED", {})
        second = self.reserve("source", self.plan("source"))
        self.ledger.close(second["id"], "FAILED", {})
        with self.assertRaisesRegex(ContractError, "unchanged failed recovery"):
            self.reserve("source", self.plan("source"))
        third = self.reserve("source", self.plan("source", strategy="verified_mirror",
                              action="Use the separately reviewed HTTPS route for the same pinned bytes"))
        self.assertEqual(third["attempt_in_generation"], 3)

    def test_persistence_requires_exact_adopted_policy_and_explicit_unlimited_fields(self):
        binding = policy_binding(self.root)
        with self.assertRaisesRegex(ContractError, "cannot carry"):
            self.ledger.reserve("work", "source", 900, persistent_policy=binding)
        policy = read_json(self.root / POLICY_PATH)
        policy["max_attempts"] = 999999999
        (self.root / POLICY_PATH).write_text(json.dumps(policy))
        with self.assertRaisesRegex(ContractError, "caps were reintroduced"):
            self.reserve("source")

    def test_version_two_unlimited_allocation_cannot_be_misread_as_version_one_finite_allocation(self):
        attempt = self.reserve("source")
        record = self.ledger.reservation_record(attempt["id"])
        self.assertEqual(record["schema"], 2)
        record["schema"] = 1
        with self.assertRaises(ContractError):
            validate_record(self.root, "BudgetReservation", record)
        record.update(reserved=900, consumed=900)
        validate_record(self.root, "BudgetReservation", record)
        record["schema"] = 2
        with self.assertRaises(ContractError):
            validate_record(self.root, "BudgetReservation", record)

    def test_interface_reader_retains_both_declared_reservation_versions_and_rejects_an_undeclared_version(self):
        package = self.root / "infra/agentinfra"
        package.mkdir(parents=True)
        (package / "__init__.py").write_text("INTERFACE_VERSION = 1\n")
        observed = observe_interfaces(self.root)
        alternatives = observed["record_protocols"]["BudgetReservation"]["anyOf"]
        self.assertEqual([d["properties"]["schema"]["const"] for d in alternatives], [1, 2])
        path = self.root / "Roadmaps/Shared/records.schema.json"
        schemas = read_json(path)
        schemas["$defs"]["BudgetReservation"]["anyOf"][1]["properties"]["schema"]["const"] = 3
        path.write_text(json.dumps(schemas))
        with self.assertRaisesRegex(ContractError, "unsupported record interface version: BudgetReservation"):
            observe_interfaces(self.root)

    def test_transitive_history_retains_ancestors_and_recovery_binds_full_history(self):
        attempts = [{"id": "a", "work_id": "old", "inherited_attempt_ids": []},
                    {"id": "b", "work_id": "intermediate", "inherited_attempt_ids": ["a"]},
                    {"id": "c", "work_id": "work", "inherited_attempt_ids": ["b"]}]
        self.assertEqual(retained_history(attempts, "work"), attempts)
        with self.assertRaisesRegex(ContractError, "missing"):
            retained_history(attempts[1:], "work")

    def test_unlimited_process_keeps_complete_private_logs_beyond_preview(self):
        logs = self.root / "logs"
        code = "import sys,time;time.sleep(.05);sys.stdout.write('x'*8192);sys.stderr.write('y'*2048)"
        result = run_process([sys.executable, "-B", "-c", code], cwd=self.root, timeout=None,
                             capture_limit=1024, output_directory=logs)
        self.assertEqual(result.returncode, 0)
        self.assertFalse(result.timed_out)
        self.assertTrue(result.stdout_truncated and result.stderr_truncated)
        for path, size, sha in ((result.stdout_path, 8192, result.stdout_sha256),
                                (result.stderr_path, 2048, result.stderr_sha256)):
            raw = Path(path).read_bytes()
            self.assertEqual((len(raw), digest(raw)), (size, sha))
            if os.name == "posix":
                self.assertEqual(Path(path).stat().st_mode & 0o777, 0o600)

    def test_actual_materialization_selects_unlimited_policy_and_preserves_exact_source_selection(self):
        (self.root / "framework.toml").write_text("version = 'fixture'\n")
        source = self.root / "infra/agentinfra/kernel.py"
        source.parent.mkdir(parents=True)
        source.write_text("def unused(value): return value + 1\n")
        compiled = {"digest": "C", "inputs": [file_binding(self.root, source.relative_to(self.root).as_posix())],
                    "policy": {"execution_policy": POLICY_PATH},
                    "milestones": {"A03": {"project": "Aegis", "checks": ["production.build"],
                                    "budget_policy": {"max_attempts": None, "max_seconds_per_recipe": None}}},
                    "recipes": {"production.build": {"max_seconds": None, "max_attempts": None}}}
        with patch("agentinfra.roadmap_work.compile_roadmaps", return_value=compiled), patch.dict(os.environ, {}, clear=True):
            spec = materialize(self.root, compiled, "A03", "production.build")
        self.assertEqual([spec[k] for k in ("max_seconds", "max_attempts", "total_seconds")], [None, None, None])
        self.assertEqual(spec["execution_policy"], policy_binding(self.root))
        self.assertIn("--invalidation-mode=checked-hash", spec["argv"])
        self.assertIn(file_binding(self.root, "infra/agentinfra/kernel.py"), spec["selection"]["production"])

    def test_legacy_esbmc_command_is_retained_without_current_policy_credit(self):
        tool = {"backend": "esbmc-python", "executable": "/pinned/esbmc", "python": "/pinned/python"}
        fixture = "verification/roadmap/python/policy_deal_positive.py"
        for claims in (False, True):
            current = esbmc_arguments(self.root, tool, fixture, claims=claims)
            self.assertNotIn("--timeout", current)
            self.assertEqual(esbmc_command_policy(self.root, tool, fixture, current,
                             producer_inputs_current=True, claims=claims), "CURRENT_UNLIMITED_SELECTION")
            legacy = current[:-1] + ["--timeout", "120s", current[-1]] if claims else current + ["--timeout", "120s"]
            self.assertEqual(esbmc_command_policy(self.root, tool, fixture, legacy,
                             producer_inputs_current=False, claims=claims), "HISTORICAL_120_SECOND_LIMIT_NO_CURRENT_CREDIT")
            with self.assertRaises(ContractError):
                esbmc_command_policy(self.root, tool, fixture, legacy, producer_inputs_current=True, claims=claims)
            with self.assertRaises(ContractError):
                esbmc_command_policy(self.root, tool, fixture, current + ["--no-assertions"],
                                     producer_inputs_current=False, claims=claims)

    def test_recovered_dispatch_isolates_outputs_and_then_reuses_success_without_another_process(self):
        from test_roadmap_durable import DurableExecutionTests
        fixture = DurableExecutionTests()
        fixture.setUp()
        self.addCleanup(fixture.tearDown)
        root = fixture.root
        shutil.copyfile(ROOT / POLICY_PATH, root / POLICY_PATH)
        adapter, owner, _ = fixture.canonical()
        (root / "framework.toml").write_text("version = 'fixture'\n")
        (root / "scripts").mkdir()
        driver = root / "scripts/validate_roadmaps.py"
        driver.write_text("from pathlib import Path\nimport sys\np=Path('.aegis/capacity')\nprint('ready' if p.exists() else 'waiting')\nsys.exit(0 if p.exists() else 1)\n")
        compiled = {"digest": "C", "inputs": [file_binding(root, "scripts/validate_roadmaps.py")],
                    "policy": {"execution_policy": POLICY_PATH},
                    "milestones": {"A03": {"project": "Aegis", "requirements": ["ROOT-03"], "checks": ["roadmap.validate"],
                                    "budget_policy": {"max_attempts": None, "max_seconds_per_recipe": None}}},
                    "recipes": {"roadmap.validate": {"max_seconds": None, "max_attempts": None}}}
        observation = {"digest": "native-fixture", "turn_id": "fixture-turn"}
        with patch("agentinfra.roadmap_work.compile_roadmaps", return_value=compiled), \
             patch("agentinfra.roadmap_work.qualify_execution", return_value=(owner, observation, "retry-fixture", ())), \
             patch.dict(os.environ, {}, clear=True):
            failed = run_work(root, compiled, "A03", "roadmap.validate")
            self.assertEqual(failed["returncode"], 1)
            (root / ".aegis/capacity").write_text("capacity is now available")
            plan = recovery_packet("retry-fixture", failed["inputs"], fixture.ledger.read()["attempts"])
            plan.update(trigger="capacity", diagnosis="The fixture now reports available capacity", strategy="wait_for_capacity",
                        action="Retry the unchanged fixed command after capacity was restored",
                        alternatives=[{"strategy": "wait_for_capacity", "reason": "Capacity is now observed"},
                                      {"strategy": "async_poll", "reason": "There is no live job to poll"}],
                        evidence=[file_binding(root, ".aegis/capacity")])
            (root / "recovery.json").write_text(json.dumps(plan))
            recovered = run_work(root, compiled, "A03", "roadmap.validate", recovery=file_binding(root, "recovery.json"))
            self.assertEqual(recovered["returncode"], 0)
            self.assertTrue(bindings_current(root, failed["artifacts"]))
            self.assertNotEqual(failed["inputs"], recovered["inputs"])
            attempts = fixture.ledger.read()["attempts"]
            self.assertEqual(attempts[0]["semantic_inputs"], attempts[1]["semantic_inputs"])
            selected = current_success(root, compiled, "A03", "roadmap.validate", attempts)
            self.assertEqual(selected["attempt"], recovered["attempt"])
            self.assertEqual(selected["spec"]["recovery_base_digest"], failed["inputs"])
            with patch("agentinfra.roadmap_work.run_process", side_effect=AssertionError("duplicate dispatch")):
                reused = run_work(root, compiled, "A03", "roadmap.validate")
            self.assertTrue(reused["reused"])
            self.assertEqual(reused["attempt"], recovered["attempt"])
        self.assertEqual(len(fixture.ledger.read()["attempts"]), 2)
        self.assertEqual(adapter.read()["work_units"]["retry-fixture"]["continuation"]["status"], "REUSED")

    def test_exact_am20_disposition_preserves_structural_failure_and_rejects_unrelated_changes(self):
        path = "Roadmaps/Shared/AM20_PERSISTENT_EXECUTION.md"
        shutil.copyfile(ROOT / path, self.root / path)
        observation = {"structural_compatible": False, "current_interface_digest": "fixture-interface",
                       "changes": [{"record": "BudgetReservation", "change": "changed_serialized_record_contract"}]}
        decision = {"schema": 1, "decision": "accept_AM20_policy_migration", "observation_digest": digest(observation),
                    "source": file_binding(self.root, path), "policy": policy_binding(self.root),
                    "approved_changes": observation["changes"],
                    "rationale": "Version two explicitly represents unlimited allocation while version one remains byte-compatible."}
        accepted = validate_compatibility_disposition(self.root, observation, decision)
        self.assertFalse(accepted["structural_compatible"])
        self.assertTrue(accepted["accepted_for_implementation"])
        self.assertFalse(accepted["domain_proof"])
        for changes in ([{"record": "GoalBinding", "change": "changed_serialized_record_contract"}],
                        [{"module": "agentinfra.process", "export": "run_process", "change": "removed_export"}]):
            changed = dict(observation, changes=changes)
            request = dict(decision, observation_digest=digest(changed), approved_changes=changes)
            with self.assertRaisesRegex(ContractError, "unrelated or removed"):
                validate_compatibility_disposition(self.root, changed, request)
        with self.assertRaisesRegex(ContractError, "current AM20"):
            validate_compatibility_disposition(self.root, observation, dict(decision, observation_digest="stale"))

    def test_removed_lifecycle_method_cannot_hide_inside_an_authorizable_class_shape_change(self):
        from test_roadmap_interfaces import ModuleInterfaceTests
        fixture = ModuleInterfaceTests()
        fixture.setUp()
        self.addCleanup(fixture.tearDown)
        path = fixture.package / "roadmap_policy.py"
        text = path.read_text()
        self.assertIn("def __enter__", text)
        path.write_text(text.replace("def __enter__", "def _removed_enter"))
        observation = compare_interfaces(fixture.root, "HEAD")
        self.assertFalse(observation["structural_compatible"])
        self.assertIn({"module": "agentinfra.roadmap_policy", "export": "Rules", "member": "__enter__",
                       "change": "removed_class_method"}, observation["changes"])

    def test_persistent_transfer_tries_all_reviewed_sources_without_an_elapsed_transfer_deadline(self):
        shutil.copyfile(ROOT / mirrors.POLICY_PATH, self.root / mirrors.POLICY_PATH)
        raw = b"identical independently pinned bytes"
        entry = {"filename": "artifact.whl", "url": "https://files.pythonhosted.org/artifact.whl",
                 "sha256": digest(raw), "size": len(raw), "sources": [
                     {"provider": "pypi", "url": "https://files.pythonhosted.org/artifact.whl"},
                     *[{"provider": "pypi", "url": "https://files.pythonhosted.org/reviewed-" + str(i) + ".whl"}
                       for i in range(4)]]}
        opener = MagicMock()
        opener.open.side_effect = [TimeoutError(), OSError(), TimeoutError(), OSError(), io.BytesIO(raw)]
        with patch.object(mirrors.urllib.request, "build_opener", return_value=opener), \
             patch.object(mirrors, "time", MagicMock(monotonic=MagicMock(side_effect=AssertionError("elapsed transfer ceiling")))):
            target = mirrors.download_with_mirrors(self.root, entry, self.root / "downloads", None)
        self.assertEqual(target.read_bytes(), raw)
        self.assertEqual(opener.open.call_count, 5)
        self.assertEqual(len(list(target.parent.glob("*.delivery-*.json"))), 5)
        self.assertEqual(opener.open.call_args.kwargs["timeout"], 60)

    def test_persistent_connection_tries_every_returned_public_address_with_original_tls_hostname(self):
        context, sock, wrapped = MagicMock(), MagicMock(), MagicMock()
        context.wrap_socket.return_value = wrapped
        wrapped.getpeercert.return_value = b"peer certificate"
        wrapped.version.return_value = "TLSv1.3"
        connection = _ResolvedConnection("files.pythonhosted.org", observations=[], context=context,
                                         timeout=60, max_addresses=None, resolver_timeout=60)
        with patch("agentinfra.roadmap_download._addresses", return_value=["151.101.0.223", "151.101.64.223", "151.101.128.223"]) as addresses, \
             patch("agentinfra.roadmap_download.socket.create_connection", side_effect=[TimeoutError(), OSError(), sock]) as connect:
            connection.connect()
        self.assertEqual(connect.call_count, 3)
        addresses.assert_called_once_with("files.pythonhosted.org", connection.observations, timeout=60)
        context.wrap_socket.assert_called_once_with(sock, server_hostname="files.pythonhosted.org")


class PersistentCompilerTests(unittest.TestCase):
    def test_all_real_contracts_are_unlimited_and_legacy_authorities_remain_covered(self):
        compiled = compile_roadmaps(ROOT)
        self.assertEqual(len(compiled["milestones"]), 40)
        self.assertIn("AM20", compiled["requirements"])
        for contract in compiled["milestones"].values():
            self.assertIsNone(contract["budget_policy"]["max_attempts"])
            self.assertIsNone(contract["budget_policy"]["max_seconds_per_recipe"])
        for recipe in compiled["recipes"].values():
            self.assertIsNone(recipe["max_attempts"])
            self.assertIsNone(recipe["max_seconds"])
