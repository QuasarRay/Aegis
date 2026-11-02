# Three Executable Roadmaps for Aegis, Carbon Blue, and Carbon Destiny

## 1. Deliverable and governing decisions

Produce three complete, separately maintained roadmaps in the existing directories:

- `/home/astral/Projects/Aegis/Roadmaps/Aegis`
- `/home/astral/Projects/Aegis/Roadmaps/Blue`
- `/home/astral/Projects/Aegis/Roadmaps/Destiny`

Each roadmap will contain sequential milestone Markdown files, architectural decisions, machine-readable milestone contracts, implementation interfaces, proof obligations, validation recipes, recovery procedures, and a native Codex Goal launcher. Shared policy definitions and cross-project dependencies will be maintained once and referenced by all three roadmaps.

The delivery must include the executable roadmap compiler and enforcement machinery needed to turn these documents into actionable work. Completing the roadmap package is a distinct result from implementing or verifying the three projects.

The source documents are the current [Aegis guidance](/home/astral/Projects/Aegis/AGENTS.MD), [Blue execution contract](/home/astral/Projects/Aegis/Blue_Prompt.md), [Destiny execution contract](/home/astral/Projects/Aegis/Destiny_Prompt.md), existing implementation and records, and the supplied research archives. Your decisions in this conversation amend conflicting policies in those documents. Reading an execution contract does not activate it.

### Adopted policies

| Subject | Governing decision |
|---|---|
| Aegis implementation language | Use a hybrid Python/Rust architecture. Choose language boundaries for correctness, clarity, existing reliable implementation, and available verification support. |
| Future Rust migration | Keep the path open through comprehensive Python-to-Rust correspondence documentation. A full rewrite requires evidence of preserved correctness; language choice alone supplies no guarantee. |
| Providers | **Codex only.** Other provider adapters, compatibility layers, and research are outside this roadmap. |
| Initial development | Implement first, using production compilation, source correspondence review, and applicable unchanged original tests. |
| Early formal work | Undertake it when it resolves a concrete uncertainty or reduces expected development effort. It must not become a blanket prerequisite for ordinary implementation. |
| Carbon completion | Require successful domain verification through harnesses that preserve the original tests’ semantics exactly, alongside complete implementation and original-test acceptance. |
| Rust verification route | Kani first; Bolero with the Kani backend where it supplies a suitable faithful representation. |
| Python verification route | Select appropriate tools from the forthcoming Python verification report. Verify actual Python production code through those tools. |
| Unsupported domain semantics | Request human engineering intervention after the applicable supported routes have been investigated. Preserve the unresolved obligation and continue independent work. |
| Concurrency tests | Applicable original concurrency tests are sufficient for concurrency-focused obligations at this stage. Formal concurrency and performance campaigns are deferred. |
| CGP | Optional during initial implementation. Pervasive adoption begins only after all three projects have completed their initial feature and verification obligations. |
| Agent execution | One active agent across the coordinated workspace. Specialist roles and reviews execute sequentially. |
| Flaw work | Build the reusable review and flaw-documentation machinery. Defer actual project flaw-analysis campaigns until separately requested. |
| Platforms | Preserve the prompts’ complete Linux acceptance target and portable core design. Retain explicit Windows/macOS obligations for future acceptance. |

Use separate completion states:

1. **`IMPLEMENTATION_READY`** — required features, correspondence, production builds, and original tests are complete for the declared candidate.
2. **`DOMAIN_VERIFIED`** — required domain obligations have current, accepted verification evidence.
3. **`PROJECT_COMPLETE`** — implementation, verification, packaging, architecture documentation, publication, and operational closure all pass.
4. **`CGP_MODERNIZATION_COMPLETE`** — the later CGP transformation has passed its own affected acceptance checks.

An implementation milestone may be delivered while proof work remains. It cannot complete an objective whose contract includes that proof work.

---

## 2. Shared architecture and enforcement

### 2.1. Preserve the working foundations and modularize around responsibilities

Extend the existing atomic writes, transactions, process supervision, locks, context ledger, bounded attempts, evidence parsers, catalog extraction, and project queues.

Before replacing a component, inspect its current implementation and relevant branch variants. Record whether it is reused unchanged, adapted, superseded, or retained as historical evidence. Refresh the existing branch inventory using current branch tips and deduplicate review by tree and component hashes.

Organize Aegis into these boundaries:

