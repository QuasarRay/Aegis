# Canonical State Protocol

The parent agent owns canonical task state in `.agents/runtime/tasks/<task-id>/state.json`. Child reports
are proposals/evidence, never canonical state mutations. Canonical state also retains decisions and completed
child handoffs so a long task does not depend on conversational memory.

## Hardened lifecycle

`CREATED → PRECHECK → TRIAGE → [EXPLORE | RESEARCH | ARCHITECT] → PLAN/IMPLEMENT →
[DIAGNOSE | REVIEW | REMEDIATE]* → VERIFY → FINAL_AUDIT → FINALIZE`

`BLOCKED` records the previous state and may resume only to that state (or fail). `FAILED` and `FINALIZE`
are terminal. Stages may be skipped only where the transition graph permits it and doing so does not bypass
a gate.

### PRECHECK gate

Before `TRIAGE`, record instruction discovery, project-overlay check, acceptance definition, and—for any
mutating task—workspace/user-change inspection.

### Finalization gates

A mutating task cannot reach `FINAL_AUDIT` without verification evidence and cannot reach `FINALIZE`
without at least one acceptance gate, all gates proven/explicitly waived, no unresolved critical risk,
no active child lease, valid evidence-chain integrity, and a final audit recorded after the latest implementation/remediation. Each entry into `IMPLEMENT` or
`REMEDIATE` advances a production-change epoch, clears verification evidence, reopens previously `PROVEN`
gates, and invalidates the prior final audit/workspace fingerprint. Explicit `WAIVED` gates remain deliberate
decisions. Evidence marked as verification is accepted only in `VERIFY` and must belong to the current epoch.

Transition history is committed atomically inside the canonical state document; an uncommitted state
change cannot leave behind a false transition record. Writes use optimistic revisions plus a process lock
to reject stale concurrent mutations.

## Runtime is disposable, policy is not

`.agents/runtime/` is normally ignored by version control. It is a local coordination/evidence cache,
not a replacement for repository history. Never store secrets in it.

`audit-complete` stores a deterministic workspace fingerprint. Git worktrees use scoped HEAD/tree, status, staged/unstaged diffs and untracked-file content; non-Git projects fall back to a full project-tree content fingerprint. Framework runtime/VCS internals are excluded. `FINALIZE` recomputes the fingerprint. If project content changed after the audit, finalization fails closed and must return through verification.
