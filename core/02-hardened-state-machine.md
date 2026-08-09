# Hardened Task State Machine

For substantial mutating work, use `.agents/bin/agentctl.py task ...` when available.

Canonical lifecycle:

`CREATED -> PRECHECK -> TRIAGE -> [EXPLORE|RESEARCH|ARCHITECT] -> PLAN -> IMPLEMENT ->
[DIAGNOSE] -> [REVIEW -> REMEDIATE] -> VERIFY -> FINAL_AUDIT -> FINALIZE`

Not every optional state is required. Skipping optional work must be deliberate; it must not
skip precheck or final acceptance proof.

## PRECHECK hard gates

Before leaving PRECHECK for mutating work record:

- applicable instructions discovered;
- project overlay checked;
- workspace/user-change snapshot inspected;
- acceptance gates defined.

## State integrity

- Parent is sole canonical writer.
- Every transition is append-only in history and increments a revision.
- Invalid transitions fail closed.
- `BLOCKED` records blocker and return state.
- Do not mark `FINALIZE` while a child lease is active.
- Do not finalize with unresolved critical risks.
- Mutating tasks require verification evidence from the current production-change epoch.
- A mutating task must have at least one acceptance gate, and every gate must be PROVEN or explicitly WAIVED before entering `FINAL_AUDIT`.
- Unresolved critical risks block `FINAL_AUDIT`, not merely finalization.
- Entering `IMPLEMENT` or `REMEDIATE` advances the production-change epoch, clears verification, reopens prior `PROVEN` gates, and invalidates the prior final audit.
- `FINALIZE` independently rechecks referenced evidence records and rejects proofs from an older production-change epoch even if task state was manually corrupted.
- Final audit must be recorded after the last behavior-changing edit and is bound to a workspace-content fingerprint.

A state file documents work; it does not prove code correctness. Evidence remains authoritative.
