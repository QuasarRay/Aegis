"""Fixed A09 source routing, isolated tool provisioning and ingestion controls."""
from __future__ import annotations

import argparse
from dataclasses import asdict
import json
import os
from pathlib import Path
import sys
import tarfile
import urllib.request
import venv

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "infra"))

from agentinfra.atomic import atomic_write_json
from agentinfra.process import run_recipe_stage
from agentinfra.roadmap import compile_roadmaps
from agentinfra.roadmap_python import classify_nagini, route, source_closure
from agentinfra.roadmap_records import digest, file_binding, read_json, require
from agentinfra.security import confined_path, minimal_subprocess_env


def _download(root: Path, entry: dict, directory: Path) -> Path:
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / entry.get("filename", entry.get("name", "archive"))
    require(path.parent == directory and path.suffix in {".whl", ".gz"}, "tool archive filename escapes the fixed download directory")
    if not path.exists():
        partial = path.with_suffix(path.suffix + ".partial")
        try:
            request = urllib.request.Request(entry["url"], headers={"User-Agent": "Aegis-A09-pinned-toolchain"})
            with urllib.request.urlopen(request, timeout=45) as response, partial.open("wb") as output:
                copied = 0
                while chunk := response.read(262144):
                    copied += len(chunk)
                    require(copied <= entry["size"], "download exceeds pinned size")
                    output.write(chunk)
            require(partial.stat().st_size == entry["size"] and digest(partial.read_bytes()) == entry["sha256"], "download hash/size differs from reviewed pin")
            partial.replace(path)
        finally:
            partial.unlink(missing_ok=True)
    require(path.stat().st_size == entry["size"] and digest(path.read_bytes()) == entry["sha256"], "cached toolchain archive changed")
    return path


def provision(root: Path, output: Path) -> dict:
    lock = read_json(root / "Roadmaps/Shared/python-toolchains.json")
    require(sys.platform == "linux" and os.uname().machine == "x86_64" and sys.version_info[:2] == (3, 14), "unqualified host platform/interpreter")
    directory = root / ".aegis/toolchains" / digest(lock)
    directory.mkdir(parents=True, exist_ok=True)
    wheels = [_download(root, package, directory / "downloads") for package in lock["packages"]]
    archive = _download(root, lock["jre"], directory / "downloads")
    java_root = directory / "java"
    if not java_root.exists():
        java_root.mkdir()
        with tarfile.open(archive) as bundle:
            # Python's data filter rejects escaping paths and unsafe link targets.
            bundle.extractall(java_root, filter="data")
    java = list(java_root.glob("*/bin/java"))
    require(len(java) == 1, "pinned JRE executable missing or ambiguous")
    environment = minimal_subprocess_env()
    environment["JAVA_HOME"] = str(java[0].parents[1])
    environment["PATH"] = str(java[0].parent) + os.pathsep + environment.get("PATH", os.defpath)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    virtual = directory / "venv"
    if not (virtual / "bin/python").exists():
        venv.EnvBuilder(with_pip=True).create(virtual)
    python = virtual / "bin/python"
    installed = run_recipe_stage([str(python), "-B", "-m", "pip", "install", "--no-index", "--no-deps", *map(str, wheels)],
                                 cwd=root, timeout=180, env=environment, capture_limit=1_000_000)
    atomic_write_json(output.parent / "pip-result.json", asdict(installed), root=root, mode=0o600)
    require(installed.returncode == 0 and not installed.timed_out, "isolated pinned wheel installation failed")
    checked = run_recipe_stage([str(python), "-B", "-m", "pip", "check"], cwd=root, timeout=30, env=environment, capture_limit=1_000_000)
    atomic_write_json(output.parent / "pip-check.json", asdict(checked), root=root, mode=0o600)
    require(checked.returncode == 0, "pinned dependency closure is incomplete")
    java_version = run_recipe_stage([str(java[0]), "-version"], cwd=root, timeout=30, env=environment, capture_limit=1_000_000)
    atomic_write_json(output.parent / "java-version.json", asdict(java_version), root=root, mode=0o600)
    require(java_version.returncode == 0, "pinned JRE cannot execute")
    files = [file_binding(root, p.relative_to(root).as_posix()) for p in directory.rglob("*") if p.is_file() and not p.is_symlink() and "__pycache__" not in p.parts]
    return {"status": "INSTALLED_NOT_QUALIFIED", "lock": file_binding(root, "Roadmaps/Shared/python-toolchains.json"),
            "python": str(python), "java": str(java[0]), "environment": environment,
            "files": sorted(files, key=lambda b: b["path"]),
            "artifacts": [file_binding(root, p.relative_to(root).as_posix()) for p in (output.parent / "pip-result.json", output.parent / "pip-check.json", output.parent / "java-version.json")]}


