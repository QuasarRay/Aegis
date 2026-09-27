"""Run the real Kani production path, recording failures without promoting claims."""
from __future__ import annotations

from dataclasses import asdict
import json
import os
from pathlib import Path
import re

from .contracts import ContractError, file_digest
from .kani_report import validate_kani_report
from .process import run_process
from .security import SecurityError, confined_path

KANI_VERSION = "0.68.0"


def tool_environment():
    # Kani's published setup.rs supports KANI_HOME; keep process HOME isolated.
    return {name: os.environ.get(name, str(Path.home() / directory)) for name, directory in
            (("RUSTUP_HOME", ".rustup"), ("CARGO_HOME", ".cargo"), ("KANI_HOME", ".kani"))}


def version(root):
    try:
        result = run_process(["cargo", "kani", "--version"], cwd=root, timeout=20, env=tool_environment())
    except (OSError, RuntimeError) as error:
        return {"available": False, "error": str(error)}
    return {"available": result.returncode == 0 and not result.timed_out
            and result.stdout.startswith(f"Kani Rust Verifier {KANI_VERSION} "), "result": asdict(result)}


def proof_manifest(root, plan, contract):
    manifest_path = confined_path(root, "spec/obligations.json", must_exist=True)
    manifest = json.loads(manifest_path.read_text())
    if manifest.get("kani_version") != KANI_VERSION:
        raise ContractError(f"Require pinned Kani {KANI_VERSION}")
    properties = manifest.get("bounded_properties", [])
    names = [item["harness"] for item in properties]
    if len(names) != len(set(names)):
        raise ContractError("Duplicate target harness inventory")
    selected = [item for item in properties if item["harness"] in plan["harnesses"]]
    if {item["harness"] for item in selected} != set(plan["harnesses"]):
        raise ContractError("Selected Kani harness is not implemented/registered yet")
    definitions = {contract["catalog"][key]["symbol"] for key in plan["obligations"]}
    covered = set()
    source = confined_path(root, "src/proofs.rs", must_exist=True).read_text()
    actual = re.findall(r"#\[kani::proof\]\s*#\[kani::unwind\((\d+)\)\]\s*fn (\w+)", source)
    if len(actual) != len(set(actual)):
        raise ContractError("Duplicate source harnesses")
    for item in selected:
        if (not item.get("domain") or type(item.get("unwind")) is not int or item["unwind"] < 1
                or (str(item["unwind"]), item["harness"]) not in actual):
            raise ContractError("Harness source, domain or unwind bound differs from the registry")
        covered.update(item["upstream"])
    if not definitions <= covered:
        raise ContractError("Selected bounded properties do not map to every selected HOL definition")
    for entry in contract["authority"]["files"]:
        if entry["local"].endswith(".sml"):
            local = confined_path(root, "spec/upstream/" + Path(entry["local"]).name, must_exist=True)
            if file_digest(local) != entry["sha256"]:
                raise ContractError("Target and coordinator do not share byte-identical HOL source")
    return {**manifest, "bounded_properties": selected}


def run_kani(root, plan, manifest, result_path):
    # A fresh, unique export path is supplied by the coordinator for every attempt.
    if result_path.exists():
        raise ContractError("Refusing to reuse a possibly stale verifier export")
    command = ["cargo", "kani", "--output-format", "terse", "-Z", "unstable-options",
               "--harness-timeout", f"{plan['budget']['harness_seconds']}s", "--export-json", str(result_path)]
    for name in plan["harnesses"]:
        command.extend(["--harness", name])
    maximum = plan["budget"]["harness_seconds"] * len(plan["harnesses"]) + 120
    try:
        result = run_process(command, cwd=root, timeout=maximum, capture_limit=256_000, env=tool_environment())
    except (OSError, RuntimeError) as error:
        return {"status": "UNAVAILABLE", "error": str(error), "claim": "No proof established"}
    try:
        report_path = confined_path(root, result_path, must_exist=True)
        if report_path.stat().st_size > 32 * 1024 * 1024:
            raise ContractError("Kani export exceeds the 32 MiB evidence budget")
        report = json.loads(report_path.read_text())
        inventory = validate_kani_report(report, manifest)
        report_hash = file_digest(report_path)
    except (OSError, ValueError, TypeError, KeyError, SecurityError) as error:
        inventory = {"passed": False, "errors": [f"No usable export: {error}"], "harnesses": []}
        report_hash = None
    passed = result.returncode == 0 and not result.timed_out and inventory["passed"]
    return {"status": "BOUNDED_PASS" if passed else "FAILED", "process": asdict(result),
            "inventory": inventory, "report_sha256": report_hash,
            "report_path": result_path.relative_to(root).as_posix(),
            "claim": "Registered finite Kani properties only; unbounded HOL refinement remains OPEN"}
