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
    original_ids = None
    permitted = {command[-1] for command in profile["checks"]["verus"]["commands"]}
    for o in obligations:
        optional = " ".join(k for k in ("evidence", "manifest") if k in o)
        exact_keys(o, "id invariant method entry expected_checks specification implementation proof_inputs assumptions limits " + optional, "obligation")
        require(isinstance(o["id"], str) and IDENT.fullmatch(o["id"]) and o["id"] not in ids, "unique canonical obligation id required")
        ids.add(o["id"])
        require(o["method"] in {"kani", "verus"} and isinstance(o["entry"], str), "supported proof method/entry required")
        proof_key = (o["method"], o.get("manifest", "verification/kani/Cargo.toml"), o["entry"])
        require(proof_key not in entries, "duplicate proof entry; combine its declared invariant instead of rerunning it")
        entries.add(proof_key)
        require(type(o["expected_checks"]) is int and o["expected_checks"] > 0, "positive reviewed proof inventory required")
        if o["method"] == "kani":
            require(RUST_PATH.fullmatch(o["entry"]) and o["expected_checks"] == 1, "Kani requires one canonical exact harness")
            manifest = o.get("manifest", "verification/kani/Cargo.toml")
            require(relative_path(manifest) == manifest and Path(manifest).name == "Cargo.toml", "canonical Kani manifest required")
            require(confined_path(root, manifest, must_exist=True).is_file(), "Kani manifest missing")
            paths.add(manifest)
        else:
            require("manifest" not in o, "manifest applies only to Kani")
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
        if "evidence" in o:
            from .catalog import qualified_index
            if original_ids is None:
                original_ids = {r["id"] for r in qualified_index(root)}
            scope = o["evidence"]
            exact_keys(scope, "kind original_cases assertion_properties reachability relation review", "evidence scope")
            require(o["method"] == "kani", "classified Destiny refinement currently requires exact Kani evidence")
            require(scope["kind"] in {"spec_proved", "production_rust_refinement_proved"}, "unknown proof assurance")
            cases = scope["original_cases"]
            require(type(cases) is list and 1 <= len(cases) <= 32 and all(isinstance(c, str) and c in original_ids for c in cases), "fixture-qualified original identities required")
            require(len(cases) == len(set(cases)), "duplicate original identity")
            props = scope["assertion_properties"]
            require(type(props) is list and 1 <= len(props) <= 128 and all(isinstance(p, str) and re.fullmatch(r'\S+\.assertion\.\d+', p) for p in props), "exact behavioral assertion properties required")
            require(len(props) == len(set(props)), "duplicate assertion property")
            for field in ("relation", "review"):
                prose(scope[field], field)
            witnesses = scope["reachability"]
            require(type(witnesses) is list and 1 <= len(witnesses) <= 32, "explicit non-vacuity witnesses required")
            for witness in witnesses:
                exact_keys(witness, "property file line", "reachability witness")
                require(isinstance(witness["property"], str) and re.fullmatch(r'\S+\.cover\.\d+', witness["property"]), "exact Kani cover property required")
                require(witness["file"] in o["proof_inputs"] + o["implementation"] + o["specification"], "witness must be a bound source")
                require(type(witness["line"]) is int and 1 <= witness["line"] <= len(confined_path(root, witness["file"]).read_text().splitlines()), "witness line is outside source")
            if scope["kind"] == "production_rust_refinement_proved":
                require(any(w["file"] in o["implementation"] and w["file"].startswith("src/") for w in witnesses),
                        "production refinement needs a reachable witness inside the bound production Rust source")
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


def active(root, profile, key=None):
    from .destiny import state_path
    if key is None:
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
    from .evidence import classified, current_receipt, proof_identity
    lock = FileLock(state_path(root, "formal.lock"), "destiny-formal-cycle")
    lock.acquire(timeout=0)
    try:
        key, binding = active(root, profile)
        found = [o for o in binding["contract"]["obligations"] if o["id"] == args.obligation]
        require(len(found) == 1, "obligation is not declared in the active binding")
        o = found[0]
        proof = proof_identity(root, o)
        run_args = Namespace(check=o["method"], harness=o["entry"] if o["method"] == "kani" else None,
                             entry=o["entry"] if o["method"] == "verus" else None,
                             expected_checks=o["expected_checks"] if o["method"] == "verus" else None,
                             budget_seconds=args.budget_seconds, fresh=bool(args.reason), reason=args.reason,
                             library=None, original=None, verus=args.verus, allow_network=args.allow_network,
                             manifest=o.get("manifest", "verification/kani/Cargo.toml"), proof_input=o["proof_inputs"])
        result = run_check(root, profile, run_args)
        # Recheck the entire bound input, including ignored declared sources, after execution.
        active(root, profile)
        status = "CHECKED_SCOPED" if result.get("proof_output_checked") and result["status"] == "OBSERVED_SUCCESS" else result["status"]
        assurance, blocker = "unclassified", None
        if status == "CHECKED_SCOPED":
            try:
                assurance = classified(root, o, current_receipt(root, profile, result))
            except (ValueError, OSError, KeyError) as exc:
                status, blocker = "INCOMPLETE_EVIDENCE", str(exc)
        observation = {"binding": key, "id": o["id"], "status": status, "result": result,
                       "assurance": assurance, "proof_identity": proof, "blocker": blocker,
                       "original_cases": o.get("evidence", {}).get("original_cases", []),
                       "assumptions": o["assumptions"], "limits": o["limits"]}
        atomic_write_json(state_path(root, f"proofs/{key}/{o['id']}.json"), seal(observation))
        return {**observation, "notice": "Scoped observation of the declared obligation; completeness and end-to-end parity are not certified."}
    finally:
        lock.release()


