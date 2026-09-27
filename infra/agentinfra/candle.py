"""Candle-only coordination: original contracts, bounded evidence, durable PRs.

Existing Aegis filesystem/process/locking safeguards are reused. This control
plane is not a sandbox against a process with the same filesystem credentials.
"""
from __future__ import annotations

from contextlib import contextmanager
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import subprocess
from urllib.request import Request, urlopen
import uuid

from .atomic import atomic_write_json
from .contracts import ContractError, digest, file_digest, load_authority, validate_plan
from .locks import FileLock
from .governance import _checkpoint_instruction_copies
from .paths import framework_dir
from .security import SecurityError, confined_path
from .verification import proof_manifest, run_kani, version
from .transaction import FileTransaction, Mutation, recover_named_transactions


def git(root, *arguments):
    result = subprocess.run(["git", *arguments], cwd=root, check=False, capture_output=True, timeout=30)
    if result.returncode:
        raise ContractError(result.stderr.decode(errors="replace").strip())
    return result.stdout.decode().strip()


def git_repository(root):
    remote = git(root, "remote", "get-url", "origin")
    allowed = {"https://github.com/QuasarRay/Candle-rs", "https://github.com/QuasarRay/Candle-rs.git",
               "git@github.com:QuasarRay/Candle-rs.git", "ssh://git@github.com/QuasarRay/Candle-rs.git"}
    if remote not in allowed:
        raise ContractError("The managed implementation repository must be QuasarRay/Candle-rs")
    return "QuasarRay/Candle-rs"


def source_snapshot(root):
    # Git-visible files include new nonignored files; build and runtime output
    # are excluded explicitly. This does not attest undeclared external inputs.
    raw = subprocess.check_output(["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"], cwd=root)
    entries = {}
    for name in sorted(set(raw.decode().split("\0")) - {""}):
        if name.split("/", 1)[0] in {".aegis", "target", "__pycache__"}:
            continue
        path = confined_path(root, name)
        if path.is_file():
            entries[name] = file_digest(path)
        elif path.exists():
            raise ContractError(f"Unsupported source entry (including submodules): {name}")
    return {"digest": digest(entries), "files": entries}


def framework_snapshot(framework):
    entries = {}
    for directory, names, files in os.walk(framework, followlinks=False):
        names[:] = sorted(n for n in names if n not in {".git", ".aegis", "dist", "target", "__pycache__"})
        for name in names:
            confined_path(framework, (Path(directory) / name).relative_to(framework), must_exist=True)
        for name in sorted(files):
            path = Path(directory) / name
            relative = path.relative_to(framework)
            checked = confined_path(framework, relative, must_exist=True)
            entries[relative.as_posix()] = file_digest(checked)
    return digest(entries)


def read_state(root):
    path = confined_path(root, ".aegis/candle/state.json")
    if not path.exists():
        return {"schema": 1, "kind": "candle-spec-workflow", "root": str(root),
                "active": None, "checkpoints": [], "events": [], "sequence": 0}
    state = json.loads(path.read_text())
    sealed = state.pop("sha256", None)
    if state.get("schema") != 1 or state.get("kind") != "candle-spec-workflow" or state.get("root") != str(root):
        raise ContractError("Wrong state schema, workflow or project; legacy receipts are not imported")
    if sealed != digest(state):
        raise ContractError("State integrity check failed")
    previous = None
    for index, event in enumerate(state["events"], 1):
        if event["sequence"] != index or event["previous"] != previous:
            raise ContractError("Event history was reordered or truncated")
        previous = digest(event)
    if state["sequence"] != len(state["events"]):
        raise ContractError("Event sequence is inconsistent")
    return state


def seal_state(state, action, detail):
    state["sequence"] += 1
    event = {"sequence": state["sequence"], "action": action, "detail": detail,
             "utc": datetime.now(timezone.utc).isoformat(),
             "previous": digest(state["events"][-1]) if state["events"] else None}
    state["events"].append(event)
    return {**state, "sha256": digest(state)}


