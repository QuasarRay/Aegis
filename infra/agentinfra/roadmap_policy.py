"""Production policy decisions. Harnesses import these functions directly."""
from __future__ import annotations

from .roadmap_records import ContractError, digest, require


COMPLETION = ("IMPLEMENTATION_READY", "DOMAIN_VERIFIED", "PROJECT_COMPLETE",
              "CGP_MODERNIZATION_COMPLETE")
DOMAIN_BACKENDS = {"kani", "bolero-kani", "nagini", "esbmc-python"}
SEMANTIC_FIELDS = ("fixture_setup", "fixture_teardown", "inputs", "quantification",
                   "helpers", "call_order", "effects", "assertions", "exceptions",
                   "numeric_semantics", "identity", "tolerances", "configuration")


def may_reserve(used: int, reserved: int, requested: int, limit: int) -> bool:
    """Budget arithmetic uses nonnegative Python integers, never floats.

    post: not __return__ or used + reserved + requested <= limit
    post: not __return__ or requested > 0
    """
    return (all(type(n) is int for n in (used, reserved, requested, limit))
            and used >= 0 and reserved >= 0 and requested > 0 and limit >= 0
            and used + reserved + requested <= limit)


def all_satisfied(required: list[str], satisfied: list[str]) -> bool:
    """Empty required sets cannot certify a completion.

    post: not __return__ or len(required) > 0
    """
    return bool(required) and len(required) == len(set(required)) and set(required) <= set(satisfied)


def cgp_eligible(project_states: dict[str, str]) -> bool:
    return all(project_states.get(p) in {"PROJECT_COMPLETE", "CGP_MODERNIZATION_COMPLETE"}
               for p in ("Aegis", "Blue", "Destiny"))


def semantic_identity(original: dict, translated: dict) -> bool:
    """Checks the declared semantic contract, not arbitrary program equivalence.

    Semantic extraction and source-to-contract adequacy require separate review.
    """
    return set(original) == set(SEMANTIC_FIELDS) == set(translated) and original == translated


def correspondence_errors(source_ids: list[str], groups: list[dict]) -> list[str]:
    errors = []
    if not source_ids or len(set(source_ids)) != len(source_ids):
        errors.append("source denominator empty or duplicated")
    owners = [g.get("source_id") for g in groups]
    targets = [g.get("target_id") for g in groups]
    if set(owners) != set(source_ids) or len(owners) != len(set(owners)):
        errors.append("canonical source ownership is not bijective")
    if any(not t for t in targets) or len(targets) != len(set(targets)):
        errors.append("canonical targets are missing or shared")
    for group in groups:
        if not group.get("production_bindings") or not group.get("members"):
            errors.append(f"{group.get('source_id')}: no actual declaration/member bindings")
        if set(group.get("required_relationships", [])) != set(group.get("implemented_relationships", [])):
            errors.append(f"{group.get('source_id')}: relationship mismatch")
    return errors


def proof_errors(obligation: dict, result: dict) -> list[str]:
    errors = []
    if result.get("backend") not in DOMAIN_BACKENDS:
        errors.append("backend does not confer domain proof credit")
    if result.get("backend") != obligation.get("backend"):
        errors.append("backend differs from the reviewed obligation")
    if result.get("status") != "PROVED" or result.get("executed") is not True:
        errors.append("no executed successful proof")
    for field in ("timed_out", "truncated", "unsupported", "unwind_incomplete", "model_only"):
        if result.get(field) is not False:
            errors.append(f"{field} is not explicitly false")
    for field in ("obligation_id", "candidate", "production_digest", "contract_digest"):
        if not obligation.get(field) or result.get(field) != obligation.get(field):
            errors.append(f"mismatched {field}")
    for field in ("assertions", "covers"):
        expected = obligation.get(field, [])
        actual = result.get(field, {})
        if not expected or set(expected) != set(actual) or any(v != "SUCCESS" for v in actual.values()):
            errors.append(f"missing, extra or unsuccessful {field}")
    for field in ("assumptions", "bounds", "toolchain"):
        if field not in obligation or result.get(field) != obligation[field]:
            errors.append(f"changed or unknown {field}")
    if obligation.get("origin") == "original_test":
        if not semantic_identity(obligation.get("original_semantics", {}), obligation.get("harness_semantics", {})):
            errors.append("original test semantics differ")
        review = obligation.get("translation_review", {})
        semantic_digest = digest({"original": obligation.get("original_semantics"),
                                  "harness": obligation.get("harness_semantics"),
                                  "production": obligation.get("production_digest")})
        if (review.get("decision") != "approve_translation" or not review.get("human")
                or not review.get("provenance") or review.get("semantic_digest") != semantic_digest
                or "original_to_harness" not in review.get("scope", [])):
            errors.append("source-to-contract translation review missing, stale or outside scope")
    return errors


