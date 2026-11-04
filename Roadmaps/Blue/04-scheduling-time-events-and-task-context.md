# B04 — Scheduling, time, events, and task context

This is a maintained execution contract. Runtime progress is derived from current evidence in the canonical project record; this document does not assert completion.

```aegis-milestone
{
  "schema": 1,
  "contract_version": 1,
  "id": "B04",
  "project": "Blue",
  "title": "Scheduling, time, events, and task context",
  "phase": "implementation",
  "requirements": [
    "BLUE-SECTION-07",
    "BLUE-SECTION-08",
    "AM01",
    "AM02",
    "AM03",
    "AM04",
    "AM05",
    "AM06",
    "AM07",
    "AM08",
    "AM09",
    "AM10",
    "AM11",
    "AM12",
    "AM13",
    "AM14",
    "AM15",
    "AM16",
    "AM17",
    "AM18",
    "AM19",
    "AM20"
  ],
  "amendments": [
    "AM01",
    "AM02",
    "AM03",
    "AM04",
    "AM05",
    "AM06",
    "AM07",
    "AM08",
    "AM09",
    "AM10",
    "AM11",
    "AM12",
    "AM13",
    "AM14",
    "AM15",
    "AM16",
    "AM17",
    "AM18",
    "AM19",
    "AM20"
  ],
  "dependencies": [
    "B02"
  ],
  "capabilities": [
    "codex",
    "single_agent",
    "max_reasoning",
    "current_source_inventory"
  ],
  "outputs": [
    "schedule/order map",
    "tasklet/context implementation",
    "event and shutdown original-test receipts"
  ],
  "write_scope": [
    "src/**",
    "tools/**",
    "migration/**",
    "python_package/**",
    "Cargo.toml",
    "Cargo.lock",
    "rust-toolchain.toml",
    "RUST_BUILD.md",
    "README.md",
    ".aegis/**"
  ],
  "implementation_units": [
    "Implement clocks, pumps, timers and ordered event dispatch",
    "Preserve synchronous tasklet suspension/resumption and task-local context",
    "Complete callbacks, reentrancy, cancellation and shutdown"
  ],
  "proof_obligations": [
    {
      "id": "B04-O01",
      "statement": "Preserve exact required source responsibility and actual production linkage for B04",
      "origin": "source_inventory_and_original_tests",
      "closure_phase": "completion",
      "status": "REQUIRES_CURRENT_PRODUCTION_EVIDENCE"
    },
    {
      "id": "B04-O02",
      "statement": "Keep every pending proof obligation visible; implementation acceptance never substitutes for domain verification",
      "origin": "source_inventory_and_original_tests",
      "closure_phase": "completion",
      "status": "REQUIRES_CURRENT_PRODUCTION_EVIDENCE"
    }
  ],
  "checks": [
    "roadmap.validate",
    "source.reconcile",
    "production.build",
    "original.tests"
  ],
  "gates": [
    "source_correspondence",
    "implemented_outputs",
    "production_build",
    "applicable_original_tests"
  ],
  "budget_policy": {
    "max_attempts": null,
    "max_seconds_per_recipe": null,
    "native_goal_token_budget": null,
    "monetary_cap": "unknown unless explicitly supplied and enforceable",
    "retry": "AM20: no internal attempt/time ceiling; reconcile handles, record evidence and at least two supported recovery alternatives before retry; preserve all history and source/domain safeguards",
    "execution_mode": "persistent_unlimited"
  },
  "recovery": "AM20 persistent recovery: reconcile the same durable handles, retain all history and native accounting, select an evidenced supported strategy from at least two alternatives; no blind duplicate dispatch, source/domain weakening or external authority evasion.",
  "rollback": "Restore the last committed record generation transactionally; retain failed receipts and spent budget. Revert only this unit's owned changes after checking concurrent edits; never reset branches or delete source references.",
  "completion": "ALL declared outputs and gates have current same-candidate receipts AND all dependencies are satisfied AND no required unresolved decision remains; no status prose or marker substitutes.",
  "references": [
    "Roadmaps/Shared/ARCHITECTURE.md",
    "Roadmaps/Shared/OPERATIONS.md",
    "Roadmaps/Shared/VERIFICATION.md",
    "Roadmaps/Shared/ADOPTED_PLAN.md"
  ],
  "provides": [
    "blue_scheduling"
  ],
  "consumes": [
    {
      "capability": "blue_vertical_runtime",
      "provider": "B02"
    }
  ],
  "protected_scope": [
    "AGENTS.MD",
    "reference/**",
    "vendor/**",
    "third_party/**",
    "src-cpp/**",
    "include/**",
    "python/**",
    "tests/**",
    "Blue_Prompt.md",
    "Destiny_Prompt.md"
  ]
}
```
## Engineering work

1. Implement clocks, pumps, timers and ordered event dispatch.
2. Preserve synchronous tasklet suspension/resumption and task-local context.
3. Complete callbacks, reentrancy, cancellation and shutdown.

Async wrappers cannot replace source-compatible synchronous APIs. Distinguish event order, callback mutation, nested dispatch and return-time visibility; keep one authoritative runtime.

## Interfaces and artifacts

Use `ProjectProfile → MilestoneContract → WorkUnit → EvidenceReceipt`; attach `ProofObligation` and `ReviewDecision` records for domain closure. All records use the shared versioned schemas. Each work packet binds source, target, contract, recipe, toolchain and configuration identities.

- schedule/order map.
- tasklet/context implementation.
- event and shutdown original-test receipts.

Record each output under the existing canonical queue/checkpoint, with an artifact path and hash. Split work by source responsibility and dependency readiness, while retaining the complete denominator. A consumed capability is credited only by its provider's current receipt; no entire-project wait is required when a narrower approved capability suffices.

## Validation and completion

Start with `roadmap.validate`. Materialize project recipe specifications with exact argv, selection, pinned tools, source identities and finite bounds before launch. Use production builds and applicable unchanged original tests during implementation. Formal work during this phase needs a documented concrete benefit; full required domain proof is mandatory for final completion.

The declared gates are conjunctive. Evidence must belong to one candidate, preserve original-test semantics, identify installed artifacts when applicable, and retain failures and missing outcomes. Use the shared verification contract for detailed original-test closure, evidence strength and human intervention. No current product state is granted by compiling this file.

## Recovery and continuation

Inspect live operation handle and verified process identity; reconcile transaction journal and current source hashes; preserve failures/reservations; resume only the same owned work or an explicitly amended unit. Restore the last committed record generation transactionally; retain failed receipts and spent budget. Revert only this unit's owned changes after checking concurrent edits; never reset branches or delete source references.

Record source facts, assumptions, alternatives, decision, expected evidence and unresolved questions in a concise decision record. Preserve independent ready work when a required human decision blocks one unit. The native objective remains the complete adopted project contract.

Write paths are repository-relative allow patterns; protected source/test/reference paths override them. Original-test byte changes need an exact separate decision. Expand adapter or package scope only through an authorized contract amendment. Every consumed capability is bound to its listed provider milestone and current evidence; finer capability receipts can be adopted explicitly without waiting for an unrelated whole project.


AM20 governs execution and recovery: no Aegis-owned attempt or job wall-clock ceiling. See [persistent execution policy](../Shared/AM20_PERSISTENT_EXECUTION.md).