def save_state(root, state, action, detail):
    path = confined_path(root, ".aegis/candle/state.json")
    atomic_write_json(path, seal_state(state, action, detail), root=root, mode=0o600)


@contextmanager
def locked(root):
    path = confined_path(root, ".aegis/candle/control.lock")
    lock = FileLock(path, "Candle specification workflow")
    lock.acquire(timeout=1)
    try:
        state = read_state(root)
        if state.get("active"):
            with _checkpoint_instruction_copies(root, state["active"]["plan"]["id"]):
                recover_named_transactions(confined_path(root, ".aegis/candle/transactions"),
                                           expected_root=root, names=["checkpoint-packet"])
            state = read_state(root)
        yield state
    finally:
        lock.release()


def active_task(root, state, framework):
    task = state.get("active")
    if not task:
        raise ContractError("No active obligation batch")
    contract = load_authority(framework)
    if task["authority_digest"] != contract["digest"] or task["framework_digest"] != framework_snapshot(framework):
        raise ContractError("Bound authority or coordinator changed; preserve the old checkpoint and replan")
    validate_plan(task["plan"], contract)
    if git(root, "branch", "--show-current") != task["plan"]["branch"]:
        raise ContractError("Implementation branch changed")
    changes = changed_files(task["baseline"], source_snapshot(root))
    packet = task.get("packet", {}).get("files", {})
    for name, expected in packet.items():
        if file_digest(confined_path(root, name, must_exist=True)) != expected:
            raise ContractError("Committed checkpoint evidence packet changed")
    unexpected = changes - set(task["plan"]["scope"]) - set(packet)
    if unexpected:
        raise ContractError("Out-of-scope changes: " + ", ".join(sorted(unexpected)))
    return task, contract


def changed_files(before, after):
    return {name for name in set(before["files"]) | set(after["files"])
            if before["files"].get(name) != after["files"].get(name)}


def begin(root, plan, framework=None):
    root = root.resolve(strict=True)
    framework = framework or framework_dir(root)
    contract = load_authority(framework)
    validate_plan(plan, contract)
    git_repository(root)
    with locked(root) as state:
        if state["active"]:
            raise ContractError("Publish and record the current stacked PR before starting another batch")
        if any(item["batch"] == plan["id"] for item in state["checkpoints"]):
            raise ContractError("Batch ID already has a durable checkpoint")
        if git(root, "status", "--porcelain", "--untracked-files=normal"):
            raise ContractError("Begin from a clean committed checkout; preserve existing user work first")
        if git(root, "branch", "--show-current") != plan["branch"]:
            raise ContractError("Check out the planned implementation branch before beginning")
        parent = state["checkpoints"][-1] if state["checkpoints"] else None
        if parent and plan["base_branch"] != parent["branch"]:
            raise ContractError("Next PR must stack on the preceding checkpoint branch")
        base = git(root, "rev-parse", "--verify", f"refs/remotes/origin/{plan['base_branch']}^{{commit}}")
        head = git(root, "rev-parse", "HEAD")
        if head != base or (parent and head != parent["head"]):
            raise ContractError("Begin the new branch exactly at the recorded remote base commit")
        state["active"] = {"plan": plan, "authority_digest": contract["digest"],
                           "framework_digest": framework_snapshot(framework),
                           "baseline": source_snapshot(root), "base_commit": base,
                           "phase": "IMPLEMENTING", "attempts": [], "evidence": []}
        save_state(root, state, "BEGIN", {"batch": plan["id"], "obligations": plan["obligations"]})
        return {"phase": "IMPLEMENTING", "obligations": "OPEN", "baseline_execution_required": False,
                "construction": plan["reuse"]["strategy"], "base_commit": base}