def audit(root, profile, binding_key=None):
    from .destiny import state_path
    from .evidence import classified, current_receipt, proof_identity, proof_output
    from types import SimpleNamespace
    lock = FileLock(state_path(root, "formal.lock"), "destiny-formal-cycle")
    lock.acquire(timeout=0)
    try:
        key, binding = active(root, profile, binding_key)
        rows = []
        for o in binding["contract"]["obligations"]:
            path = state_path(root, f"proofs/{key}/{o['id']}.json")
            status = "NOT_RUN"
            assurance, blocker, record = "unclassified", None, None
            if path.exists():
                record = unseal(path)
                require(record["binding"] == key and record["id"] == o["id"], "observation belongs to another obligation")
                status = record["status"]
                if status == "CHECKED_SCOPED":
                    try:
                        require(record.get("proof_identity") == proof_identity(root, o), "source/harness digest differs")
                        receipt = current_receipt(root, profile, record["result"])
                        require(receipt["proof_output_checked"] and receipt["id"] == o["method"], "receipt did not discharge proof")
                        expected = {"method": o["method"], "entry": o["entry"], "expected_checks": o["expected_checks"]}
                        if o["method"] == "kani":
                            expected["manifest"] = o.get("manifest", "verification/kani/Cargo.toml")
                        require(receipt["identity"]["obligation"] == expected, "receipt proof scope differs")
                        require(len(receipt["commands"]) == 1 and proof_output(expected, SimpleNamespace(**receipt["commands"][0])), "vacuous or invalid proof output")
                        assurance = classified(root, o, receipt)
                    except (ValueError, OSError, KeyError) as exc:
                        blocker = str(exc)
                        status = blocker if blocker.startswith("STALE_") else "UNAVAILABLE" if blocker.startswith("UNAVAILABLE:") else "INCOMPLETE_EVIDENCE"
            rows.append({"id": o["id"], "method": o["method"], "status": status,
                         "entry": o["entry"], "assurance": assurance, "blocker": blocker or (record or {}).get("blocker"),
                         "proof_identity": proof_identity(root, o),
                         "pinned_version": profile["checks"][o["method"]]["expect"][0],
                         "receipt": (record or {}).get("result", {}).get("receipt"),
                         "original_cases": o.get("evidence", {}).get("original_cases", []),
                         "assumptions": o["assumptions"], "limits": o["limits"]})
        # Do not race a source edit made during audit into a fresh claim.
        active(root, profile, key)
        return {"status": "CHECKED_SCOPED" if all(r["status"] == "CHECKED_SCOPED" for r in rows) else "INCOMPLETE",
                "binding": key, "obligations": rows,
                "notice": "Declared obligations only; specification adequacy and complete Destiny parity remain separate obligations."}
    finally:
        lock.release()


def proof_inventory(root, profile):
    """Keep proofs from earlier bindings visible; stale bindings get no credit."""
    from .destiny import state_path
    rows, blockers = [], []
    paths = sorted(state_path(root, "bindings").glob("*.json"))
    require(len(paths) <= 1024, "proof inventory exceeds bounded queue input; archive obsolete bindings")
    for path in paths:
        try:
            result = audit(root, profile, path.stem)
            rows.extend({**r, "binding": path.stem} for r in result["obligations"])
        except (ValueError, RuntimeError, OSError, KeyError) as exc:
            blockers.append({"binding": path.stem, "reason": str(exc)})
            try:
                binding = unseal(path)
                for o in binding["contract"]["obligations"]:
                    rows.append({"id": o["id"], "method": o["method"], "entry": o["entry"],
                                 "original_cases": o.get("evidence", {}).get("original_cases", []),
                                 "status": "STALE_OR_INVALID_BINDING", "assurance": "unclassified",
                                 "binding": path.stem, "blocker": str(exc)})
            except (ValueError, RuntimeError, OSError, KeyError):
                pass  # The global blocker retains corrupt binding evidence.
    return rows, blockers
