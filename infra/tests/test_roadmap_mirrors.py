"""Mirror integrity, bounded failover and exact user retry scope controls."""
from __future__ import annotations

from contextlib import contextmanager
import copy
import io
import json
from pathlib import Path
import shutil
import tempfile
import time
import unittest
from unittest.mock import patch
import urllib.request

from agentinfra import roadmap_mirrors as mirrors
from agentinfra.roadmap_records import ContractError, digest, file_binding, read_json
from agentinfra.roadmap_runtime import BudgetLedger, retry_limits


SOURCE = Path(__file__).resolve().parents[2]


class MirrorDeliveryTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        policy = self.root / mirrors.POLICY_PATH
        policy.parent.mkdir(parents=True)
        shutil.copyfile(SOURCE / mirrors.POLICY_PATH, policy)
        self.directory = self.root / ".aegis/downloads"
        self.good = b"exact upstream artifact\n"
        self.entry = {"filename": "artifact.whl", "url": "https://files.pythonhosted.org/packages/artifact.whl",
                      "sha256": digest(self.good), "size": len(self.good), "sources": [
                          {"provider": "pypi", "url": "https://files.pythonhosted.org/packages/artifact.whl"},
                          {"provider": "tuna-pypi", "url": "https://mirrors.tuna.tsinghua.edu.cn/pypi/web/packages/artifact.whl"}]}

    def delivery(self, effects, entry=None):
        opener = unittest.mock.Mock()
        opener.open.side_effect = effects
        with patch.object(mirrors.urllib.request, "build_opener", return_value=opener):
            result = mirrors.download_with_mirrors(self.root, entry or self.entry, self.directory, time.monotonic() + 599)
        return result, opener

    def observations(self):
        return [read_json(p) for p in self.directory.glob("*.delivery-*.json")]

    def test_transport_failure_uses_identical_reviewed_mirror(self):
        result, opener = self.delivery([TimeoutError("primary"), io.BytesIO(self.good)])
        self.assertEqual(result.read_bytes(), self.good)
        self.assertEqual(opener.open.call_count, 2)
        observations = self.observations()
        self.assertEqual({r["status"] for r in observations}, {"DELIVERY_FAILED", "VERIFIED_DELIVERY"})
        self.assertTrue(all(r["expected_sha256"] == digest(self.good) and not r["domain_proof"] for r in observations))
        self.assertTrue(all(r["upstream_url"] == self.entry["url"] for r in observations))

    def test_wrong_hash_quarantined_before_next_route(self):
        bad = b"X" * len(self.good)
        result, _ = self.delivery([io.BytesIO(bad), io.BytesIO(self.good)])
        self.assertEqual(result.read_bytes(), self.good)
        self.assertEqual([p.read_bytes() for p in (self.directory / "quarantine").glob("*")], [bad])
        failed = next(r for r in self.observations() if r["status"] == "DELIVERY_FAILED")
        self.assertEqual(failed["observed_sha256"], digest(bad))
        self.assertIn("untrusted_bytes", failed)

    def test_oversize_source_cannot_be_promoted(self):
        result, _ = self.delivery([io.BytesIO(self.good + b"extra"), io.BytesIO(self.good)])
        self.assertEqual(result.read_bytes(), self.good)
        self.assertTrue(any(r.get("observed_size", 0) > len(self.good) for r in self.observations()))

    def test_exhausted_sources_leave_no_installable_artifact(self):
        with self.assertRaisesRegex(ContractError, "sources exhausted"):
            self.delivery([TimeoutError(), OSError()])
        self.assertFalse((self.directory / self.entry["filename"]).exists())
        self.assertEqual(len(self.observations()), 2)

    def test_original_upstream_cannot_be_removed(self):
        entry = copy.deepcopy(self.entry)
        entry["sources"] = entry["sources"][1:]
        with self.assertRaisesRegex(ContractError, "upstream provenance"):
            self.delivery([], entry)

    def test_credential_http_unknown_host_and_extra_routes_rejected(self):
        for url in ("http://files.pythonhosted.org/x", "https://user:secret@files.pythonhosted.org/x", "https://unreviewed.example/x"):
            entry = copy.deepcopy(self.entry)
            entry["sources"][1]["url"] = url
            with self.subTest(url=url), self.assertRaises(ContractError):
                self.delivery([], entry)
        entry = copy.deepcopy(self.entry)
        entry["sources"] *= 2
        with self.assertRaises(ContractError):
            self.delivery([], entry)

    def test_redirect_scope_and_count_preserve_https(self):
        request = urllib.request.Request(self.entry["url"])
        redirect = mirrors._MirrorRedirect(["files.pythonhosted.org"], 1)
        for url in ("http://files.pythonhosted.org/x", "https://unknown.example/x", "https://user@files.pythonhosted.org/x"):
            with self.subTest(url=url), self.assertRaises(ContractError):
                redirect.redirect_request(request, None, 302, "", {}, url)
        next_request = redirect.redirect_request(request, None, 302, "", {}, self.entry["url"] + "?next")
        self.assertEqual(next_request.aegis_redirects, 1)
        with self.assertRaises(ContractError):
            redirect.redirect_request(next_request, None, 302, "", {}, self.entry["url"])

    def test_cache_tamper_and_partial_bytes_are_preserved(self):
        self.directory.mkdir(parents=True)
        target = self.directory / self.entry["filename"]
        target.write_bytes(b"unreviewed cache")
        with self.assertRaisesRegex(ContractError, "cached artifact"):
            self.delivery([])
        self.assertEqual(target.read_bytes(), b"unreviewed cache")
        target.unlink()
        partial = self.directory / (self.entry["filename"] + ".source-0.partial")
        partial.write_bytes(b"prior interrupted bytes")
        with self.assertRaisesRegex(ContractError, "reconciliation"):
            self.delivery([])
        self.assertEqual(partial.read_bytes(), b"prior interrupted bytes")

    def test_valid_cache_reuses_exact_bytes_without_network(self):
        self.directory.mkdir(parents=True)
        target = self.directory / self.entry["filename"]
        target.write_bytes(self.good)
        result, opener = self.delivery([])
        self.assertEqual(result, target)
        opener.open.assert_not_called()

    def test_deadline_and_weakened_policy_are_denied(self):
        with self.assertRaisesRegex(ContractError, "deadline"):
            mirrors.download_with_mirrors(self.root, self.entry, self.directory, time.monotonic() - 1)
        policy = read_json(self.root / mirrors.POLICY_PATH)
        policy["allow_tls_downgrade"] = True
        (self.root / mirrors.POLICY_PATH).write_text(json.dumps(policy))
        with self.assertRaisesRegex(ContractError, "precautions"):
            self.delivery([])


class RetryScopeTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.work_id = digest({"recipe": "python.toolchain", "root": str(self.root), "native_thread": "thread",
                               "project": "Aegis", "milestone": "A09"})
        self.native = {"thread_id": "thread", "objective": "objective", "observation": {"createdAt": 1}}
        self.record = {"execution": {"native_binding": self.native, "budget_amendments": {}}}
        registry = self.root / "Roadmaps/Shared/registry.json"
        registry.parent.mkdir(parents=True)
        shutil.copyfile(SOURCE / "Roadmaps/Shared/registry.json", registry)
        shutil.copyfile(SOURCE / "Roadmaps/Shared/records.schema.json", registry.with_name("records.schema.json"))
        canonical = self.root / ".aegis/project.json"
        canonical.parent.mkdir(parents=True)
        canonical.write_text(json.dumps({"schema": 1, "project": "Aegis", **self.record}))
        self.prior = [{"id": str(i), "work_id": self.work_id, "inputs": "input" + str(i), "status": "FAILED",
                       "reserved_seconds": 900, "generation": 1} for i in range(2)]
        dependency = self.root / "pin.json"
        dependency.write_text("pinned")
        self.amendment = {"schema": 1, "kind": "user_authorized_single_retry", "work_id": self.work_id,
                          "recipe": "python.toolchain", "milestone": "A09", "native_thread": "thread",
                          "goal_created_at": 1, "objective": "objective", "source": {"role": "user", "content": "try mirrors",
                          "question_item_id": "question", "observed_native_turn": "turn"},
                          "base_limits": {"max_attempts": 2, "total_seconds": 1800},
                          "limits": {"max_attempts": 3, "total_seconds": 2700}, "additional_seconds": 900,
                          "dependencies": [file_binding(self.root, "pin.json")], "prior_attempts": copy.deepcopy(self.prior),
                          "preserve_attempt_lineage": True, "domain_proof": False}

    def bind(self):
        (self.root / "authorization.json").write_text(json.dumps(self.amendment))
        self.record["execution"]["budget_amendments"][self.work_id] = file_binding(self.root, "authorization.json")

    @contextmanager
    def state(self, ledger=None):
        with patch("agentinfra.roadmap_project.ProjectAdapter.read", return_value=self.record), \
             patch.object(BudgetLedger, "read", return_value={"attempts": self.prior if ledger is None else ledger}):
            yield

    def test_default_and_other_work_unit_limits_remain_unchanged(self):
        with self.state():
            self.assertEqual(retry_limits(self.root, "A09", "python.toolchain", 2, 1800), {"max_attempts": 2, "total_seconds": 1800})
        self.bind()
        with self.state():
            self.assertEqual(retry_limits(self.root, "A04", "original.tests", 2, 1800), {"max_attempts": 2, "total_seconds": 1800})

    def test_exact_scope_preserves_two_failed_attempts(self):
        self.bind()
        with self.state():
            limits = retry_limits(self.root, "A09", "python.toolchain", 2, 1800)
        self.assertEqual((limits["max_attempts"], limits["total_seconds"]), (3, 2700))
        self.assertEqual(self.prior, self.amendment["prior_attempts"])
        third = dict(self.prior[-1], id="third", status="RESERVED")
        with self.state([*self.prior, third]):
            self.assertEqual(retry_limits(self.root, "A09", "python.toolchain", 2, 1800), limits)

    def test_stale_pin_goal_scope_and_false_authority_denied(self):
        for field, value in (("goal_created_at", 2), ("recipe", "original.tests"), ("preserve_attempt_lineage", False),
                             ("source", {"role": "assistant", "content": "approved"})):
            original = self.amendment[field]
            self.amendment[field] = value
            self.bind()
            with self.subTest(field=field), self.state(), self.assertRaises(ContractError):
                retry_limits(self.root, "A09", "python.toolchain", 2, 1800)
            self.amendment[field] = original
        self.bind()
        (self.root / "pin.json").write_text("changed")
        with self.state(), self.assertRaisesRegex(ContractError, "inputs changed"):
            retry_limits(self.root, "A09", "python.toolchain", 2, 1800)

    def test_missing_or_modified_failed_history_denied(self):
        self.bind()
        with self.state(self.prior[1:]), self.assertRaises(ContractError):
            retry_limits(self.root, "A09", "python.toolchain", 2, 1800)
        changed = copy.deepcopy(self.prior)
        changed[0]["reserved_seconds"] = 0
        with self.state(changed), self.assertRaises(ContractError):
            retry_limits(self.root, "A09", "python.toolchain", 2, 1800)

    def test_consumed_retry_cannot_expand_a_later_candidate_or_generation(self):
        self.bind()
        spec = {"candidate": "authorized-candidate"}
        spec["digest"] = digest(spec)
        (self.root / "spec.json").write_text(json.dumps(spec))
        third = dict(self.prior[-1], id="third", status="SUCCESS", inputs=spec["digest"],
                     operation={"spec": file_binding(self.root, "spec.json")})
        base = {"max_attempts": 2, "total_seconds": 1800}
        with self.state([*self.prior, third]):
            self.assertEqual(retry_limits(self.root, "A09", "python.toolchain", 2, 1800, candidate="later-candidate"), base)
            self.assertEqual(retry_limits(self.root, "A09", "python.toolchain", 2, 1800,
                                          candidate="authorized-candidate")["max_attempts"], 3)
        later = dict(third, id="fourth", generation=2)
        with self.state([*self.prior, third, later]):
            self.assertEqual(retry_limits(self.root, "A09", "python.toolchain", 2, 1800, candidate="later-candidate"), base)


if __name__ == "__main__":
    unittest.main()
