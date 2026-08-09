from __future__ import annotations

import hashlib
import json
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / ".agents" / "infra"))
sys.path.insert(0, str(ROOT / ".agents" / "infra" / "law_tests"))

from agentinfra.audit import audit
from agentinfra.manifest import build_archive, entries, safe_extract, verify as verify_manifest
from agentinfra.process import run_process
from build_traceability import build as build_traceability


FINAL_STATUSES = {
    "EXISTING_AND_VERIFIED",
    "IMPLEMENTED_AND_PASSING",
    "SUPERSEDED_BY_STRONGER_EQUIVALENT_AND_PROVEN",
    "NOT_APPLICABLE_WITH_CONCRETE_JUSTIFICATION",
    "BLOCKED_BY_PROVEN_EXTERNAL_LIMITATION",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def immutable_snapshot(root: Path) -> str:
    values: dict[str, str] = {}
    for relative, digest in entries(root):
        values[relative] = digest
        source = root / Path(relative).relative_to(".agents")
        if (root / "framework.toml").is_file() and source.is_file():
            values["source:" + source.relative_to(root).as_posix()] = sha(source)
    for relative in (".agents/MANIFEST.sha256", "MANIFEST.sha256", "RELEASE.json", "AGENTS.md"):
        path = root / relative
        if path.is_file():
            values[relative] = sha(path)
    return hashlib.sha256(json.dumps(values, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()


def execute(label: str, argv: list[str], cwd: Path, *, expected: set[int] = {0}, timeout: float = 180.0) -> tuple[dict, str]:
    result = run_process(argv, cwd=cwd, timeout=timeout, capture_limit=256_000)
    record = {
        "label": label,
        "argv": list(result.argv),
        "exit": result.returncode,
        "timed_out": result.timed_out,
        "duration_seconds": result.duration_seconds,
        "stdout_bytes": result.stdout_bytes,
        "stderr_bytes": result.stderr_bytes,
        "stdout_sha256": result.stdout_sha256,
        "stderr_sha256": result.stderr_sha256,
    }
    if result.timed_out or result.returncode not in expected:
        raise RuntimeError(
            f"{label} failed: {record}; stdout={result.stdout[-4000:]!r}; stderr={result.stderr[-4000:]!r}"
        )
    return record, result.stdout


def validate_traceability(root: Path, ledger: Path) -> dict:
    artifact = json.loads((root / ".agents" / "infra" / "law_tests" / "traceability.json").read_text(encoding="utf-8"))
    rebuilt = build_traceability(root, ledger)
    if artifact != rebuilt:
        committed = {item.get("name"): item for item in artifact.get("requirements", [])}
        fresh = {item.get("name"): item for item in rebuilt.get("requirements", [])}
        drift = [name for name in sorted(set(committed) | set(fresh)) if committed.get(name) != fresh.get(name)]
        top_level = [key for key in sorted(set(artifact) | set(rebuilt)) if key != "requirements" and artifact.get(key) != rebuilt.get(key)]
        raise RuntimeError(
            "committed traceability is not the exact deterministic projection of the fresh outer ledger; "
            f"top_level_drift={top_level[:8]} requirement_drift={drift[:8]}"
        )
    requirements = artifact.get("requirements", [])
    if artifact.get("requirement_count") != 834 or len(requirements) != 834:
        raise RuntimeError("traceability does not contain exactly 834 requirements")
    if any(item.get("status") not in FINAL_STATUSES or not item.get("last_result") for item in requirements):
        raise RuntimeError("traceability contains a missing, pending, or unproved requirement")
    counts: dict[str, int] = {}
    for item in requirements:
        counts[item["status"]] = counts.get(item["status"], 0) + 1
    return dict(sorted(counts.items()))


def main() -> int:
    root = ROOT.resolve(strict=True)
    before = immutable_snapshot(root)
    commands: list[dict] = []

    manifest_ok, manifest_detail = verify_manifest(root, require_release_anchor=True)
    if not manifest_ok:
        raise RuntimeError(f"source manifest failed: {manifest_detail}")
    source_issues = audit(root)
    if source_issues:
        raise RuntimeError(f"source audit failed: {source_issues}")
    python = sys.executable
    source_ledger = root / ".agents" / "persistent" / "law-results" / "release-source.json"
    outer_record, _ = execute(
        "outer-834-laws",
        [python, "-B", ".agents/infra/law_tests/run_suite.py", "--root", str(root), "--output", str(source_ledger)],
        root,
        timeout=900.0,
    )
    commands.append(outer_record)
    traceability_counts = validate_traceability(root, source_ledger)
    for label, argv, timeout in (
        ("unit", [python, "-B", "-m", "unittest", "discover", "-s", ".agents/infra/tests", "-p", "test_*.py"], 180.0),
        ("traceability-meta", [python, "-B", "-m", "unittest", "discover", "-s", ".agents/infra/law_tests", "-p", "test_meta.py"], 900.0),
        ("exact-name-adapters", [python, "-B", "-m", "unittest", "discover", "-s", ".agents/infra/law_tests", "-p", "test_specification.py"], 900.0),
        ("built-in-laws", [python, "-B", ".agents/scripts/selftest.py"], 120.0),
        ("codex-static", [python, "-B", ".agents/modules/codex/verify.py"], 60.0),
        ("xonsh-live", [python, "-B", ".agents/modules/xonsh/verify.py"], 90.0),
    ):
        record, _ = execute(label, argv, root, timeout=timeout)
        commands.append(record)
    python_meta, python_meta_stdout = execute(
        "python-meta", [python, "-B", ".agents/modules/python-meta/probe.py"], root, expected={0, 2}, timeout=60.0
    )
    meta_payload = json.loads(python_meta_stdout)
    if python_meta["exit"] == 2 and not (
        meta_payload.get("outcome") == "UNAVAILABLE"
        and meta_payload.get("capability_status") == "MISSING"
        and meta_payload.get("core_without_extensions") is True
    ):
        raise RuntimeError("optional Python-meta absence was not reported explicitly")
    commands.append(python_meta)

    with tempfile.TemporaryDirectory(prefix="aegis-release-clean-room-") as directory:
        temporary = Path(directory)
        first_archive = temporary / "aegis-first.zip"
        second_archive = temporary / "aegis-second.zip"
        first = build_archive(root, first_archive)
        second = build_archive(root, second_archive)
        if first["sha256"] != second["sha256"]:
            raise RuntimeError("release archives are not byte reproducible")
        extracted = temporary / "extracted"
        members = safe_extract(first_archive, extracted)
        if ".agents/tests-to-impl/INDEX.md" not in members:
            raise RuntimeError("clean release omits the executable law specification")
        bootstrap_record, _ = execute(
            "clean-bootstrap", [python, "-B", str(extracted / ".agents" / "bootstrap" / "install.py"), "--apply"], extracted, timeout=60.0
        )
        commands.append(bootstrap_record)
        clean_manifest_ok, clean_manifest_detail = verify_manifest(extracted, require_release_anchor=True)
        if not clean_manifest_ok:
            raise RuntimeError(f"clean manifest failed: {clean_manifest_detail}")
        clean_ledger = extracted / ".agents" / "persistent" / "law-results" / "release-clean.json"
        clean_outer, _ = execute(
            "clean-outer-834-laws",
            [python, "-B", ".agents/infra/law_tests/run_suite.py", "--root", str(extracted), "--output", str(clean_ledger)],
            extracted,
            timeout=900.0,
        )
        commands.append(clean_outer)
        clean_traceability_counts = validate_traceability(extracted, clean_ledger)
        if clean_traceability_counts != traceability_counts:
            raise RuntimeError("clean and source traceability status counts differ")
        for label, argv, timeout in (
            ("clean-unit", [python, "-B", "-m", "unittest", "discover", "-s", ".agents/infra/tests", "-p", "test_*.py"], 180.0),
            ("clean-traceability-meta", [python, "-B", "-m", "unittest", "discover", "-s", ".agents/infra/law_tests", "-p", "test_meta.py"], 900.0),
            ("clean-built-in-laws", [python, "-B", ".agents/scripts/selftest.py"], 120.0),
        ):
            record, _ = execute(label, argv, extracted, timeout=timeout)
            commands.append(record)
        clean_issues = audit(extracted)
        if clean_issues:
            raise RuntimeError(f"clean audit failed: {clean_issues}")
        generated = sorted(
            path.relative_to(extracted).as_posix()
            for path in extracted.rglob("*")
            if path.name == "__pycache__" or path.suffix in {".pyc", ".pyo"}
        )
        if generated:
            raise RuntimeError(f"clean verification generated forbidden bytecode: {generated}")
        clean_summary = {
            "archive_sha256": first["sha256"],
            "archive_members": first["members"],
            "extracted_members": len(members),
            "manifest": clean_manifest_detail,
        }

    after = immutable_snapshot(root)
    if before != after:
        raise RuntimeError("verification mutated immutable source or release files")
    generated_source = sorted(
        path.relative_to(root).as_posix()
        for path in root.rglob("*")
        if ".git" not in path.parts and (path.name == "__pycache__" or path.suffix in {".pyc", ".pyo"})
    )
    if generated_source:
        raise RuntimeError(f"source verification generated forbidden bytecode: {generated_source}")
    print(
        json.dumps(
            {
                "ok": True,
                "immutable_snapshot": after,
                "traceability_statuses": traceability_counts,
                "source_manifest": manifest_detail,
                "clean_room": clean_summary,
                "commands": commands,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
