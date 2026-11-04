"""Pinned ESBMC provisioning and actual unchanged-source ingestion controls."""
from __future__ import annotations

from dataclasses import asdict
import os
from pathlib import Path, PurePosixPath
import shutil
import stat
import sys
import time
import venv
import zipfile

from agentinfra.atomic import atomic_write_json
from agentinfra.process import run_recipe_stage
from agentinfra.roadmap_mirrors import download_with_mirrors, read_download_policy, TRANSPORT
from agentinfra.roadmap_python import classify_esbmc, esbmc_arguments, esbmc_link_state, source_closure
from agentinfra.roadmap_records import bindings_current, digest, file_binding, read_json, require
from agentinfra.security import confined_path, minimal_subprocess_env


def extract_release(root: Path, archive: Path, destination: Path) -> None:
    """Publish one confined archive generation; preserve interrupted extraction."""
    destination = confined_path(root, destination)
    marker = destination / "aegis-release-identity.json"
    archive_binding = file_binding(root, archive.relative_to(root).as_posix())
    if destination.exists():
        require(marker.is_file(), "existing ESBMC release needs extraction recovery")
        saved = read_json(marker)
        require(saved.get("archive") == archive_binding and bindings_current(root, saved.get("files", [])), "installed release changed")
        state = esbmc_link_state(root, {"release_root": destination.relative_to(root).as_posix(), "symlinks": saved.get("symlinks", [])})
        require(all(x["safe"] and x["observed"] == x["expected"] for x in state), "installed release symlinks changed")
        return
    staging = destination.with_name(destination.name + ".staging")
    require(not staging.exists(), "interrupted ESBMC extraction requires reconciliation")
    links = []
    with zipfile.ZipFile(archive) as bundle:
        entries = bundle.infolist()
        require(0 < len(entries) <= 50000 and sum(x.file_size for x in entries) <= 3_000_000_000, "unbounded ESBMC archive")
        names = [x.filename.rstrip("/") for x in entries]
        require(len(names) == len(set(names)) and "aegis-release-identity.json" not in names, "duplicate/reserved archive destination")
        for entry in entries:
            name = entry.filename.rstrip("/")
            path = PurePosixPath(name)
            require(name and not path.is_absolute() and ".." not in path.parts and "\\" not in name and str(path) == name,
                    "archive path is not confined/canonical")
            mode = entry.external_attr >> 16
            require(stat.S_IFMT(mode) in {0, stat.S_IFREG, stat.S_IFDIR, stat.S_IFLNK}, "archive contains a special device")
        staging.mkdir(parents=True)
        for entry in entries:
            target = confined_path(root, staging / entry.filename.rstrip("/"))
            mode = entry.external_attr >> 16
            if stat.S_ISLNK(mode):
                link = bundle.read(entry).decode("utf-8")
                require(link and not Path(link).is_absolute() and "\\" not in link and "\x00" not in link,
                        "unsafe release symlink")
                resolved = (target.parent / link).resolve()
                require(resolved.is_relative_to(staging.resolve()), "release symlink escapes its archive")
                links.append((target, link))
            elif entry.is_dir():
                target.mkdir(parents=True, exist_ok=True)
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                require(not target.exists(), "archive file destination already exists")
                with bundle.open(entry) as source, target.open("xb") as output:
                    shutil.copyfileobj(source, output, 262144)
                target.chmod((mode & 0o777) or 0o644)
    for target, link in links:
        require(not target.exists() and not target.is_symlink(), "symlink collides with extracted data")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.symlink_to(link)
    for target, _ in links:
        require(target.resolve().is_relative_to(staging.resolve()) and target.exists(), "release symlink is dangling/escaping/cyclic")
    staging.rename(destination)
    files = [file_binding(root, p.relative_to(root).as_posix()) for p in destination.rglob("*") if p.is_file() and not p.is_symlink()]
    symlinks = [{"path": (destination / p.relative_to(staging)).relative_to(root).as_posix(), "target": link} for p, link in links]
    atomic_write_json(marker, {"schema": 1, "archive": archive_binding, "files": sorted(files, key=lambda b: b["path"]),
                               "symlinks": symlinks}, root=root, mode=0o600)