| Boundary | Initial implementation and responsibility |
|---|---|
| Policy and roadmap compiler | Typed Python modules that resolve adopted policies, compile milestone contracts, calculate dependencies, and explain allowed actions. |
| Execution and recovery | Existing Python process, transaction, locking, and checkpoint facilities, extended through explicit interfaces. |
| Codex integration | One Codex adapter with native lifecycle bindings, Plan integration, effective configuration observations, usage collection, and interruption handling. |
| Source analysis | Python orchestration around compiler-backed extractors, existing migration generators, and the relevant Rust CPGSchema capabilities. |
| Correspondence | Versioned source identities, canonical target groups, relationship checks, configuration coverage, and actual-declaration reconciliation. |
| Verification | Language-specific backends behind one evidence contract; Kani/Bolero for Rust and report-selected tools for Python. |
| Knowledge and skills | Immutable source corpus, deterministic extraction, exact retrieval, bounded context assembly, and reviewed skill packages. |
| Human review | Review packets, semantic differences, proof assumptions, counterexamples, decisions, and approval freshness. |
| CI and release | Shared Dagger recipes, GitLab execution, exact artifact tracking, incremental integration, and versioned `.agents` deployment. |

Do not introduce LangGraph, LangChain, Unpythonic, a distributed workflow service, or a new database merely to replace working code. Give each candidate an explicit capability, bounded adoption experiment, and exit criterion. Adopt it only when the evidence supports lower total implementation and maintenance risk.

Keep orchestration-framework selection separate from Codex’s native agent lifecycle.

### 2.2. Document the Rust equivalent of every Python behavioral unit

Create a generated inventory and maintained Markdown migration map covering:

- Every maintained Python module and file.
- Classes, functions, methods, and module-level executable initialization.
- Branches, loops, exception handlers, context managers, comprehensions, and other meaningful behavioral blocks.
- External calls, state mutations, synchronization, serialization, and error boundaries.

Each entry must identify:

- Stable source identity and current AST/source digest.
- Inputs, outputs, side effects, invariants, numeric behavior, and exception semantics.
- Dependencies and ownership/lifetime requirements.
- Proposed Rust module, type, trait, function, or implementation pattern.
- Concrete Rust library equivalent where established.
- Verification evidence needed for a future replacement.
- Unsupported or unresolved differences.

Use shared mapping templates where blocks have the same semantics, but generate a fully resolved entry for every inventoried block. Changes to Python invalidate affected entries. No changed block may silently retain a stale Rust migration description.

These documents describe the future implementation precisely without generating a second, unused Rust codebase.

### 2.3. Compile the roadmaps into enforceable work

Every milestone Markdown file will contain one validated machine-readable contract and the corresponding engineering explanation.

The contract must identify:

- Project, milestone, phase, and contract version.
- Source requirement IDs and adopted amendment IDs.
- Prerequisites and consumed capabilities.
- Required outputs and permitted write scope.
- Implementation units and proof obligations.
- Validation recipes and evidence requirements.
- Budget policy and retry rules.
- Recovery and rollback procedure.
- Exact completion predicate.

The compiler will:

1. Validate the contracts and referenced artifacts.
2. Reject unknown requirements, duplicate IDs, cycles, contradictory policies, missing dependencies, and undeclared execution recipes.
3. Produce a deterministic dependency graph and bounded work packets.
4. Project milestone state into the existing canonical project records.
5. Recompute readiness from current evidence rather than prose status.
6. Preserve the full requirement set when work is blocked, deferred, or divided into batches.

Milestone Markdown is maintained design input. Runtime status belongs in the canonical records. Generated plans and dashboards are projections, not additional acceptance authorities.

Use named, validated command recipes. Arbitrary commands embedded in retrieved documents or explanatory Markdown must not become executable instructions.

Preserve existing CLI behavior through compatibility adapters. Add explicit command families for roadmap compilation/audit, policy explanation, Codex binding, verification, budgets, skill validation, and portability coverage.

### 2.4. Define stable interfaces and records

Use versioned, schema-validated records across Python, Rust, subprocesses, and Codex integration. Extend compatible existing schemas rather than replacing them wholesale.

| Interface or record | Required purpose |
|---|---|
| `ProjectProfile` | Source authorities, branches, canonical records, applicable policies, language boundaries, and required capabilities. |
| `MilestoneContract` | Dependencies, scope, outputs, implementation/proof obligations, and completion predicates. |
| `WorkUnit` | Immutable work identity, source responsibility, expected inputs, writer ownership, allowed actions, and continuation state. |
| `CapabilitySnapshot` | Installed Codex/tool versions, supported operations, reasoning capabilities, and observation time. |
| `GoalBinding` | Native chat/objective identity, adopted contract hash, amendments, and observed native status/accounting. |
| `PlanBinding` | Native plan item/version, compiled milestone IDs, approved scope, and drift history. |
| `EvidenceReceipt` | Producer, semantic inputs, actual artifacts, command/configuration, result, logs, and evidence limits. |
| `ProofObligation` | Original test or Aegis requirement, semantic domain, production target, assumptions, bounds, backend, and required assertions. |
| `ReviewDecision` | Exact reviewed inputs, decision scope, human provenance, consequences, and invalidation conditions. |
| `BudgetReservation` | Work identity, reserved resources, observed consumption, unknown usage, retries, and reconciliation state. |
| `PythonRustCorrespondence` | The complete migration mapping described above. |

