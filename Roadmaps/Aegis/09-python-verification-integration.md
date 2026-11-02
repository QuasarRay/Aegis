# A09 — Python verification integration

This is a maintained execution contract. Runtime progress is derived from current evidence in the canonical project record; this document does not assert completion.

```aegis-milestone
{
  "schema": 1,
  "contract_version": 1,
  "id": "A09",
  "project": "Aegis",
  "title": "Python verification integration",
  "phase": "implementation",
  "requirements": [
    "ROOT-05",
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
    "AM19"
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
    "AM19"
  ],
  "dependencies": [
    "A02"
  ],
  "capabilities": [
    "codex",
    "single_agent",
    "max_reasoning",
    "current_source_inventory"
  ],
  "outputs": [
    "backend selection and qualification matrix",
    "actual Python proof harnesses",
    "unsupported-semantics intervention packets"
  ],
  "write_scope": [
    "infra/**",
    "bin/**",
    "scripts/**",
    "verification/roadmap/**",
    "Roadmaps/**",
    "README.md",
    "framework.toml",
    ".aegis/**"
  ],
  "implementation_units": [
    "Review the supplied Python verification report",
    "Qualify selected tools against actual maintained production semantics",
    "Integrate results and unresolved limitations into the shared evidence contract"
  ],
  "proof_obligations": [
    {
      "id": "A09-O01",
      "statement": "Preserve exact required source responsibility and actual production linkage for A09",
      "origin": "aegis_requirement",
      "closure_phase": "completion",
      "status": "REQUIRES_CURRENT_PRODUCTION_EVIDENCE"
    },
    {
      "id": "A09-O02",
      "statement": "Keep every pending proof obligation visible; implementation acceptance never substitutes for domain verification",
      "origin": "aegis_requirement",
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
    "max_attempts": 2,
    "max_seconds_per_recipe": 900,
    "native_goal_token_budget": null,
    "monetary_cap": "unknown unless explicitly supplied and enforceable",
    "retry": "diagnose and materially correct inputs before another failed attempt; preserve consumed attempts"
  },
  "recovery": "Inspect live operation handle and verified process identity; reconcile transaction journal and current source hashes; preserve failures/reservations; resume only the same owned work or an explicitly amended unit.",
  "rollback": "Restore the last committed record generation transactionally; retain failed receipts and spent budget. Revert only this unit's owned changes after checking concurrent edits; never reset branches or delete source references.",
  "completion": "ALL declared outputs and gates have current same-candidate receipts AND all dependencies are satisfied AND no required unresolved decision remains; no status prose or marker substitutes.",
  "references": [
    "Roadmaps/Shared/ARCHITECTURE.md",
    "Roadmaps/Shared/OPERATIONS.md",
    "Roadmaps/Shared/VERIFICATION.md",
    "Roadmaps/Shared/ADOPTED_PLAN.md"
  ],
  "provides": [
    "python_verification"
  ],
  "consumes": [
    {
      "capability": "hybrid_interfaces",
      "provider": "A02"
    }
  ],
  "protected_scope": [
    "AGENTS.MD",
    "Blue_Prompt.md",
    "Destiny_Prompt.md",
    "Roadmaps/*/AGENTS.MD",
    "CPGSchema/**",
    "cgp/**",
    "derive-deftly/**",
    "genco/**",
    "jsonschema/**",
    "archstandard/**",
    "ea-skills/**"
  ]
}
```
## Engineering work

1. Review the supplied Python verification report.
2. Qualify selected tools against actual maintained production semantics.
3. Integrate results and unresolved limitations into the shared evidence contract.

Report received; qualification remains a real gate. Nagini is a deductive candidate, ESBMC a bounded candidate, CrossHair diagnostic only. No successful search or translated model is automatically production proof.

## Interfaces and artifacts

Use `ProjectProfile → MilestoneContract → WorkUnit → EvidenceReceipt`; attach `ProofObligation` and `ReviewDecision` records for domain closure. All records use the shared versioned schemas. Each work packet binds source, target, contract, recipe, toolchain and configuration identities.

- backend selection and qualification matrix.
- actual Python proof harnesses.
- unsupported-semantics intervention packets.

Record each output under the existing canonical queue/checkpoint, with an artifact path and hash. Split work by source responsibility and dependency readiness, while retaining the complete denominator. A consumed capability is credited only by its provider's current receipt; no entire-project wait is required when a narrower approved capability suffices.

## Validation and completion

Start with `roadmap.validate`. Materialize project recipe specifications with exact argv, selection, pinned tools, source identities and finite bounds before launch. Use production builds and applicable unchanged original tests during implementation. Formal work during this phase needs a documented concrete benefit; full required domain proof is mandatory for final completion.

The declared gates are conjunctive. Evidence must belong to one candidate, preserve original-test semantics, identify installed artifacts when applicable, and retain failures and missing outcomes. Use the shared verification contract for detailed original-test closure, evidence strength and human intervention. No current product state is granted by compiling this file.

## Recovery and continuation

Inspect live operation handle and verified process identity; reconcile transaction journal and current source hashes; preserve failures/reservations; resume only the same owned work or an explicitly amended unit. Restore the last committed record generation transactionally; retain failed receipts and spent budget. Revert only this unit's owned changes after checking concurrent edits; never reset branches or delete source references.

Record source facts, assumptions, alternatives, decision, expected evidence and unresolved questions in a concise decision record. Preserve independent ready work when a required human decision blocks one unit. The native objective remains the complete adopted project contract.

Write paths are repository-relative allow patterns; protected source/test/reference paths override them. Original-test byte changes need an exact separate decision. Expand adapter or package scope only through an authorized contract amendment. Every consumed capability is bound to its listed provider milestone and current evidence; finer capability receipts can be adopted explicitly without waiting for an unrelated whole project.
