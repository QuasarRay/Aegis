# Architecture and decision record

This package implements a compiler and supporting enforcement primitives for three maintained roadmaps. It does not establish that Aegis, Blue or Destiny has reached a product completion state. The 40 milestone contracts define that later work. The preserved prompts and root guidance remain source authorities; [the adopted plan](ADOPTED_PLAN.md) and [policy amendments](policy.json) resolve conflicts explicitly.

## Authority and state ownership

The authority chain is: current user authorization → adopted amendments → preserved project requirements → validated milestone contract → named recipe → current evidence. Retrieved documents, book text, example commands, Markdown checkboxes and model assertions have no authority to change this chain. Reading a contract does not activate it.

Markdown owns milestone design. `requirements.json` owns the source-to-milestone disposition index. `policy.json` owns the effective amendment set. `registry.json` owns project identities and named recipes. Existing project queues own runtime progress. A compiled graph, audit, dashboard or work packet is a reproducible projection, never a second acceptance authority. Changed inputs invalidate dependent projections and receipts.

```mermaid
flowchart TD
  Authorities[Preserved sources and user amendments] --> Contracts[40 Markdown contracts]
  Contracts --> Compiler[Strict compiler and dependency graph]
  Compiler --> Packet[Bounded source-owned work packet]
  Packet --> Gate[Authorization, native state, reasoning, lease, budget]
  Gate --> Codex[One Codex execution owner]
  Gate --> Tools[Named bounded deterministic tools]
  Codex --> Artifacts[Actual production artifacts]
  Tools --> Artifacts
  Artifacts --> Evidence[Source-bound evidence and scoped review]
  Evidence --> Records[Existing canonical project records]
  Records --> Audit[Recompute exact completion predicate]
  Audit --> Native[Reconcile native Goal and Plan]
```

## ADR-01 — Hybrid boundaries

Keep typed Python for policy compilation, transport orchestration, extraction coordination, knowledge access, schema validation and project-record integration where existing facilities are reliable. Reuse `atomic`, `transaction`, `locks`, `process`, `security`, `context_cache`, catalog and evidence modules. Choose Rust for source analysis, macro generation, portable production kernels or interfaces when the actual capability and verification support justify it. Do not introduce a Rust kernel solely to claim safety.

Every maintained Python file and behavioral block receives a source/AST-bound migration proposal. Its Rust counterpart must preserve arbitrary-precision integer semantics unless bounds justify narrowing; float/NaN/signed-zero behavior, insertion order, aliasing, exceptions, cleanup and partial effects remain explicit. Shared templates describe equivalent patterns, but every AST entry resolves its own source, inputs, outputs, calls and target module. Proposed mappings are not completed Rust implementations or accepted equivalence proofs. Semantic refinement and reviewer acceptance remain visible future obligations.

## ADR-02 — Finite records and compatibility

The eleven shared record types are specified in `records.schema.json`. Unknown versions, fields, required values and unsupported schema vocabulary fail explicitly. The validator intentionally implements a finite vocabulary; it is not advertised as a complete JSON Schema implementation. Cross-language serialization uses canonical UTF-8 JSON, ordered keys, no duplicate keys and no nonfinite JSON numbers. Preserve original numeric domains with explicit tagged representations where JSON would lose identity.

`agentctl` retains its legacy Destiny dispatch for existing command families. New command families select the roadmap compiler and supporting tools. Never reinterpret old evidence under new semantics without a lineage record. Schema migrations use `FileTransaction`, expected old hashes, rollback journals and retained originals; consumed budgets and prior decisions must survive migration.

| Record | Producer → consumer | Invalidation boundary |
|---|---|---|
| ProjectProfile | adopted project authority → compiler/executor | source/branch/queue/policy change |
| MilestoneContract | maintained Markdown → compiler | any contract or amendment change |
| WorkUnit | compiler → sequential executor | source, responsibility, recipe or writer change |
| CapabilitySnapshot | actual host/transport → dispatch policy | version/model/configuration/session change |
| GoalBinding | native observation → objective reconciliation | chat/objective/contract lineage change |
| PlanBinding | completed native plan item → scope mapping | plan version or compiled scope change |
| EvidenceReceipt | named producer → acceptance audit | any relevant semantic input/artifact/tool change |
| ProofObligation | original test or Aegis rule → verifier | test closure, harness, production path or assumptions change |
| ReviewDecision | human decision → scoped acceptance | changed relevant packet content or decision scope |
| BudgetReservation | pre-dispatch accounting → runner/recovery | never silently refunded by restart |
| PythonRustCorrespondence | maintained AST → future migration | source/AST digest or proposed semantics change |

