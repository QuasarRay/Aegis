"""Reviewed mirror delivery for exact pinned public artifacts.

Mirrors change delivery routes, never artifact identity or proof strength. The
existing named recipe and ledger own the operation and its cumulative budget.
"""
from __future__ import annotations

import hashlib
from pathlib import Path
import ssl
import time
import urllib.request

from .atomic import atomic_write_json
from .roadmap_download import _host, _ResolvedConnection, DNS_ENDPOINT
from .roadmap_records import digest, file_binding, read_json, require, ContractError
from .security import confined_path


INTERFACE_VERSION = 1
POLICY_PATH = "Roadmaps/Shared/download-policy.json"
TRANSPORT = "reviewed-mirrors-original-host-tls-v1"


def read_download_policy(root: Path) -> dict:
    policy = read_json(confined_path(root, POLICY_PATH, must_exist=True))
    require(policy.get("schema") == 1 and policy.get("transport") == TRANSPORT and
            policy.get("identity") == "exact_upstream_sha256_and_size" and
            policy.get("tls") == "required_original_hostname" and policy.get("dns_endpoint") == DNS_ENDPOINT,
            "download identity/TLS/DNS policy is unsupported or weakened")
    for field, maximum in (("max_sources_per_artifact", 4), ("max_addresses_per_source", 4),
                           ("socket_timeout_seconds", 20), ("source_timeout_seconds", 120),
                           ("stage_timeout_seconds", 600), ("max_redirects", 8)):
        require(type(policy.get(field)) is int and 0 < policy[field] <= maximum, "unbounded mirror policy: " + field)
    require(policy.get("quarantine_integrity_failures") is True and policy.get("preserve_attempt_lineage") is True and
            policy.get("allow_credentials") is False and policy.get("allow_tls_downgrade") is False,
            "mirror precautions were weakened")
    providers = policy.get("providers", {})
    require(providers and len(providers) <= 16, "empty or unbounded mirror provider registry")
    for name, provider in providers.items():
        require(name and provider.get("review_source") and provider.get("hosts") and len(provider["hosts"]) <= 16,
                "mirror provider lacks reviewed provenance/host bounds")
        for host in provider["hosts"]:
            require(_host("https://" + host) == host and "*" not in host, "mirror host allowlist must contain exact HTTPS hostnames")
    return policy


def _sources(entry: dict, policy: dict) -> list[dict]:
    sources = entry.get("sources")
    require(isinstance(sources, list) and 1 <= len(sources) <= policy["max_sources_per_artifact"], "artifact needs a bounded reviewed source list")
    require(len({source.get("url") for source in sources}) == len(sources), "duplicate mirror delivery route")
    for source in sources:
        provider = policy["providers"].get(source.get("provider"))
        require(provider and _host(source["url"]) in provider["hosts"], "artifact mirror is outside reviewed provider hosts")
    require(any(source["url"] == entry["url"] for source in sources), "original upstream provenance was omitted from the delivery list")
    return sources


class _MirrorHTTPS(urllib.request.HTTPSHandler):
    def __init__(self, events: list[dict], hosts: list[str], deadline: float, policy: dict):
        super().__init__(context=ssl.create_default_context())
        require(self._context.check_hostname and self._context.verify_mode == ssl.CERT_REQUIRED, "mirror TLS verification is required")
        self.events, self.hosts, self.deadline, self.policy = events, hosts, deadline, policy

    def https_open(self, request):
        require(_host(request.full_url) in self.hosts, "mirror request left the reviewed provider hosts")
        def connection(host, **kwargs):
            return _ResolvedConnection(host, observations=self.events, deadline=self.deadline,
                                       max_addresses=self.policy["max_addresses_per_source"], **kwargs)
        return self.do_open(connection, request, context=self._context)


class _MirrorRedirect(urllib.request.HTTPRedirectHandler):
    def __init__(self, hosts: list[str], maximum: int):
        self.hosts, self.maximum = hosts, maximum

    def redirect_request(self, request, fp, code, message, headers, newurl):
        count = getattr(request, "aegis_redirects", 0) + 1
        require(count <= self.maximum and _host(newurl) in self.hosts, "mirror redirect exceeds its reviewed HTTPS host/count scope")
        result = super().redirect_request(request, fp, code, message, headers, newurl)
        if result is not None:
            result.aegis_redirects = count
        return result