def authorize_write(root, relative, framework=None):
    root = root.resolve(strict=True)
    with locked(root) as state:
        task, _ = active_task(root, state, framework or framework_dir(root))
        if task.get("packet"):
            raise ContractError("The checkpoint packet is frozen; publish before further implementation")
        confined_path(root, relative)
        if relative not in task["plan"]["scope"]:
            raise ContractError("Destination is not in the bound implementation scope")
        return {"authorized": True, "path": relative, "batch": task["plan"]["id"]}


def verify(root, framework=None):
    root = root.resolve(strict=True)
    framework = framework or framework_dir(root)
    with locked(root) as state:
        task, contract = active_task(root, state, framework)
        if task.get("packet"):
            raise ContractError("Checkpoint packet is frozen; publish it before starting another batch")
        plan = task["plan"]
        before = source_snapshot(root)
        tools = version(root)
        cache_key = digest({"source": before["digest"], "authority": contract["digest"],
                            "framework": task["framework_digest"], "plan": plan, "tool": {
                                "available": tools["available"],
                                "version": tools.get("result", {}).get("stdout", "")}})
        for item in task["evidence"]:
            if item["cache_key"] == cache_key:
                report = confined_path(root, item["path"], must_exist=True)
                if file_digest(report) != item["sha256"]:
                    raise ContractError("Cached evidence changed")
                cached = json.loads(report.read_text())
                raw = cached["result"]
                if raw.get("report_sha256") and file_digest(confined_path(root, raw["report_path"], must_exist=True)) != raw["report_sha256"]:
                    raise ContractError("Cached raw verifier export changed")
                return {**cached, "cached": True}
        if len(task["attempts"]) >= plan["budget"]["verifier_runs"]:
            raise ContractError("Verifier budget exhausted; checkpoint failed work and replan explicitly")
        attempt = uuid.uuid4().hex
        task["attempts"].append(attempt)
        save_state(root, state, "VERIFY_STARTED", {"attempt": attempt, "source": before["digest"]})
        export = confined_path(root, f".aegis/candle/evidence/{attempt}-kani.json")
        export.parent.mkdir(parents=True, exist_ok=True)
        try:
            manifest = proof_manifest(root, plan, contract)
            result = run_kani(root, plan, manifest, export) if tools["available"] else {
                "status": "UNAVAILABLE", "claim": "Pinned Kani is unavailable"}
        except (OSError, ValueError, KeyError, TypeError, SecurityError) as error:
            result = {"status": "OPEN", "error": str(error), "claim": "Missing or invalid implementation/proof input"}
        except RuntimeError as error:
            result = {"status": "FAILED", "error": str(error), "claim": "Verifier execution failed; no proof"}
        after = source_snapshot(root)
        if before != after or framework_snapshot(framework) != task["framework_digest"]:
            result["status"] = "STALE"
        record = {"schema": 1, "batch": plan["id"], "attempt": attempt, "cache_key": cache_key,
                  "source_sha256": before["digest"], "commit": git(root, "rev-parse", "HEAD"),
                  "dirty": bool(git(root, "status", "--porcelain", "--untracked-files=normal")),
                  "authority_digest": contract["digest"], "plan_digest": digest(plan), "tool": tools,
                  "source_unchanged": before == after, "result": result, "refinement": "OPEN"}
        path = confined_path(root, f".aegis/candle/evidence/{attempt}.json")
        atomic_write_json(path, record, root=root, mode=0o600)
        task["evidence"].append({"path": path.relative_to(root).as_posix(), "sha256": file_digest(path),
                                 "cache_key": cache_key, "status": result["status"]})
        task["phase"] = "EVIDENCE_RECORDED"
        save_state(root, state, "VERIFY_FINISHED", {"attempt": attempt, "status": result["status"]})
        return record


