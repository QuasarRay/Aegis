# Evidence-Driven Workflow

1. **PRECHECK** — instruction scope, repository roots, user changes, acceptance gates, cheapest
   relevant baseline.
2. **TRIAGE** — classify task, blast radius, uncertainty, interfaces and likely subsystem.
3. **EXPLORE/RESEARCH** only for unresolved material facts.
4. **ARCHITECT/PLAN** — choose one falsifiable design; identify rollback and narrow validation.
5. **IMPLEMENT** — one coherent hypothesis at a time; no unrelated cleanup.
6. **DIAGNOSE** if evidence falsifies the plan; do not stack speculative patches.
7. **REVIEW** independently for high-risk/large changes when it adds information.
8. **REMEDIATE** root causes, not fixture-specific symptoms.
9. **VERIFY** from narrow to broad, honoring project-required commands.
10. **FINAL_AUDIT** — diff, tests/laws, user work, temporary artifacts, contracts, unresolved risk.
11. **FINALIZE** only after gates and evidence are complete.

Use deterministic tooling for bookkeeping and filtering. Max model reasoning should be spent on
semantic decisions, not on repeatedly reconstructing state a program can preserve exactly.