def _save(root: Path, directory: Path, name: str, record: dict) -> None:
    path = confined_path(root, directory / (name + ".delivery-" + digest(record) + ".json"))
    atomic_write_json(path, record, root=root, mode=0o600)


def download_with_mirrors(root: Path, entry: dict, directory: Path, deadline: float) -> Path:
    """Try bounded reviewed routes, admitting only identical pinned bytes."""
    policy = read_download_policy(root)
    sources = _sources(entry, policy)
    directory = confined_path(root, directory)
    directory.mkdir(parents=True, exist_ok=True)
    name = entry.get("filename", entry.get("name", ""))
    require(name and Path(name).name == name and name not in {".", ".."}, "artifact filename escapes its directory")
    require(type(entry.get("size")) is int and entry["size"] > 0 and len(entry.get("sha256", "")) == 64 and
            all(c in "0123456789abcdef" for c in entry["sha256"]), "artifact needs an exact reviewed size/SHA-256")
    require(deadline > time.monotonic() and deadline - time.monotonic() <= policy["stage_timeout_seconds"] + 1,
            "mirror stage deadline is expired or exceeds policy")
    target = confined_path(root, directory / name)
    if target.exists():
        require(target.stat().st_size == entry["size"] and digest(target.read_bytes()) == entry["sha256"], "cached artifact differs from upstream pin")
        return target
    results = []
    for ordinal, source in enumerate(sources):
        require(time.monotonic() < deadline, "mirror stage deadline exhausted")
        events, created = [], False
        partial = confined_path(root, directory / (name + ".source-" + str(ordinal) + ".partial"))
        require(not partial.exists(), "pre-existing partial artifact requires reconciliation")
        source_deadline = min(deadline, time.monotonic() + policy["source_timeout_seconds"])
        provider = policy["providers"][source["provider"]]
        record = {"schema": 1, "transport": TRANSPORT, "provider": source["provider"], "source_url": source["url"],
                  "upstream_url": entry["url"], "expected_sha256": entry["sha256"], "expected_size": entry["size"],
                  "policy": file_binding(root, POLICY_PATH), "events": events, "domain_proof": False}
        try:
            opener = urllib.request.build_opener(urllib.request.ProxyHandler({}),
                        _MirrorHTTPS(events, provider["hosts"], source_deadline, policy),
                        _MirrorRedirect(provider["hosts"], policy["max_redirects"]))
            request = urllib.request.Request(source["url"], headers={"User-Agent": "Aegis-pinned-mirror-delivery", "Accept-Encoding": "identity",
                                                                     "Accept": "application/octet-stream"})
            hashed, count = hashlib.sha256(), 0
            with opener.open(request, timeout=policy["socket_timeout_seconds"]) as response:
                with partial.open("xb") as output:
                    created = True
                    while True:
                        require(time.monotonic() < source_deadline, "mirror source deadline exhausted")
                        chunk = response.read1(262144)
                        if not chunk:
                            break
                        count += len(chunk)
                        hashed.update(chunk)
                        output.write(chunk)
                        require(count <= entry["size"], "mirror artifact exceeds reviewed byte length")
            record.update(observed_size=count, observed_sha256=hashed.hexdigest())
            require(count == entry["size"] and hashed.hexdigest() == entry["sha256"], "mirror bytes differ from the independent upstream pin")
            require(not target.exists(), "artifact destination changed during delivery")
            partial.replace(target)
            record.update(status="VERIFIED_DELIVERY", artifact=file_binding(root, target.relative_to(root).as_posix()))
            _save(root, directory, name, record)
            return target
        except Exception as exc:
            require(not target.exists(), "verified artifact promotion requires delivery-observation reconciliation")
            record.update(status="DELIVERY_FAILED", error_type=type(exc).__name__)
            if created and partial.exists():
                raw = partial.read_bytes()
                quarantine = confined_path(root, directory / "quarantine" / (name + "-" + digest(raw) + ".unverified"))
                quarantine.parent.mkdir(parents=True, exist_ok=True)
                if quarantine.exists():
                    require(quarantine.read_bytes() == raw, "quarantined artifact identity conflicts")
                    partial.unlink()
                else:
                    partial.replace(quarantine)
                record.update(untrusted_bytes=file_binding(root, quarantine.relative_to(root).as_posix()),
                              observed_size=len(raw), observed_sha256=digest(raw))
            _save(root, directory, name, record)
            results.append({"provider": source["provider"], "error_type": type(exc).__name__})
    raise ContractError("reviewed mirror sources exhausted: " + str(results))
