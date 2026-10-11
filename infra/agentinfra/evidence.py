"""Small, conservative evidence readers. Source review remains an explicit premise.

Kani regular output and reachability semantics are pinned to kani-0.68.0.
Successful safety checks alone do not establish a reachable behavioral assertion.
"""
from pathlib import Path
import re

from .destiny_reuse import checked_output, digest, require
from .security import confined_path


def kani_properties(output):
    rows = {}
    for match in re.finditer(r'^Check \d+: (\S+)\s*\n(.*?)(?=^Check \d+:|^SUMMARY:|^VERIFICATION:|\Z)', output, re.M | re.S):
        name, body = match.groups()
        status = re.findall(r'^\s*- Status: ([A-Z_]+)\s*$', body, re.M)
        location = re.findall(r'^\s*- Location: (.+?)\s*$', body, re.M)
        require(name not in rows and len(status) == 1, "duplicate or malformed Kani property")
        rows[name] = {"status": status[0], "location": location[0] if len(location) == 1 else ""}
    return rows


def proof_output(obligation, result):
    if not checked_output(obligation, result):
        return False
    if obligation["method"] != "kani":
        return True
    try:
        rows = kani_properties(result.stdout + "\n" + result.stderr)
    except ValueError:
        return False
    # Explicit cover witnesses complement Kani's default assertion reachability
    # checks. No cover, no behavioral assertion, or an unknown property => no credit.
    return (bool(rows) and all(r["status"] in {"SUCCESS", "SATISFIED"} for r in rows.values())
            and any(".assertion." in n and r["status"] == "SUCCESS" for n, r in rows.items())
            and any(".cover." in n and r["status"] == "SATISFIED" for n, r in rows.items()))


def proof_identity(root, obligation):
    from .destiny import sha256_file
    return {"method": obligation["method"], "entry": obligation["entry"],
            "expected_checks": obligation["expected_checks"],
            "manifest": obligation.get("manifest", "verification/kani/Cargo.toml") if obligation["method"] == "kani" else None,
            "files": {field: {name: sha256_file(confined_path(root, name, must_exist=True)) for name in obligation[field]}
                      for field in ("specification", "implementation", "proof_inputs")},
            "classification": obligation.get("evidence")}


def current_receipt(root, profile, result):
    """Revalidate actual fresh output and its current identities, not a status label."""
    from .destiny import PROFILE, environment, matches_version, sha256_file, source_snapshot, state_path
    from .formal import unseal
    require(result.get("executed") is True and result.get("status") == "OBSERVED_SUCCESS", "cached/failed result is not fresh evidence")
    path = confined_path(root, result["receipt"], must_exist=True)
    require(path.parent == state_path(root, "receipts"), "receipt escaped its directory")
    receipt = unseal(path)
    require(receipt["status"] == "OBSERVED_SUCCESS" and receipt["returncode"] == 0, "receipt is not successful")
    identity = receipt["identity"]
    require(receipt["key"] == result["key"] == digest(identity) and receipt["id"] == result["id"], "receipt identity differs")
    spec = profile["checks"][receipt["id"]]
    require(identity["project"] == str(root), "receipt belongs to another checkout")
    require(identity["source"] == receipt["source_after"] == source_snapshot(root, identity.get("read_globs", spec.get("read_globs", []))), "STALE_SOURCE")
    for name, previous in identity.get("proof_inputs", {}).items():
        require(sha256_file(confined_path(root, name, must_exist=True)) == previous, "STALE_HARNESS")
    require(identity["profile"] == sha256_file(PROFILE), "STALE_PROFILE")
    require(identity["runner"] == sha256_file(Path(__file__).with_name("destiny.py")), "STALE_RUNNER")
    require(identity["helpers"] == digest({p.name: sha256_file(p) for p in sorted(Path(__file__).parent.glob("*.py"))}), "STALE_HELPERS")
    env = environment(root, identity["allow_network"])
    external_paths = identity.get("external_paths", {})
    for name, previous in identity["external"].items():
        require(name in external_paths, "missing external source identity")
        source = Path(external_paths[name])
        current = sha256_file(source) if name == "library" else source_snapshot(source)
        require(current == previous, "STALE_EXTERNAL_INPUT")
        if name == "library":
            env["DESTINY_BEVY_COMPAT_LIBRARY"] = str(source)
    require(digest(env) == identity["environment"], "STALE_ENVIRONMENT")
    for tool in identity["tools"].values():
        require(Path(tool["path"]).is_file(), "UNAVAILABLE: recorded verifier/tool is missing")
        require(sha256_file(Path(tool["path"])) == tool["sha256"], "STALE_TOOL")
    probes = receipt["probes"]
    require(identity.get("pinned_versions") == spec.get("expect", []), "pinned verifier identity differs")
    require(len(probes) == len(spec.get("expect", [])), "missing pinned version probes")
    for probe, expected in zip(probes, spec.get("expect", [])):
        require(probe["returncode"] == 0 and matches_version(expected, probe["stdout"] + probe["stderr"]), "UNAVAILABLE: pinned verifier version differs")
    outputs = receipt["commands"]
    require(outputs and [c["argv"] for c in outputs] == identity["commands"], "command inventory differs")
    for command in outputs:
        require(command["returncode"] == 0 and not any(command[k] for k in ("timed_out", "stdout_truncated", "stderr_truncated")), "failed or incomplete command output")
    return receipt


