"""Persistent named execution and source-bound recovery over the existing ledger.

Observation windows and transport safeguards do not allocate a job lifetime.
Recovery records are reviewed agent decisions, not executable retrieved text.
"""
from __future__ import annotations

from pathlib import Path

from .roadmap_records import bindings_current, digest, file_binding, read_json, require
from .security import confined_path


POLICY_PATH = "Roadmaps/Shared/execution-policy.json"
STRATEGIES = frozenset({"correct_inputs", "resume_checkpoint", "async_poll", "reconnect_reobserve",
                        "verified_mirror", "wait_for_capacity", "supported_tool_mode", "expand_observation",
                        "alternate_tool", "incremental_workflow", "equivalent_acceleration"})
PRESERVES = ["work_identity_and_history", "source_and_domain", "assertions_and_counterexamples",
             "artifact_identity_and_tls", "native_goal_accounting", "external_authority"]


def read_execution_policy(root: Path) -> dict:
    policy = read_json(confined_path(root, POLICY_PATH, must_exist=True))
    require(policy.get("schema") == 1 and policy.get("amendment") == "AM20" and
            policy.get("mode") == "persistent_unlimited", "persistent AM20 execution policy required")
    require(all(policy.get(field, "missing") is None for field in
                ("max_seconds", "max_attempts", "total_seconds")), "Aegis execution caps were reintroduced")
    require(policy.get("recovery_strategies") == sorted(STRATEGIES) and
            policy.get("preserves") == PRESERVES and policy.get("require_recovery_record") is True and
            policy.get("reconcile_before_redispatch") is True and
            policy.get("external_authority") == "respect_permissions_quotas_and_retry_after",
            "persistent recovery safeguards changed")
    require(policy.get("deployment_profile") == "personal_laptop_unreliable_network" and
            policy.get("routine_recovery_owner") == "agent_without_repeated_human_allowance" and
            policy.get("adaptation") == "small_increment_between_roadmap_units" and
            policy.get("performance") == "equivalent_faster_algorithms_incremental_cache_rust_simd_cuda_when_applicable",
            "personal laptop resilience policy changed")
    return policy


def policy_binding(root: Path) -> dict:
    read_execution_policy(root)
    return file_binding(root, POLICY_PATH)


def validate_policy_binding(root: Path, binding: dict) -> None:
    require(binding == policy_binding(root) and bindings_current(root, [binding]),
            "persistent execution policy binding is stale or missing")


def retained_history(attempts: list[dict], work_id: str, inherited: tuple[str, ...] = ()) -> list[dict]:
    by_id = {a["id"]: a for a in attempts}
    require(len(by_id) == len(attempts), "duplicate durable attempt identity")
    selected = {a["id"] for a in attempts if a["work_id"] == work_id} | set(inherited)
    pending = list(selected)
    while pending:
        ident = pending.pop()
        require(ident in by_id, "retained attempt is missing")
        for ancestor in by_id[ident].get("inherited_attempt_ids", []):
            if ancestor not in selected:
                selected.add(ancestor)
                pending.append(ancestor)
    return [a for a in attempts if a["id"] in selected]


def recovery_packet(work_id: str, inputs: str, prior: list[dict]) -> dict:
    failed = prior[-1] if prior and prior[-1]["status"] != "SUCCESS" else None
    return {"schema": 1, "kind": "persistent_recovery", "work_id": work_id, "inputs": inputs,
            "prior_attempt": failed["id"] if failed else None,
            "prior_inputs": failed["inputs"] if failed else None,
            "history_digest": digest(prior), "strategies": sorted(STRATEGIES), "preserves": PRESERVES,
            "required": ["trigger", "diagnosis", "strategy", "action", "alternatives", "evidence"],
            "next_action": "Reconcile any live or unknown handle; record concrete alternatives and bind the selected recovery before redispatch. No Aegis attempt/time ceiling applies."}


def validate_recovery(root: Path, binding: dict | None, work_id: str, inputs: str,
                      prior: list[dict]) -> dict | None:
    if not prior or prior[-1]["status"] == "SUCCESS":
        require(binding is None, "recovery cannot invent a failed predecessor")
        return None
    require(prior[-1]["status"] in {"FAILED", "INTERRUPTED"}, "reconcile the existing operation before recovery")
    require(binding and bindings_current(root, [binding]), "persistent retry requires a current recovery record")
    plan = read_json(confined_path(root, binding["path"], must_exist=True))
    packet = recovery_packet(work_id, inputs, prior)
    require(all(plan.get(k) == packet[k] for k in
                ("schema", "kind", "work_id", "inputs", "prior_attempt", "prior_inputs", "history_digest", "preserves")),
            "recovery lost its exact work, failure, history or preserved semantics")
    require(plan.get("strategy") in STRATEGIES and
            all(isinstance(plan.get(k), str) and plan[k].strip() for k in ("trigger", "diagnosis", "action")),
            "recovery needs a supported strategy and concrete diagnosis/action")
    alternatives = plan.get("alternatives", [])
    require(isinstance(alternatives, list) and len(alternatives) >= 2 and
            all(isinstance(a, dict) for a in alternatives) and
            len({a.get("strategy") for a in alternatives}) == len(alternatives) and
            all(a.get("strategy") in STRATEGIES and isinstance(a.get("reason"), str) and a["reason"].strip()
                for a in alternatives) and plan["strategy"] in {a["strategy"] for a in alternatives},
            "recovery must consider at least two distinct supported strategies with reasons")
    evidence = plan.get("evidence", [])
    require(isinstance(evidence, list) and evidence and bindings_current(root, evidence),
            "recovery requires current evidence of failure or changed conditions")
    fingerprint = digest({k: plan[k] for k in ("strategy", "action", "evidence")})
    old = [a.get("recovery_fingerprint") for a in prior if a.get("semantic_inputs", a["inputs"]) == inputs]
    require(fingerprint not in old, "unchanged failed recovery cannot redispatch; choose or substantiate another strategy")
    return {"binding": binding, "fingerprint": fingerprint, "strategy": plan["strategy"]}
