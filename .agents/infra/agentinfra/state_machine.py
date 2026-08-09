from __future__ import annotations


STATES = {
    "CREATED",
    "PRECHECK",
    "TRIAGE",
    "EXPLORE",
    "RESEARCH",
    "ARCHITECT",
    "PLAN",
    "IMPLEMENT",
    "DIAGNOSE",
    "REVIEW",
    "REMEDIATE",
    "VERIFY",
    "FINAL_AUDIT",
    "FINALIZE",
    "BLOCKED",
    "FAILED",
    "CANCELLED",
    "ABANDONED",
}

TERMINAL_STATES = {"FAILED", "FINALIZE", "CANCELLED", "ABANDONED"}

ALLOWED = {
    "CREATED": {"PRECHECK", "CANCELLED", "ABANDONED", "FAILED"},
    "PRECHECK": {"TRIAGE", "BLOCKED", "CANCELLED", "ABANDONED", "FAILED"},
    "TRIAGE": {"EXPLORE", "RESEARCH", "ARCHITECT", "PLAN", "IMPLEMENT", "BLOCKED", "CANCELLED", "ABANDONED", "FAILED"},
    "EXPLORE": {"TRIAGE", "RESEARCH", "ARCHITECT", "PLAN", "BLOCKED", "CANCELLED", "ABANDONED", "FAILED"},
    "RESEARCH": {"TRIAGE", "EXPLORE", "ARCHITECT", "PLAN", "BLOCKED", "CANCELLED", "ABANDONED", "FAILED"},
    "ARCHITECT": {"PLAN", "TRIAGE", "BLOCKED", "CANCELLED", "ABANDONED", "FAILED"},
    "PLAN": {"IMPLEMENT", "BLOCKED", "CANCELLED", "ABANDONED", "FAILED"},
    "IMPLEMENT": {"DIAGNOSE", "REVIEW", "VERIFY", "BLOCKED", "CANCELLED", "ABANDONED", "FAILED"},
    "DIAGNOSE": {"IMPLEMENT", "REVIEW", "REMEDIATE", "BLOCKED", "CANCELLED", "ABANDONED", "FAILED"},
    "REVIEW": {"REMEDIATE", "VERIFY", "BLOCKED", "CANCELLED", "ABANDONED", "FAILED"},
    "REMEDIATE": {"IMPLEMENT", "REVIEW", "VERIFY", "BLOCKED", "CANCELLED", "ABANDONED", "FAILED"},
    "VERIFY": {"DIAGNOSE", "REMEDIATE", "FINAL_AUDIT", "BLOCKED", "CANCELLED", "ABANDONED", "FAILED"},
    "FINAL_AUDIT": {"REMEDIATE", "VERIFY", "FINALIZE", "BLOCKED", "CANCELLED", "ABANDONED", "FAILED"},
    "BLOCKED": STATES - {"CREATED", "FINALIZE"},
    "FAILED": set(),
    "FINALIZE": set(),
    "CANCELLED": set(),
    "ABANDONED": set(),
}

PRECHECK_KEYS = {"instructions_discovered", "project_overlay_checked", "acceptance_defined"}


class TransitionError(RuntimeError):
    pass


def _transition_targets(task: dict) -> list[str]:
    return [item.get("to") for item in task.get("transitions", [])]