def classified(root, obligation, receipt):
    """Check declared behavioral assertions and production reachability witnesses.

    This does not infer the adequacy of the reviewed relation from Rust syntax.
    In particular an imported production module or a marker alone is insufficient.
    """
    scope = obligation.get("evidence")
    if not scope:
        return "unclassified"
    properties = kani_properties("\n".join(c["stdout"] + "\n" + c["stderr"] for c in receipt["commands"]))
    for name in scope["assertion_properties"]:
        require(name in properties and properties[name]["status"] == "SUCCESS", f"behavioral assertion not discharged: {name}")
    for witness in scope["reachability"]:
        row = properties.get(witness["property"], {})
        require(row.get("status") == "SATISFIED", "reachability witness is missing or vacuous")
        location = re.fullmatch(r'(.+?):(\d+)(?::\d+)?(?: in function .+)?', row.get("location", ""))
        require(location is not None, "reachability witness has no precise source location")
        actual = Path(location[1])
        actual = actual if actual.is_absolute() else root / actual
        require(actual.resolve() == (root / witness["file"]).resolve() and int(location[2]) == witness["line"], "reachability witness is in different source")
    return scope["kind"]


def differential_cases(root, profile, manifest):
    """Read reviewed original-case/scenario mappings backed by current runner receipts."""
    from .formal import exact_keys, prose, read
    value = read(confined_path(root, manifest, must_exist=True))
    exact_keys(value, "schema records", "differential mapping")
    require(value["schema"] == 1 and type(value["records"]) is list and 1 <= len(value["records"]) <= 64, "bounded differential mapping required")
    rows, receipts = [], {}
    for record in value["records"]:
        exact_keys(record, "case observation scenarios rationale", "differential record")
        prose(record["rationale"], "original/runtime scenario correspondence")
        observation = record["observation"]
        cache_key = digest(observation)
        if cache_key not in receipts:
            receipt = current_receipt(root, profile, observation)
            require(receipt["id"] in {"native-differential", "original-formations"}, "receipt is not a differential recipe")
            require("library" in receipt["identity"]["external"], "runtime evidence needs an actual native library")
            successful = set()
            for command in receipt["commands"]:
                out = command["stdout"] + "\n" + command["stderr"]
                scenarios = re.findall(r'^(\S+ \([^\n]+\)) \.\.\. ok\s*$', out, re.M)
                counts = re.findall(r'^Ran (\d+) tests? in ', out, re.M)
                require(len(counts) == 1 and int(counts[0]) == len(scenarios) > 0 and re.search(r'^OK\s*$', out, re.M), "empty, skipped or incomplete runtime evidence")
                successful.update(scenarios)
            receipts[cache_key] = (receipt, successful)
        receipt, successful = receipts[cache_key]
        scenarios = record["scenarios"]
        require(type(scenarios) is list and scenarios and all(s in successful for s in scenarios), "mapped runtime scenario was not executed successfully")
        rows.append({"case": record["case"], "receipt": observation["receipt"], "scenarios": scenarios,
                     "rationale": record["rationale"], "source_digest": receipt["identity"]["source"]["digest"],
                     "boundary": "Reviewed scenario correspondence and runtime observations only; no universal refinement proof."})
    return rows