def prepare_checkpoint(root, framework=None):
    root = root.resolve(strict=True)
    framework = framework or framework_dir(root)
    with locked(root) as state:
        task, _ = active_task(root, state, framework)
        if task.get("packet"):
            return task["packet"]
        if not task["attempts"]:
            raise ContractError("Record a verification attempt, including unavailable/failed results, before checkpointing")
        snapshot = source_snapshot(root)
        base = f"supervision/checkpoints/{task['plan']['id']}"
        directory = confined_path(root, base)
        if directory.exists() and any(directory.rglob("*")):
            raise ContractError("Refusing to overwrite a checkpoint packet")
        architecture = confined_path(root, task["plan"]["architecture_record"], must_exist=True)
        if not architecture.is_file() or not architecture.read_text().strip():
            raise ContractError("Checkpoint needs its actual architecture decision record")
        files, payloads = {}, {}

        def retain(relative, data):
            import hashlib
            confined_path(root, relative)
            payloads[relative] = data
            files[relative] = hashlib.sha256(data).hexdigest()

        current_results = []
        completed = set()
        for evidence in task["evidence"]:
            path = confined_path(root, evidence["path"], must_exist=True)
            if file_digest(path) != evidence["sha256"]:
                raise ContractError("Evidence changed before checkpoint preparation")
            record = json.loads(path.read_text())
            completed.add(record["attempt"])
            retain(base + "/" + path.name, path.read_bytes())
            result = record["result"]
            export_name = result.get("report_path")
            if export_name and result.get("report_sha256"):
                exported = confined_path(root, export_name, must_exist=True)
                if file_digest(exported) != result["report_sha256"]:
                    raise ContractError("Raw verifier export changed")
                retain(base + "/" + exported.name, exported.read_bytes())
            current_results.append({"attempt": record["attempt"], "status": result["status"],
                                    "current": record["source_sha256"] == snapshot["digest"]})
        for attempt in task["attempts"]:
            if attempt not in completed:
                current_results.append({"attempt": attempt, "status": "INTERRUPTED", "current": False})
        summary = {"plan": task["plan"], "source_sha256": snapshot["digest"],
                   "authority_digest": task["authority_digest"], "results": current_results,
                   "refinement": "OPEN", "claim": "Checkpoint of implementation progress; no unbounded equivalence claim"}
        retain(base + "/summary.json", (json.dumps(summary, indent=2) + "\n").encode())
        # Required instruction copies are generated only into newly created packet directories.
        canonical = confined_path(root, "AGENTS.md", must_exist=True).read_bytes()
        for name in ("supervision/AGENTS.md", "supervision/checkpoints/AGENTS.md", base + "/AGENTS.md"):
            destination = confined_path(root, name)
            if destination.exists():
                if destination.read_bytes() != canonical:
                    raise ContractError("Existing supervision instructions diverge from root")
            else:
                retain(name, canonical)
        task["packet"] = {"directory": base, "files": files, "implementation_snapshot": snapshot}
        state_path = confined_path(root, ".aegis/candle/state.json", must_exist=True)
        sealed = seal_state(state, "PACKET_PREPARED", {"batch": task["plan"]["id"], "files": files})
        mutations = [Mutation(confined_path(root, name), data, expected_exists=False, mode=0o644)
                     for name, data in payloads.items()]
        mutations.append(Mutation(state_path, (json.dumps(sealed, indent=2, sort_keys=True) + "\n").encode(),
                                  expected_sha256=file_digest(state_path), expected_exists=True, mode=0o600))
        with _checkpoint_instruction_copies(root, task["plan"]["id"]):
            FileTransaction(root, mutations, state_dir=confined_path(root, ".aegis/candle/transactions"),
                            name="checkpoint-packet").commit(retain=False)
        return {"directory": base, "results": current_results,
                "next": "Commit the packet and implementation, push the planned branch, open a draft stacked PR, then record checkpoint"}


