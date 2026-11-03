"""Fixed A09 source routing, isolated tool provisioning and ingestion controls."""
from __future__ import annotations

import argparse
from dataclasses import asdict
import json
import os
from pathlib import Path
import sys
import tarfile
import time
import venv

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "infra"))

from agentinfra.atomic import atomic_write_json
from agentinfra.process import run_recipe_stage
from agentinfra.roadmap_mirrors import download_with_mirrors, read_download_policy, TRANSPORT
from agentinfra.roadmap import compile_roadmaps
from agentinfra.roadmap_python import classify_nagini, classify_deal, route, source_closure
from agentinfra.roadmap_records import digest, file_binding, read_json, require
from agentinfra.security import confined_path, minimal_subprocess_env


def _download(root: Path, entry: dict, directory: Path, deadline: float) -> Path:
    return download_with_mirrors(root, entry, directory, deadline)


def provision(root: Path, output: Path) -> dict:
    lock = read_json(root / "Roadmaps/Shared/python-toolchains.json")
    require(lock.get("download_transport") == TRANSPORT, "toolchain download transport differs from the reviewed profile")
    require(sys.platform == "linux" and os.uname().machine == "x86_64" and sys.version_info[:2] == (3, 14), "unqualified host platform/interpreter")
    directory = confined_path(root, ".aegis/toolchains/" + digest(lock))
    directory.mkdir(parents=True, exist_ok=True)
    deadline = time.monotonic() + read_download_policy(root)["stage_timeout_seconds"]
    wheels = [_download(root, package, directory / "downloads", deadline) for package in lock["packages"]]
    archive = _download(root, lock["jre"], directory / "downloads", deadline)
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
    nagini = virtual / "bin/nagini"
    require(nagini.is_file(), "pinned Nagini console entrypoint was not installed")
    java_version = run_recipe_stage([str(java[0]), "-version"], cwd=root, timeout=30, env=environment, capture_limit=1_000_000)
    atomic_write_json(output.parent / "java-version.json", asdict(java_version), root=root, mode=0o600)
    require(java_version.returncode == 0, "pinned JRE cannot execute")
    files = [file_binding(root, p.relative_to(root).as_posix()) for p in directory.rglob("*") if p.is_file() and not p.is_symlink() and "__pycache__" not in p.parts]
    return {"status": "INSTALLED_NOT_QUALIFIED", "lock": file_binding(root, "Roadmaps/Shared/python-toolchains.json"),
            "python": str(python), "nagini": str(nagini), "java": str(java[0]), "environment": environment,
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
        environment = dict(toolchain["environment"], PYTHONPATH=str(root / "infra"), MYPYPATH=str(root / "infra"))
        result = run_recipe_stage([toolchain["python"], "-B", toolchain["nagini"], "--mypy-path", str(root / "infra"), str(source)],
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


def provision_deal(root: Path, output: Path) -> dict:
    profile = "Roadmaps/Shared/python-deal-toolchains.json"
    lock = read_json(root / profile)
    require(lock.get("backend") == "deal" and lock.get("download_transport") == TRANSPORT and
            sys.platform == "linux" and os.uname().machine == "x86_64" and sys.version_info[:2] == (3, 14),
            "unqualified Deal download profile/platform/interpreter")
    directory = confined_path(root, ".aegis/toolchains/deal/" + digest(lock))
    directory.mkdir(parents=True, exist_ok=True)
    deadline = time.monotonic() + read_download_policy(root)["stage_timeout_seconds"]
    wheels = [_download(root, entry, directory / "downloads", deadline) for entry in lock["packages"]]
    virtual = directory / "venv"
    if not (virtual / "bin/python").exists():
        venv.EnvBuilder(with_pip=True).create(virtual)
    python = virtual / "bin/python"
    environment = dict(minimal_subprocess_env(), PYTHONDONTWRITEBYTECODE="1")
    artifacts = []
    for name, argv in (("pip-result.json", [str(python), "-B", "-m", "pip", "install", "--no-index", "--no-deps", *map(str, wheels)]),
                       ("pip-check.json", [str(python), "-B", "-m", "pip", "check"])):
        result = run_recipe_stage(argv, cwd=root, timeout=180, env=environment, capture_limit=1_000_000)
        path = output.parent / name
        atomic_write_json(path, asdict(result), root=root, mode=0o600)
        artifacts.append(file_binding(root, path.relative_to(root).as_posix()))
        require(result.returncode == 0 and not result.timed_out and not result.stdout_truncated and not result.stderr_truncated,
                "isolated Deal installation/dependency check failed")
    files = [file_binding(root, p.relative_to(root).as_posix()) for p in directory.rglob("*")
             if p.is_file() and not p.is_symlink() and "__pycache__" not in p.parts]
    return {"backend": "deal", "status": "INSTALLED_NOT_QUALIFIED", "lock": file_binding(root, profile),
            "python": str(python), "environment": environment, "files": sorted(files, key=lambda b: b["path"]), "artifacts": artifacts}


def qualify_deal(root: Path, output: Path, toolchain_path: str) -> dict:
    from agentinfra.roadmap_records import bindings_current
    binding = file_binding(root, toolchain_path)
    toolchain = read_json(confined_path(root, toolchain_path, must_exist=True))
    require(toolchain.get("backend") == "deal" and toolchain.get("status") == "INSTALLED_NOT_QUALIFIED" and
            bindings_current(root, [toolchain["lock"], *toolchain["files"]]), "Deal toolchain is missing or changed")
    runs, artifacts = [], []
    for name in ("policy_deal_positive.py", "policy_deal_negative.py"):
        fixture = file_binding(root, "verification/roadmap/python/" + name)
        observed_path = output.parent / (name + ".observation.json")
        environment = dict(toolchain["environment"], PYTHONPATH=str(root / "infra"))
        result = run_recipe_stage([toolchain["python"], "-B", "scripts/roadmap_deal.py", "--fixture", fixture["path"],
                                   "--output", observed_path.relative_to(root).as_posix()],
                                  cwd=root, timeout=180, env=environment, capture_limit=1_000_000)
        result_path = output.parent / (name + ".result.json")
        atomic_write_json(result_path, asdict(result), root=root, mode=0o600)
        observed = read_json(observed_path) if observed_path.is_file() else {"status": "MISSING_OBSERVATION"}
        dependencies = [fixture, file_binding(root, result_path.relative_to(root).as_posix())]
        if observed_path.is_file():
            dependencies.append(file_binding(root, observed_path.relative_to(root).as_posix()))
        artifacts.extend(dependencies)
        runs.append({"fixture": fixture, "intent": "positive" if name == "policy_deal_positive.py" else "deliberately_wrong_assertion",
                     "result": dependencies[1], "observation": dependencies[2] if len(dependencies) == 3 else None,
                     "classification": classify_deal(asdict(result), observed)})
    return {"backend": "deal", "status": "INGESTION_TRIAL_UNQUALIFIED", "toolchain": binding, "runs": runs,
            "production": source_closure(root, "agentinfra.roadmap_policy:may_reserve"),
            "original": file_binding(root, "infra/tests/test_roadmap.py"), "artifacts": artifacts,
            "qualification_limit": "Actual imported AST inference, module initialization/state, numeric/bool semantics, original translation, assertion identities and reachability remain unqualified. Skips, empty/partial results and model-only results grant no domain proof."}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("route", "toolchain", "qualify"))
    parser.add_argument("--output", required=True)
    parser.add_argument("--candidate", required=True)
    parser.add_argument("--toolchain")
    parser.add_argument("--backend", choices=("nagini", "deal"), default="nagini")
    args = parser.parse_args()
    output = confined_path(ROOT, args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    details = {"schema": 1, "candidate": args.candidate, "domain_proof": False, "action": args.action}
    try:
        if args.action == "route":
            details.update(route(ROOT, compile_roadmaps(ROOT), args.candidate))
        elif args.action == "toolchain":
            details.update(provision_deal(ROOT, output) if args.backend == "deal" else provision(ROOT, output))
        else:
            require(bool(args.toolchain), "current toolchain receipt required")
            details.update(qualify_deal(ROOT, output, args.toolchain) if args.backend == "deal" else qualify(ROOT, output, args.toolchain))
    except Exception as exc:
        details.update(status="ERROR", error={"type": type(exc).__name__, "message": str(exc)})
        atomic_write_json(output, details, root=ROOT, mode=0o600)
        raise
    atomic_write_json(output, details, root=ROOT, mode=0o600)
    print(json.dumps({"action": args.action, "status": details.get("status", "ROUTED"), "domain_proof": False}))


if __name__ == "__main__":
    main()