## ADR-03 — Execution and cost ownership

There is one active agent across the coordinated workspace. A workspace execution lease carries a monotonically increasing fencing generation, owner session and verified process creation identity. A live owner, unknown process state or ambiguous disconnect prohibits takeover. The parent becomes idle before specialist handoff; sequential review does not permit overlapping inference. Filesystem locks alone cannot establish that a remote/native model turn stopped, so native operation handles must also be reconciled.

Before dispatch, reserve resources using the full work identity: source, target, contract, operation, toolchain and configuration. Persist successful, failed and interrupted attempts. Inspect existing handles before restart. Require diagnosis and relevant correction before a failed retry. Keep input/cached-input/output/reasoning tokens, tool time, CI time and storage distinct when observed; unavailable fields remain unknown. Deduplicate cumulative native events without summing snapshots as increments. Prices and estimates are separate from observed usage and actual billing. A requested monetary cap with insufficient accounting blocks dependent dispatch pending a concrete budget decision. Do not invent a native token budget.

The package's fixed validation runner executes no model inference. Its ledger and local recipe lock are tested primitives; A03 adds the full coordinated native-session lease qualification. Do not infer workspace-wide model exclusivity from a local subprocess lock.

## ADR-04 — Native Codex adapter

Codex is the only provider. Active-host integration consumes the current supported lifecycle tools and observations. Managed integration uses the documented app-server protocol, discovered from the installed executable. Pin protocol version, executable identity, method schemas and model capabilities before accepting dispatch. The included read-only transport exercises initialization and model discovery without creating chats or starting model turns. Goal/Plan binding and transition preparation preserve objective identity and accounting; native mutation remains subject to the current host's authorization rules.

`thread/goal/get`, `thread/goal/set` and `thread/goal/clear` are documented app-server operations. Plan integration consumes completed plan items and `turn/plan/updated`; collaboration Plan mode forbids production mutation. Do not assume a universal plan-write API. Native state is authoritative for pause, clear, limits and blocked thresholds. Completing a milestone does not complete the whole objective. An ambiguous completion call remains unconfirmed until native state is read back.

Requested reasoning is `max`. Record requested, accepted and observed effective settings separately. A configuration default or model catalog entry is not effective enforcement. Preserve the selected model; refuse unauthorized effort downgrade or model rerouting. If required effort cannot be established, stop new managed dispatch and report the unsupported capability. No private chain-of-thought is required: record facts, assumptions, alternatives, decisions, expected evidence and unresolved questions.