def github_pr(number):
    url = f"https://api.github.com/repos/QuasarRay/Candle-rs/pulls/{number}"
    request = Request(url, headers={"Accept": "application/vnd.github+json", "User-Agent": "Aegis-Candle"})
    with urlopen(request, timeout=20) as response:
        data = response.read(2_000_001)
    if len(data) > 2_000_000:
        raise ContractError("GitHub response exceeds metadata budget")
    return json.loads(data)


def checkpoint(root, pr_url, framework=None):
    root = root.resolve(strict=True)
    framework = framework or framework_dir(root)
    match = re.fullmatch(r"https://github.com/QuasarRay/Candle-rs/pull/([1-9][0-9]*)", pr_url)
    if not match:
        raise ContractError("Checkpoint must be a Candle-rs GitHub pull request")
    with locked(root) as state:
        task, _ = active_task(root, state, framework)
        if not task.get("packet"):
            raise ContractError("Prepare and commit the evidence packet before checkpointing")
        current = source_snapshot(root)
        application = {k: v for k, v in current["files"].items() if k not in task["packet"]["files"]}
        if application != task["packet"]["implementation_snapshot"]["files"]:
            raise ContractError("Implementation changed after checkpoint packet preparation")
        if git(root, "status", "--porcelain", "--untracked-files=normal"):
            raise ContractError("Commit every in-scope change before recording its remote checkpoint")
        head = git(root, "rev-parse", "HEAD")
        if head == task["base_commit"]:
            raise ContractError("Empty checkpoint has no implementation progress")
        git(root, "merge-base", "--is-ancestor", task["base_commit"], head)
        pr = github_pr(int(match[1]))
        plan = task["plan"]
        if (pr.get("state") != "open" or pr.get("merged") or pr.get("draft") is not True
                or pr.get("head", {}).get("sha") != head or pr["head"].get("ref") != plan["branch"]
                or pr["head"].get("repo", {}).get("full_name") != "QuasarRay/Candle-rs"
                or pr.get("base", {}).get("ref") != plan["base_branch"]
                or pr["base"].get("sha") != task["base_commit"]
                or pr["base"].get("repo", {}).get("full_name") != "QuasarRay/Candle-rs"):
            raise ContractError("GitHub does not show the expected open draft PR, branch, base and commit")
        remote = git(root, "ls-remote", "--exit-code", "origin", f"refs/heads/{plan['branch']}").split()
        if not remote or remote[0] != head:
            raise ContractError("Remote branch does not retain the current commit")
        if git(root, "rev-parse", "HEAD") != head or source_snapshot(root) != current:
            raise ContractError("Workspace changed during remote checkpoint verification")
        record = {"batch": plan["id"], "head": head, "branch": plan["branch"], "base": plan["base_branch"],
                  "pr": pr_url, "source_sha256": source_snapshot(root)["digest"],
                  "packet": task["packet"]["directory"], "refinement": "OPEN", "claim": "Durable progress, not proof completion"}
        state["checkpoints"].append(record)
        state["active"] = None
        save_state(root, state, "CHECKPOINT", record)
        return record


def status(root, framework=None):
    root = root.resolve(strict=True)
    framework = framework or framework_dir(root)
    contract = load_authority(framework)
    state = read_state(root)
    task = state.get("active")
    current = None
    if task:
        active_task(root, state, framework)
        current = source_snapshot(root)["digest"]
    return {"authority_digest": contract["digest"], "paper": contract["authority"]["paper"]["doi"],
            "indexed_definitions": len(contract["catalog"]), "catalog_scope": contract["scope"],
            "active": None if not task else {"id": task["plan"]["id"], "phase": task["phase"],
                "obligations": task["plan"]["obligations"], "verifier_attempts": len(task["attempts"]),
                "results": [{"status": x["status"], "path": x["path"]} for x in task["evidence"]]},
            "current_source_sha256": current, "checkpoints": state["checkpoints"],
            "unbounded_refinement": "OPEN", "full_candle_completion": False,
            "final_verification": contract["authority"]["final_verification"]}
