"""Declared obligations, source binding and scoped evidence, adapted from Candle/MetaRocq.

This is local integrity bookkeeping. It cannot establish that a user-supplied
specification is complete or authenticate an adversarial same-user toolchain.
"""
from __future__ import annotations

from argparse import Namespace
from pathlib import Path
import re

from .atomic import atomic_write_json
from .destiny_reuse import digest, load_json, require
from .locks import FileLock
from .security import confined_path

FRAMEWORK = Path(__file__).resolve().parents[2]
AUTHORITY = FRAMEWORK / "contracts/destiny.json"
IDENT = re.compile(r"[a-z][a-z0-9_-]{0,63}\Z")
RUST_PATH = re.compile(r"[A-Za-z_][A-Za-z0-9_]*(?:::[A-Za-z_][A-Za-z0-9_]*)*\Z")


def read(path):
    require(path.stat().st_size <= 256_000, "contract/receipt exceeds bounded JSON size")
    return load_json(path.read_text(encoding="utf-8"))


def exact_keys(obj, fields, label):
    require(type(obj) is dict and set(obj) == set(fields.split()), f"{label}: expected fields {fields}")


def prose(value, label):
    require(isinstance(value, str) and 1 <= len(value.strip()) <= 8000, f"{label}: nonempty bounded text required")
    require(not re.search(r"REPLACE_|<[^>]+>|\bTODO\b", value), f"{label}: unresolved template marker")


def framework_identity():
    paths = [*sorted((FRAMEWORK / "infra/agentinfra").glob("*.py")), AUTHORITY,
             FRAMEWORK / "modules/destiny/profile.toml", FRAMEWORK / "VERSION"]
    return digest({p.relative_to(FRAMEWORK).as_posix(): digest(p.read_bytes()) for p in paths})


def validate_plan(root, profile, value):
    from .destiny import relative_path
    exact_keys(value, "schema objective authority_sha256 reference_review reuse obligations", "formal plan")
    require(type(value["schema"]) is int and value["schema"] == 1, "unsupported formal plan schema")
    require(value["authority_sha256"] == digest(AUTHORITY.read_bytes()), "authority identity differs; review contracts/destiny.json")
    prose(value["objective"], "objective")
    prose(value["reference_review"], "reference review")
    reuse = value["reuse"]
    exact_keys(reuse, "strategy sources license reason generator", "reuse decision")
    require(reuse["strategy"] in {"reuse", "generate", "handwrite"}, "unknown reuse strategy")
    for field in ("license", "reason"):
        prose(reuse[field], f"reuse.{field}")
    require(type(reuse["sources"]) is list and len(reuse["sources"]) <= 30, "bounded reuse.sources required")
    for source in reuse["sources"]:
        prose(source, "reuse source")
    require(reuse["sources"] or reuse["strategy"] == "handwrite", "reuse/generation requires provenance")
    require(type(reuse["generator"]) is list and all(isinstance(a, str) and a for a in reuse["generator"]), "generator must be argv")
    require(reuse["strategy"] != "generate" or reuse["generator"], "generation requires a reproducible recipe")
    obligations = value["obligations"]
    require(type(obligations) is list and 1 <= len(obligations) <= 32, "declare between 1 and 32 scoped obligations")
    ids, entries, paths = set(), set(), set()
    permitted = {command[-1] for command in profile["checks"]["verus"]["commands"]}
    for o in obligations:
        exact_keys(o, "id invariant method entry expected_checks specification implementation proof_inputs assumptions limits", "obligation")
        require(isinstance(o["id"], str) and IDENT.fullmatch(o["id"]) and o["id"] not in ids, "unique canonical obligation id required")
        ids.add(o["id"])
        require(o["method"] in {"kani", "verus"} and isinstance(o["entry"], str), "supported proof method/entry required")
        require((o["method"], o["entry"]) not in entries, "duplicate proof entry; combine its declared invariant instead of rerunning it")
        entries.add((o["method"], o["entry"]))
        require(type(o["expected_checks"]) is int and o["expected_checks"] > 0, "positive reviewed proof inventory required")
        if o["method"] == "kani":
            require(RUST_PATH.fullmatch(o["entry"]) and o["expected_checks"] == 1, "Kani requires one canonical exact harness")
        else:
            require(o["entry"] in permitted, "Verus entry is outside the inspected profile")
            require(o["entry"] in o["proof_inputs"], "Verus entry must be included in proof_inputs")
        for field in ("invariant", "assumptions", "limits"):
            prose(o[field], field)
        for field in ("specification", "implementation", "proof_inputs"):
            require(type(o[field]) is list and 1 <= len(o[field]) <= 64, f"{field}: bounded source paths required")
            for name in o[field]:
                require(isinstance(name, str) and relative_path(name) == name, "canonical relative source path required")
                p = confined_path(root, name, must_exist=True)
                require(p.is_file(), f"{field}: source must be a file")
                paths.add(name)
    return sorted(paths)


def current_identity(root, profile, path):
    from .destiny import source_snapshot
    contract = read(path)
    paths = validate_plan(root, profile, contract)
    paths.append(path.relative_to(root).as_posix())
    # Include ignored proof files actually consumed by Destiny's verifier entry points.
    paths.extend(profile["checks"]["proof-markers"]["read_globs"])
    return {"plan": digest(path.read_bytes()), "framework": framework_identity(),
            "source": source_snapshot(root, paths)}, contract