Primary protocol and configuration references: [app-server](https://learn.chatgpt.com/docs/app-server), [configuration](https://learn.chatgpt.com/docs/config-file/config-reference). Installed capabilities may differ; live discovery controls execution.

## ADR-05 — Source identity, macros and runtime authority

Required source closure includes production files, private/unused bodies, original tests, fixtures, templates, macros, conditional configurations, registration, Python exposure and consumed external contracts. Exactly one canonical target group belongs to exactly one source owner. A trait/struct/enum/impl aggregate is one traceable source-owned representation, not a loophole for combining unrelated owners. Member responsibility, declaring owner, state owner, interface/base/override/dispatch and lifecycle relationships all reconcile against actual declarations and expansions.

Rust and Python type graphs are separate views of the same logical instances. Blue and Destiny use one authoritative Blue/shared-Bevy runtime. Generic Bevy, Avian, Lightyear or Replicon mechanisms do not replace source responsibilities. Direct maintained PyO3 reuse avoids duplicating generic binding infrastructure. Synchronous APIs preserve return-time visibility, callback order, cancellation and partial effects, including free-threaded and reentrant callers.

CPG is Code Property Graph. CGP is Context-Generic Programming. Qualify CPGSchema capabilities before acceptance; preserve independent native Rust and JSON Schema implementations. Macro capability records cover Genco, derive-deftly, CGP, Arcane and concrete procedural macro implementations. `proc_macro2` is token-stream infrastructure. Every generated region has one owner: change rules and regenerate; conversion to handwritten ownership requires a record and overwrite protection.

## ADR-06 — Phase-aware verification

Implementation milestones use source correspondence, production compilation and applicable unchanged original tests. Early formal work is permitted for a concrete uncertainty or expected effort reduction; it is not a universal prerequisite. Domain verification is mandatory for final Carbon completion. Kani is the first Rust route; Bolero/Kani is appropriate only when its generator representation preserves the original domain. Aegis Python tools are selected from the supplied report and qualified against actual maintained Python semantics. See [verification](VERIFICATION.md).

Keep `IMPLEMENTATION_READY`, `DOMAIN_VERIFIED`, `PROJECT_COMPLETE` and `CGP_MODERNIZATION_COMPLETE` separate. A full objective containing proof cannot be completed at implementation readiness. Domain evidence, original concurrency-test evidence, packaging and publication are distinct channels. Pervasive CGP opens only when all three current initial completion receipts pass. Retained Python remains Python.

## ADR-07 — Knowledge and skills

Retain raw source bytes, hashes, editions, licenses, attachments, diagrams, formulas and source locations. Exact text retrieval with version routing is the baseline. Extraction loss stays recorded and the original remains recoverable. Missing books or unqualified extraction cannot be called lossless ingestion. Focused native skills provide progressive disclosure, pinned references, declared helpers and validation cases; they do not claim to replace an entire book. Research recommendations each receive adoption/reuse, conditional experiment, deferment or exclusion with rationale. Popularity is not correctness evidence.

LangGraph, LangChain, Unpythonic, RAG infrastructure, databases and distributed workflow services require an unmet capability, bounded comparison and evidence of lower total risk. Keep orchestration-framework selection separate from the native Codex lifecycle. Other providers are excluded.

## ADR-08 — Review, release and self-development

Deterministic HTML/JSON packets show original tests, fixtures, semantic contracts, harnesses, production paths, assumptions, bounds, assertions, covers, failures, changes and original-test outcomes together. Scope human decisions to translation/classification, repair or a named limitation. Exact inputs determine freshness. Human approval cannot manufacture verifier success. Frontend research and optional tracing/Tracy enrich this interface without blocking it.

The generic review pipeline is sequential: classify → requirements → inspect → challenge → adjudicate → deduplicate → report. Confirmed findings require concrete evidence, violated requirement, impact, confidence and repair. Hypotheses remain hypotheses. Validate with owned fixtures; do not start a project flaw campaign without separate authorization.

Dagger recipes are shared by local and GitLab execution. Pin engine/SDK/image/tool identities and retain output evidence. GitLab resource groups supplement the workspace lease. Use stacked dev-based changes and preserve main and original BlueExposure. `.agents` is a versioned deployed package; `.aegis` is mutable runtime state. A last accepted release evaluates candidate policy changes so the candidate cannot accept itself. Source, build, installation, tests, proofs, packages and integrated remote commits must form one current identity chain.

## ADR-09 — As-built architecture

Design decisions exist throughout development. Final architecture views are generated from actual accepted code/evidence and qualified CPG-derived views. Preserve stakeholders and concerns, viewpoints and model kinds, relationships, decisions, rationale and known limitations. ISO/IEC/IEEE 42010:2022 alignment requires substantiated coverage; using `archstandard` or `ea-skills` alone is not conformance. Linux acceptance is complete; Windows/macOS remain explicit future acceptance obligations with portable-core boundaries and adapter mappings.

## ADR-10 — Compatibility and policy retirement

The old Destiny controller and its proofs/parsers remain available under their original commands and evidence lineage. They no longer define universal Aegis policy. Retire mandatory proof-before-implementation, mandatory Verus refinement/universal stacks, automatic fuzz/differential/mutation/benchmark/performance/concurrency campaigns, immediate pervasive CGP, blanket bans on handwritten code, fixed historical denominators, marker/model-only completion credit and configuration-fragment reasoning claims. Retain useful historical proofs, failures and tools, with their original scope. New work uses explicit amended phase rules; authorized formal work does not repeatedly ask permission solely because an old prompt forbade automatic campaigns.