def validate_transition(task: dict, target: str, *, reason: str | None = None) -> None:
    target = target.upper()
    current = task["state"]
    if reason is not None and not reason.strip():
        raise TransitionError("transition reason must not be empty")
    if target not in STATES:
        raise TransitionError(f"unknown state: {target}")
    if current == target == "FINALIZE":
        return
    if target not in ALLOWED[current]:
        raise TransitionError(f"invalid transition {current} -> {target}")
    if current == "BLOCKED" and target != "FAILED":
        previous = task.get("previous_state")
        if not previous or target != previous:
            raise TransitionError(f"BLOCKED task may resume only to previous state {previous!r}, not {target}")
    if current == "PRECHECK" and target == "TRIAGE":
        required = set(PRECHECK_KEYS)
        if task.get("mode") == "write":
            required.add("workspace_inspected")
            if not isinstance(task.get("precheck", {}).get("workspace_snapshot"), dict):
                raise TransitionError("write-task precheck requires an actual workspace snapshot")
        missing = sorted(key for key in required if not task.get("precheck", {}).get(key))
        if missing:
            raise TransitionError(f"precheck incomplete: {', '.join(missing)}")
    if target == "IMPLEMENT":
        history = _transition_targets(task)
        if current == "TRIAGE" and task.get("complexity") == "XL":
            raise TransitionError("XL task cannot jump directly from TRIAGE to IMPLEMENT")
        if task.get("risk") in {"high", "critical"} and "PLAN" not in history and current != "PLAN":
            raise TransitionError(f"{task.get('risk')} risk task requires PLAN before IMPLEMENT")
    if target == "FINAL_AUDIT":
        if task.get("active_child"):
            raise TransitionError("cannot enter FINAL_AUDIT with an active child")
        if not task.get("verification_evidence"):
            raise TransitionError("task requires direct verification evidence before FINAL_AUDIT")
        if task.get("verification_epoch") != int(task.get("change_epoch", 0)):
            raise TransitionError("verification evidence is stale for the current implementation epoch")
        if task.get("mode") == "write":
            if not task.get("gates"):
                raise TransitionError("mutating task requires at least one acceptance gate before FINAL_AUDIT")
            if not any(gate.get("status") == "PROVEN" for gate in task.get("gates", [])):
                raise TransitionError("mutating task requires at least one proven, non-waived acceptance gate")
        bad = [gate["id"] for gate in task.get("gates", []) if gate.get("status") not in {"PROVEN", "WAIVED"}]
        if bad:
            raise TransitionError("unresolved acceptance gates before FINAL_AUDIT: " + ", ".join(bad))
        blocking = [
            risk["id"]
            for risk in task.get("risks", [])
            if risk.get("severity") in {"high", "critical"} and risk.get("status") != "resolved"
        ]
        if blocking:
            raise TransitionError("unresolved blocking risks before FINAL_AUDIT: " + ", ".join(blocking))
        current_epoch=int(task.get("change_epoch",0))
        current_review=any(item.get("to")=="REVIEW" and item.get("epoch")==current_epoch for item in task.get("transitions",[]))
        if task.get("risk") in {"high", "critical"} and not current_review:
            raise TransitionError(f"{task.get('risk')} risk task requires independent REVIEW before FINAL_AUDIT")
        if task.get("risk") == "critical":
            specialist_review = any(
                item.get("outcome") in {"accepted", "partial"}
                and any(marker in str(item.get("role", "")).casefold() for marker in ("adversarial", "security"))
                for item in task.get("child_history", [])
            )
            if not specialist_review:
                raise TransitionError("critical risk task requires an accepted adversarial or security child review")
    if target == "FINALIZE":
        if task.get("active_child"):
            raise TransitionError("cannot finalize with active child lease")
        if task.get("mode") == "write" and not task.get("gates"):
            raise TransitionError("mutating task requires at least one acceptance gate")
        if task.get("mode") == "write" and not any(gate.get("status") == "PROVEN" for gate in task.get("gates", [])):
            raise TransitionError("mutating task requires at least one proven, non-waived acceptance gate")
        bad = [gate["id"] for gate in task.get("gates", []) if gate.get("status") not in {"PROVEN", "WAIVED"}]
        if bad:
            raise TransitionError("unresolved acceptance gates: " + ", ".join(bad))
        blocking = [
            risk["id"]
            for risk in task.get("risks", [])
            if risk.get("severity") in {"high", "critical"} and risk.get("status") != "resolved"
        ]
        if blocking:
            raise TransitionError("unresolved blocking risks: " + ", ".join(blocking))
        if not task.get("verification_evidence"):
            raise TransitionError("task requires direct verification evidence")
        if task.get("verification_epoch") != int(task.get("change_epoch", 0)):
            raise TransitionError("verification evidence is stale for the current implementation epoch")
        if not task.get("final_audit_complete"):
            raise TransitionError("final audit not recorded")
