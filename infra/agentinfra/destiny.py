"""Bounded Destiny context, conservative verification plans, and observations.

Source markers, command exit codes and cached reports are not formal proofs.
The formal cycle binds exact verifier observations to declared obligations.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import fnmatch
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import sys
import tarfile
import time
import tomllib
import uuid

from .atomic import atomic_write_json
from .context_cache import ContextLedger, sha256_file
from .destiny_reuse import digest, load_json
from .evidence import proof_output
from .locks import FileLock
from .process import run_process
from .security import confined_path, minimal_subprocess_env, redact_text


PROFILE = Path(__file__).resolve().parents[2] / "modules/destiny/profile.toml"
CONTROL = ".aegis/destiny"


def relative_path(value):
    value = value.replace("\\", "/")
    parts = PurePosixPath(value).parts
    if not parts or value.startswith("/") or re.match(r"^[A-Za-z]:", value) or ".." in parts or "\x00" in value:
        raise ValueError(f"not a confined project path: {value!r}")
    if parts[0].casefold() in {".git", ".aegis"}:
        raise ValueError("Git metadata and runtime state are not source inputs")
    return PurePosixPath(value).as_posix()


def git(root, *args):
    result = run_process(["git", "-C", str(root), *args], cwd=root, timeout=30, capture_limit=2_000_000,
                         env={"GIT_OPTIONAL_LOCKS": "0", "GIT_TERMINAL_PROMPT": "0"})
    if result.returncode or result.timed_out or result.stdout_truncated:
        raise RuntimeError(f"Git discovery failed: {result.stderr[-1000:]}")
    return result.stdout


def load_profile():
    profile = tomllib.loads(PROFILE.read_text(encoding="utf-8"))
    if profile.get("schema") != 1:
        raise ValueError("unsupported Destiny profile schema")
    ordered_checks(profile, set(profile["checks"]))
    return profile


def validate_project(root, profile):
    manifest = confined_path(root, "Cargo.toml", must_exist=True)
    package = tomllib.loads(manifest.read_text(encoding="utf-8")).get("package", {})
    if package.get("name") != profile["project"]["name"]:
        raise ValueError("project is not the inspected Destiny Rust crate")
    confined_path(root, "verification/spec/src/catalog.rs", must_exist=True)
    # Do not accidentally fingerprint an enclosing repository or unrelated subtree.
    if Path(git(root, "rev-parse", "--show-toplevel").strip()).resolve() != root:
        raise ValueError("--project must be the Git repository root")


def ordered_checks(profile, selected):
    result, visiting, visited = [], set(), set()

    def visit(name):
        if name in visited:
            return
        if name in visiting or name not in profile["checks"]:
            raise ValueError(f"unknown or cyclic verification dependency: {name}")
        visiting.add(name)
        for dependency in profile["checks"][name].get("requires", []):
            visit(dependency)
        visiting.remove(name)
        visited.add(name)
        result.append(name)

    for name in sorted(selected):
        visit(name)
    return result


def changed_paths(root, base):
    paths = set()
    # Include staged AND unstaged edits, deletions, both rename endpoints and untracked files.
    for args in (("diff", "--name-only", "--no-renames", "-z"),
                 ("diff", "--cached", "--name-only", "--no-renames", "-z"),
                 ("ls-files", "--others", "--exclude-standard", "-z")):
        paths.update(git(root, *args).split("\0"))
    if base:
        revision = git(root, "rev-parse", "--verify", "--end-of-options", base + "^{commit}").strip()
        paths.update(git(root, "diff", "--name-only", "--no-renames", "-z", revision, "HEAD", "--").split("\0"))
    return sorted(relative_path(p) for p in paths if p and p.split("/", 1)[0] != ".aegis")


def plan(root, profile, paths, release=False):
    paths = sorted({relative_path(p) for p in paths})
    selected, unmapped = set(), []
    for path in paths:
        matches = [r for r in profile["routes"] if any(
            ("/" in p or "/" not in path) and fnmatch.fnmatchcase(path, p) for p in r["paths"])]
        if not matches:
            unmapped.append(path)
        for route in matches:
            selected.update(route["checks"])
    if release or unmapped or "*" in selected:
        selected = set(profile["checks"])
    checks = [{"id": name, "status": "NOT_RUN", **profile["checks"][name]}
              for name in ordered_checks(profile, selected)]
    return {"schema": 1, "status": "PLANNED", "project": str(root), "changed": paths,
            "unmapped": unmapped, "checks": checks, "manual_gates": profile["manual_gates"] if checks else [],
            "notice": "Selection is a triage plan, never an acceptance waiver. Use --release for the complete matrix."}


def source_snapshot(root, read_globs=()):
    # Track filenames as well as contents: additions/deletions must invalidate reuse.
    names = set(git(root, "ls-files", "--cached", "--others", "--exclude-standard", "-z").split("\0"))
    for pattern in read_globs:
        names.update(p.relative_to(root).as_posix() for p in root.glob(pattern))
    # Git-ignored build configuration can still alter verification semantics.
    cargo = confined_path(root, ".cargo")
    if cargo.is_dir():
        names.update(p.relative_to(root).as_posix() for p in cargo.rglob("*") if not p.is_dir() or p.is_symlink())
    entries = {}
    repositories = {}
    for name in sorted(names):
        if not name or name.split("/", 1)[0].casefold() in {".aegis", ".git"}:
            continue
        name = relative_path(name)
        path = confined_path(root, name)
        if path.is_dir():
            # Git collapses an embedded repository to its directory in --others.
            # Bind it separately, including dirty/untracked source and its HEAD;
            # never omit the controller or vendor inputs from the parent identity.
            if Path(git(path, "rev-parse", "--show-toplevel").strip()).resolve() != path.resolve():
                raise ValueError(f"directory input is not a separate Git repository: {name}")
            nested_globs = [p[len(name) + 1:] for p in read_globs if p.startswith(name + "/")]
            before_head = git(path, "rev-parse", "--verify", "HEAD^{commit}").strip()
            nested = source_snapshot(path, nested_globs)
            if git(path, "rev-parse", "--verify", "HEAD^{commit}").strip() != before_head:
                raise RuntimeError(f"repository HEAD changed during fingerprint: {name}")
            repositories[name] = {"commit": before_head, "source": nested}
            entries[name] = {"repository": repositories[name]}
            continue
        if not path.exists():
            entries[name] = {"missing": True}
            continue
        before = path.stat()
        if not path.is_file():
            raise ValueError(f"unsupported source input: {name}")
        sha = sha256_file(path)
        after = path.stat()
        if (before.st_size, before.st_mtime_ns, before.st_ctime_ns) != (after.st_size, after.st_mtime_ns, after.st_ctime_ns):
            raise RuntimeError(f"source changed during fingerprint: {name}")
        entries[name] = {"sha256": sha, "mode": after.st_mode & 0o777}
    result = {"digest": digest(entries), "files": len(entries)}
    if repositories:
        result["repositories"] = repositories
    return result


def state_path(root, suffix=""):
    return confined_path(root, f"{CONTROL}/{suffix}".rstrip("/"))


def context(root, profile, args):
    name = relative_path(args.path)
    path = confined_path(root, name, must_exist=True)
    if args.start < 1 or args.lines < 1 or not 1 <= args.max_bytes <= profile["economy"]["max_context_bytes"]:
        raise ValueError("context start/lines must be positive; max-bytes must be between 1 and 64000")
    confined_path(root, ".aegis/cache/context-ledger.json")
    ledger = ContextLedger(root)
    selection = f"destiny-v1:{args.start}:{args.lines}:{args.max_bytes}"
    previous = ledger.check_file(path)
    if previous.get("fresh") and previous.get("conclusion") == selection and not args.fresh:
        return {"status": "UNCHANGED", "path": name, "sha256": previous["sha256"], "text": "",
                "notice": "Reuse the prior excerpt; --fresh rereads it explicitly."}
    # Stream lines; never load a large source or log just to return a small excerpt.
    before = sha256_file(path)
    data = bytearray()
    truncated = False
    with path.open("rb") as stream:
        number = 1
        while number < args.start:
            chunk = stream.readline(64_000)
            if not chunk:
                break
            if chunk.endswith(b"\n"):
                number += 1
        while number >= args.start:
            remaining = args.max_bytes - len(data)
            # Bound memory even for a generated source with a multi-megabyte line.
            line = stream.readline(remaining + 1)
            if not line:
                break
            if number >= args.start + args.lines:
                truncated = True
                break
            data.extend(line[:remaining])
            if len(line) > remaining:
                truncated = True
                break
            if line.endswith(b"\n"):
                number += 1
    recorded = ledger.record_file(path, selection)
    if recorded["sha256"] != before:
        ledger.record_file(path, "destiny-context-invalidated-during-read")
        raise RuntimeError("context changed while reading; discard the excerpt")
    text = redact_text(bytes(data).decode("utf-8", "ignore")).encode("utf-8")
    truncated = truncated or len(text) > args.max_bytes
    return {"status": "READ", "path": name, "sha256": before, "start": args.start,
            "text": text[:args.max_bytes].decode("utf-8", "ignore"), "truncated": truncated,
            "budget_bytes": args.max_bytes}


def environment(root, allow_network):
    env = minimal_subprocess_env()
    env.pop("PYTHONHOME", None)
    env["PYTHONPATH"] = str(root / "python")
    for name in ("CARGO_HOME", "RUSTUP_HOME", "KANI_HOME", "RUSTFLAGS", "CARGO_BUILD_TARGET", "CC", "CXX", "CFLAGS", "CXXFLAGS"):
        if name in os.environ:
            env[name] = os.environ[name]
    # Preserve already installed toolchains while preventing rustup auto-install.
    for name, directory in (("CARGO_HOME", ".cargo"), ("RUSTUP_HOME", ".rustup")):
        env.setdefault(name, str(Path.home() / directory))
    # run_process isolates HOME. Kani's installed bundle must be explicit so a
    # version probe never starts an implicit download into that temporary HOME.
    env.setdefault("KANI_HOME", str(Path.home() / ".kani"))
    env.update({"RUSTUP_AUTO_INSTALL": "0", "CARGO_NET_OFFLINE": "false" if allow_network else "true",
                "CARGO_TERM_COLOR": "never", "NO_COLOR": "1", "GIT_TERMINAL_PROMPT": "0"})
    return env


def expand_commands(commands, replacements):
    return [[token.format_map(replacements) for token in argv] for argv in commands]


def matches_version(expected, output):
    """Require a complete version token, not a prefix of a different release."""
    return re.search(r"(?<![A-Za-z0-9_.])" + re.escape(expected) + r"(?![A-Za-z0-9_.-])", output) is not None


def receipt_summary(record, receipt, *, reused=False):
    status = record["status"]
    if reused:
        status = "REUSED" if status == "OBSERVED_SUCCESS" else "PREVIOUS_FAILURE"
    return {"status": status, "executed": not reused, "id": record["id"], "key": record["key"],
            "receipt": receipt, "claim": record["claim"], "returncode": record["returncode"],
            "proof_output_checked": record.get("proof_output_checked", False),
            "output_truncated": any(c["stdout_truncated"] or c["stderr_truncated"] for c in record["commands"]),
            "notice": "Observation only; this receipt does not prove parity or discharge an Aegis gate."}


def reserve_attempt(root, profile, key, seconds, reason):
    """Adapt extraction_budget.reserve: reserve durable budget before launching.

    Unlike MetaRocq extraction cycles, these independent check recipes are keyed
    by current inputs. Both success and failed/interrupted work consume attempts.
    No automatic reset, and no manual receipt is promoted into acceptance proof.
    """
    path = state_path(root, f"attempts/{key}.json")
    history = load_json(path.read_text()) if path.exists() else {"schema": 1, "key": key, "attempts": []}
    if history.get("schema") != 1 or history.get("key") != key or not isinstance(history.get("attempts"), list):
        raise ValueError("invalid attempt ledger")
    attempts = history["attempts"]
    for attempt in attempts:
        if not isinstance(attempt, dict) or type(attempt.get("reserved_seconds")) is not int or attempt["reserved_seconds"] <= 0:
            raise ValueError("invalid budget reservation")
    cap = profile["economy"]["max_attempts_per_input"]
    if len(attempts) >= cap or sum(a["reserved_seconds"] for a in attempts) + seconds > cap * seconds:
        return False
    if attempts and not (reason and reason.strip()):
        raise ValueError("retry after a previous or interrupted attempt requires a recorded diagnosis via --fresh --reason")
    attempts.append({"number": len(attempts) + 1, "status": "RESERVED", "reserved_seconds": seconds,
                     "reason": reason, "reserved_at": datetime.now(timezone.utc).isoformat()})
    atomic_write_json(path, history)
    return True


def executable_identities(commands, env):
    result = {}
    for argv in commands:
        found = shutil.which(argv[0], path=env.get("PATH"))
        if found is None:
            raise ValueError(f"executable disappeared: {argv[0]}")
        path = Path(found).resolve(strict=True)
        result[argv[0]] = {"path": str(path), "sha256": sha256_file(path)}
    return result


def registry_source_files(root, manifest, env):
    """Bind actual Cargo registry source consumed by a standalone proof crate.

    Lockfile identities alone do not detect local changes to a cached math or
    procedural-macro implementation. Missing/ambiguous registry trees fail before
    a proof; package checksums identify the requested release, and every current
    extracted file is hashed as part of the payload (including build scripts).
    """
    manifest = confined_path(root, manifest, must_exist=True)
    lock = manifest.parent / "Cargo.lock"
    if not lock.is_file():
        raise ValueError("UNAVAILABLE: selected proof manifest requires its Cargo.lock")
    packages = tomllib.loads(lock.read_text()).get("package", [])
    home = Path(env["CARGO_HOME"]).resolve(strict=True)
    paths = {lock}
    paths.update(p for p in (home / "config", home / "config.toml") if p.is_file())
    for package in packages:
        source = package.get("source")
        if source is None:  # path crates are separately bound by source_snapshot
            continue
        if source != "registry+https://github.com/rust-lang/crates.io-index":
            raise ValueError("UNAVAILABLE: proof registry/git source needs a separately reviewed resolver")
        name = package["name"] + "-" + package["version"]
        candidates = [p for p in (home / "registry/src").glob("*/" + name) if p.is_dir()]
        if len(candidates) != 1:
            raise ValueError("UNAVAILABLE: missing or ambiguous proof registry source: " + name)
        directory = candidates[0]
        # Recent Cargo releases no longer create .cargo-checksum.json. Bind the
        # locked archive instead and check its actual extracted source bytes.
        archives = [p for p in (home / "registry/cache").glob("*/" + name + ".crate") if p.is_file()]
        if len(archives) != 1 or sha256_file(archives[0]) != package.get("checksum"):
            raise ValueError("UNAVAILABLE: proof registry release checksum differs: " + name)
        paths.add(archives[0])
        with tarfile.open(archives[0], "r:gz") as archive:
            for member in archive:
                if member.isdir():
                    continue
                parts = PurePosixPath(member.name).parts
                if not member.isfile() or not parts or parts[0] != name or ".." in parts:
                    raise ValueError("UNAVAILABLE: invalid locked proof registry archive")
                extracted = directory.joinpath(*parts[1:])
                if not extracted.is_file() or not extracted.resolve().is_relative_to(directory.resolve()):
                    raise ValueError("UNAVAILABLE: incomplete proof registry extraction: " + name)
                data = archive.extractfile(member).read()
                if digest(data) != sha256_file(extracted):
                    raise ValueError("UNAVAILABLE: proof registry source differs from locked archive: " + name)
        paths.update(p for p in directory.rglob("*") if p.is_file())
    return paths


def tool_payload(root, profile, check, commands, env):
    """Bind compiler/solver payloads behind launchers, including Kani's stdlib.

    Hash real files each time. A rustup shim or a version string alone cannot
    detect replacement of the compiler, embedded SAT solver or proof libraries.
    """
    paths = set()
    toolchains = []
    if check == "kani":
        for argv in commands:
            if "--manifest-path" in argv:
                paths.update(registry_source_files(root, argv[argv.index("--manifest-path") + 1], env))
        bundle = Path(env["KANI_HOME"]) / ("kani-" + profile["project"]["kani"])
        if not bundle.is_dir():
            raise ValueError("UNAVAILABLE: installed pinned Kani bundle is missing")
        for name in ("rust-toolchain-version", "rustc-version"):
            paths.add(bundle / name)
        for name in ("cbmc", "goto-analyzer", "goto-cc", "goto-instrument", "kani-compiler", "kani-driver", "kissat"):
            paths.add(bundle / "bin" / name)
        paths.update(p for p in (bundle / "lib").rglob("*") if p.is_file())
        toolchain = (bundle / "toolchain").resolve(strict=True)
        if toolchain.name != (bundle / "rust-toolchain-version").read_text().strip():
            raise ValueError("UNAVAILABLE: Kani compiler toolchain differs from bundle pin")
        toolchains.append(toolchain)
    if any(Path(argv[0]).name in {"cargo", "rustc"} for argv in commands):
        result = run_process(["rustup", "which", "--toolchain", profile["project"]["rust"], "rustc"],
                             cwd=root, env=env, timeout=10, capture_limit=4000)
        if result.returncode or result.timed_out or result.stdout_truncated:
            raise ValueError("UNAVAILABLE: pinned Rust compiler path cannot be resolved")
        toolchains.append(Path(result.stdout.strip()).resolve(strict=True).parents[1])
    for toolchain in toolchains:
        paths.update(toolchain / "bin" / name for name in ("rustc", "cargo"))
        paths.update(p for p in (toolchain / "lib").glob("*") if p.is_file())
        paths.update((toolchain / "lib" / "rustlib").rglob("*.rlib"))
    if check == "verus":
        executable = Path(shutil.which(commands[0][0], path=env.get("PATH"))).resolve(strict=True)
        directory = executable.parent
        for name in ("z3", "rust_verify", "version.json", "vstd.vir"):
            if (directory / name).is_file():
                paths.add(directory / name)
        paths.update(directory.glob("*.rlib"))
        paths.update(directory.glob("*.so"))
    return {str(p.resolve(strict=True)): sha256_file(p) for p in sorted(paths)}


def scoped_verus_commands(commands, entry, replacements):
    """Select one registered configuration without dropping verifier flags."""
    selected = [command for command in commands if command[-1] == entry]
    if len(selected) != 1:
        raise ValueError("scoped Verus requires one unique registered command")
    return expand_commands(selected, replacements)


def scoped_kani_commands(commands, manifest, harness):
    """Retain reviewed features/contract flags while selecting one exact proof."""
    if len(commands) != 1 or commands[0][:2] != ["cargo", "kani"]:
        raise ValueError("scoped Kani requires one registered cargo kani configuration")
    command = commands[0]
    retained = command[:2]
    index = 2
    while index < len(command):
        argument = command[index]
        if argument in {"--manifest-path", "--output-format"}:
            if index + 1 >= len(command):
                raise ValueError("incomplete registered Kani option")
            index += 2
        elif argument.startswith(("--manifest-path=", "--output-format=")):
            index += 1
        elif argument in {"--harness", "--exact", "--force-build"} or argument.startswith("--harness="):
            raise ValueError("registered Kani command must not preselect a harness")
        else:
            retained.append(argument)
            index += 1
    return [retained + ["--manifest-path", manifest, "--harness", harness,
                        "--exact", "--force-build", "--output-format", "regular"]]


def run_check(root, profile, args):
    if args.check not in profile["checks"]:
        raise ValueError(f"unknown verification check: {args.check}")
    if args.fresh and not (args.reason and args.reason.strip()):
        raise ValueError("--fresh requires --reason so repeated work is deliberate")
    if not math.isfinite(args.budget_seconds) or args.budget_seconds <= 0:
        raise ValueError("budget-seconds must be finite and positive")
    spec = dict(profile["checks"][args.check])
    proof_inputs = getattr(args, "proof_input", None) or []
    for name in proof_inputs:
        if relative_path(name) != name or not confined_path(root, name, must_exist=True).is_file():
            raise ValueError("canonical proof source files required")
    spec["read_globs"] = list(spec.get("read_globs", [])) + proof_inputs
    if args.harness or args.entry:
        spec["timeout"] = spec.get("scoped_timeout", spec["timeout"])
    replacements = {"python": sys.executable, "project": str(root), "verus": args.verus,
                    "library": args.library or "", "original": args.original or ""}
    external = {}
    for name in spec.get("inputs", []):
        value = replacements[name]
        if not value or not Path(value).exists() or (name == "library" and not Path(value).is_file()):
            return {"status": "UNAVAILABLE", "id": args.check, "executed": False,
                    "reason": f"explicit --{name} input is required; a skipped gate is not success"}
        replacements[name] = str(Path(value).resolve())
        if name == "original":
            if git(Path(value), "rev-parse", "HEAD").strip() != profile["project"]["original_test_commit"]:
                raise ValueError("original reference revision differs from the inspected CI pin")
            if git(Path(value), "status", "--porcelain", "--untracked-files=all").strip():
                raise ValueError("original reference must be clean and read-only during verification")
        external[name] = sha256_file(Path(value)) if name == "library" else source_snapshot(Path(value).resolve())
    if args.budget_seconds < spec["timeout"]:
        return {"status": "BUDGET_EXCEEDED", "id": args.check, "executed": False,
                "reason": f"recipe reserves {spec['timeout']} seconds; increase the explicit budget or select a smaller check"}
    env = environment(root, args.allow_network)
    if args.library:
        env["DESTINY_BEVY_COMPAT_LIBRARY"] = replacements["library"]
    commands = expand_commands(spec["commands"], replacements)
    probes = expand_commands(spec.get("probes", []), replacements)
    obligation = None
    if args.harness:
        if args.check != "kani" or not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*(?:::[A-Za-z_][A-Za-z0-9_]*)*", args.harness):
            raise ValueError("--harness requires a canonical exact Kani harness name")
        manifest = getattr(args, "manifest", None) or "verification/kani/Cargo.toml"
        if relative_path(manifest) != manifest or Path(manifest).name != "Cargo.toml":
            raise ValueError("canonical Cargo.toml manifest required")
        commands = scoped_kani_commands(commands, manifest, args.harness)
        obligation = {"method": "kani", "entry": args.harness, "expected_checks": 1, "manifest": manifest}
    if args.entry or args.expected_checks is not None:
        permitted = {command[-1] for command in spec["commands"]} if args.check == "verus" else set()
        if args.entry not in permitted or type(args.expected_checks) is not int or args.expected_checks < 1:
            raise ValueError("scoped Verus requires a profile entry and positive --expected-checks")
        # Preserve the registered target's flags (including feature/model and
        # diagnostic controls). Rebuilding a generic command silently drops
        # the reviewed configuration and its generated-symbol inventory.
        commands = scoped_verus_commands(spec["commands"], args.entry, replacements)
        obligation = {"method": "verus", "entry": args.entry, "expected_checks": args.expected_checks}
    if args.check in {"kani", "verus"} and not obligation and not getattr(args, "full_suite", False):
        return {"status": "SCOPE_REQUIRED", "executed": False,
                "reason": "Select one --harness or counted --entry. A broad verifier run requires explicit --full-suite."}
    identity_commands = commands + probes
    if args.check == "kani":
        identity_commands += [["cargo-kani"], ["rustc"]]
    for argv in identity_commands:
        if shutil.which(argv[0], path=env.get("PATH")) is None:
            return {"status": "UNAVAILABLE", "id": args.check, "executed": False,
                    "reason": f"required executable is missing: {argv[0]}"}
    lock = FileLock(state_path(root, "run.lock"), "destiny-sequential-verification")
    lock.acquire(timeout=0)
    try:
        before = source_snapshot(root, spec.get("read_globs", []))
        tools_before = executable_identities(identity_commands, env)
        payload_before = tool_payload(root, profile, args.check, commands, env)
        identity = {"schema": 1, "project": str(root), "source": before, "external": external,
                    "external_paths": {name: replacements[name] for name in external},
                    "proof_inputs": {name: sha256_file(confined_path(root, name, must_exist=True)) for name in proof_inputs},
                    "read_globs": spec["read_globs"], "pinned_versions": spec.get("expect", []),
                    "tool_payload": payload_before,
                    "profile": sha256_file(PROFILE), "runner": sha256_file(Path(__file__)),
                    "python": {"version": sys.version, "executable": sha256_file(Path(sys.executable))},
                    "environment": digest(env), "allow_network": bool(args.allow_network),
                    "commands": commands, "tools": tools_before, "obligation": obligation,
                    "helpers": digest({p.name: sha256_file(p) for p in sorted(Path(__file__).parent.glob("*.py"))})}
        key = digest(identity)
        index_path = state_path(root, f"cache/{key}.json")
        cacheable = spec.get("cacheable", False)
        if cacheable and index_path.exists() and not args.fresh:
            index = load_json(index_path.read_text())
            receipt_path = confined_path(root, index["receipt"], must_exist=True)
            if receipt_path.parent != state_path(root, "receipts"):
                raise ValueError("cache receipt is outside the receipt directory")
            record = load_json(receipt_path.read_text())
            seal = record.pop("sha256")
            if digest(record) != seal or index["sha256"] != seal or record["key"] != key or record["id"] != args.check:
                raise ValueError("cached observation integrity failure")
            return receipt_summary(record, index["receipt"], reused=True)
        if not reserve_attempt(root, profile, key, spec["timeout"], args.reason):
            return {"status": "BUDGET_EXCEEDED", "id": args.check, "executed": False,
                    "reason": "attempt budget exhausted for these inputs; preserve the diagnosis and change the inputs before new work"}
        start = time.monotonic()
        observations = []
        for index, argv in enumerate(probes):
            remaining = spec["timeout"] - (time.monotonic() - start)
            if remaining <= 0:
                return {"status": "TIMEOUT", "id": args.check, "executed": False, "reason": "tool probes exhausted the reserved time"}
            result = run_process(argv, cwd=root, env=env, timeout=min(20, remaining), capture_limit=4000)
            observations.append({"argv": argv, "returncode": result.returncode, "stdout": result.stdout, "stderr": result.stderr})
            expected = spec.get("expect", [])[index]
            if result.returncode or result.timed_out or result.stdout_truncated or result.stderr_truncated or not matches_version(expected, result.stdout + result.stderr):
                return {"status": "UNAVAILABLE", "id": args.check, "executed": False,
                        "reason": "pinned tool version unavailable", "probes": observations}
        outputs, returncode, status = [], 0, "OBSERVED_SUCCESS"
        run_id = uuid.uuid4().hex
        verus_inventory = None
        for argv in commands:
            remaining = spec["timeout"] - (time.monotonic() - start)
            if remaining <= 0:
                status, returncode = "TIMEOUT", 124
                break
            if obligation and obligation["method"] == "verus":
                from .verus_evidence import prepare_log
                prepare_log(root, argv)
            result = run_process(argv, cwd=root, env=env, timeout=remaining,
                                 capture_limit=profile["economy"]["output_bytes"])
            outputs.append({"argv": argv, "returncode": result.returncode, "stdout": result.stdout,
                            "stderr": result.stderr, "stdout_sha256": result.stdout_sha256,
                            "stderr_sha256": result.stderr_sha256, "stdout_bytes": result.stdout_bytes,
                            "stderr_bytes": result.stderr_bytes, "stdout_truncated": result.stdout_truncated,
                            "stderr_truncated": result.stderr_truncated, "timed_out": result.timed_out})
            if obligation and obligation["method"] == "verus":
                from .verus_evidence import capture
                try:
                    verus_inventory = capture(root, argv, run_id)
                except (ValueError, OSError) as error:
                    status, returncode = "INCOMPLETE_EVIDENCE", 1
                    outputs[-1]["inventory_error"] = str(error)
                    break
            if result.timed_out or result.returncode:
                status = "TIMEOUT" if result.timed_out else "FAILED"
                returncode = result.returncode or 124
                break
            if obligation and not proof_output(obligation, result):
                status, returncode = "FAILED", 1
                break
        after = source_snapshot(root, spec.get("read_globs", []))
        external_after = {name: sha256_file(Path(replacements[name])) if name == "library" else source_snapshot(Path(replacements[name]))
                          for name in external}
        if (before != after or external != external_after or executable_identities(identity_commands, env) != tools_before
                or tool_payload(root, profile, args.check, commands, env) != payload_before):
            status, returncode = "INPUTS_CHANGED", 1
        record = {"schema": 1, "id": args.check, "key": key, "identity": identity,
                  "claim": spec["claim"], "status": status, "returncode": returncode, "probes": observations,
                  "proof_output_checked": bool(obligation and status == "OBSERVED_SUCCESS"),
                  "commands": outputs, "reason": args.reason, "source_after": after,
                  "created_at": datetime.now(timezone.utc).isoformat(), "duration_seconds": time.monotonic() - start}
        if obligation and obligation["method"] == "verus":
            record["verus_inventory"] = verus_inventory
        record["sha256"] = digest(record)
        receipt = f"{CONTROL}/receipts/{run_id}.json"
        atomic_write_json(confined_path(root, receipt), record)
        if cacheable and status in {"OBSERVED_SUCCESS", "FAILED"}:
            atomic_write_json(index_path, {"receipt": receipt, "sha256": record["sha256"]})
        return receipt_summary(record, receipt)
    finally:
        lock.release()


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, required=True)
    sub = parser.add_subparsers(dest="action", required=True)
    p = sub.add_parser("plan", help="select and deduplicate checks; never executes them")
    p.add_argument("--changed", action="append")
    p.add_argument("--base", help="include committed changes since this locally available Git ref")
    p.add_argument("--release", action="store_true")
    p = sub.add_parser("context", help="return a bounded source excerpt or an unchanged receipt")
    p.add_argument("path")
    p.add_argument("--start", type=int, default=1)
    p.add_argument("--lines", type=int, default=100)
    p.add_argument("--max-bytes", type=int, default=12000)
    p.add_argument("--fresh", action="store_true")
    p = sub.add_parser("run", help="execute ONE named recipe; follow plan order for prerequisites")
    p.add_argument("check")
    p.add_argument("--budget-seconds", type=float, default=900)
    p.add_argument("--fresh", action="store_true")
    p.add_argument("--reason")
    p.add_argument("--library")
    p.add_argument("--original")
    p.add_argument("--verus", default=os.environ.get("VERUS_BIN", "verus"))
    p.add_argument("--allow-network", action="store_true")
    p.add_argument("--harness", help="one exact Kani harness, checked with the existing Aegis output validator")
    p.add_argument("--manifest", default="verification/kani/Cargo.toml", help="manifest containing the exact Kani harness")
    p.add_argument("--proof-input", action="append", help="bind an explicit harness source digest, including ignored files")
    p.add_argument("--entry", help="one Verus entry from the reviewed profile")
    p.add_argument("--expected-checks", type=int, help="positive Verus obligation count for --entry")
    p.add_argument("--full-suite", action="store_true", help="explicitly authorize a broad verifier sweep")
    p = sub.add_parser("catalog", help="bounded original-case search; preserves duplicate fixture obligations")
    p.add_argument("--query", default="")
    p.add_argument("--unmarked", action="store_true")
    p.add_argument("--limit", type=int, default=8)
    p.add_argument("--offset", type=int, default=0)
    p.add_argument("--original", type=Path)
    p = sub.add_parser("queue", help="write all fixture-qualified obligations and distinct assurance levels to JSON")
    p.add_argument("--original", type=Path)
    p.add_argument("--output", help="path within the target checkout; defaults to .aegis/destiny/work-queue.json")
    p.add_argument("--differential", help="reviewed mapping of original cases to current runtime receipts")
    p = sub.add_parser("harness", help="automatically extract one fixture and its case from pinned original source")
    p.add_argument("--case", required=True)
    p.add_argument("--original", type=Path, help="local Git repository containing the catalog revision; defaults to the target")
    p.add_argument("--max-bytes", type=int, default=12000)
    p.add_argument("--fresh", action="store_true")
    p.add_argument("--reason")
    p = sub.add_parser("harness-close", help="record a result/blocker before opening another work item")
    p.add_argument("--outcome", choices=("implemented", "reuse", "blocked"), required=True)
    p.add_argument("--note", required=True)
    p = sub.add_parser("bind", help="bind a complete formal contract to the current source")
    p.add_argument("contract")
    p = sub.add_parser("verify", help="freshly verify one declared obligation in the active binding")
    p.add_argument("obligation")
    p.add_argument("--budget-seconds", type=float, default=900)
    p.add_argument("--reason", help="diagnosis required before repeating an attempted obligation")
    p.add_argument("--verus", default=os.environ.get("VERUS_BIN", "verus"))
    p.add_argument("--allow-network", action="store_true")
    sub.add_parser("audit", help="audit declared proof observations against current source and tools")
    args = parser.parse_args(argv)
    try:
        root = args.project.resolve(strict=True)
        profile = load_profile()
        validate_project(root, profile)
        if args.action == "plan":
            paths = args.changed if args.changed is not None else changed_paths(root, args.base)
            result = plan(root, profile, paths, args.release)
        elif args.action == "context":
            result = context(root, profile, args)
        elif args.action in {"catalog", "queue", "harness", "harness-close"}:
            from . import catalog
            if args.action == "catalog":
                result = catalog.search(root, args)
            elif args.action == "queue":
                result = catalog.work_queue(root, profile, args)
            elif args.action == "harness":
                result = catalog.brief(root, profile, args)
            else:
                result = catalog.close(root, args)
        elif args.action in {"bind", "verify", "audit"}:
            from . import formal
            if args.action == "bind":
                result = formal.bind(root, profile, args.contract)
            elif args.action == "verify":
                result = formal.verify(root, profile, args)
            else:
                result = formal.audit(root, profile)
        else:
            result = run_check(root, profile, args)
    except (OSError, ValueError, RuntimeError, KeyError, TypeError) as exc:
        result = {"status": "ERROR", "executed": False, "reason": redact_text(str(exc))}
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] in {"PLANNED", "READ", "UNCHANGED", "OBSERVED_SUCCESS", "REUSED", "BOUND", "CHECKED_SCOPED",
                                   "CATALOG", "WORK_QUEUE", "HARNESS_BRIEF", "REUSED_PACKET", "WORK_RECORDED", "WORK_ALREADY_RECORDED"} else 1