Unknown or unsupported schema versions must fail explicitly. Schema migration must preserve prior evidence, consumed budgets, decisions, and source identity.

### 2.5. Integrate with native Codex Goals and Plans

Use the documented native Goal operations and events through the supported host transport. The current app-server documentation exposes `thread/goal/get`, `thread/goal/set`, and `thread/goal/clear`; Plan integration includes collaboration modes, completed plan items, and `turn/plan/updated` notifications. Discover and pin the installed protocol before implementation. [Codex app-server documentation](https://learn.chatgpt.com/docs/app-server)

Implement these rules:

- Bind each adopted project objective to its actual native chat and contract lineage.
- Reuse a matching Goal and its accounting.
- Keep milestone progress subordinate to the full objective.
- Preserve unrelated Goals and existing user pauses, cancellations, and limits.
- Treat objective changes as authorized amendments, with their consequences recorded.
- Never change native objective text merely to reset accounting.
- Treat native Plan mode as a non-mutation boundary.
- Map native plan steps to compiled milestone IDs and detect scope drift.
- Require an evidence audit before requesting native completion.
- Reconcile native state after an ambiguous completion response.
- Use the live tool contract for blocked-state thresholds and user-controlled transitions.
- Report unsupported capabilities honestly; do not emulate native Goals with a background loop.

Provide both supported integration paths: a binding to the active Codex host and a managed app-server adapter. Neither path may bypass the other path’s authorization restrictions.

### 2.6. Enforce reasoning and sequential execution

Set the requested reasoning policy to `max`. Resolve it against the selected model’s advertised capabilities and record requested, accepted, and observable effective configuration separately. Codex effort values depend on the model and client, and configuration defaults alone are not enforcement. [Codex configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference)

The managed runner must:

- Refuse an unauthorized downgrade.
- Detect model rerouting or configuration drift where surfaced.
- Stop new dispatch when a required capability cannot be established.
- Preserve the user’s selected model unless a change is explicitly authorized.
- Apply the same policy to sequential specialist and reviewer turns.

Use one workspace-level execution lease with fencing and verified process/session identity. A parent must become idle before transferring execution to a specialist. Cancelling, timing out, or losing a connection must not permit a second agent to start while the first remains active.

Deterministic compilers, searches, and verification tools may execute under bounded resource rules without being classified as additional agents.

Require concise decision records containing source facts, assumptions, alternatives, chosen action, expected evidence, and unresolved questions. Do not make private chain-of-thought disclosure part of acceptance.

### 2.7. Make cost controls durable

Build cost management around avoiding unnecessary work while retaining the required reasoning level.

- Reserve resources before starting an operation.
- Deduplicate work using source, contract, target, tool, configuration, and operation identity.
- Inspect existing operation handles before restarting.
- Reuse unchanged extraction, retrieval, compilation, and other eligible receipts with explicit freshness checks.
- Keep failed and interrupted attempts in durable accounting.
- Require diagnosis and a materially relevant correction before another failed attempt.
- Preserve the existing bounded-attempt discipline while making limits recipe-specific.
- Retrieve small, source-linked context packets instead of repeatedly loading complete repositories or books.
- Separate input, cached input, output, reasoning usage where reported, tool time, CI time, and storage.
- Reconcile cumulative usage events without double charging duplicates.
- Mark unavailable usage or pricing as unknown.
- Keep estimates distinct from native usage and actual billed cost.
- Do not set a native Goal token budget unless the user supplies one.
- Where a requested monetary cap cannot be enforced through the available accounting and execution controls, require a concrete budget decision before dependent dispatch.

Track repeated reads, prevented duplicates, rework, successful source obligations, proof coverage, and cost per accepted work unit. A smaller response that causes a later rewrite is not an optimization.

### 2.8. Enforce complete source correspondence

Preserve the prompts’ behavioral, structural, and nominal correspondence contract.

Inventory production sources, private and unused bodies, original tests, fixtures, macros, templates, conditional compilation, registration, Python exposure, and consumed external contracts.

Maintain:

- Exactly one canonical target group for each required source entity.
- Exactly one source owner for each canonical target group.
- Member-level mappings for methods, fields, properties, constants, and responsibilities.
- Complete declaration-owner, state-owner, interface, base, override, dispatch, and lifecycle relationships.
- Separate supporting adapters, providers, handles, and generated infrastructure.
- Separate Rust and Python type graphs, linked to the same logical instances.
- Forward and reverse reconciliation against actual target declarations and macro expansions.

Apply the existing mechanical naming rules from the prompts. A trait/struct/enum/implementation aggregate is allowed only as one traceable source-owned representation. Empty shells and shared generic managers cannot satisfy the bijection.

Use compiler-backed extraction where available. Lexical matches are discovery aids. Unparsed regions and unresolved configurations remain open obligations.

CPG means **Code Property Graph**. CGP means **Context-Generic Programming**. Validate the CPGSchema capabilities used by Aegis before relying on them for acceptance. Preserve the independence of its native Rust and JSON Schema implementations.

### 2.9. Establish semantic identity before accepting formal evidence

For Carbon, construct each obligation from the complete original test closure:

- Fixture setup and teardown.
- Constants, generated inputs, ranges, and quantification.
- Helper functions and imported assertion behavior.
- Call order, state transitions, and side effects.
- Expected values, exceptions, and failure conditions.
- Numeric widths, overflow, narrowing, NaN behavior, signed zero, and comparison semantics.
- Ordering, identity, aliasing, and lifecycle observations.
- Original tolerances and rounding rules.

Preserve fixture-qualified identities and distinct parameter/configuration occurrences.

A fixed original scenario must remain that scenario. A generalized property is a separate obligation. Neither a stronger-looking property nor an approximate numerical check replaces the original test’s semantics.

Use this evidence chain:

**Original test → semantic contract → harness representation → actual production path → verifier result.**

Each link has its own identity, review status, and evidence. A successful solver result does not establish that the original test was translated faithfully.

For Kani and Bolero:

- Select exact harnesses.
- Bind them to current production code, dependencies, toolchain, and configuration.
- Require the intended behavioral assertions and relevant reachability witnesses.
- Reject vacuity, unsupported operations, incomplete unwinding, truncation, timeout, stale inputs, or missing results.
- Account for every introduced assumption and bound.
- Keep model-only proofs distinct from production-linked proofs.
- Preserve failures and counterexamples.

Bolero’s Kani backend still invokes Kani and can impose generator restrictions. Its implementation includes explicit validity coverage and bounded byte generation, so those details must be checked against the source domain. [Bolero Kani engine](https://github.com/camshaft/bolero/blob/master/lib/bolero-kani/src/lib.rs), [Bolero Kani invocation](https://github.com/camshaft/bolero/blob/master/bin/cargo-bolero/src/kani.rs)

Classify concurrency-focused tests from their actual assertions and dependencies. Keep mixed domain/concurrency responsibilities visible; classification cannot be used to evade difficult domain obligations.

For Python, leave backend selection explicitly pending until the promised report arrives. The selection gate must evaluate production-source linkage, supported Python semantics, assumptions, trust boundaries, reproducibility, counterexamples, and evidence strength. Select complementary tools where appropriate. A backend that provides bounded bug finding must not be relabeled as unrestricted proof.

### 2.10. Provide lossless knowledge access and specialized skills

Preserve original book/document bytes, editions, licenses, hashes, attachments, diagrams, code, formulas, and source locations. Retain extraction-loss reports and a route back to the original representation.

“Zero information loss” means complete retained source material and recoverable access. A small skill entry point is not a lossless replacement for a book, and bounded retrieval does not establish that every fact was considered.

Start with deterministic exact retrieval and version-aware routing. Add more retrieval infrastructure only when measured retrieval failures justify it.

Provide focused skills for:

- Roadmap execution and native Goal/Plan reconciliation.
- Source inventory and canonical correspondence.
- Original-test discovery and execution.
- Exact test-to-harness translation.
- Kani and Bolero evidence interpretation.
- Python verification, after backend selection.
- Bevy state and scheduling.
- PyO3 exposure, ownership, and interpreter lifetime.
- Numeric and serialization fidelity.
- CGP and macro design.
- Human proof review.
- Evidence finalization, recovery, and cost control.
- Generic review and flaw documentation.
- Python-to-Rust migration mapping.

Cover every named book/manual in the guidance, plus the relevant supplied references. Record a disposition for every research recommendation rather than silently adopting or omitting it.

Package skills with pinned source references, declared tools, executable helpers, and validation cases. Use progressive disclosure through native Codex skill support. [OpenAI skill packaging guidance](https://developers.openai.com/plugins/build/skills)

### 2.11. Add a controlled macro ecosystem

Create a versioned registry of approved macro and generator capabilities covering existing Genco generation, `derive-deftly`, CGP, Arcane, and actual attribute/derive/delegation implementations.

Record inputs, expansion provenance, ownership, diagnostics, reproducibility, and proof impact.

Use `proc_macro2` as token-stream infrastructure. Attribute and derive entry points use Rust’s procedural macro mechanisms; delegation requires a concrete implementation or selected crate.

Maintain one owner for generated regions. Fix their rules or generators and regenerate. Conversion to handwritten ownership requires an explicit ownership record and protection against later overwrite.

Macros remain optional during initial development. Existing useful machinery stays available without forcing a speculative framework migration.

### 2.12. Build human supervision and the deferred review pipeline

Produce review packets that show, together:

- Original test and fixture source.
- Exact semantic contract.
- Generated or maintained harness.
- Production functions reached.
- Assumptions, bounds, and unsupported features.
- Assertions and reachability results.
- Counterexamples and original-test outcomes.
- Changes since the last reviewed candidate.

Group identical unchanged obligations and prioritize semantic changes. Review reuse requires identical relevant inputs.

Human decisions must be scoped: approving a translation, accepting a classification, requesting repair, or resolving a specific verification limitation. A review action cannot turn an unsuccessful verifier result into a proof.

Provide deterministic HTML/JSON review packets and a stable review-service interface first. Keep frontend-generator selection open for the forthcoming research. Optional tracing and Tracy integration may enrich diagnosis without becoming a performance-verification prerequisite.

Build the aggressive review pipeline as sequential, bounded stages:

**Input classification → requirement extraction → evidence inspection → challenge review → finding adjudication → deduplication → report.**

Support code, prompts, roadmaps, and other declared inputs. Findings require concrete evidence locations, violated requirements, impact, confidence, and repair guidance. Distinguish confirmed findings from hypotheses.

Validate this machinery with Aegis-owned fixtures. Actual Carbon/Aegis flaw-analysis campaigns remain deferred.

### 2.13. Use Dagger, GitLab, and reproducible releases

Define one set of pinned Dagger recipes for local and CI execution. Use the Python SDK where it best fits the hybrid implementation. [Dagger Python SDK](https://docs.dagger.io/reference/sdks/python/)

GitLab runs those recipes, retains evidence artifacts, and serializes state-changing integration jobs. GitLab resource groups supplement Aegis’s workspace-wide lease; they do not replace it. [GitLab resource groups](https://docs.gitlab.com/ci/resource_groups/)

Maintain exact relationships between source, build outputs, installed artifacts, tests, proofs, packages, and integrated remote commits.

Use stacked development changes based on Aegis `dev`, integrating into `dev`. Blue and Destiny integrate into their respective Rust development branches. Preserve all `main` branches and the original BlueExposure repository.

Deploy Aegis as a versioned `.agents` package. Keep runtime state in `.aegis`. Use the last accepted Aegis release to evaluate candidate Aegis changes so a candidate cannot approve itself by modifying its own acceptance rules.

Generate final architecture descriptions from actual code and accepted evidence, using CPG-derived views and ISO/IEC/IEEE 42010:2022 requirements. Preserve stakeholder concerns, viewpoints, relationships, decisions, and known limitations. `archstandard` and `ea-skills` are implementation resources; conformance claims require their own substantiation. [ISO/IEC/IEEE 42010:2022](https://www.iso.org/standard/74393.html)

---

## 3. The three milestone roadmaps

Each row becomes a separate milestone Markdown file with the executable contract described above. The tables define minimum scope; the complete source inventory and requirement matrix remain authoritative.

### Aegis roadmap

| ID | Milestone | Required result and exit gate |
|---|---|---|
| **A00** | Authority, branch inventory, and preservation | Reconcile current guidance, user amendments, prompts, research inputs, existing queues, branch variants, and dirty work. Produce complete requirement coverage and component reuse decisions. |
| **A01** | Policy transition and roadmap compiler | Implement phase-aware policies and compile all three roadmaps. Reject contradictory gates and missing requirements. Archive superseded policies while preserving historical evidence. |
| **A02** | Modular hybrid controller | Separate policy, execution, evidence, project profiles, source analysis, and verification interfaces. Preserve working CLI compatibility and recovery behavior. Establish Python/Rust boundary records. |
| **A03** | Durable execution, deduplication, and budgets | Enforce the single-agent lease, writer ownership, pre-launch reservations, persistent retries, operation recovery, semantic work identities, and freshness-aware reuse. |
| **A04** | Native Codex integration | Implement supported Goal/Plan bindings, reasoning enforcement, capability discovery, usage observations, user steering, interruption, and terminal reconciliation. Demonstrate the real Codex path. |
| **A05** | Source inventory and correspondence | Generalize the existing Destiny specialization into Aegis, Blue, and Destiny profiles. Preserve complete test identities and reconcile source/target graphs. Validate consumed CPGSchema capabilities. |
| **A06** | Knowledge corpus and skills | Ingest all required sources without discarding originals. Implement exact retrieval, version routing, source maps, skill packaging, and context budgets. Every named source has an explicit ingestion status. |
| **A07** | Macro and generation support | Integrate approved existing macro/generator tools through reproducible recipes. Enforce expansion provenance, generated-region ownership, and source-name preservation. |
| **A08** | Rust verification infrastructure | Implement exact Kani execution, Bolero/Kani routing, semantic-identity records, production linkage, reachability checks, counterexample retention, and truthful proof classification. |
| **A09** | Python verification integration | Consume the forthcoming report, select appropriate backends, qualify them against actual Aegis Python semantics, and implement the shared evidence interface. Unsupported obligations retain a human-intervention path. |
| **A10** | Human proof supervision | Deliver review packets and decision workflows for original tests, semantic translations, Kani/Bolero harnesses, and Python verification. Approval reuse and invalidation must work. |
| **A11** | Generic review and flaw-documentation engine | Deliver the Markdown procedures and executable sequential pipeline. Validate evidence attribution, deduplication, disagreement handling, and findings on controlled fixtures. |
| **A12** | CI, deployment, and self-development | Integrate Dagger/GitLab, stacked changes, artifact verification, `.agents` packaging, deployment rollback, and last-accepted-release governance. |
| **A13** | Aegis domain verification and completion | Verify Aegis’s policy, budget, work-state, evidence, correspondence, and completion rules using the appropriate language backends. Complete actual integration tests, portability mappings, documentation, and publication. |
| **A14** | Pervasive CGP modernization | Open only after all three projects are `PROJECT_COMPLETE`. Refactor appropriate Rust boundaries and implementations into pervasive CGP while preserving public contracts and revalidating affected evidence. |

Aegis’s designed proof obligations must cover at least:

- A milestone cannot complete with a missing required obligation.
- Implementation status cannot substitute for verification evidence.
- A scope change cannot silently remove required source responsibilities.
- Duplicate work cannot consume a second reservation without a distinct authorized operation.
- Restart cannot refund consumed attempts or erase failures.
- Evidence reuse requires the complete relevant input identity.
- A stale review cannot authorize changed semantics.
- A many-to-one canonical mapping cannot pass correspondence.
- An unsupported backend result cannot become a proof.
- A rejected or unknown native transition cannot become confirmed completion.
- An unauthorized policy downgrade cannot enable execution.
- A future CGP milestone cannot start before the three-project completion barrier.

Keep runtime and concurrency tests for locking, process recovery, atomic updates, and transport behavior. Formal domain proofs must accurately state their boundaries.

### Carbon Blue roadmap

| ID | Milestone | Required result and exit gate |
|---|---|---|
| **B00** | Source authority and full inventory | Pin Blue and imported BlueExposure references, licenses, configurations, original tests, and consumed external contracts. Reconcile existing implementation and records without replacing them. |
| **B01** | Unified build and early feasibility | Establish the Blue-rooted workspace and supported native, extension, embedding, and C++ test-adapter routes. Resolve synchronous tasklet strategy, interpreter lifetime, discovery anomalies, and Linux test applicability before dependent expansion. |
| **B02** | Complete canonical vertical path | Implement construction → registration/root identity → interface/base view → state mutation → real Bevy execution → Python observation → destruction. Use one runtime and authoritative state. |
| **B03** | Object model, exposure, and lifetime | Complete type discovery, interfaces, inheritance views, overrides, properties, conversions, wrapper identity, copying, strong/weak references, GC, logical deletion, and finalization. Reuse maintained PyO3 mechanisms. |
| **B04** | Scheduling, time, events, and task context | Complete clocks, pumps, timers, synchronous tasklets, suspension/resumption, task-local context, ordered events, callbacks, reentrancy, cancellation, and shutdown. Preserve synchronous return-time guarantees. |
| **B05** | Streams, paths, and external I/O | Complete memory/file/network/remote streams, path behavior, external providers, error handling, and source-defined ordering. Preserve portable behavior inside platform-oriented code. |
| **B06** | Resources, persistence, and structured data | Complete resource identity, loading, caches, background work, ownership, marshaling, black/dictionary/YAML formats, structured rows, and every source-defined serialization configuration. |
| **B07** | Remaining production closure | Complete statistics, accumulators, logging, diagnostics, process/OS interfaces, private helpers, unused required bodies, macro variants, and all residual inventory obligations. |
| **B08** | Integrated implementation acceptance | Compile actual production artifacts, install candidate packages, verify loaded identities and free-threaded runtime state, and pass complete applicable unchanged Blue/BlueExposure tests. Reach `IMPLEMENTATION_READY`. |
| **B09** | Exact domain verification | Close the original-test-to-harness identity chain and verify every required domain obligation with Kani or Bolero/Kani. Resolve unsupported domain semantics with a human engineer. Retain original-test evidence for concurrency-focused obligations. |
| **B10** | Final acceptance, documentation, and publication | Reconcile all original Blue acceptance predicates plus the new domain-proof gate against one candidate. Complete architecture descriptions, packages, remote integration, and native Goal closure. |
| **B11** | Pervasive CGP modernization | After the global barrier, introduce CGP behind canonical Blue contracts and state ownership. Re-run affected original tests, domain proofs, integration, and packaging checks. |

The Blue roadmap must explicitly retain:

- Original names, declaring owners, and complete base/interface graphs.
- One Blue/BlueExposure implementation and one authoritative runtime.
- Actual free-threaded Python as the default.
- Supported parallel and reentrant calls without unsourced receiver-borrow failures.
- Original conversion, exception, callback, cancellation, and partial-effect behavior.
- Source-compatible synchronous APIs.
- Maintained production macros and direct PyO3 reuse.
- Real installed artifacts, with no original C++ production-runtime dependency.
- The finite newest-stable Bevy selection and final recheck policy.

### Carbon Destiny roadmap

| ID | Milestone | Required result and exit gate |
|---|---|---|
| **D00** | Authority and existing-work reconciliation | Reuse the current queue, continuation, source rules, generators, and receipts. Revalidate the adopted source and complete denominator instead of hardcoding historical catalog totals. |
| **D01** | Current Blue and shared-runtime integration | Establish the real Python → current Blue → canonical Destiny → shared Bevy route. Align dependency versions and extension composition. Route missing Blue capabilities into bounded Blue-owned changes. |
| **D02** | Canonical objects and lifecycle | Complete world/ballpark construction, factories, registration, identity, membership, lookup, methods, fields, interface/base views, destruction, and independent world scopes. Preserve `Ball`, `Partitionable`, `IBall`, `INotify`, `Ballpark`, and reference-point relationships. |
| **D03** | Numeric state, time, and geometry | Complete old/new linear and angular state, precision/narrowing, interpolation, acceleration/damping ownership, step order, transforms, shapes, radii/bounds, and geometry queries. |
| **D04** | Forces, collisions, and spatial organization | Complete force/torque accumulation, integration, mass/inertia, collision detection/response, filters, contacts, partitions, boxes, bubbles, and spatial membership/query behavior. |
| **D05** | Movement modes and transitions | Complete every source-defined movement mode and variant, including goto, follow, stop, warp, orbit, missile, formation, boid, mushroom, troll, field, rigid, and miniball behavior where present in the selected source. Preserve eligibility, targets, timeouts, and transition effects. |
| **D06** | Visibility, proximity, and notifications | Complete cloaking, relevance, proximity, subscriptions, entrance/exit notifications, subscriber order, nested dispatch, callback mutation, reentrancy, and source-defined errors. |
| **D07** | Mutation, persistence, and temporal behavior | Complete canonical setters/actions/queries, immediate/deferred visibility, batching, snapshots, restore, streams, history, corrections, replay, identity restoration, and format variants. |
| **D08** | Client/server and host closure | Complete authority, synchronization, relevance, batching, sequencing, wire behavior, Blue service consumption, task context, resources, errors, cancellation, and shutdown across the integrated runtime. |
| **D09** | Complete implementation acceptance | Close every required source/configuration obligation. Compile and package the integrated candidate, run complete applicable original suites against installed artifacts, and reconcile actual loaded Blue/Destiny identities. Reach `IMPLEMENTATION_READY`. |
| **D10** | Exact domain verification | Verify all required original-test-equivalent domain obligations, including their fixture and numerical semantics. Use Kani, then suitable Bolero/Kani representations; route remaining limitations to human engineering intervention. |
| **D11** | Final acceptance and publication | Reconcile all Destiny acceptance predicates plus the domain-proof gate, final dependency observations, architecture documentation, package evidence, and remote integration. Complete the native objective only after operational closure. |
| **D12** | Pervasive CGP modernization | After the global barrier, refactor implementation dependencies and reusable behavior into CGP while retaining canonical source owners, state authority, identity, and exact semantics. Revalidate affected acceptance evidence. |

Generic Bevy, Avian, Lightyear, Replicon, or other facilities may supply suitable mechanisms. Each retained Destiny responsibility still requires its own correspondence and behavior evidence. A standalone world engine remains useful, but it does not replace the required integrated production path.

---

## 4. Dependency order, policy retirement, and adoption

### Cross-project execution order

Use capability dependencies so one project does not wait unnecessarily for another project’s entire completion.

1. Complete **A00–A03** to establish policy, executable milestones, preservation, and durable work control.
2. Establish **A04–A05** and begin **B00–B02**.
3. Start **D00–D02** once the exact consumed Blue capabilities are available.
4. Complete Blue and Destiny subsystem work in dependency-ready batches, with one active agent.
5. Develop Aegis skills, macros, review, verification, and CI capabilities when they reduce upcoming repeated work.
6. Close initial implementation acceptance before allowing comprehensive proof closure to dominate the remaining schedule.
7. Complete Aegis, Blue, and Destiny domain-verification and final-acceptance milestones.
8. Open the pervasive-CGP phase only when all three current completion receipts are valid.

The Python verification report is a required input to **A09**. Its absence blocks dependent Python proof completion, not unrelated implementation. Frontend-generator research is an optional renderer-selection input; usable review packets and decision records do not depend on it.

For Aegis, later CGP adoption applies to its Rust implementations and component boundaries. Retained Python remains explicitly Python. A future complete Rust migration requires its own accepted semantic-correspondence evidence.

### Retire conflicting active policies

Replace these active mandates with phase-aware rules:

- Mandatory formal verification before ordinary Carbon implementation.
- Mandatory Verus refinement or a universal verifier stack for every project.
- Automatic concurrency, performance, fuzzing, differential, mutation, or benchmark campaigns.
- Immediate pervasive CGP and blanket prohibition of handwritten production code.
- Fixed historical test counts as the current source denominator.
- Marker coverage or model-only proofs as production-completion evidence.
- A reasoning preference fragment being treated as effective enforcement.
- Destiny-specific controller assumptions being treated as universal Aegis policy.

Retain the useful verifiers, parsers, source mappings, historical proofs, failures, and receipts. Historical evidence remains scoped to the policy and inputs under which it was produced.

Current user-authorized formal work must not repeatedly request permission merely because the preserved V2 prompts originally prohibited automatic new campaigns. Additional behavior changes, semantic test changes, and unresolved domain limitations still require their exact applicable decisions.

### Adoption and release discipline

- Preserve the supplied prompts and root guidance; record effective amendments explicitly.
- Revalidate existing active work before adopting a new roadmap contract.
- Keep one canonical queue and writer per project.
- Migrate schemas transactionally and retain rollback data.
- Bind reviews and validation to the tested candidate and integrated remote content.
- Keep `.agents` deployment distinct from Aegis source development.
- Report local commits, published commits, integrated changes, deployed governance, and visible-checkout state separately.
- Generate final as-built documentation after implementation and verification; maintain design decisions during development.

---

## 5. Validation and completion criteria

### Validate the roadmap package itself

The roadmap-authoring work is complete only when:

- All three roadmap directories contain their complete milestone sequences.
- Every current root requirement, Blue requirement and acceptance predicate, Destiny requirement and acceptance predicate, and conversation amendment has an explicit disposition.
- Every relevant research recommendation has a recorded reuse, adoption, deferment, or exclusion decision.
- The cross-project dependency graph compiles without cycles or missing references.
- Implementation, domain verification, project completion, and CGP modernization remain distinct.
- Deferred flaw analysis is not accidentally scheduled as current work.
- The Codex-only restriction is enforced throughout.
- Python verification selection is visibly dependent on the forthcoming report.
- Each milestone has concrete outputs, verification obligations, allowed scope, recovery, and acceptance conditions.
- Generated roadmap artifacts are deterministic.
- Native Goal launchers reference the complete intended objectives without activating them.
- No future implementation, unexecuted proof, or unavailable capability is represented as already complete.

### Validate Aegis’s enforcement mechanisms

Include positive and negative scenarios for:

- Missing or duplicated source entities and target owners.
- Missing fixtures, duplicate test names, and configuration-specific occurrences.
- Weakened assertions, changed tolerances, omitted teardown, altered quantification, and narrowed input domains.
- Vacuous, stale, truncated, interrupted, or model-only proof results.
- Changed generators, dependencies, production bodies, and installed artifacts.
- Native Goal replacement, accounting reset, pause/clear handling, and ambiguous completion responses.
- Plan-mode writes and unapproved scope expansion.
- Reasoning downgrade or unavailable effective configuration.
- Duplicate dispatch, interrupted reservations, stale leases, and recovery after partial writes.
- Lost, duplicated, cumulative, or unavailable usage observations.
- Stale human approval and approvals applied outside their scope.
- Retrieved instructions attempting to alter policy.
- Missing corpus material, damaged extraction, incorrect citations, and version mismatch.
- Python blocks missing Rust migration documentation.
- CI success attributed to the wrong tree or package.
- Early activation of the CGP modernization phase.

Formal checks address the declared domain rules. Existing and necessary runtime tests address actual filesystem, process, transport, concurrency, and integration behavior.

### Validate Carbon completion

For both Blue and Destiny, require one coherent accepted candidate containing:

- Complete required source/body/configuration coverage.
- Current bidirectional object and relationship correspondence.
- Actual implementation of every required responsibility.
- Successful production builds.
- Correct installed and loaded artifact identities.
- Complete applicable original-test execution.
- Accepted semantic identity between required original domain tests and their harnesses.
- Successful current production-linked domain verification.
- Explicit original-test acceptance for concurrency-focused obligations.
- No unresolved required human decision.
- Reproducible packages and source-backed portability boundaries.
- Accurate architecture descriptions.
- Verified publication and canonical-record closure.

Report evidence at its actual strength: source review, structural reconciliation, compilation, original-test execution, reviewed translation identity, mechanically established properties, packaging, and publication. None may silently substitute for another.

The result is three complete execution contracts supported by reusable machinery, with implementation progress preserved, final domain correctness enforced, and future CGP and Rust evolution bounded by explicit evidence.
