"""Bind original HOL source; this indexes definitions, it does not interpret HOL."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re

from .security import confined_path


class ContractError(ValueError):
    pass


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def file_digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def uncomment(text):
    # Reused narrow extraction from Candle-rs tools/repo.py; pinned source shape.
    output, depth, index = [], 0, 0
    while index < len(text):
        if text[index:index + 2] == "(*":
            if not depth:
                output.append(" ")
            depth += 1
            index += 2
        elif text[index:index + 2] == "*)" and depth:
            depth -= 1
            index += 2
        else:
            if not depth or text[index] == "\n":
                output.append(text[index])
            index += 1
    if depth:
        raise ContractError("Unterminated HOL comment")
    return "".join(output)


def load_authority(framework: Path):
    path = confined_path(framework, "contracts/candle/authority.json", must_exist=True)
    authority = json.loads(path.read_text())
    if authority.get("paper", {}).get("doi") != "10.4230/LIPIcs.ITP.2022.3":
        raise ContractError("The Candle paper authority is missing or changed")
    if authority.get("target_repository") != "QuasarRay/Candle-rs" or authority.get("model") != "gpt-6-astra":
        raise ContractError("Unexpected target repository or model authority")
    if len(authority.get("files", [])) != 4:
        raise ContractError("Incomplete pinned contract inventory")
    catalog = {}
    for entry in authority["files"]:
        source = confined_path(framework, entry["local"], must_exist=True)
        data = source.read_bytes()
        blob = b"blob " + str(len(data)).encode() + b"\0" + data
        if hashlib.sha256(data).hexdigest() != entry["sha256"] or hashlib.sha1(blob).hexdigest() != entry["git_blob"]:
            raise ContractError(f"Original HOL source changed: {entry['local']}")
        if source.suffix == ".sml":
            for symbol in re.findall(r"^Definition\s+(\w+)(?:\[[^\]]*\])?:", uncomment(data.decode()), re.M):
                key = f"{source.stem}::{symbol}"
                if key in catalog:
                    raise ContractError(f"Duplicate definition: {key}")
                catalog[key] = {"file": entry["local"], "symbol": symbol,
                                "sha256": entry["sha256"], "status": "OPEN"}
    if not catalog:
        raise ContractError("No original HOL definitions found")
    route = authority.get("final_verification", {})
    if route.get("checker") != "Original Candle" or route.get("status") != "OPEN":
        raise ContractError("Original Candle is the final checker; no refinement adapter is implemented yet")
    for entry in authority.get("reuse_sources", []):
        source = confined_path(framework, entry["local"], must_exist=True)
        data = source.read_bytes()
        if (hashlib.sha256(data).hexdigest() != entry["sha256"]
                or hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest() != entry["git_blob"]):
            raise ContractError(f"Original Candle reuse source changed: {entry['local']}")
    return {"authority": authority, "digest": digest(authority), "catalog": catalog,
            "scope": "Explicit definitions in three pinned theories; not a complete Candle coverage claim"}


def validate_plan(plan, contract):
    if not isinstance(plan, dict) or plan.get("schema") != 1:
        raise ContractError("Plan schema must be 1")
    fields = {"schema", "id", "obligations", "branch", "base_branch", "scope", "reuse",
              "budget", "harnesses", "architecture_record", "authority_conflicts"}
    if set(plan) - fields:
        raise ContractError("Unknown plan fields; obsolete policy switches are not accepted")
    if plan.get("authority_conflicts", []) != []:
        raise ContractError("Resolve paper/source authority discrepancies before implementation")
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,63}", str(plan.get("id", ""))):
        raise ContractError("Invalid batch ID")
    obligations = plan.get("obligations")
    if (not isinstance(obligations, list) or not 1 <= len(obligations) <= 16
            or any(not isinstance(x, str) for x in obligations)
            or len(obligations) != len(set(obligations))):
        raise ContractError("Select 1–16 distinct original HOL obligations per checkpoint")
    if set(obligations) - set(contract["catalog"]):
        raise ContractError("Plan names an unknown original HOL definition")
    for key in ("branch", "base_branch"):
        if not re.fullmatch(r"[a-zA-Z0-9][a-zA-Z0-9/_-]{0,127}", str(plan.get(key, ""))):
            raise ContractError(f"Invalid {key}")
    if plan["branch"] in {"master", "main", "candle-rs", plan["base_branch"]}:
        raise ContractError("Use a separate implementation branch for the stacked PR")
    scope = plan.get("scope")
    if not isinstance(scope, list) or not scope:
        raise ContractError("An explicit file write scope is required")
    for name in scope:
        if (not isinstance(name, str) or not name or Path(name).is_absolute() or "\\" in name
                or any(p in {"", ".", ".."} for p in name.split("/"))
                or any(c in name for c in "*?[]")
                or name.casefold().startswith((".git/", ".agents/", ".aegis/", "spec/upstream/", "supervision/checkpoints/"))
                or name.split("/", 1)[0].casefold() in {".git", ".agents", ".aegis", "target", "__pycache__"}
                or Path(name).name.casefold() == "agents.md"):
            raise ContractError(f"Invalid or immutable write scope: {name}")
    reuse = plan.get("reuse", {})
    if reuse.get("strategy") not in {"reuse", "generate", "manual"}:
        raise ContractError("Record a reuse/generation decision before implementation")
    candidates = reuse.get("candidates")
    if not isinstance(candidates, list) or not candidates:
        raise ContractError("Inspect reusable code and generator candidates first")
    for item in candidates:
        if not isinstance(item, dict) or any(not isinstance(item.get(k), str) or not item[k].strip()
                                             for k in ("source", "revision", "assessment", "license")):
            raise ContractError("Reuse candidate needs source, revision, assessment and license")
    if not isinstance(reuse.get("reason"), str) or not reuse["reason"].strip():
        raise ContractError("Construction decision needs a token/credit rationale")
    if reuse["strategy"] == "manual" and reuse.get("manual_reason") not in {
            "no_suitable_reuse", "no_reliable_generation", "lower_expected_cost"}:
        raise ContractError("Manual implementation needs an allowed reason")
    original = reuse.get("original_candle", {})
    if original.get("revision") != contract["authority"]["repositories"]["candle"]["commit"]:
        raise ContractError("Assess Original Candle at the pinned revision before writing code")
    for capability in ("proof_replay", "metaprogramming", "code_generation"):
        item = original.get(capability, {})
        if (item.get("decision") not in {"use", "defer"} or type(item.get("saves_cost")) is not bool
                or not isinstance(item.get("reason"), str) or not item["reason"].strip()):
            raise ContractError(f"Assess Original Candle {capability}: decision, saves_cost, reason")
        if item["saves_cost"] and item["decision"] != "use":
            raise ContractError(f"Use Original Candle {capability} when it saves tokens/credits")
    budget = plan.get("budget", {})
    for key, upper in (("verifier_runs", 8), ("harness_seconds", 600)):
        if type(budget.get(key)) is not int or not 1 <= budget[key] <= upper:
            raise ContractError(f"Explicit bounded budget required: {key} (1–{upper})")
    harnesses = plan.get("harnesses")
    if (not isinstance(harnesses, list) or not harnesses
            or any(not isinstance(h, str) or not re.fullmatch(r"[A-Za-z_]\w*", h) for h in harnesses)
            or len(harnesses) != len(set(harnesses))):
        raise ContractError("Register distinct Kani harness names; missing harnesses are allowed until verification")
    if not isinstance(plan.get("architecture_record"), str) or not plan["architecture_record"].strip():
        raise ContractError("Name the architecture decision record for this batch")
    return plan
