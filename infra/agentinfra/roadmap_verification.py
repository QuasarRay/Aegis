"""Original-test denominator and native-transition reconciliation checks."""
from __future__ import annotations

from .roadmap_records import digest, require


def test_occurrence_identity(test: dict) -> str:
    fields = ("source", "fixture", "test", "parameters", "configuration", "closure_digest")
    require(all(k in test for k in fields), "incomplete original-test identity")
    require(all(test[k] for k in ("source", "fixture", "test", "configuration", "closure_digest")), "empty fixture/configuration identity")
    return digest({k: test[k] for k in fields})


def reconcile_original_tests(required: list[dict], executed: list[dict], candidate: str) -> dict:
    expected = [test_occurrence_identity(t) for t in required]
    require(expected and len(expected) == len(set(expected)), "empty or duplicate original-test denominator")
    actual = [test_occurrence_identity(t) for t in executed]
    require(len(actual) == len(set(actual)), "duplicate execution occurrence")
    require(set(actual) <= set(expected), "execution has unowned source occurrence")
    passing = {test_occurrence_identity(t) for t in executed
               if t.get("outcome") == "PASS" and t.get("candidate") == candidate
               and t.get("loaded_artifact") == t.get("expected_artifact") and bool(t.get("loaded_artifact"))}
    missing = sorted(set(expected) - passing)
    return {"complete": not missing, "required": len(expected), "accepted": len(passing), "missing": missing}


def reconcile_native_transition(before: dict, response: dict | None, after: dict | None, desired: str) -> dict:
    """A successful-looking reply alone never certifies native state."""
    reasons = []
    if response is None or response.get("error"):
        reasons.append("transition response ambiguous or rejected")
    if not after:
        reasons.append("native reconciliation unavailable")
    else:
        for field in ("threadId", "objective"):
            if after.get(field) != before.get(field) or not before.get(field):
                reasons.append("native identity changed: " + field)
        if after.get("status") != desired:
            reasons.append("native state not confirmed")
        for field in ("tokensUsed", "timeUsedSeconds"):
            old, new = before.get(field), after.get(field)
            if type(old) is not int or type(new) is not int or new < old:
                reasons.append("native accounting missing or reset")
    # An ambiguous response may be resolved by an authoritative matching read-back.
    confirmed = bool(after) and not any(r != "transition response ambiguous or rejected" for r in reasons)
    if response and response.get("error"):
        confirmed = False
    return {"confirmed": confirmed, "reasons": reasons,
            "observation_digest": digest(after) if after else None}