def authorize(action: str, context: dict) -> dict:
    reasons = []
    if context.get("provider") != "codex":
        reasons.append("CODEX_ONLY")
    if action not in {"read", "plan", "implement", "verify", "publish", "complete", "review_campaign", "cgp"}:
        reasons.append("UNKNOWN_ACTION")
    if action not in {"read", "plan"}:
        if context.get("mode") != "execute":
            reasons.append("PLAN_MODE_OR_UNKNOWN_MODE")
        if context.get("authorized") is not True:
            reasons.append("ACTION_NOT_AUTHORIZED")
        if context.get("goal_status") != "active":
            reasons.append("GOAL_NOT_ACTIVE")
        if any(context.get(k) != "max" for k in ("requested_effort", "accepted_effort", "effective_effort")):
            reasons.append("MAX_REASONING_NOT_ESTABLISHED")
        if not context.get("selected_model") or context.get("observed_model") != context.get("selected_model"):
            reasons.append("MODEL_CHANGED_OR_UNOBSERVED")
        if context.get("monetary_cap") is not None and context.get("cap_enforceable") is not True:
            reasons.append("MONETARY_CAP_REQUIRES_CONCRETE_DECISION")
        if context.get("active_agents") != 1 or context.get("lease_valid") is not True:
            reasons.append("SINGLE_AGENT_LEASE_NOT_ESTABLISHED")
        if not context.get("expected_inputs") or context.get("expected_inputs") != context.get("current_inputs"):
            reasons.append("INPUTS_STALE_OR_UNKNOWN")
    if action == "verify" and context.get("phase") == "implementation" and not context.get("early_proof_justification"):
        reasons.append("EARLY_PROOF_REQUIRES_CONCRETE_BENEFIT")
    if action == "review_campaign" and context.get("campaign_authorized") is not True:
        reasons.append("FLAW_CAMPAIGN_DEFERRED")
    if action == "cgp" and not cgp_eligible(context.get("project_states", {})):
        reasons.append("THREE_PROJECT_COMPLETION_BARRIER")
    if action == "complete" and not all_satisfied(context.get("required_gates", []), context.get("satisfied_gates", [])):
        reasons.append("ACCEPTANCE_INCOMPLETE")
    return {"allowed": not reasons, "reasons": reasons, "context_digest": digest(context)}


def goal_transition(current: dict, requested: dict, *, user_authorized: bool, acceptance: bool = False) -> dict:
    """Prepare native requests; callers must reconcile the returned native state."""
    require(user_authorized, "native lifecycle action requires its authorization")
    require(current.get("thread_id") == requested.get("thread_id") and bool(current.get("thread_id")), "wrong native thread")
    action = requested.get("action")
    require(action in {"complete", "pause", "clear", "resume", "budget"}, "unknown lifecycle action")
    require(requested.get("objective", current.get("objective")) == current.get("objective"), "objective replacement would reset accounting")
    if action == "complete":
        require(current.get("status") == "active" and acceptance, "completion requires an active goal and current acceptance")
    if action == "resume":
        require(current.get("status") in {"paused", "blocked", "budget_limited", "usage_limited", "budgetLimited", "usageLimited"}, "goal is not resumable")
    params = {"threadId": current["thread_id"], "origin": "automatic" if action == "complete" else "user"}
    if action == "budget":
        budget = requested.get("token_budget")
        require(type(budget) is int and budget > 0, "an explicit positive token budget is required")
        params["tokenBudget"] = budget
    elif action != "clear":
        params["status"] = {"complete": "complete", "pause": "paused", "resume": "active"}[action]
    return {"method": "thread/goal/clear" if action == "clear" else "thread/goal/set", "params": params}
