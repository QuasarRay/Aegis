# Branch audit and reuse decisions

Audit date: 2026-10-11. Inventory: 25 Aegis heads (24 distinct trees), 33 Destiny heads (30 trees), and 85 PMAT heads (81 trees). See `branch-inventory.json` for every exact revision, tree identity and relevant path differences. This is head/tree coverage plus source review of relevant unique implementations, not a claim to have executed every branch or audited every line.

The initial inspection covered Aegis `main` only. HOL4/MetaRocq capabilities do exist on other branches. No claim that those capabilities are absent from the project is retained.

## Aegis branch coverage

| Branch | Revision | Relationship to the reviewed MetaRocq tip |
| --- | --- | --- |
| `candle-rs` | `ea47c4122566` | Divergent; relevant tree/component differences inspected |
| `candle/01-authority` | `552aa8e77a29` | In tip history; component blob identities compared |
| `candle/02-contract-runtime` | `d7a99e137ee6` | In tip history; component blob identities compared |
| `candle/03-verifier-hardening` | `82afa955e495` | In tip history; component blob identities compared |
| `candle/04-audit` | `f8b8511558d7` | In tip history; component blob identities compared |
| `candle/05-hol4-mcp` | `464e8e7906f7` | In tip history; component blob identities compared |
| `candle/06-tactictoe-persistence` | `e01523fbf936` | In tip history; component blob identities compared |
| `codex/aegis-candle-audit` | `471f6f60f57a` | Divergent; relevant tree/component differences inspected |
| `codex/aegis-candle-authorities` | `31fffa3e7c69` | Divergent; relevant tree/component differences inspected |
| `codex/aegis-candle-runtime` | `00bef82818af` | Divergent; relevant tree/component differences inspected |
| `main` | `01060f8d731e` | In tip history; component blob identities compared |
| `metarocq/01-supervision` | `9d9cb6d4a0a8` | In tip history; component blob identities compared |
| `metarocq/02-extraction-evidence` | `3528552a4141` | Divergent; relevant tree/component differences inspected |
| `metarocq/03-extraction-budget` | `8433db24a037` | In tip history; component blob identities compared |
| `metarocq/04-z3-replay` | `fed54f274c23` | In tip history; component blob identities compared |
| `metarocq/05-artifact-inspection` | `1f22db21056a` | In tip history; component blob identities compared |
| `metarocq/06-proof-retention` | `f00afb96e35e` | In tip history; component blob identities compared |
| `metarocq/06-proof-retention-pre-rebase-80b6cb6` | `80b6cb6b8dd1` | Divergent; relevant tree/component differences inspected |
| `metarocq/07-sequential-bootstrap` | `be9ab3db96fd` | Divergent; relevant tree/component differences inspected |
| `metarocq/08-gitlab-runtime` | `7020aff92cd7` | In tip history; component blob identities compared |
| `metarocq/09-ruby-rust-transpiler` | `b57f45baf95b` | In tip history; component blob identities compared |
| `metarocq/10-github-bridge` | `f361a68b75a7` | In tip history; component blob identities compared |
| `metarocq/11-ruby-metaprogramming-review` | `ab9b75e6245d` | In tip history; component blob identities compared |
| `metarocq/12-astra-adoption-fallback` | `6baff3ff215f` | In tip history; component blob identities compared |
| `metarocq/13-target-adoption` | `3ca3f2bb048b` | In tip history; component blob identities compared |

## Reused capabilities

