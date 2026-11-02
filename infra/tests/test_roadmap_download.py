"""Pinned artifact transport regressions; no external services are contacted."""
from __future__ import annotations

import io
import json
from pathlib import Path
import ssl
import tempfile
import unittest
from unittest.mock import MagicMock, patch

from agentinfra.roadmap_download import (_addresses, _HTTPSHandler, _HTTPSRedirect,
                                        _ResolvedConnection, download_pinned)
from agentinfra.roadmap_records import ContractError, digest
from agentinfra.security import SecurityError


class PinnedDownloadTests(unittest.TestCase):
    def entry(self, raw=b"pinned wheel"):
        return {"filename": "tool.whl", "url": "https://files.pythonhosted.org/packages/tool.whl",
                "size": len(raw), "sha256": digest(raw)}

    def test_selected_ip_preserves_original_tls_hostname_and_certificate_observation(self):
        context, sock, wrapped = MagicMock(), MagicMock(), MagicMock()
        context.wrap_socket.return_value = wrapped
        wrapped.getpeercert.return_value = b"peer certificate"
        wrapped.version.return_value = "TLSv1.3"
        events = []
        connection = _ResolvedConnection("files.pythonhosted.org", observations=events, context=context, timeout=20)
        with patch("agentinfra.roadmap_download._addresses", return_value=["151.101.0.223"]), patch("agentinfra.roadmap_download.socket.create_connection", return_value=sock) as connect:
            connection.connect()
        connect.assert_called_once_with(("151.101.0.223", 443), 20, None)
        context.wrap_socket.assert_called_once_with(sock, server_hostname="files.pythonhosted.org")
        self.assertEqual(connection.sock, wrapped)
        self.assertEqual(events[0]["peer_certificate_sha256"], digest(b"peer certificate"))
        self.assertEqual(events[0]["host"], "files.pythonhosted.org")

    def test_tls_handler_requires_default_certificate_and_hostname_verification(self):
        handler = _HTTPSHandler([])
        self.assertTrue(handler._context.check_hostname)
        self.assertEqual(handler._context.verify_mode, ssl.CERT_REQUIRED)

    def test_dns_wrong_question_truncation_disabled_validation_and_private_addresses_rejected(self):
        base = {"Status": 0, "TC": False, "CD": False, "Question": [{"name": "files.pythonhosted.org.", "type": 1}],
                "Answer": [{"type": 1, "data": "151.101.0.223"}]}
        for update in ({"Status": False}, {"TC": True}, {"CD": True}, {"Question": [{"name": "other.example", "type": 1}]},
                       {"Answer": []}, {"Answer": [{"type": 1, "data": "127.0.0.1"}]}):
            with self.subTest(update=update), patch("agentinfra.roadmap_download.urllib.request.urlopen", return_value=io.BytesIO(json.dumps(dict(base, **update)).encode())):
                with self.assertRaises(ContractError):
                    _addresses("files.pythonhosted.org", [])
        events = []
        with patch("agentinfra.roadmap_download.urllib.request.urlopen", return_value=io.BytesIO(json.dumps(base).encode())):
            self.assertEqual(_addresses("files.pythonhosted.org", events), ["151.101.0.223"])
        self.assertTrue(events[0]["response_sha256"])

    def test_wrong_or_oversized_blob_is_never_promoted_and_partial_is_removed(self):
        for raw in (b"wrong! wheel", b"pinned wheel with extra bytes"):
            with self.subTest(raw=raw), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                opener = MagicMock()
                opener.open.return_value = io.BytesIO(raw)
                with patch("agentinfra.roadmap_download.urllib.request.build_opener", return_value=opener):
                    with self.assertRaises(ContractError):
                        download_pinned(root, self.entry(), root / "downloads")
                self.assertFalse((root / "downloads/tool.whl").exists())
                self.assertFalse((root / "downloads/tool.whl.partial").exists())

    def test_exact_blob_reuses_immutable_pin_without_another_network_request(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            opener = MagicMock()
            opener.open.return_value = io.BytesIO(b"pinned wheel")
            with patch("agentinfra.roadmap_download.urllib.request.build_opener", return_value=opener) as build:
                first = download_pinned(root, self.entry(), root / "downloads")
                second = download_pinned(root, self.entry(), root / "downloads")
            self.assertEqual(first, second)
            self.assertEqual(build.call_count, 1)
            observation = json.loads(next(first.parent.glob("tool.whl.transport-*.json")).read_text())
            self.assertEqual(observation["artifact"]["sha256"], self.entry()["sha256"])
            self.assertFalse(observation["domain_proof"])

    def test_tampered_cache_and_escaping_filenames_are_preserved_and_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            cache = root / "downloads"
            cache.mkdir()
            target = cache / "tool.whl"
            target.write_bytes(b"user bytes")
            with self.assertRaises(ContractError):
                download_pinned(root, self.entry(), cache)
            self.assertEqual(target.read_bytes(), b"user bytes")
            with self.assertRaises(ContractError):
                download_pinned(root, dict(self.entry(), filename="../escape.whl"), cache)

    def test_preexisting_partial_is_preserved_and_failure_observation_retained(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            cache = root / "downloads"
            cache.mkdir()
            partial = cache / "tool.whl.partial"
            partial.write_bytes(b"preexisting bytes")
            opener = MagicMock()
            opener.open.return_value = io.BytesIO(b"pinned wheel")
            with patch("agentinfra.roadmap_download.urllib.request.build_opener", return_value=opener):
                with self.assertRaises(FileExistsError):
                    download_pinned(root, self.entry(), cache)
            self.assertEqual(partial.read_bytes(), b"preexisting bytes")
            observation = json.loads(next(cache.glob("tool.whl.transport-*.json")).read_text())
            self.assertEqual(observation["status"], "ERROR")
            self.assertEqual(observation["error_type"], "FileExistsError")

    def test_redirect_cannot_downgrade_https(self):
        for url in ("http://files.pythonhosted.org/tool.whl", "file:///tmp/tool.whl", "https://user:password@example.com/tool.whl"):
            with self.subTest(url=url), self.assertRaises(ContractError):
                _HTTPSRedirect().redirect_request(None, None, 302, "redirect", {}, url)


if __name__ == "__main__":
    unittest.main()