def seal(data):
    return {**data, "sha256": digest(data)}


def unseal(path):
    data = read(path)
    require(type(data) is dict and "sha256" in data, "missing record integrity seal")
    sha = data.pop("sha256")
    require(digest(data) == sha, "record integrity differs")
    return data


def bind(root, profile, name):
    from .destiny import relative_path, state_path
    require(relative_path(name) == name, "contract path must be canonical and outside runtime state")
    path = confined_path(root, name, must_exist=True)
    lock = FileLock(state_path(root, "formal.lock"), "destiny-formal-cycle")
    lock.acquire(timeout=0)
    try:
        identity, contract = current_identity(root, profile, path)
        binding = {"schema": 1, "path": name, "identity": identity, "contract": contract}
        key = digest(binding)
        atomic_write_json(state_path(root, f"bindings/{key}.json"), seal(binding))
        atomic_write_json(state_path(root, "active-binding.json"), {"key": key})
        return {"status": "BOUND", "binding": key, "obligations": [o["id"] for o in contract["obligations"]],
                "notice": "Declared obligations only. No proof has been run by binding."}
    finally:
        lock.release()


def active(root, profile):
    from .destiny import state_path
    pointer = read(state_path(root, "active-binding.json"))
    key = pointer.get("key")
    require(isinstance(key, str) and re.fullmatch(r"[a-f0-9]{64}", key), "invalid active binding")
    binding = unseal(state_path(root, f"bindings/{key}.json"))
    require(digest(binding) == key, "binding identity differs")
    identity, contract = current_identity(root, profile, confined_path(root, binding["path"], must_exist=True))
    require(identity == binding["identity"] and contract == binding["contract"], "STALE binding: source, plan or controller changed; review and bind again")
    return key, binding


def verify(root, profile, args):
    from .destiny import run_check, state_path
    lock = FileLock(state_path(root, "formal.lock"), "destiny-formal-cycle")
    lock.acquire(timeout=0)
    try:
        key, binding = active(root, profile)
        found = [o for o in binding["contract"]["obligations"] if o["id"] == args.obligation]
        require(len(found) == 1, "obligation is not declared in the active binding")
        o = found[0]
        run_args = Namespace(check=o["method"], harness=o["entry"] if o["method"] == "kani" else None,
                             entry=o["entry"] if o["method"] == "verus" else None,
                             expected_checks=o["expected_checks"] if o["method"] == "verus" else None,
                             budget_seconds=args.budget_seconds, fresh=bool(args.reason), reason=args.reason,
                             library=None, original=None, verus=args.verus, allow_network=args.allow_network)
        result = run_check(root, profile, run_args)
        # Recheck the entire bound input, including ignored declared sources, after execution.
        active(root, profile)
        status = "CHECKED_SCOPED" if result.get("proof_output_checked") and result["status"] == "OBSERVED_SUCCESS" else result["status"]
        observation = {"binding": key, "id": o["id"], "status": status, "result": result,
                       "assumptions": o["assumptions"], "limits": o["limits"]}
        atomic_write_json(state_path(root, f"proofs/{key}/{o['id']}.json"), seal(observation))
        return {**observation, "notice": "Scoped observation of the declared obligation; completeness and end-to-end parity are not certified."}
    finally:
        lock.release()


def audit(root, profile):
    from .destiny import environment, sha256_file, state_path
    lock = FileLock(state_path(root, "formal.lock"), "destiny-formal-cycle")
    lock.acquire(timeout=0)
    try:
        key, binding = active(root, profile)
        rows = []
        for o in binding["contract"]["obligations"]:
            path = state_path(root, f"proofs/{key}/{o['id']}.json")
            status = "NOT_RUN"
            if path.exists():
                record = unseal(path)
                require(record["binding"] == key and record["id"] == o["id"], "observation belongs to another obligation")
                status = record["status"]
                if status == "CHECKED_SCOPED":
                    result = record["result"]
                    receipt_path = confined_path(root, result["receipt"], must_exist=True)
                    require(receipt_path.parent == state_path(root, "receipts"), "receipt escaped its directory")
                    receipt = unseal(receipt_path)
                    require(receipt["proof_output_checked"] and receipt["status"] == "OBSERVED_SUCCESS", "receipt did not discharge a fresh exact observation")
                    require(receipt["key"] == result["key"] and receipt["id"] == o["method"], "receipt identity differs")
                    expected = {"method": o["method"], "entry": o["entry"], "expected_checks": o["expected_checks"]}
                    require(receipt["identity"]["obligation"] == expected, "receipt proof scope differs")
                    if digest(environment(root, receipt["identity"]["allow_network"])) != receipt["identity"]["environment"]:
                        status = "STALE_ENVIRONMENT"
                    for tool in receipt["identity"]["tools"].values():
                        if not Path(tool["path"]).is_file() or sha256_file(Path(tool["path"])) != tool["sha256"]:
                            status = "STALE_TOOL"
            rows.append({"id": o["id"], "method": o["method"], "status": status,
                         "assumptions": o["assumptions"], "limits": o["limits"]})
        # Do not race a source edit made during audit into a fresh claim.
        active(root, profile)
        return {"status": "CHECKED_SCOPED" if all(r["status"] == "CHECKED_SCOPED" for r in rows) else "INCOMPLETE",
                "binding": key, "obligations": rows,
                "notice": "Declared obligations only; specification adequacy and complete Destiny parity remain separate obligations."}
    finally:
        lock.release()