def qualify(root: Path, output: Path, toolchain_path: str) -> dict:
    from agentinfra.roadmap_records import bindings_current
    toolchain = read_json(confined_path(root, toolchain_path, must_exist=True))
    require(toolchain.get("status") == "INSTALLED_NOT_QUALIFIED" and bindings_current(root, toolchain["files"]) and
            bindings_current(root, [toolchain["lock"]]), "toolchain changed or was not installed by the fixed producer")
    runs = []
    for name in ("policy_positive.py", "policy_negative.py"):
        source = root / "verification/roadmap/python" / name
        environment = dict(toolchain["environment"], PYTHONPATH=str(root / "infra"))
        result = run_recipe_stage([toolchain["python"], "-B", "-m", "nagini_translation.main", str(source)],
                                  cwd=root, timeout=180, env=environment, capture_limit=1_000_000)
        path = output.parent / (name + ".result.json")
        atomic_write_json(path, asdict(result), root=root, mode=0o600)
        runs.append({"fixture": file_binding(root, source.relative_to(root).as_posix()),
                     "intent": "positive" if name == "policy_positive.py" else "deliberately_wrong_assertion",
                     "result": file_binding(root, path.relative_to(root).as_posix()), "classification": classify_nagini(asdict(result))})
    outcomes = [r["classification"]["outcome"] for r in runs]
    return {"backend": "nagini", "status": "INGESTION_CONTROLS_PASSED_REVIEW_REQUIRED" if outcomes == ["VERIFIED_TOOL_RESULT", "ASSERTION_COUNTEREXAMPLE"] else "UNSUPPORTED_OR_UNQUALIFIED",
            "production": source_closure(root, "agentinfra.roadmap_policy:may_reserve"),
            "original": file_binding(root, "infra/tests/test_roadmap.py"),
            "toolchain": file_binding(root, toolchain_path), "runs": runs,
            "artifacts": [r["fixture"] for r in runs] + [r["result"] for r in runs],
            "qualification_limit": "Original-test translation, numeric/bool semantics, import closure, exact assertion locations and reachability require review; no domain proof is promoted"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("route", "toolchain", "qualify"))
    parser.add_argument("--output", required=True)
    parser.add_argument("--candidate", required=True)
    parser.add_argument("--toolchain")
    args = parser.parse_args()
    output = confined_path(ROOT, args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    details = {"schema": 1, "candidate": args.candidate, "domain_proof": False, "action": args.action}
    try:
        if args.action == "route":
            details.update(route(ROOT, compile_roadmaps(ROOT), args.candidate))
        elif args.action == "toolchain":
            details.update(provision(ROOT, output))
        else:
            require(bool(args.toolchain), "current toolchain receipt required")
            details.update(qualify(ROOT, output, args.toolchain))
    except Exception as exc:
        details.update(status="ERROR", error={"type": type(exc).__name__, "message": str(exc)})
        atomic_write_json(output, details, root=ROOT, mode=0o600)
        raise
    atomic_write_json(output, details, root=ROOT, mode=0o600)
    print(json.dumps({"action": args.action, "status": details.get("status", "ROUTED"), "domain_proof": False}))


if __name__ == "__main__":
    main()
