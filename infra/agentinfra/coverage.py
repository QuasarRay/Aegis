"""Conjoin assertion-level case obligations; a partial proof is never a full case."""
import re
from .evidence import property_name
from .destiny_reuse import load_json, require
from .security import confined_path
from .context_cache import sha256_file

LANES = ("spec_proved", "production_rust_refinement_proved")


def mappings(root, rows):
    path = confined_path(root, "verification/cases/mappings.json")
    if not path.exists():
        return {}
    require(path.stat().st_size <= 4_000_000, "assertion mapping exceeds bounded input size")
    document = load_json(path.read_text())
    require(document.get("schema") == 1 and document.get("original_commit") == rows[0]["original_commit"],
            "assertion mapping authority differs")
    require(type(document.get("cases")) is list, "assertion mapping cases must be a list")
    index = {r["id"]: r for r in rows}
    inventory_path = confined_path(root, "verification/cases/inventory.json", must_exist=True)
    require(inventory_path.stat().st_size <= 2_000_000, "case inventory exceeds bounded input size")
    inventory = load_json(inventory_path.read_text())
    require(inventory.get("original_commit") == rows[0]["original_commit"] and
            inventory.get("catalog_sha256") == sha256_file(confined_path(root, "verification/spec/src/catalog.rs")),
            "assertion inventory authority differs")
    original_cases = {c["id"]: c for c in inventory["cases"]}
    require(len(original_cases) == len(inventory["cases"]) and set(original_cases) == set(index),
            "assertion inventory omitted or merged a fixture-qualified original")
    found = {}
    for record in document["cases"]:
        identity = record.get("id")
        require(identity in index and identity not in found, "unknown/ambiguous/duplicate assertion mapping identity")
        require(record.get("original_source_sha256") == index[identity]["original_source_sha256"], "assertion mapping original source differs")
        require(record.get("status") in {"Specified", "ImplementationMissing", "ProofMissing", "KnownMismatch"},
                "assertion mapping must retain an unproved Destiny obligation status")
        original = original_cases[identity]
        require(original["original_source_sha256"] == record["original_source_sha256"], "case inventory source differs")
        if record.get("rust_translation_reviewed") is True:
            require(original["extraction_status"] != "BLOCKED", "blocked source extraction cannot discharge assertion review")
            require(type(record.get("assertions")) is list and
                    len(record["assertions"]) == len({a["original_id"] for a in record["assertions"]}) and
                    {a["original_id"] for a in record["assertions"]} == set(original["assertion_ids"]),
                    "every original assertion/helper site needs a distinct reviewed mapping")
            require(type(record.get("dependency_mappings")) is list and
                    {d["original_id"] for d in record["dependency_mappings"]} == set(original["dependency_ids"]) and
                    len(record["dependency_mappings"]) == len(original["dependency_ids"]),
                    "every setup/helper dependency needs a reviewed mapping")
            require(isinstance(record.get("execution_review"), str) and bool(record["execution_review"].strip()),
                    "no-unexpected-exception, ordering and teardown review required")
            require(isinstance(record.get("reference_review"), str) and bool(record["reference_review"].strip()),
                    "implementation dependency reference review required")
            for assertion in record["assertions"]:
                require(isinstance(assertion.get("rule"), str) and bool(assertion["rule"].strip()), "original-backed rule required")
                require(type(assertion.get("rust_assertions")) is list and assertion["rust_assertions"], "Rust assertion locations required")
                for rust in assertion["rust_assertions"]:
                    source = confined_path(root, rust["file"], must_exist=True)
                    lines = source.read_text().splitlines()
                    require(type(rust["line"]) is int and 1 <= rust["line"] <= len(lines) and
                            "assert" in lines[rust["line"] - 1], "mapped Rust assertion location differs")
                    require(isinstance(rust.get("entry"), str) and isinstance(rust.get("manifest"), str) and
                            isinstance(rust.get("property"), str) and
                            property_name(rust["property"], "assertion"),
                            "mapped assertion must name its exact selected harness and observed property")
            for dependency in record["dependency_mappings"]:
                require(isinstance(dependency.get("relation"), str) and bool(dependency["relation"].strip()), "dependency relation required")
        require(type(record.get("required_obligations")) is dict and set(record["required_obligations"]) == set(LANES),
                "declare both independent proof lanes")
        for lane in LANES:
            requirements = record["required_obligations"][lane]
            require(type(requirements) is list and all(
                type(r) is dict and set(r) == {"entry", "manifest", "assertion_properties"} and
                isinstance(r["entry"], str) and isinstance(r["manifest"], str) and
                type(r["assertion_properties"]) is list and r["assertion_properties"] and
                all(property_name(p, "assertion") for p in r["assertion_properties"]) for r in requirements),
                "exact required manifest/harness declarations needed")
            require(len(requirements) == len({(r["manifest"], r["entry"]) for r in requirements}), "duplicate case proof requirement")
        if record.get("rust_translation_reviewed") is True:
            declared = {(r["entry"], r["manifest"], p) for requirements in record["required_obligations"].values()
                        for r in requirements for p in r["assertion_properties"]}
            require(all((r["entry"], r["manifest"], r["property"]) in declared for a in record["assertions"]
                        for r in a["rust_assertions"]), "mapped assertion is absent from required obligations")
        residual = record.get("residual_correspondence", [])
        require(type(residual) is list and all(type(r) is dict and set(r) == {"lane", "relation"} and
                r["lane"] in LANES and isinstance(r["relation"], str) and bool(r["relation"].strip()) for r in residual),
                "residual correspondence obligations need an exact lane and concrete relation")
        found[identity] = record
    return found


def assurance(record, proofs):
    if record is None:
        return {lane: False for lane in LANES}
    levels = {}
    for lane in LANES:
        requirements = record["required_obligations"][lane]
        # Unmapped assertions/setup or a missing required proof keeps this false.
        reviewed = record.get("rust_translation_reviewed") is True
        residual = any(r["lane"] == lane for r in record.get("residual_correspondence", []))
        levels[lane] = reviewed and not residual and bool(requirements) and all(any(
            p.get("status") == "CHECKED_SCOPED" and p.get("assurance") == lane and
            p.get("entry") == r["entry"] and p.get("manifest", "verification/kani/Cargo.toml") == r["manifest"] and
            set(r["assertion_properties"]).issubset(p.get("assertion_properties", []))
            and all(p.get("assertion_locations", {}).get(a["property"]) ==
                    {"file": a["file"], "line": a["line"]}
                    for assertion in record.get("assertions", [])
                    for a in assertion.get("rust_assertions", [])
                    if a["entry"] == r["entry"] and a["manifest"] == r["manifest"])
            for p in proofs) for r in requirements)
    return levels