| Existing capability | Destiny integration |
| --- | --- |
| `contracts.py`: digest, strict JSON, validation errors | Five portable symbols, including the verifier below, copied verbatim into `destiny_reuse.py`; source and symbol SHA-256 values are recorded in `reuse-provenance.json`. |
| `verifiers.py`: exact Kani/Verus success parsing | Used for optional single-harness / counted-Verus execution. Rejects wrong or repeated inventories, vacuity, unresolved properties, failed/truncated/timed-out execution. The later parser distinguishes solver UNSAT from failed property statuses. |
| `extraction_budget.py`: reserve before launch | Adapted to per-input check recipes, two durable attempts and bounded total reserved time; a restart or missing cache index does not erase reservations. Explicit diagnosis precedes another attempt. |
| `contracts.source_snapshot`, extraction evidence, HOL4 execution | Working-tree identity, before/after source and tool checks, and explicit reuse provenance. The Destiny adapter additionally handles deleted files and ignored inputs actually consumed by reports. |
| Core `ContextLedger`, `FileLock`, atomic writes, process capture, path confinement | Reused directly from the current source core. No duplicate context database, lock implementation, subprocess supervisor or general proof engine. |
| `pipelines/roadmap.py`: runtime DAG and dependency invalidation | Declarative Destiny recipe graph with a single topological plan, conservative change routing, deduplicated prerequisites and observations that cannot self-certify proof. |

## Existing components kept as references

- **HOL4/MCP/TacticToe:** retain source pointers and their separation of cached libraries, fresh replay and orchestration smoke tests. Destiny currently uses Kani/Verus; installing a HOL4 stack or claiming a new Destiny-to-HOL correspondence would add unsupported obligations. No existing branch is modified or deleted.
- **MetaRocq extraction / proof retention:** pinned Rocq/Peregrine/CakeML recipes, retained proof data and CI artifact inspection are useful implementations for that pipeline. Destiny has no such extraction pipeline, so it inherits their budgeting/provenance patterns, not hard-coded Rocq `.v` anchors, the MetaRocq JACM paper or proof-retention claims.
- **PostgreSQL supervision / GitLab / Dagger / Rails:** inspected controller, store, roadmap and fallback variants. They introduce services, credentials and operating costs for a different target. The source README explicitly says qualified semantic replay and provider-authenticated agent dispatch are blocked. Do not import them as a completed general proof service. Bound contracts and compact local receipts suffice for this scope.
- **PR checkpoints:** `checkpoints.py` already validates exact open PR repository/base/head and verifies remote preservation. Do not invent another checkpoint protocol. Use that existing adapter when a future workflow needs it; this change creates a local branch and does not assert a remote checkpoint.
- **Older Candle report importer:** inspected `kani_report.py` and its retained RPL-1.5 notice. It expects a different JSON manifest/report protocol and hard-codes the `proofs::` harness prefix. Use the later native text adapter already in Aegis; no RPL-licensed external code is copied.
- **Pre-rebase proof-retention branch:** its only tree difference from the retained proof-retention branch is nine lines documenting historical HOL4/TacticToe qualification runs. Preserve the branch pointer as historical evidence; it establishes no Destiny proof result.
- **Target-adoption versus sequential-bootstrap tip:** inspected the five-file difference. The later target-adoption work preserves GitLab execution failures through fallback. The Destiny runner likewise never converts failed execution into a success or retries it as an invisible fallback.

## Destiny and toolkit coverage

The active Destiny formalization, runtime-fix, formation-slot and integration branches are ancestors of `destiny-rs-dev`; `ci/13-integration-gates` is exactly the same head. The older backup/pre-restack branches and `formal/11-visibility-contracts` were compared at their tips; the latter lacks the later visibility/geometry/formation proof and runtime files now present on the target. Original `main` remains a distinct behavioral reference. No target implementation is overwritten by an older branch.

All 85 PMAT heads were inventoried. For the three candidate source components, the working-tree cache contract has one unique blob among the 33 heads carrying it; dependency-cache and context-builder code each have three unique variants. Those variants were compared directly. Older dependency-cache variants write in-project state and can call unlocked `cargo tree`; later variants improve placement and lock discipline but keep the mtime validity predicate. Context-builder variants do not add a needed bounded-context mechanism. No variant justifies importing the large toolkit as a runtime dependency.

## Boundary of this customization

This branch now adopts the formal-contract migration already established by the Candle
and MetaRocq branches. It retires the previous generic acceptance controller and duplicate
release mirror instead of retaining conflicting mandates. Reusable low-level primitives
remain; target-specific Rocq authorities and unrelated service deployments remain on their
existing branches. The Destiny contract, exact proof adapters and bounded local workflow
replace the retired control surface. No other branch or target implementation is modified.
