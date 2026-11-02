"""Explicit roadmap command families; legacy commands retain their dispatcher."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from .atomic import atomic_write_json, atomic_write_text
from .roadmap import compile_roadmaps, audit_evidence, packet, project_into_record, save_compiled
from .roadmap_codex import bind_goal, bind_plan, capabilities, read_native_goal
from .roadmap_knowledge import retrieve, validate_skills
from .roadmap_policy import authorize, goal_transition, proof_errors
from .roadmap_portability import inventory, markdown, shards
from .roadmap_records import ContractError, digest, read_json, require, validate_record
from .roadmap_review import render_packet, validate_decision, adjudicate_findings
from .roadmap_runtime import BudgetLedger, run_recipe
from .roadmap_inventory import authority_inventory, reconcile_inventory, save_inventory
from .roadmap_verification import reconcile_original_tests, reconcile_native_transition
from .security import confined_path


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    groups = p.add_subparsers(dest="family", required=True)
    r = groups.add_parser("roadmap").add_subparsers(dest="action", required=True)
    r.add_parser("compile").add_argument("--save", action="store_true")
    r.add_parser("audit").add_argument("--evidence", type=Path)
    a = r.add_parser("packet"); a.add_argument("milestone"); a.add_argument("--evidence", type=Path)
    a = r.add_parser("inventory"); a.add_argument("--remote", action="store_true"); a.add_argument("--save", action="store_true")
    a = r.add_parser("reconcile"); a.add_argument("--inventory", type=Path, required=True)
    a = r.add_parser("run"); a.add_argument("recipe"); a.add_argument("--diagnosis"); a.add_argument("--milestone")
    a = r.add_parser("project"); a.add_argument("--record", required=True); a.add_argument("--expected-digest", required=True); a.add_argument("--evidence", type=Path, required=True)
    a = groups.add_parser("policy"); a.add_argument("action", choices=["explain"]); a.add_argument("operation"); a.add_argument("--context", type=Path, required=True)
    c = groups.add_parser("codex").add_subparsers(dest="action", required=True)
    c.add_parser("inspect")
    c.add_parser("read-goal").add_argument("--thread", required=True)
    a = c.add_parser("bind"); a.add_argument("--observation", type=Path, required=True); a.add_argument("--thread", required=True); a.add_argument("--objective", required=True); a.add_argument("--contract", required=True)
    a = c.add_parser("plan"); a.add_argument("--item", type=Path, required=True); a.add_argument("--milestones", required=True)
    a = c.add_parser("transition"); a.add_argument("--current", type=Path, required=True); a.add_argument("--request", type=Path, required=True)
    a = c.add_parser("reconcile"); a.add_argument("--before", type=Path, required=True); a.add_argument("--after", type=Path); a.add_argument("--response", type=Path); a.add_argument("--desired", required=True)
    v = groups.add_parser("verification").add_subparsers(dest="action", required=True)
    a = v.add_parser("audit"); a.add_argument("--obligation", type=Path, required=True); a.add_argument("--result", type=Path, required=True)
    a = v.add_parser("reconcile-tests"); a.add_argument("--inventory", type=Path, required=True); a.add_argument("--executed", type=Path, required=True); a.add_argument("--candidate", required=True)
    b = groups.add_parser("budget").add_subparsers(dest="action", required=True); b.add_parser("status")
    a = b.add_parser("observe"); a.add_argument("--thread", required=True); a.add_argument("--event", required=True); a.add_argument("--total", type=int)
    r = groups.add_parser("review").add_subparsers(dest="action", required=True)
    a = r.add_parser("render"); a.add_argument("--packet", type=Path, required=True); a.add_argument("--output", required=True)
    a = r.add_parser("decision"); a.add_argument("--packet", type=Path, required=True); a.add_argument("--decision", type=Path, required=True)
    a = r.add_parser("findings"); a.add_argument("--input", type=Path, required=True)
    a = groups.add_parser("skills"); a.add_argument("action", choices=["validate"])
    a = groups.add_parser("portability"); a.add_argument("action", choices=["build", "check"])
    a = groups.add_parser("knowledge"); a.add_argument("action", choices=["get"]); a.add_argument("--source", required=True); a.add_argument("--start", type=int, required=True); a.add_argument("--end", type=int, required=True)
    return p


def execute(a) -> dict:
    root = a.root.resolve()
    if a.family == "roadmap":
        compiled = compile_roadmaps(root)
        if a.action == "compile":
            if a.save: save_compiled(root, compiled)
            return compiled
        if a.action == "inventory":
            record = authority_inventory(root, remote=a.remote)
            if a.save:
                return save_inventory(root, record)
            return record
        if a.action == "reconcile": return reconcile_inventory(root, read_json(a.inventory))
        if a.action == "run": return run_recipe(root, compiled, a.recipe, diagnosis=a.diagnosis, milestone=a.milestone)
        evidence = read_json(a.evidence) if a.evidence else {"schema": 1, "compiled_digest": compiled["digest"], "receipts": []}
        audit = audit_evidence(root, compiled, evidence)
        if a.action == "audit": return audit
        if a.action == "packet": return packet(compiled, audit, a.milestone)
        return project_into_record(root, a.record, audit, a.expected_digest)
    if a.family == "policy": return authorize(a.operation, read_json(a.context))
    if a.family == "codex":
        if a.action == "inspect": return capabilities()
        if a.action == "read-goal": return read_native_goal(a.thread)
        if a.action == "bind": return bind_goal(read_json(a.observation), thread_id=a.thread, objective=a.objective, contract_hash=a.contract)
        if a.action == "plan": return bind_plan(read_json(a.item), a.milestones.split(","), compile_roadmaps(root))
        if a.action == "reconcile": return reconcile_native_transition(read_json(a.before), read_json(a.response) if a.response else None, read_json(a.after) if a.after else None, a.desired)
        request = read_json(a.request)
        return {"prepared_only": True, "request": goal_transition(read_json(a.current), request,
                user_authorized=request.get("user_authorized") is True, acceptance=request.get("acceptance") is True)}
    if a.family == "verification":
        if a.action == "reconcile-tests": return reconcile_original_tests(read_json(a.inventory), read_json(a.executed), a.candidate)
        obligation = read_json(a.obligation); validate_record(root, "ProofObligation", obligation)
        errors = proof_errors(obligation, read_json(a.result))
        return {"accepted": not errors, "errors": errors, "limit": "record consistency; backend qualification and source-to-contract adequacy remain separate"}
    if a.family == "budget":
        ledger = BudgetLedger(root)
        return ledger.read() if a.action == "status" else ledger.observe_usage(a.thread, a.event, a.total)
    if a.family == "review":
        if a.action == "findings": return {"findings": adjudicate_findings(root, read_json(a.input))}
        review = read_json(a.packet)
        if a.action == "render":
            output = confined_path(root, a.output)
            atomic_write_text(output, render_packet(root, review), root=root)
            return {"output": str(output), "packet_digest": digest(review)}
        decision = read_json(a.decision); validate_record(root, "ReviewDecision", decision); validate_decision(review, decision)
        return {"decision_valid": True, "proof_credit": False}
    if a.family == "skills": return validate_skills(root)
    if a.family == "knowledge": return retrieve(root, a.source, a.start, a.end)
    if a.family == "portability":
        record = inventory(root); destination = root / "Roadmaps/Shared/python-rust/inventory.json"
        index, parts = shards(record)
        if a.action == "build":
            for name, value in parts.items():
                atomic_write_json(destination.parent / "units" / name, value, root=root)
            for source in record["files"]:
                units = [u for u in record["units"] if u["file"] == source["path"]]
                path = destination.parent / (source["path"].replace("/", "__") + ".md")
                atomic_write_text(path, markdown(dict(record, files=[source], units=units)), root=root)
            # Publish the index last. Interrupted generation cannot pass freshness checks.
            atomic_write_json(destination, index, root=root)
            return {"files": len(record["files"]), "units": len(record["units"]), "shards": len(parts), "digest": record["digest"]}
        require(read_json(destination) == index, "Python-to-Rust mapping is missing or stale; regenerate and review changed blocks")
        for name, value in parts.items():
            require(read_json(destination.parent / "units" / name) == value, "Python-to-Rust inventory shard missing or changed")
        for source in record["files"]:
            path = destination.parent / (source["path"].replace("/", "__") + ".md")
            units = [u for u in record["units"] if u["file"] == source["path"]]
            require(path.read_text() == markdown(dict(record, files=[source], units=units)), "Rust migration description missing/stale")
        return {"status": "CURRENT", "files": len(record["files"]), "units": len(record["units"])}
    raise ContractError("unknown command family")


def main(argv=None) -> int:
    p = parser(); args = p.parse_args(argv)
    try:
        result = execute(args)
        print(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False))
        if any(result.get(field) is False for field in ("allowed", "accepted", "complete", "confirmed")): return 1
        if args.family == "roadmap" and args.action == "run":
            return 0 if result["returncode"] == 0 and not result["timed_out"] and not result["truncated"] else 1
        return 0
    except (ContractError, OSError, KeyError, TypeError, TimeoutError) as exc:
        p.exit(2, f"roadmap rejected: {exc}\n")
