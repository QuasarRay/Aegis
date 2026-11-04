"""Bounded pinned-artifact HTTPS transport with recipe-local HTTPS DNS.

No resolver, proxy, certificate store or host-network setting is changed. DNS
answers select a connection address; TLS still authenticates the original host
and the artifact must match its reviewed byte length and SHA-256 before use.
"""
from __future__ import annotations

import http.client
import ipaddress
from pathlib import Path
import socket
import ssl
import time
import urllib.parse
import urllib.request

from .atomic import atomic_write_json
from .roadmap_records import digest, file_binding, loads, require
from .security import confined_path


INTERFACE_VERSION = 1
DNS_ENDPOINT = "https://1.1.1.1/dns-query"
TRANSPORT = "https-dns-original-host-tls-v1"


def _host(url: str) -> str:
    parsed = urllib.parse.urlsplit(url)
    require(parsed.scheme == "https" and parsed.hostname and parsed.port in {None, 443} and
            parsed.username is None and parsed.password is None, "pinned downloads require credential-free HTTPS on port 443")
    return parsed.hostname.encode("idna").decode("ascii").lower().rstrip(".")


def _addresses(host: str, observations: list[dict], *, timeout: float = 12) -> list[str]:
    query = DNS_ENDPOINT + "?" + urllib.parse.urlencode({"name": host, "type": "A"})
    request = urllib.request.Request(query, headers={"Accept": "application/dns-json", "User-Agent": "Aegis-pinned-download"})
    # The resolver URL uses an IP literal with a certificate valid for that IP;
    # this bootstrap does not depend on the failing host resolver.
    with urllib.request.urlopen(request, timeout=timeout) as response:
        raw = response.read(65537)
    require(len(raw) <= 65536, "HTTPS DNS response exceeds the fixed bound")
    answer = loads(raw.decode("utf-8"))
    questions = answer.get("Question", [])
    require(type(answer.get("Status")) is int and answer["Status"] == 0 and answer.get("TC") is False and
            answer.get("CD") is False and len(questions) == 1 and questions[0].get("name", "").lower().rstrip(".") == host and
            type(questions[0].get("type")) is int and questions[0]["type"] == 1,
            "HTTPS DNS response is unsuccessful, truncated or for another question")
    addresses = sorted({str(ipaddress.IPv4Address(row["data"])) for row in answer.get("Answer", []) if row.get("type") == 1})
    require(addresses and all(ipaddress.IPv4Address(address).is_global for address in addresses),
            "HTTPS DNS returned no public IPv4 artifact addresses")
    observations.append({"kind": "https_dns", "host": host, "resolver": DNS_ENDPOINT,
                         "response_sha256": digest(raw), "addresses": addresses})
    return addresses


class _ResolvedConnection(http.client.HTTPSConnection):
    def __init__(self, host: str, *, observations: list[dict], deadline: float | None = None,
                 max_addresses: int | None = 16, resolver_timeout: float = 12, **kwargs):
        super().__init__(host, **kwargs)
        self.observations = observations
        self.deadline = deadline
        self.max_addresses = max_addresses
        self.resolver_timeout = resolver_timeout

    def connect(self) -> None:
        require(not self._tunnel_host, "pinned artifact transport does not use ambient tunnels")
        last_error = None
        addresses = _addresses(self.host, self.observations, timeout=self.resolver_timeout)
        for address in addresses if self.max_addresses is None else addresses[:self.max_addresses]:
            sock = None
            try:
                if self.deadline is not None:
                    remaining = self.deadline - time.monotonic()
                    require(remaining > 0, "pinned source deadline exhausted")
                    self.timeout = min(self.timeout, remaining)
                sock = socket.create_connection((address, self.port), self.timeout, self.source_address)
                self.sock = self._context.wrap_socket(sock, server_hostname=self.host)
                self.observations.append({"kind": "tls_connection", "host": self.host, "address": address,
                                          "tls_version": self.sock.version(),
                                          "peer_certificate_sha256": digest(self.sock.getpeercert(binary_form=True))})
                return
            except OSError as exc:
                if sock is not None:
                    sock.close()
                self.observations.append({"kind": "tls_connection_failed", "host": self.host,
                                          "address": address, "error_type": type(exc).__name__})
                last_error = exc
        require(last_error is not None, "artifact connection was not attempted")
        raise last_error


class _HTTPSHandler(urllib.request.HTTPSHandler):
    def __init__(self, observations: list[dict]):
        super().__init__(context=ssl.create_default_context())
        require(self._context.verify_mode == ssl.CERT_REQUIRED and self._context.check_hostname,
                "artifact TLS hostname/certificate verification is required")
        self.observations = observations

    def https_open(self, request):
        _host(request.full_url)
        def connection(host, **kwargs):
            return _ResolvedConnection(host, observations=self.observations, **kwargs)
        return self.do_open(connection, request, context=self._context)


class _HTTPSRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, message, headers, newurl):
        _host(newurl)
        return super().redirect_request(request, fp, code, message, headers, newurl)


def download_pinned(root: Path, entry: dict, directory: Path) -> Path:
    """Download one exact reviewed blob or verify and reuse the existing blob."""
    directory = confined_path(root, directory)
    directory.mkdir(parents=True, exist_ok=True)
    name = entry.get("filename", entry.get("name", ""))
    require(name and Path(name).name == name and name not in {".", ".."}, "artifact filename escapes its directory")
    path = confined_path(root, directory / name)
    require(type(entry.get("size")) is int and entry["size"] > 0 and len(entry.get("sha256", "")) == 64,
            "artifact needs an exact positive byte length and SHA-256")
    _host(entry["url"])
    if path.exists():
        require(path.stat().st_size == entry["size"] and digest(path.read_bytes()) == entry["sha256"], "cached artifact differs from reviewed pin")
        return path
    partial = confined_path(root, directory / (name + ".partial"))
    observations = []
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), _HTTPSHandler(observations), _HTTPSRedirect())
    created_partial = False
    try:
        request = urllib.request.Request(entry["url"], headers={"User-Agent": "Aegis-pinned-download", "Accept-Encoding": "identity"})
        with opener.open(request, timeout=20) as response:
            with partial.open("xb") as output:
                created_partial = True
                count = 0
                while chunk := response.read(262144):
                    count += len(chunk)
                    require(count <= entry["size"], "artifact exceeds reviewed byte length")
                    output.write(chunk)
        require(partial.stat().st_size == entry["size"] and digest(partial.read_bytes()) == entry["sha256"],
                "downloaded artifact differs from reviewed size or SHA-256")
        partial.replace(path)
        observation = {"schema": 1, "status": "DOWNLOADED", "transport": TRANSPORT, "source_url": entry["url"], "events": observations,
                       "artifact": file_binding(root, path.relative_to(root).as_posix()), "domain_proof": False}
        atomic_write_json(path.with_name(name + ".transport-" + digest(observation) + ".json"), observation, root=root, mode=0o600)
        return path
    except Exception as exc:
        observation = {"schema": 1, "status": "ERROR", "transport": TRANSPORT, "source_url": entry["url"],
                       "events": observations, "error_type": type(exc).__name__, "domain_proof": False}
        atomic_write_json(path.with_name(name + ".transport-" + digest(observation) + ".json"), observation, root=root, mode=0o600)
        raise
    finally:
        if created_partial:
            partial.unlink(missing_ok=True)