def provision_esbmc(root: Path, output: Path) -> dict:
    profile = "Roadmaps/Shared/python-esbmc-toolchains.json"
    lock = read_json(root / profile)
    require(lock.get("backend") == "esbmc-python" and lock.get("download_transport") == TRANSPORT and
            sys.platform == "linux" and os.uname().machine == "x86_64" and sys.version_info[:2] == (3, 14), "unqualified ESBMC profile/platform")
    directory = confined_path(root, ".aegis/toolchains/esbmc/" + digest(lock))
    directory.mkdir(parents=True, exist_ok=True)
    deadline = time.monotonic() + read_download_policy(root)["stage_timeout_seconds"]
    wheels = [download_with_mirrors(root, p, directory / "downloads", deadline) for p in lock["packages"]]
    archive = download_with_mirrors(root, lock["archive"], directory / "downloads", deadline)
    release = directory / "release"
    extract_release(root, archive, release)
    executables = [p for p in release.rglob("esbmc") if p.is_file() and os.access(p, os.X_OK)]
    require(len(executables) == 1, "release executable is missing or ambiguous")
    virtual = directory / "venv"
    if not (virtual / "bin/python").exists():
        venv.EnvBuilder(with_pip=True).create(virtual)
    python = virtual / "bin/python"
    environment = dict(minimal_subprocess_env(), PYTHONDONTWRITEBYTECODE="1")
    artifacts = []
    for name, argv in (("pip-result.json", [str(python), "-B", "-m", "pip", "install", "--no-index", "--no-deps", *map(str, wheels)]),
                       ("pip-check.json", [str(python), "-B", "-m", "pip", "check"]),
                       ("esbmc-version.json", [str(executables[0]), "--version"])):
        result = run_recipe_stage(argv, cwd=root, timeout=180, env=environment, capture_limit=1_000_000)
        path = output.parent / name
        atomic_write_json(path, asdict(result), root=root, mode=0o600)
        artifacts.append(file_binding(root, path.relative_to(root).as_posix()))
        require(result.returncode == 0 and not result.timed_out and not result.stdout_truncated and not result.stderr_truncated,
                "ESBMC installation/dependency/version query failed")
    files = [file_binding(root, p.relative_to(root).as_posix()) for p in directory.rglob("*") if p.is_file() and not p.is_symlink() and "__pycache__" not in p.parts]
    identity = read_json(release / "aegis-release-identity.json")
    return {"backend": "esbmc-python", "status": "INSTALLED_NOT_QUALIFIED", "lock": file_binding(root, profile),
            "python": str(python), "executable": str(executables[0]), "environment": environment,
            "files": sorted(files, key=lambda b: b["path"]), "artifacts": artifacts,
            "release_root": release.relative_to(root).as_posix(), "symlinks": identity["symlinks"]}


def qualify_esbmc(root: Path, output: Path, toolchain_path: str) -> dict:
    binding = file_binding(root, toolchain_path)
    toolchain = read_json(confined_path(root, toolchain_path, must_exist=True))
    require(toolchain.get("backend") == "esbmc-python" and toolchain.get("status") == "INSTALLED_NOT_QUALIFIED" and
            bindings_current(root, [toolchain["lock"], *toolchain["files"]]), "ESBMC installation changed")
    require(all(x["safe"] and x["observed"] == x["expected"] for x in esbmc_link_state(root, toolchain)), "ESBMC symlink identity changed")
    runs, artifacts = [], []
    for name in ("policy_deal_positive.py", "policy_deal_negative.py"):
        fixture = file_binding(root, "verification/roadmap/python/" + name)
        environment = dict(toolchain["environment"], PYTHONPATH=str(root / "infra"))
        result = run_recipe_stage(esbmc_arguments(root, toolchain, fixture["path"]), cwd=root, timeout=180,
                                  env=environment, capture_limit=1_000_000)
        path = output.parent / ("esbmc-" + name + ".result.json")
        atomic_write_json(path, asdict(result), root=root, mode=0o600)
        result_binding = file_binding(root, path.relative_to(root).as_posix())
        artifacts.extend([fixture, result_binding])
        classification = classify_esbmc(asdict(result))
        claims_binding = None
        if classification["outcome"] in {"TOOL_VERDICT_PROPERTIES_UNQUALIFIED", "FAILURE_PROPERTY_UNREVIEWED"}:
            claims = run_recipe_stage(esbmc_arguments(root, toolchain, fixture["path"], claims=True), cwd=root, timeout=180,
                                      env=environment, capture_limit=1_000_000)
            claims_path = output.parent / ("esbmc-" + name + ".claims.json")
            atomic_write_json(claims_path, asdict(claims), root=root, mode=0o600)
            claims_binding = file_binding(root, claims_path.relative_to(root).as_posix())
            artifacts.append(claims_binding)
        runs.append({"fixture": fixture, "intent": "positive" if name == "policy_deal_positive.py" else "deliberately_wrong_assertion",
                     "result": result_binding, "claims": claims_binding, "classification": classification,
                     "assertion_reachability": "NOT_ESTABLISHED"})
    return {"backend": "esbmc-python", "status": "INGESTION_TRIAL_UNQUALIFIED", "toolchain": binding, "runs": runs,
            "production": source_closure(root, "agentinfra.roadmap_policy:may_reserve"),
            "original": file_binding(root, "infra/tests/test_roadmap.py"), "artifacts": artifacts,
            "qualification_limit": "Exact property/source identities, reachability, imports/state, model coverage and full Python integer/bool semantics remain unqualified. --ir requests integer/real solver encoding but does not prove frontend/operational-model fidelity. No explicit unwind/input bound or assertion-disabling option is used; release defaults and unsupported/model gaps cannot be full-domain proof."}
