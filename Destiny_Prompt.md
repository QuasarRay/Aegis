# Destiny Rust Reimplementation — Integrated Codex Goal Contract V2

Version: 2. Authoring date: 2026-11-02, Australia/Melbourne.

This is the self-contained execution contract for completing Carbon Engine's Destiny in Rust on Bevy, integrated with the current Blue and BlueExposure Rust implementation. It includes the objective, source and naming rules, implementation sequence, evidence requirements, acceptance predicates, and a Goal launcher. The companion [authoring audit](/home/astral/Projects/destiny/DESTINY_RS_REIMPLEMENTATION_PROMPT_V2_COVERAGE.md) traces the supplied guidance and Blue V2 requirements; execution does not depend on reopening the Blue example.

**Every required Destiny-specific source entity and responsibility MUST have exactly one canonical Rust counterpart. Correspondence MUST be simultaneously behavioral, structural, and nominal. Source names, declaring owners, object identity, state ownership, interface and concrete-base relationships, dispatch, lifecycle, and complete behavior must survive the migration. A matching name, empty wrapper, registry entry, successful build, passing subset of tests, or partial world engine is not completion.**

**The objective is complete Linux acceptance of the required Destiny implementation, including actual Python → blue-rs → Destiny → Bevy execution. Intermediate batches are checkpoints of that objective. They cannot complete it.**

## Contents

- [1. Authority, adopted decisions, and preservation](#authority)
- [2. Native Goal lifecycle and contract binding](#goals)
- [3. Source authority, complete inventory, and finite dependency boundary](#sources)
- [4. Canonical correspondence and public contracts](#correspondence)
- [5. Current Blue, BlueExposure, and Python exposure](#blue)
- [6. Bevy execution, state, and scheduling](#bevy)
- [7. Concurrent Python, reentrancy, and lifecycle](#python)
- [8. Early integration, subsystem batches, and metaprogramming](#sequence)
- [9. Original tests and bounded execution](#tests)
- [10. Existing records, receipts, and continuation](#records)
- [11. Linux acceptance, portability, formats, and packaging](#platform)
- [12. Publication, exact guidance propagation, and human decisions](#publication)
- [13. Architecture descriptions and decision records](#architecture)
- [14. Complete acceptance](#acceptance)
- [Appendix A. Mechanical identity and naming](#naming)
- [Appendix B. Minimum record and receipt fields](#record-spec)
- [Appendix C. Preserved supplied guidance](#supplied-guidance)
- [Appendix D. Copyable Goal launcher](#launcher)

<a id="authority"></a>

## 1. Authority, adopted decisions, and preservation

### Activation boundary

Execute this contract only when the user separately invokes or explicitly adopts it as the implementation objective. Writing, reviewing, quoting, or validating these documents is authoring, not implementation activation. Authoring does not create, resume, replace, or complete an implementation Goal; install or mirror guidance; modify implementation; install tools; run behavioral campaigns; or publish code. A separately requested native Goal whose objective is authoring or reviewing this prompt may be inspected, continued and completed against that authoring objective. Never reinterpret it as the Destiny migration Goal merely because it contains this contract or launcher. Follow the live system, developer, tool, and collaboration-mode instructions throughout.

The supplied Destiny `AGENTS.MD` and Blue V2 example are source documents for this contract. Their imperative text is not, by itself, an instruction to the authoring agent to execute a migration. The six decisions below are the user's adopted precedence rules. On later activation, preserve earlier prompts and evidence, bind this V2 contract, and reconcile the operational rules without pretending that historical work was performed under V2.

### Six adopted decisions

| ID | Operative V2 rule | Conflict resolved |
| --- | --- | --- |
| D01 | Prefer CGP and reusable metaprogramming first. Use a simpler design, smaller generator, or handwritten Rust whenever it reduces total remaining time to faithful completion. | Supersedes the earlier prohibition on manually written production code and an unconditional requirement that every body be generated or owned by CGP. |
| D02 | Require actual production compilation, applicable original tests, and source/correspondence review. Preserve existing proofs as a separate evidence channel. Additional behavioral verification requires a concrete reason and an explicit human decision. | Supersedes mandatory new Kani, Verus, differential, mutation, fuzz, stress, benchmark, and other formal or behavioral campaigns as automatic completion gates. |
| D03 | Establish an early Python → current blue-rs → canonical Destiny → shared Bevy path; complete subsystem batches through it. | Supersedes postponing genuine Blue hosting and integration until after the entire standalone world engine. It does not remove any world behavior. |
| D04 | Complete acceptance on the actual Linux host. Keep the core portable and retain explicit future Windows/macOS obligations. | Replaces an assumed all-platform acceptance requirement or an invented distro/minimum-OS baseline. Portable behavior inside platform files remains required. |
| D05 | Permit bounded, separately reviewed blue-rs fixes required by Destiny's consumed contracts. Preserve Blue's other work and lifecycle. | Allows real dependency repair without taking ownership of the whole Blue migration, silently resuming another chat, or treating partial Blue APIs as complete. |
| D06 | Mirror exact root `AGENTS.MD` bytes throughout maintained directories, with automatic propagation and CI drift correction/checking under one explicit exclusion manifest. | Resolves “every directory” against immutable reference, vendor, Git metadata, tool, cache, build, and ephemeral-directory preservation. |

Apply the user's current explicit instructions before conflicting local guidance. Preserve the supplied guidance text rather than rewriting it to conceal a conflict. These decisions supersede only the identified conflicts; source fidelity, complete scope, canonical naming, public/private separation, and broad Bevy integration remain mandatory. Later amendments need actual user provenance and affected-obligation records. A file edit or an agent's preference does not authorize a new exception.

### Repositories and preserved work

| Role | Location or branch |
| --- | --- |
| Destiny implementation and records | `/home/astral/Projects/destiny` |
| Destiny remote and integration branch | `https://github.com/QuasarRay/destiny.git`, `destiny-rs-dev` |
| Current canonical Blue/BlueExposure Rust implementation | `/home/astral/Projects/blue` |
| Blue remote and integration branch | `https://github.com/QuasarRay/blue.git`, `blue-rs-dev` |
| Supplied Destiny guidance | `/home/astral/Projects/destiny agentsmd/AGENTS.MD`; exact text is embedded in [Appendix C](#supplied-guidance) |
| Historical Blue V2 example | `/home/astral/.codex/attachments/7aa0aab5-2a01-4d60-b022-76ef81d95e97/Pasted text.txt` |

At activation inspect branch, HEAD, remotes, staged/dirty/untracked changes, existing worktrees, records, and writer ownership in each repository you will touch. Preserve both `main` branches, original references/tests, earlier prompts, existing verification artifacts, immutable controller/reference material, and unrelated work. Never reset or clean the checkout to simplify the migration. Do not replace the existing queue or generation machinery merely because V2 uses different terminology. Preserve compatible implemented behavior and compliant canonical names.

<a id="goals"></a>

## 2. Native Goal lifecycle and contract binding

Use the native Goal service as lifecycle authority, following its currently exposed schemas. “Goal Plugin” in this contract refers to the actual Goal capability provided by the active Codex runtime; discover that capability rather than assuming a separately installed plugin, HTTP endpoint or repository daemon. Repository records track implementation and evidence; they are not a second Goal engine. The `/goal` launcher is a command for the Codex chat command surface, not a shell command or executable script. The [Codex Goals guide](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex) describes the user command surface; live tool instructions control agent operations.

On explicit implementation invocation, discover the current Goal capabilities and call `get_goal` before creating anything. Record the returned chat/thread identity, objective and status, adopted V2 absolute path/version/full-byte SHA-256, actual user adoption/amendments, previous contract lineage, source pins, schema version, and worktree writer. Compute the hash externally at activation; do not embed a recursive self-hash in this file. A launcher-created matching Goal is already the Goal to use.

| Live state | Action |
| --- | --- |
| No Goal, or a completed unrelated prior Goal, with explicit implementation invocation | Create the complete V2 objective naming this contract. Do not set a token budget unless the user specifies one. |
| Matching active Goal | Reuse it and its accounting. Milestones and subsystem batches are not new Goals. |
| Matching paused Goal | Preserve the pause unless the user explicitly resumes. Use the supported user/service-controlled resumption path and confirm state; do not invent `status: active`. |
| Matching blocked Goal | Inspect the exact blocker. Resume only through an authorized supported path, then restart the consecutive-blocker audit from the resumed run. |
| Matching budget-limited or usage-limited Goal | Respect the limit. Only the user/system may extend or resume it. Never replace it to reset accounting. |
| Matching completed Goal | Do not reopen work because this document was read. Require explicit direction to reopen or undertake a new objective. |
| Unrelated unfinished Goal | Preserve it, report the objective conflict, and obtain direction before adopting a different objective. Continue only independently authorized work. |
| Goal capability unavailable or state unknown | Report the actual gap, preserve the checkpoint, and use only operations supported by current instructions. Do not claim Goal activation or emulate continuation with a daemon. |

If the user clears or cancels the Goal, preserve completed work and stop pursuing that objective. Its subsequent absence is not permission to recreate it from an old checkpoint or a prior launcher invocation. A new objective requires new explicit direction. User commands such as `/goal pause`, `/goal resume` or `/goal clear`, when supported by the installed client, are not invented `update_goal` status values.

“Matching” means the same complete objective and authorized contract lineage, not a similar title. If the service cannot edit objective text, retain the actual returned objective and bind an explicitly authorized V2 amendment in the existing record. Do not invent an objective-update API. Detect contract-hash changes before relying on changed rules and preserve the prior binding.

While active, checkpoint each batch and continue dependency-ready work. Ask about a localized required decision and keep working on independent obligations. Pause only on the user's explicit request; use the supported pause operation, report its returned status, and stop Goal work. Respect budgets and hard service limits without converting unfinished work to success.

Use `blocked` only under the live tool contract: the same genuine blocker has recurred for at least three consecutive distinct Goal turns, including the original turn, and no meaningful independent work remains. Persist its fingerprint, observation turn IDs, last material change, alternatives, affected obligations, recoverable process handles, and exact unblock requirement. Polling three times in one turn is one turn. A resumed blocked Goal starts a fresh sequence. Check existing operations before relaunching or declaring an impasse. Difficulty, slowness, pending tests, or a partial milestone is not a blocker by itself.

Complete the native implementation Goal only when every applicable [acceptance predicate](#acceptance) is satisfied. Report actual tool-returned status and required final usage, including token usage for a budgeted Goal. Do not claim invisible background continuation after execution ends.

### Native capability contract

At V2 authoring, the active runtime exposes the operations below. Re-discover their exact names/schemas at activation and after a capability change. These are conditional invocation shapes for the implementation agent, not instructions to execute them when reading this file.

| Operation | Supported shape and use | Guard |
| --- | --- | --- |
| Inspect | `get_goal({})` returns the current objective/status and service-provided accounting. | Read before activation, each continuation and terminal reconciliation. A repository checkpoint cannot override it. |
| Create | `create_goal({"objective":"<complete objective naming this V2 contract>"})`; add `token_budget` only for an explicit user budget. | Only when creation is expressly authorized and no unfinished Goal exists. Do not create after a clear, at a limit, or to replace an unrelated or matching active Goal. |
| Complete | `update_goal({"status":"complete"})`. | Full current-objective completion audit passed; for migration, every applicable A01–A15 passed. A prompt-authoring Goal uses its separate authoring requirements. |
| Pause | `update_goal({"status":"paused"})`. | Explicit user pause request only; report returned status and stop Goal work. |
| Block | `update_goal({"status":"blocked"})`. | Same genuine blocker for at least three distinct consecutive Goal turns, no meaningful independent progress, and the current tool supports this status. |
| Resume, extend a limit, clear, or change objective | Use only a currently supported user/service-controlled mechanism with its actual authorization. | The exposed `update_goal` does not accept an objective, token budget, `active`, `resume`, `budget-limited`, or `clear` operation. Do not invent one or alter repository state to simulate it. |

Store returned native fields as observations, including their actual names/availability, observation time and capability identity. Keep native accounting separate from implementation counters and optional tool-trial estimates. Do not estimate credits as if they were service accounting. A new worktree, branch, compaction or milestone does not create a new Goal or reset its usage. The binding belongs to the returned chat/thread; copying files to another chat does not transfer its native lifecycle authority.

### Per-turn protocol and progress classification

At the beginning of each implementation turn or automatic continuation:

1. Inspect live Goal state, actual user steering, adopted contract hash, branch/writer ownership, committed record generation, source/dependency identities, checkpoint and the relevant queue slice. Respect pause, clear, limits and objective conflicts before substantive work.
2. Recover interrupted record transactions and inspect existing operation handles. A log, checkpoint, lock file or statement that work is running does not establish that it is currently live.
3. Classify the previous turn from evidence using the table below. Revalidate any no-progress condition, then choose the next safe dependency-ready action against the unchanged full objective. A status question is steering, not cancellation; answer it and continue unless the user actually stops or changes the objective.
4. Complete the selected batch's source-owned behavior, integrated path, authorized validation and publication work as ready. When one decision is pending, work on independent obligations. Keep D02's additional-verification boundary intact.
5. Commit actual receipts and coherent queue/checkpoint state, recording the next exact action and live handles. Continue useful work while the native Goal permits; report progress or concrete blockers without treating the report itself as implementation progress.

| Previous-turn classification | Required evidence and next action |
| --- | --- |
| `PROGRESS` | A material artifact/state change, completed obligation, or new evidence that changes the next action. A successful source review may qualify; a repeated plan or status recap does not. Record the affected IDs and evidence. |
| `VERIFIED_WAIT` | A specific operation is confirmed live now through its supported tool/session/process handle. Record operation/input identity, owning tool, handle, last observed status and finite deadline; poll that same handle. Observation timeout or transient polling failure is not terminal. |
| `NO_PROGRESS` | No material state/evidence change and no currently verified live wait. Inspect current state and choose the next available safe action. If none exists, update the durable blocker audit without manufacturing turns or retries. |

Associate process handles with the tool that issued them: an execution cell ID, shell session ID and process identity are not interchangeable. Use its documented wait/poll operation; for a raw PID, verify process start/command identity to avoid reuse mistakes. A missing/terminal handle requires current-state diagnosis and safe recovery, not a continuing “waiting” claim. A failed observation requires re-polling or another authoritative liveness check before restarting. Preserve one operation per input/run identity where appropriate and avoid duplicate execution or killing unrelated processes.

Checkpoint before compaction/handoff or an impending limit when permitted. On continuation, restore the committed state and revalidate drift-prone identities; do not restart completed work or shrink the objective to the easiest remaining subset. Native continuation is service-controlled and is not a promise of work while a turn, queued user input, pause or limit prevents it.

### Completion audit and terminal handshake

Treat completion as unproven until checked against current authoritative state. Re-derive the full requirement set from the adopted objective, contract, source obligations and actual decisions. For every requirement/deliverable/configuration/gate/invariant, identify the evidence needed and inspect that evidence at its actual scope. Classify it as satisfied, contradicted, incomplete, indirect/insufficient, or missing. Only satisfied requirements and exact authorized exceptions can pass. A green manifest, validator, test subset or completion flag is evidence only after its coverage and current inputs have been inspected; no marker proves itself.

Prepare a durable acceptance record binding the frozen candidate, all predicate results, exceptions, evidence and full objective. Re-read live Goal state and ensure that the same objective is active, permitted and still complete; if inputs or user steering changed, reconcile them before any terminal call. Do not mark complete because of a checkpoint, first generation, report, budget boundary or exhausted tool trial.

Call the supported completion operation only after that audit. On success, record the returned native status/accounting and terminal receipt in the existing record system without changing accepted production inputs. On error, timeout or ambiguous response, inspect native state before retrying: if already complete, recover the missing bookkeeping; if still active, preserve the prepared evidence and diagnose the failure; if paused, limited, cleared or changed, respect that state. Never fabricate a successful transition, recreate the Goal, reset usage, or resume substantive work merely to repair a terminal receipt.

<a id="sources"></a>

## 3. Source authority, complete inventory, and finite dependency boundary

### Authority and raw-source provenance

Original Destiny's selected C++ and Python sources define Destiny behavior and its object model. Original Blue and BlueExposure define consumed Blue semantics; current blue-rs supplies their Rust implementation. Source contracts outrank guesses based on current Rust code, a documentation title list, an old nested dependency, or a passing test subset.

Revalidate existing source manifests and chosen pins. Do not silently replace the intended original revision with a newer or easier one. Record origins, Git object/archive identities, licenses/notices, raw file digests, original/imported paths, file modes and symlinks, encodings, and configurations. Compare reference bytes to the pinned Git objects or authenticated archives. A worktree hash labeled with a revision is not proof that those bytes belong to it. Record intentional dirty overlays separately with parent, additions/modifications/deletions, digests, rationale, and authority decision. Relocation does not authorize line-ending or encoding normalization.

Inspect the current Blue source/model records in `/home/astral/Projects/blue`, including its selected original Blue and imported BlueExposure references. Revalidate their pins and resolve conflicting source ownership. `/home/astral/Projects/destiny/blue-rs` is an older nested snapshot and MUST NOT define the architectural baseline. Existing imports or lockfiles pointing at it are migration obligations, not authority. Do not duplicate Blue's canonical types or rebuild its object model locally.

Freeze each implementation candidate's dependency revision and any intentional overlay. A final installed build must resolve Blue from a reproducible pinned dependency, published package, or complete licensed/provenance-backed source snapshot, not an undocumented sibling path. A local path dependency may support development only when its complete input identity and final replacement are recorded.

### Complete source closure

Inventory all authoritative production regions, not just exports or original tests:

- Objects, structs, interfaces, aliases, namespaces, fields, properties, constants, enums, methods, overloads, constructors/destructors, operators, registrations, factories, and Python-visible contracts.
- Public, protected, private, inline, unused and indirectly invoked bodies; static initialization and teardown; macro definitions and expansions; templates, specializations, required instantiations, and generated source.
- Concrete-base/interface ancestry, declaring owners, overrides, inherited behavior, shared state, identity, reference/lifetime relationships, and callback responsibilities.
- Original Python production logic, bindings/converters, configuration/build inputs, source test definitions, fixtures/assertions/data, discovery rules, and consumed external contracts.
- Conditional/platform branches and all incompatible body variants. Preserve portable behavior even when found in a Windows-oriented file or a branch not compiled by the initial Linux configuration.

For every file/configuration, record inspected regions, declarations/definitions, body coverage, macro expansion provenance, template coverage, parse failures, unresolved symbols, and source-reviewed resolutions. Preserve raw bytes and decode with identified encodings; replacement-character decoding cannot establish closure. Duplicate declarations share an entity identity when they denote one entity, while distinct bodies, specializations, configurations and test occurrences remain distinguishable.

Use existing AST/compiler data, extracted documents, structured parsing, and targeted source review. Missing Clang-doc/Doxygen output is not missing source behavior. Documentation without bodies cannot establish implementation completeness. Close every unparsed region explicitly. Initial inventory and refinement may proceed with implementation, but unresolved regions remain in the denominator and final acceptance requires closure.

### World-simulation scope

The following is a minimum review matrix, not a substitute for the source inventory. Every source-defined variant, private helper and relationship belonging to these areas is required:

| Area | Required responsibilities |
| --- | --- |
| Object lifecycle and identity | Construction, factories/registration, ballpark membership, lookup, reference/interface views, destruction, ownership, IDs, copying, independent ballpark scopes, and logical versus physical lifetime. |
| Motion and transitions | Every source movement mode and transition, including source-defined goto, follow, stop, warp, orbit, missile, formation, boid, mushroom, troll, field, rigid and miniball behavior; eligibility, targets, timeouts, and transition side effects. Discover exact names and variants from source. |
| Linear and angular state | Old/new position, velocity, orientation, angular velocity, interpolation/extrapolation, acceleration/damping, speed limits, source precision/narrowing, and step-order dependencies. |
| Forces and collisions | Integration, force/torque accumulation, collision detection/response, filters, mass/inertia, contact effects, and source-specific interaction rules. |
| Geometry | Primitive/compound shapes, transforms, radii/bounds, miniballs, geometric queries and all source-defined shape variants. |
| Spatial organization | Partitions, boxes, bubbles, insertion/removal/movement, hierarchy, spatial queries, stable ordering and cross-boundary updates. |
| Visibility and proximity | Cloaking, visibility/relevance, proximity detection, subscriptions, entrance/exit notifications and changes caused by mutation or stepping. |
| Time and ordering | Clock units/epochs, ticks, fixed-step policy, timestamps, ordering, pause/rebase, deferred work, scheduling, and deterministic tie rules where specified. |
| Callbacks and errors | Notifications, subscriber order, reentrancy, callback mutation, partial effects, errors, invalid inputs, and lifecycle interactions. |
| State mutation and queries | Every canonical setter/action/query, validation, immediate versus deferred visibility, batching, transactional boundaries and error outcomes. |
| Persistence and temporal state | Snapshots, restore, streams, history, correction, replay, version/configuration formats, reference identity and ordering. |
| Client/server behavior | Source client/server actions, authority, relevance, synchronization, batching, sequencing, serialization and consumption of Blue services. |

Do not substitute an empty controller, state-only data model, generic physics simulation, fake callback, unconditional success, or a hidden disabled feature for any required responsibility. Standalone world behavior and Blue hosting are both required; integration ordering cannot omit mechanics.

### External closure and applicability

For every consumed external declaration, follow only the dependencies needed to supply its signatures, constants, ancestry, identity/lifetime and invoked semantics. Record the original authority and concrete provider: current Blue/BlueExposure, maintained Bevy/Rust/PyO3 facility, or a narrow Destiny adapter. Stop expanding when every consumed contract has a working provider and no unresolved transitive semantic dependency remains. This finite boundary does not require migrating all of Blue or unrelated external libraries. Inherited obligations do not disappear because their definitions live in another repository.

Track independent dimensions: role, applicability, implementation status, and evidence. Useful roles include `DESTINY_SPECIFIC`, `BLUE_PROVIDED`, `NATIVE_RUST_MECHANISM`, `BEVY_PROVIDED`, `EXTERNAL_BOUNDARY`, and `AUXILIARY`. Applicability distinguishes `REQUIRED_LINUX`, source-backed `FUTURE_PLATFORM`, exact `HUMAN_APPROVED_EXCEPTION`, and `UNRESOLVED`. None is an implementation or verification result.

Replace generic allocation, pointer bookkeeping, ABI/vtable scaffolding and undefined C++ mechanisms with native Rust facilities. Retain every attached Destiny-specific responsibility, including relevant numeric/storage/serialization contracts. A “generic” label cannot hide domain behavior. Split mixed obligations with source-owner links. A missing dependency, absent test, private declaration or unavailable parser is never a scope exclusion.

Freeze the applicability set per acceptance candidate. Scope corrections require source evidence or explicit user decisions; preserve before/after counts and invalidate affected receipts. Windows/macOS-only obligations remain visible future work. Portable sub-obligations and all required Linux configurations stay in the current denominator.

<a id="correspondence"></a>

## 4. Canonical correspondence and public contracts

### Defined bijection

Let `S` be the complete set of required Destiny-specific logical source entities after documented declaration deduplication and allowed mechanism classification. Let `R` be their canonical Rust counterparts. Establish an auditable bijection `f: S ↔ R`: every required source entity has exactly one canonical target, every canonical target has exactly one source owner, and distinct source entities are not silently merged. Configuration variants attach to logical entities while retaining their separate body obligations. Distinct nominal specializations remain distinguishable under [Appendix A](#naming).

Each source entity's Destiny-specific responsibilities have stable owner-local IDs and exactly one corresponding responsibility under its target owner. One source method may implement several responsibilities without inventing extra canonical methods. Shared helpers may serve multiple counterparts, but cannot become a replacement canonical owner. Auxiliary adapters, handles, systems, providers, infrastructure types and replaced generic mechanisms are explicitly outside the canonical bijection and linked to the source responsibilities they support.

Properties, fields, constants, namespaces, registrations and lifecycle operations need actual target declarations, accessors, registration entries and executable effects where applicable. Metadata-only claims receive no implementation credit. The mapping may describe a language-required structural transformation; it may not flatten source owners into a generic manager or convert meaningful classes into empty named shells.

### Ownership, relationships, and dispatch

Use native Rust structs, traits/supertraits, composition, delegation, associated items and private providers to implement the source relationship graph. Rust has no named or inherited `impl` blocks. Preserve logical declaring/override ownership while identifying the actual concrete Rust `impl` item, as specified in [Appendix A](#naming) and the [Rust Reference](https://doc.rust-lang.org/reference/items/implementations.html).

| Source construct | Required canonical representation |
| --- | --- |
| Concrete class or struct | Original-named nominal Rust type with real state/lifecycle responsibility; private ECS storage may support it under the same logical owner. |
| Interface or pure abstract contract | Original-named trait with its declaring methods and correct supertrait ancestry. Auxiliary provider traits remain separately identified. |
| Concrete base | Explicit composition/base view and delegation preserving base-owned state, identity and derived override dispatch. |
| Interface implementation | Actual trait implementation on the canonical type or a documented representation boundary, with a real route to that same instance. |
| Inherent/private method | Owner-bound implementation or explicitly linked private provider retaining the canonical self type, visibility intent and responsibility. |
| Inherited method | Declaring-owner and override-chain links; forwarding reaches the authoritative body instead of an independently evolving copy. |
| Field/property/constant/registration | Real owner-bound storage/accessor/value/registration behavior and mechanical identity; a metadata row alone is insufficient. |

Resolve diamond/shared-base paths when the source uses them. Preserve cross-interface access, root resolution and shared base state without reproducing C++ pointer offsets or compiler vtables. A stable handle may represent an object only when its canonical type/methods retain the source responsibilities and operate on the authoritative instance; an untyped entity ID cannot absorb unrelated owners.

For every base/interface edge, identify the real view/conversion path, shared object identity, state authority, inherited implementation source, override dispatch target, query success/failure behavior, and lifetime effects. Trait bounds and relationship metadata alone do not provide those behaviors. An inherited source method remains owned by its source declaring type; generated forwarding code is a linked bridge, not another canonical source method.

The following source relationships require explicit review against the selected source revision:

- `Ball` has `INotify`, `IBall`, and concrete `Partitionable` relationships. A `Partitionable` view must refer to the corresponding base-owned state of the same `Ball`, and `INotify`/`IBall` calls must reach the correct implementation and source effects.
- `Ballpark` has `IEveBallpark` and `IBlueEvents` relationships. Both views must retain the same ballpark identity, registrations, lifecycle and relevant state.
- `IEveBallpark` has `IEveReferencePoint` ancestry. An inherited reference-point view/call must preserve ownership, dispatch and identity rather than cloning a reference-point state object.

Keep the entire graph, not only these examples. Describe concrete-base composition separately from interface ancestry and Python bases. Where multiple interfaces share a root or state, retain one authority. Multiple view handles may alias it; creation/copy operations that produce new source identities must create distinct corresponding instances.

### Fields, representation, and public/private separation

Record every source field/property's logical owner, canonical target, physical storage, aliases, mutable authority, access paths and lifecycle. Moving storage into an ECS component does not transfer its logical ownership away from the canonical object. No independent wrapper snapshot or duplicate registry may become another authoritative copy. Derived caches need source/refresh/invalidation rules and cannot secretly override source state.

At representation boundaries record owned/borrowed storage, alias visibility, buffer validity, lifetime, lock/unlock obligations, endian/width/signedness, overflow/error policy, float rounding/narrowing, NaN/infinity/signed-zero behavior where source-relevant, and exact bits when externally observable. Do not copy undefined C++ behavior as an implementation technique. For ambiguous or undefined behavior affecting an observable contract, record the source evidence and unresolved decision; do not invent equivalence.

Define the public surface from actual Rust visibility/re-exports, public signatures/associated types, extension registrations, Python names/descriptors and source contracts. Preserve canonical public names, owners and behavior. Keep CGP provider types, ECS storage, runtime locks, delegation machinery, incidental dependency types and adapters private unless the source contract or a documented integration boundary requires exposure. Private public-signature leaks are discrepancies even if rustdoc hides them.

Internal changes under a stable source contract must not require redesigning the canonical public API. Source-derived public types may expose stable wrappers/views, but these must operate on the real canonical object and its responsibilities. Public/private cleanup cannot remove source methods, properties or required visibility semantics.

### Bidirectional reconciliation

Reconcile the complete source inventory with actual Rust declarations, bodies, exports and expanded generated/macro output in both directions. Include method signatures, logical and concrete owners, configurations, fields, base/interface/override edges, property accessors, registrations, Python graph and lifecycle effects. Use compiler-aware extraction where available and explicit source review for unresolved expansions; an unavailable extraction tool cannot confer credit.

Reject missing/duplicate canonical targets, missing bodies, orphan production declarations without an auxiliary classification, incorrect declaring owners, accidental helper API exposure, renamed entities without mechanical mapping, relationship markers without executable paths, and stale mappings. A self-authored manifest does not verify itself. Keep source inventory evidence and actual target reconciliation evidence independently attributable. Generated and handwritten implementations satisfy identical correspondence rules.

<a id="blue"></a>

## 5. Current Blue, BlueExposure, and Python exposure

### Consume the actual current implementation

Review the live Blue workspace and its authoritative original/model records at activation. Determine actual root identity, interface ancestry and views, class/factory registration, BlueExposure/PyO3 policy, reference/lifetime behavior, event dispatch, clocks, Bevy runtime access and shutdown. An API name or a compiling placeholder does not establish semantic completeness.

Early authoring inspection identified areas requiring revalidation: root/interface ownership and identity, registration completeness, shared runtime access for Destiny plugins, lock-held callback/reentrant mutation paths, and extension composition. These are investigation obligations, not permanent claims about a moving Blue checkout. Use current source and relevant original cases to resolve them before expanding dependent architecture.

A missing consumed capability becomes an explicit dependency obligation naming its original authority, required behavior, affected Destiny IDs, provider owner, proposed bounded change, and evidence. Implement narrowly necessary Blue fixes when authorized by activation, in a separately reviewed Blue contribution. Preserve unrelated Blue changes and its Goal/accounting. Do not resume another chat, rewrite Blue's complete contract, or gate Destiny on unrelated Blue migration obligations.

### One runtime and one object authority

Python wrappers, Blue root/interface views, canonical Destiny objects, and Bevy systems must resolve to the same logical instance and authoritative state. Record the identity key/generation, provider, state location, reference strengths, query/view path and destruction behavior. A borrowed/view wrapper does not clone authoritative state. Independent ballparks have separate simulation scopes while sharing the required host services and lifecycle.

Integrate with Blue's actual Bevy runtime, registration, events, clocks, task/schedule facilities and shutdown. Choose a supported runtime/plugin access boundary; do not construct a disconnected second engine because the access hook is missing. A separately usable world core may exist, but the production integrated path must use the canonical host and the same implementation.

Resolve extension composition explicitly. Two extension modules that statically link separate copies of Blue globals may produce duplicate runtimes, registries or type identities even when their Rust code is identical. Prefer one authoritative module/runtime owner or a supported shared-service boundary. Document module load order, runtime acquisition, identity exchange and teardown. Do not rely on a process-global address assumption or Python module names alone. Interpreter scoping follows [section 7](#python).

### Reuse exposure, preserve both type graphs

Consume maintained Blue/BlueExposure and PyO3 facilities. Keep Destiny-specific registration, converters and exposure policy where required; do not recreate a second generic Python binding framework. Replace deprecated production macros with maintained selected-version facilities. Original C++ test infrastructure is a distinct validation concern, not a production dependency.

Map Rust and Python type graphs separately and link them: exposed class/interface names, bases/MRO where observable, descriptors/properties, constructors, methods/defaults, exceptions, `isinstance`/type identity, root/interface queries, wrapper caches and the underlying instance. Preserve Python-visible names independently of Rust keyword escapes or overload suffixes. Do not assume a Rust supertrait automatically creates a Python base or Python interface behavior.

For each exposure record, also preserve overload selection, positional/keyword binding, inherited descriptor owners, `issubclass` behavior where applicable, Blue registration IDs/discovery and failed-query outcomes. Record source-specific conversion policy for bool versus int, signedness/range/overflow, float narrowing, strings versus bytes/encoding, borrowed buffers, return ownership and exception type. Generic PyO3 conversion success is not evidence of Destiny/Blue conversion equivalence. If a canonical Rust type cannot directly be exposed as a pyclass, use an explicit supported adapter linked to the same instance and keep the adapter outside the canonical bijection.

Source synchronous APIs retain their call/return contract. Async adapters may be auxiliary, but a returned future or queued command cannot silently replace a completed mutation, query, notification or destruction operation. Use the same state and source-defined completion rules through every public path.

<a id="bevy"></a>

## 6. Bevy execution, state, and scheduling

### Version and ecosystem policy

At activation resolve the newest stable, non-prerelease, non-yanked Bevy release from official release/package sources and record the exact version, source response/reference and observation time. Align Blue, Destiny and selected ecosystem dependencies to one compatible Bevy type/runtime universe. Resolve duplicate incompatible `World`, `Entity`, scheduling, asset, math and plugin types at the actual integration boundary; matching type names do not make versions interchangeable.

Pin the chosen dependencies and lockfiles for each candidate. At one bounded final version gate, observe the newest stable release again. If that gate finds a newer stable release, perform the required coordinated upgrade and affected validation before accepting that candidate. Freeze that observation as the release criterion for the validation run; do not restart indefinitely whenever a release appears later. A proven compatibility blocker needs an exact human decision and qualified version exception, not an unannounced downgrade. Use [Bevy releases](https://bevy.org/news/) and the [Bevy package](https://crates.io/crates/bevy); this document does not hardcode an authoring-time version as “newest.”

Reopen the version gate if the final acceptance attempt is abandoned, resumed after a pause/limit, or its selected dependency candidate changes for another reason. Routine polling, continuation or compaction within the same active bounded attempt does not restart release chasing. Record the attempt identity and report “newest stable observed at” its timestamp, never a timeless latest claim.

Use Bevy ECS, schedules, resources, events/messages/observers, assets, tasks and compatible ecosystem facilities when their real semantics fit. Existing Avian, Lightyear, Replicon or other integrations are candidates to reconcile, not automatic substitutes for Destiny collision, networking, relevance, ordering or numeric rules. Reuse generic facilities; retain or implement Destiny-specific algorithms when a generic engine differs. Avoid two owners applying damping, forces, transforms, integration or state correction to the same physical variable.

### Subsystem integration records

Every required subsystem must record its production Python/native entry points, canonical owners, state locations and aliases, Blue providers, Bevy components/resources/systems/plugins, schedule and clock domains, input/output flow, completion points, callback/error path, original-test evidence and source-reviewed limits. Explain justified exceptions where no particular Bevy facility fits; merely importing Bevy is not integration.

Vertical integration follows real calls from public entry points through the canonical object and shared runtime to resulting state/notifications. Horizontal integration follows interactions between movement, spatial membership, collisions, visibility, callbacks, persistence, client/server actions and host services. A standalone plugin that is never reached by Blue/Python production calls has no integrated completion credit.

Headless Linux execution must work without requiring a window or GPU. Use task, asset, reflection/metadata, diagnostics and other Bevy facilities for actually consumed source responsibilities; record a source-backed reason when a facility is inapplicable. Broad integration does not invent rendering requirements or require every object to become an arbitrary entity/component decomposition.

### Ordering and synchronous completion

For each mutation/query/step define its read/write set, synchronization mechanism, linearization and observable completion points. Preserve source behavior for when changes, callback effects, errors and returned values become visible. Source-immediate calls may require an owner-local synchronous path; an owner must not queue work and block waiting on itself. Cross-thread calls may queue only with a source-compatible completion/wait protocol that releases guards and Python attachment state needed for the owner to progress. A canonical synchronous call must not return while required work is still pending.

Specify exclusive world/object access, command flushing, schedule phases, lock order and nested calls. Do not hold a non-reentrant object/world/registry lock or conflicting Python receiver borrow while invoking user callbacks that may reenter. Capture the source-required dispatch state, release guards where appropriate, invoke callbacks, then reconcile mutations under an explicit protocol without inventing atomicity or losing source ordering.

Record subscriber order, ties, snapshot-versus-live iteration, addition/removal during dispatch, nested dispatch, callback errors and immediate versus posted/deferred delivery. Bevy system order or an observer API alone does not establish subscriber semantics.

Map clock units, epochs, resolution, scales, pause/rebase behavior, simulation step, wall/monotonic time, timestamps, timers and pump phases to actual Blue/Bevy sources. Keep ballpark-local time/state independent where the source requires it. Bevy `Time` defaults and rendering frames are not automatically Destiny's simulation clock.

For assets/resources and background work, preserve identity, strong/weak handles, load/ready/failure states, cancellation, cache eviction/reload, ownership and release. Use one authoritative lifecycle. Record bounded admission/capacity where required, queue ownership, backpressure, suspended work, cancellation and shutdown drain. Avoid pool deadlock from tasks waiting on work that can only run in the same exhausted pool.

<a id="python"></a>

## 7. Concurrent Python, reentrancy, and lifecycle

Inherit Blue's free-threaded default and support its required concurrent, parallel, asynchronous and multithreaded use while preserving Destiny's canonical synchronous contracts. Verify the selected Python/PyO3/runtime build and actual loaded extension mode; a configuration label is insufficient. Use maintained selected-version PyO3 guidance for [free threading](https://pyo3.rs/main/free-threading.html) and [class implementation](https://pyo3.rs/main/class.html), resolving the pinned-version equivalents during implementation.

Record the interpreter executable, stable version/build configuration, supported PyO3 version and actual runtime GIL state before and after required imports. Capability for free threading and the currently enabled GIL are different facts. Later required imports that alter the state need their own observation. Diagnose any dependency that silently restores a GIL-dependent default and resolve it within the consumed contract; an extension declaration alone cannot earn default-runtime credit.

Thread-safe storage or `Send + Sync` is insufficient if pyclass receiver borrowing rejects valid parallel or reentrant calls. Design shared receivers/handles and synchronization so allowed calls reach the source-compatible serialization/parallel path without unsourced mutable-borrow failures or a process-wide interpreter lock. Scope unavoidable serialization to the state/source contract that requires it; do not serialize independent ballparks by accident.

Attach workers through supported selected-version PyO3 APIs before Python access, retain owning-interpreter identities and use appropriate owned references across worker boundaries. Attachment is not exclusive access. Do not use unjustified unsafe `Send`/`Sync` implementations or `unsendable` objects to hide invalid cross-thread ownership. No incompatible World/Python borrow or internal guard may cross an async suspension or reentrant callback; blocking waits must release what the selected runtime needs to make progress while retaining valid object lifetimes.

Record lock/borrow acquisition and release around blocking work and Python callbacks, reentrant mutation/query behavior, nested dispatch, cancellation points, partial effects and synchronous completion. Use a documented state machine or operation phases where needed. A callback cannot wait on a lock held by its caller. Releasing a lock cannot permit an unsourced partially initialized or destroyed object to escape.

Consume Blue's tasklet/suspension/context semantics where Destiny actually depends on them. Establish synchronous suspension feasibility early for consumed APIs; async syntax or free threading does not by itself replace stack suspension. Keep logical task identity, inherited context, current-task lookup and timer stacks distinct from worker-thread identity. Delegate the generic task runtime to Blue rather than building another Destiny scheduler.

Bevy/Blue own engine scheduling; the relevant Python event loop owns its coroutine/task objects. Use supported loop-safe submission, result delivery and cancellation bridges. Do not manipulate Python tasks from arbitrary workers or add a competing general executor for convenience. Async overlap is not evidence of parallel Python execution. Carry and restore source-required task context through spawn, suspend/resume, callback, cancellation and completion, including errors/tracing and nested timer context where consumed.

Define cross-runtime strong/weak references, cycles, Python GC traversal/clearing, wrapper-cache ownership, logical deletion, physical reclamation, callbacks/finalization and identity reuse/generation. Weak interface views must not resurrect dead objects or alias a new object reusing an ID. Keep source-visible deletion and reference effects even when Rust storage uses different ownership machinery.

Define interpreter ownership for extension and embedding modes, supported interpreter scope, initialize/finalize/restart behavior, handle validity, cancellation and shutdown order. Do not share interpreter-owned objects across interpreters or reuse stale handles after restart. If original fixtures require unsupported repeated initialization or another interpreter boundary, resolve the exact adapter/isolation or human decision before dependent expansion. Never invent support for an unverified interpreter mode.

Drain/cancel/join work and clear interpreter-owned references before finalization; destructors must not call into a finalized interpreter. A process-global `OnceLock` containing Python references is not a restart policy. Isolation of independent original cases is valid only when it preserves their meaning; it cannot erase a same-process restart requirement. Subinterpreters are required only when the source contract demands them, not merely because threading is enabled.

Map original errors/exceptions, panic boundaries, poisoning, callback failures, cancellation and partially applied operations. Do not unwind across an incompatible FFI boundary, swallow failures, or turn poisoning into unconditional success. Keep original validation order and observable effects where specified. Establish source-compatible stop/admission/drain behavior for shutdown, pending work, reference release and final callbacks through the one host lifecycle.

Separate recoverable source errors from fatal invariant violations. Record cancellation before an effect, after commitment, or during source-defined partial results; never report “cancelled with no effect” after mutating authoritative state. Every accepted task receives a terminal result/exception or explicit shutdown disposition, and no callback may use logically destroyed state.

<a id="sequence"></a>

## 8. Early integration, subsystem batches, and metaprogramming

### Early feasibility gate

Before building broad architecture on an uncertain assumption, resolve these dependencies using current source review, compilation and applicable existing original cases. Record an executable supported route or an exact pending decision; keep independent work moving.

| Dependency | Required result |
| --- | --- |
| Blue root and interface model | Canonical source ownership, root identity, real interface/base views, query failure, shared state and dispatch; no assumption that an empty or partial root trait is sufficient. |
| Registration and extension composition | Actual factory/registration path and one runtime/registry/type authority across all loaded extensions. |
| Blue runtime access | Supported Destiny plugin/system/state access to Blue's actual Bevy runtime, aligned versions, independent ballpark scopes and coordinated shutdown. |
| Reentrant mutation and parallel receivers | Source-compatible synchronization/completion protocol that releases conflicting locks/borrows before callbacks, with real provider changes where needed. |
| Consumed tasklet and interpreter behavior | Supported synchronous suspension/context and initialization/finalization route for required Destiny calls and original fixtures. Generic Blue-only obligations remain Blue's responsibility. |
| Original test execution | Correct discovery and real Rust artifact loading; C++ fixture route to Rust; exact Linux guard/skip/uncollected-case dispositions. Do not copy Blue-specific fixture names as Destiny obligations. |
| External providers and packaging | Finite consumed closure, pinned reproducible Blue dependency, supported build/link modes and no undocumented sibling dependency. |

### Implementation order

1. Reconcile preserved work, source/contract pins, current records, writers, required configurations and applicability. Identify the complete source denominator and refine unresolved regions without hiding them.
2. Establish a complete original-object path: Python construction → Blue registration/root identity → canonical Destiny object → interface/base view → mutation → actual shared Bevy execution → Python observation → source-compatible destruction/unregistration. Use relevant original cases where they exist and label reviewed-only aspects honestly. Do not add a new behavioral demo/test without the decision required by D02.
3. Complete dependency-ready subsystem batches through that architecture. Each batch closes actual bodies, owner/state/relationship mappings, Python/native exposure, Blue/Bevy interactions, compilation, relevant original tests, durable evidence and authorized incremental publication.
4. Close every remaining source/configuration/provider obligation, reconcile actual target declarations, run the complete applicable original suites against installed candidates, finalize architecture records, reconcile remote integrated content and evaluate every acceptance predicate.

No “first generation complete,” standalone-engine milestone, API catalog, focused proof result, package build, or successful batch terminates the full V2 objective. The source denominator defines completion. Do not replace it with the number of tests or an old catalog total.

### CGP first, measured whole-project cost

**CGP means Context-Generic Programming. CPG means Code Property Graph. They are different tools and abstractions.** Prefer [CGP](https://github.com/contextgeneric/cgp) for separating stable source contracts from private interchangeable implementations where it improves the design. Keep canonical declaring owners and public types intact; a provider graph cannot replace the original object graph with unrelated contexts or exposed implementation types.

Evaluate existing machinery and the named candidates against the remaining project's repeated work: `proc_macro2`, attribute/derive/delegation macros, `derive-deftly`, `arcane`, `comprende`, `better_comprehension`, and Genco. `proc_macro2` supplies token-stream infrastructure; actual procedural macro entry points use Rust's `proc_macro` mechanism, with parsing/quotation libraries as appropriate. Do not assume a nonexistent built-in “proc_macro2 delegate” API. Select maintained concrete crates/versions and verify their capabilities before depending on them. Pythonic convenience must preserve source clarity, exact semantics, diagnostics, and public ownership.

Reuse `/home/astral/Projects/destiny/tools/migrate_destiny.py`, `verification/codegen/`, current extraction rules and Genco integration where they save work. Treat existing generated production bodies as generated until an explicit, recorded ownership conversion. For generated code, version inputs, schema, mapping rules and generator; change those inputs/rules and regenerate. A direct edit that regeneration overwrites is not an accepted fix. If a region becomes handwritten for speed, retire or narrow its generator ownership, record provenance and prevent later regeneration from destroying it. Idiomatic refactoring of generated output belongs in the generator/rules; handwritten regions may be refactored directly under the same correspondence review.

Use Clang-doc, LibTooling/AST data, Doxygen XML and **Joern's [CPG schema](https://cpg.joern.io/)** as machine-readable inputs when useful. CodeQL, SVF and PhASAR may add static call/dataflow information. CBMC and KLEE are behavioral/formal analysis tools: prior outputs may be inspected as separately labeled evidence; new verification campaigns require D02's human decision. Do not mandate installing or repairing every listed tool before implementation can proceed.

Normalize useful extracted facts into a small typed IR with source/configuration provenance, then feed existing Genco or focused Rust emitters. Preserve full required Joern schema semantics, source bodies/relationships and unresolved facts; do not infer completeness from a filtered export, AST-only graph, absent edge or unreachable analysis result. Pin schema/frontend/extractor versions. Inspect existing CPGSchema facilities if relevant, but do not migrate that project or treat an unverified schema implementation as authoritative without checking the consumed fields.

If useful Trinity Doxygen configurations, XML or schemas already exist, reuse their documentation-generation patterns with provenance/license and isolated Destiny configuration. They are tooling inspiration, not authority for Destiny's types or behavior. Do not relabel Trinity entities as Destiny, modify immutable originals, or make finding Trinity artifacts a prerequisite. Configure Destiny's own source/include/define matrix and retain raw-source closure. Generated documentation describes the selected Destiny sources; it does not substitute for them.

Before substantial optional-tool work, record a short whole-project cost/reuse estimate, finite trial and stop condition. Default to at most two diagnosed repair attempts or 30 minutes for an optional integration before choosing a simpler workable route, unless concrete evidence justifies a bounded extension. This is a tool-investment limit, not a feature-completion limit. Measure setup, debugging, compile cost, repeated use, corrections, regeneration and maintenance; no benchmark campaign is required.

Cache extraction by semantic inputs, query only relevant graph neighborhoods, reuse templates and previous source review, and keep context summaries concise to conserve tokens/credits. Do not repeatedly load whole repositories or re-run unchanged analyses. Handwritten Rust is an allowed speed fallback under D01, never a waiver of naming, ownership, integration or behavior. Tooling difficulty must not shrink scope or defer final completion indefinitely.

Candidate references: [derive-deftly](https://docs.rs/derive-deftly/latest/derive_deftly/), [comprende](https://github.com/QuasarRay/comprende), [better-comprehension](https://github.com/Natural-selection1/better-comprehension-in-rust), [arcane](https://github.com/arcane-rs/arcane). Their listing is an evaluation requirement, not a promise that every library fits or must remain in production.

<a id="tests"></a>

## 9. Original tests and bounded execution

**The V2 verification standard is source/correspondence review, successful compilation of actual production artifacts, and applicable original tests. Preserve original assertions, fixtures, expectations and data. A build receipt, test result and source review are distinct evidence channels. None alone establishes full correspondence or formal proof.**

### Preserve test bytes, subject, and meaning

Keep original test references byte-preserved against their authority pins. Use their original executable code by default. Infrastructure adaptation may change build/link configuration, module loading, fixture registration, packaging or process isolation only when it preserves assertions, subjects, ordering, lifecycle and outcomes. Record adapters outside immutable references. A semantic harness change requires the same approval as an assertion edit even when original test bytes are unchanged.

Separate discovery mocks from execution. Discovery tools may stub unavailable imports to enumerate definitions; those mocks must not remain on the production path. Verify the actual loaded Rust extension/native libraries, Blue provider, helper modules and transitive fixture imports, including changes introduced after the initial import. Record module paths/digests, loader/search path, package identity and relevant adapters. A shim that returns expected answers, substitutes the old engine, swallows exceptions or forces success invalidates the result.

For each original C++ suite, identify its real subject and a narrow build/adapter route through unchanged fixtures/assertions to actual Rust behavior, using PyO3/Blue facilities or a test-only ABI adapter where suitable. A test-only bridge is not a required production C++ runtime. Tests linked to original Destiny/Blue production bodies do not validate Rust. Do not automatically translate assertions into Rust, recreate the old production binding framework, or replace a fixture with a mock. If the unchanged fixture cannot reach the migrated subject while retaining meaning, present the exact conflict and obtain a human decision.

Blue-dependent fixtures containing required world assertions remain in scope. Classify their dependencies and provide the Blue path or a precise authorized adaptation; do not skip their world assertions because a prior standalone-engine plan called the fixture a host adapter. Run relevant original Blue/BlueExposure cases for bounded Blue changes; do not make unrelated Blue migration coverage part of Destiny's denominator.

### Complete test accounting

Maintain linked but distinct sets:

1. Source-defined occurrences, including fixture/class qualification, duplicate/shadowed definitions, top-level functions, inherited tests, parameterization sites, malformed/uncollected definitions and configuration variants.
2. Cases actually discovered by the intended runner, with reasons for missing/shadowed/unavailable occurrences.
3. Requested/selected executable cases and configurations for each run.
4. Cases actually started and their terminal outcomes.

Preserve existing `source::fixture::test` identities and enrich them with repository/path, occurrence, parameter and configuration when needed. Do not collapse fixture-qualified cases to unqualified names or replace the source denominator with a historical count. A line number is provenance, not a sufficient stable identity. Distinct parameter instances link to their definition. A shadowed duplicate is not a second execution.

Every required source test occurrence needs an applicability/discovery disposition. Every selected executable case needs a terminal result or an explicit incomplete outcome. Report `passed`, `failed`, `skipped`, `undiscovered`, `blocked`, `timed_out`, `interrupted`, and exact approved exceptions separately. A nonempty selection with zero executed cases is an infrastructure failure regardless of the process exit code. An intentionally empty selection earns no behavioral credit.

Resolve original Linux/platform guards, unconditional skips and uncollected definitions early from the actual Destiny inventory. Do not import Blue example fixture names as new Destiny requirements. Do not globally spoof the platform, silently remove a skip, alter discovery semantics, or weaken assertions. A source-backed platform deferral keeps portable portions in scope; an unexpected Linux skip is unresolved unless its exact disposition is approved.

### Bounded execution and external conditions

Before any potentially blocking build/test operation, record command, working directory, selected cases/features, expected source waits, finite wall-time limit, output/log destination, input identity and recoverable process/session handle. Derive limits from source waits and legitimate observed duration. Use an external watchdog if the runtime may deadlock. Tool polling should normally be no longer than 60 seconds so progress can be reported; the process may continue within its recorded finite limit.

At timeout, capture useful diagnostics, stop or preserve the specifically identified operation under a recovery action, and record incomplete status. Extend a limit only with current evidence of progress or a source-backed correction. Check the existing handle before relaunching. Never kill unrelated processes or start duplicate test/build processes because an earlier poll returned no output.

Record external prerequisites and conditions: services, endpoints, filesystem/permissions, clock/environment assumptions, interpreter and library availability. Distinguish implementation failures, discovery/import/build failures, unavailable prerequisites, timeout/deadlock and approved exceptions. Do not fabricate service responses or turn missing infrastructure into a pass.

Do not repeatedly retry unchanged failures. One diagnostic retry may confirm a documented transient condition; retain both results. Further retries need a changed input or new diagnosis. Cache/reuse applies only under [section 10](#records). Once appropriate checks pass, broaden or repeat them only when remaining full-suite obligations, changed inputs, failures or unresolved concerns justify it.

### Decisions about additional verification

When original tests leave a concrete required behavior unexercised, identify its source ID, production path, existing evidence, precise gap, and smallest proposed verification with expected cost. Request a scoped human decision. Do not automatically introduce new unit, differential, parity, fuzz, stress, benchmark, mutation, concurrency or formal-proof campaigns. Source inventory/reconciliation, compilation and deterministic artifact/document checks are not permission to smuggle in a new behavioral suite.

Record the actual answer: authorize the proposed verification, choose another bounded method, or explicitly accept the stated review/build-only evidence limit. Group related gaps into one concrete decision with an explicit affected-ID set when that reduces repeated interruptions; reuse a prior decision within its actual scope. A pending required decision remains pending; elapsed time and silence are not approval. The original behavior remains required regardless of test coverage. Continue independent work while awaiting a decision.

Preserve existing Kani/Verus/Aegis and other receipts without relabeling them. `mapped_or_marked`, `spec_proved`, `production_rust_refinement_proved`, and `runtime_differential_evidence` remain separate where present. A source marker, harness, compile success, cache or old proof does not establish current refinement. V2 does not require new proof completion, but any proof claim must retain its actual inputs, bounds, assumptions and production linkage. No existing proof failure may be rewritten as success to make a V2 report green.

<a id="records"></a>

## 10. Existing records, receipts, and continuation

### One queue and schema lineage

At activation inspect and reuse the existing migration/acceptance system. `verification/tools/update_migration.py` declares the canonical queue at `.aegis/destiny/work-queue.json`. Other entry points include `verification/migration/CONTINUATION.md`, `verification/migration/next_batch.json`, `verification/migration/world_scope.json`, `tools/migrate_destiny.py`, and `verification/codegen/`. Revalidate actual ownership and paths; if these are projections or have moved, follow their current canonical source and document the mapping. Do not introduce a second backlog, competing acceptance controller, or disconnected subsystem catalog.

The authoring checkout on 2026-11-02 did not contain the local runtime queue JSON although the maintained writer and continuation declare it. At activation recheck its presence, recover any existing authoritative generation/snapshot and reconstruct missing derived state through the maintained record path. Preserve historical receipts and label absent/stale evidence accurately; absence is not a fresh empty project or permission to reset accounting. Inspect writer subcommand side effects before execution and adapt the maintained V2 acceptance path first where necessary, so recovery does not automatically launch a superseded proof or differential campaign.

Extend the canonical schema/readers/writers to represent this V2 contract. Preserve historic schemas and receipts. Record a deliberate migration from older formal-proof requirements, generated-only constraints and world-first host deferral to D01–D03, effective only after authorized activation. Historical `WORLD_CORE`, `HOST_ADAPTER`, `MIXED` or `UNKNOWN` labels may remain as provenance; they cannot silently exclude integrated V2 obligations. Do not edit immutable `.agents` or external controller snapshots to manufacture compatible policy.

One batch record owns its source/body/configuration IDs, dependencies, paths/writer, expected parent, implementation and validation actions, evidence, decisions, publication and exact next action. Keep continuation concise and generated from the current committed generation where feasible. The queue is an index of actual obligations, not a replacement for their source evidence.

### Writer ownership and recoverable progress

Use a single agreed writer or isolated worktree for each mutable path set. Inspect existing writers and dirty work before edits. In shared worktrees use expected-parent/content checks and refuse to overwrite changed inputs. Blue changes have separate ownership and integration records. Do not stage unrelated files or build evidence from a moving tree without detecting changes.

Record writer identity and its actual operation/session handles. Before reclaiming a stale-looking lock, verify the previous owner's current liveness; elapsed time or a lock timestamp is insufficient. A cooperative lock does not exclude uncooperative writers. Use an immutable build snapshot or reliable exclusion when transient edits could occur; before/after hashes alone cannot detect edits made and restored during a run.

Write immutable run receipts/log identities first. Stage updated record payloads under one generation, validate schema and parent digests, atomically publish the payloads, then update the canonical generation pointer/commit record last. Multi-file atomicity needs this explicit commit point; separate atomic renames alone do not form a transaction. Keep before/after generations and a recovery rule for interrupted writes. Readers consume only a complete committed generation. On interruption, reconcile orphan receipts and incomplete payloads rather than overwriting history or granting completion credit.

Flush staged files and directory entries where supported before publishing the commit point. If it still names the old generation, restore its committed views; if it names the new generation, recover the new queue/checkpoint from its transaction payload. Preserve independently valid receipts for explicit reconciliation in either case. If parent identities differ because another writer intervened, preserve both states and resolve ownership; never guess which payload to overwrite. Prepared state does not establish approval, completion or a native Goal transition.

Version schemas and migrate readers/writers together. Older writers must not silently erase V2 fields. Use an exclusive lock or compare-and-swap/expected-parent discipline suited to the existing system. Avoid a new database or elaborate controller when small deterministic extensions suffice.

### Continuous evidence chain and freshness

Preserve a continuous chain:

`pinned source + declared overlays/configuration → actual production inputs → successful build outputs → installed/loaded artifact → original-test execution → actual integrated publication content`.

Each receipt records producer/tool/version, command or review method, relevant inputs, exact output/log identities, outcome, timestamps and parent receipts. Capture an immutable build snapshot or verify before/after input identities; a build racing another writer cannot earn unqualified candidate credit. Failed/interrupted/unknown outcomes stay visible.

Compute recipe-specific semantic input closure: source bodies and includes, generated inputs/rules, macros/templates, helpers, tests/fixtures/adapters, build flags, configuration, dependency pins/overlays, toolchain, relevant environment, Python mode, target/host ABI, and loaded artifacts. `HEAD`, a green boolean or modification time alone is insufficient. Check the loaded candidate, not just what a build was expected to produce.

Reuse current receipts only when their semantic inputs, required configuration, artifact identities and evidence scope match the candidate. Documentation-only changes need not invalidate unrelated compilation; a changed generator, source body, dependency, harness or runtime does invalidate affected evidence. Do not make receipts hash their own changing checkpoint/prose as semantic inputs. Preserve superseded failures and stale receipts by reference instead of erasing them.

An original-test receipt must link a successful production build receipt and actual installed/loaded artifact identities. Packaging and publication receipts link that same candidate or a proven equivalent semantic input set. A newer package, remote tree or sibling Blue overlay cannot inherit older test credit merely because the API names or branch match.

### Continuation and cost control

Persist adopted contract binding, current generation, branch/worktree and ownership, source/dependency changes, current batch, completed/incomplete operations, live handles, exact blockers/decisions, evidence limits, remote/local/visible-checkout state and next command. Preserve actual Goal accounting; do not infer budget from token estimates or reset it in local records. Store tool-trial costs and extraction cache identities for reuse.

On continuation, read the compact checkpoint and relevant queue slice before broad repository scans. Refresh only drift-prone facts and affected evidence. Do not re-run successful unchanged batches, reread all sources, create a parallel queue, or restart live operations. [Appendix B](#record-spec) defines the minimum logical fields and statuses without prescribing replacement infrastructure.

<a id="platform"></a>

## 11. Linux acceptance, portability, formats, and packaging

### Actual host and future platforms

Record the actual Linux architecture, OS/kernel, libc, toolchain, Python ABI/free-threaded mode, linker and relevant dependencies used for acceptance. Keep the core independent of distribution names, OS versions and machine-specific paths. Place necessary platform facilities behind justified boundaries. Tested-host success does not establish a minimum supported Linux ABI, every distribution, Windows or macOS.

Keep Windows/macOS-only integration obligations with source IDs, required adapters and future validation conditions. Portable algorithms, formats, numeric contracts and shared branches in those files remain required now. Do not use a future-platform label to omit a Linux-consumed dependency or portable subsystem. Future platforms do not prevent the defined Linux objective from completing, but final reporting must qualify the platform scope.

### Build and installation modes

Distinguish native Rust library/application, Python extension, embedding, and original-test adapter outputs. Use supported facilities for the selected PyO3/Python versions and correct mode-specific linking/features. An extension-only configuration need not link as an embedding executable; record actual supported recipes rather than assuming one artifact serves all modes. Include debug/release or other production configurations required by source contracts and packaging, without inventing an unnecessary platform matrix.

Produce reproducible locked builds with the pinned Blue implementation and compatible Bevy dependencies. Include required runtime modules, data/configuration, licenses/notices, generated-code provenance and usage/build instructions. Final builds must not require original Destiny/Blue C++ production libraries, stale extension artifacts, undocumented environment variables, an unrecorded sibling checkout or obsolete exposure frameworks.

Build actual release/package outputs and required consuming executables, not only `cargo check` metadata. Keep extension-only linking settings from leaking into embedding/native modes. A single successful feature combination does not validate every required consumer. Determine package ABI/library requirements from actual outputs; a relevant host/interpreter/library update invalidates affected results and requires appropriately scoped rebuild/original-test refresh. Do not invent a cross-distribution behavioral matrix without D02's human decision. Local packaging and the authorized Git milestones are in scope; uploading to a public package registry or deploying a service requires separate explicit authorization.

Install the actual candidate into a controlled environment and run the applicable original suites against it, with verified import/library locations and digests. Do not let source-tree imports shadow the installed candidate. Record package contents, target/ABI tags, dependency resolution and installed identities. Keep original C++ test harness artifacts clearly separate from production deliverables.

### Formats, snapshots and replay

For each source-defined stream, snapshot/history/replay, client/server action and persistence mode, record the real production configuration, schema/version, field ordering, numeric/bit encoding, endian/width, object/reference identity, defaults, errors, compatibility rules, correction/restore order and applicable original cases. Preserve exact bytes where the source contract requires them. Generic Serde output or a new JSON schema cannot silently replace an existing wire/storage format.

Include construction/persistence hooks, string encodings and malformed-input behavior. The actual loaded production serializer must select the recorded mode; changing a test expectation or test-only environment switch does not show that production selected it. Preserve required legacy data compatibility without assuming an obsolete Python production runtime is necessary.

Map every source mode, including disabled/conditional variants, to a required current configuration, source-backed future-platform obligation, or exact approved exception. Snapshot/restore must reconstruct the correct logical identities, graph, state owners, pending effects and temporal state where required. Serialization equality is not sufficient if restored runtime behavior or reference aliasing differs. Apply D02 to any proposed new behavioral verification of uncovered modes.

<a id="publication"></a>

## 12. Publication, exact guidance propagation, and human decisions

### Implementation publication after activation

Authoring these documents does not authorize publication. A later explicit implementation invocation under this contract authorizes ordinary incremental milestone commits/pushes and stacked PRs into `destiny-rs-dev`, plus bounded separately reviewed Blue contributions into `blue-rs-dev`. Preserve both `main` branches and unrelated work. Follow actual repository protection and approval rules; never bypass them or force-push shared history.

Use the integration branch directly where safe, or a `codex/` work branch/worktree with explicit milestone integration. Publish small coherent verified milestones, recording dependencies so later stacked work is not merged without its prerequisites. Keep source references immutable and stage only owned changes. Blue contributions state the exact consumed capability, source authority, affected Destiny obligations, scope limits and relevant validation; their acceptance is separate from the whole Blue migration.

Check remote identity, available access, branch protections and Git metadata writability early through appropriate read-only preflight. Resolve actual publication prerequisites before promising remote completion; do not use speculative permission requests or a destructive test push. An existing authorization for ordinary milestone publication need not be requested again.

For each milestone, record tested candidate inputs, local commit/tree, expected remote parent, actual remote branch/commit/tree, PR/integration status, relevant Blue pin and visible-checkout state. Verify the remote ref after pushing and the integrated content after merging. If a merge or conflict resolution changes relevant inputs, revalidate affected evidence. Equal source semantics may permit receipt reuse under the documented closure; a different integration tree may not inherit credit without that comparison.

Distinguish local commits, successful remote publication, merged integration and the user's visible checkout. A bundle, unpushed commit, successful PR creation or focused CI run is not final integrated publication. Report credential/protection/network failures accurately and continue independent work. Remote publication is an acceptance gate unless the user explicitly amends it; never call a local-only result fully accepted under the unchanged contract.

### Exact-text guidance propagation

The supplied guidance in [Appendix C](#supplied-guidance) remains preserved. On implementation activation, inspect root guidance. If no canonical root `AGENTS.MD` exists, adopt the supplied exact bytes at the root under D06. If a root file already exists, preserve it and reconcile its identity/version with actual user instructions; never overwrite user changes merely to match the attachment. Resolve a substantive authority conflict before propagation. Record D01–D06 as contract precedence rules outside the preserved text.

Define one maintained-directory manifest and exclusion set used by the mirror, drift checker and source-reference verifier. Mirror the canonical root `AGENTS.MD` bytes into every included existing maintained directory, including newly created maintained directories. “Exact” means byte-for-byte, including case of filename, encoding and newlines; a link or “read the root” stub is insufficient. Avoid symlink traversal outside scope. Preserve and reconcile divergent existing files before replacing them.

Exclude immutable original source/test references, imported `reference/` trees, third-party vendor snapshots, immutable `.agents`/external controller snapshots, Git metadata, tool installations, caches, virtual environments, build/package output and ephemeral runtime directories. Record concrete path/glob boundaries; exclusions cannot become a blanket excuse to omit maintained source, generator, script, documentation or CI directories. Generated maintained source directories remain included unless they are explicitly disposable build outputs. An excluded tree's preexisting guidance remains part of its original pin.

Implement idempotent automatic propagation on root updates and directory creation through the existing development/CI workflow. CI should run correction in its workspace and verify that the corrected result matches the submitted tree, failing on drift with an actionable patch or the repository's authorized bot correction flow. Do not silently push from CI without such authorization. Use the same manifest for sync/check; never rewrite excluded reference bytes. Do not install this mechanism during prompt authoring.

### Exact decisions and exceptions

Routine reversible implementation choices within scope do not require repeated approval. Required decisions concern actual conflicts or gaps: semantic original-test changes/retirement, new behavioral verification, unresolved authority/undefined behavior, incompatible dependency/version or scope changes, and external protections. Complete the source analysis and concrete proposal needed for an informed decision first; continue independent work.

A request identifies the affected source/test IDs and paths, precise assertion/dependency or evidence gap, current failure/source contradiction, candidate implementation path, smallest resolution, cost and acceptance consequence. Store the actual human response and provenance. Do not infer consent from silence, a skipped test, a past unrelated approval or an elapsed trial budget.

A test-only exception waives only the specified execution obligation, never the associated behavior, object correspondence or integration. Apply approved exceptions consistently to every affected predicate while retaining original counts and exception scope. If the user removes required behavior, record an explicit objective amendment and report qualified scope; do not describe the result as an exception-free one-to-one reimplementation. Pending decisions and unknown applicability are not successful exceptions.

<a id="architecture"></a>

## 13. Architecture descriptions and decision records

Maintain architecture descriptions and Architecture Decision Records with source/provenance links and machine-readable indexes where useful. Align the description with **ISO/IEC/IEEE 42010:2022** concepts: system of interest and environment, stakeholders and concerns, viewpoints and model kinds, views/models, correspondences and known inconsistencies, decisions, rationale and consequences. See the [ISO standard record](https://www.iso.org/standard/74393.html). Do not claim certification or full standards conformance from a template or a list of ADRs.

Cover at least:

- Canonical source/target object and relationship graphs, ownership, naming transformations, public/private boundaries and source responsibilities.
- Blue/BlueExposure dependency boundary, root/interface identity, module/extension composition, shared host and bounded dependency decisions.
- Bevy state ownership, plugins, subsystem interactions, schedules, clock phases and synchronous completion/callback paths.
- Python/Rust type relationships, concurrency, receiver borrowing, lock order, reentrancy, task context, references/GC, interpreter lifetime and shutdown.
- Persistence, streams, snapshots/replay, wire/storage formats, configurations and portable/host-specific boundaries.
- Generation/handwritten ownership, CGP/provider decisions, tool trial results, reproducible inputs and simplifications chosen for total completion cost.
- Build/installation/publication chain, original-test applicability, decisions/exceptions, evidence limits and future-platform obligations.

Each record identifies status/date, context, source obligations, alternatives, decision/rationale, consequences, actual production paths, affected evidence and superseded decisions. Generate catalogs/diagrams from current records where useful, and review the explanatory text for accuracy. Retain historical ADRs with supersession links. Update architecture alongside implementation and final idiomatic refactoring; do not document a desired architecture as if it already runs.

Refactor completed generated or handwritten implementation into idiomatic Rust and idiomatic Bevy while retaining canonical source naming, ownership, behavior and stable public contracts. Use narrowly scoped naming-lint allowances when source case requires them. Prefer native ownership, error handling and ECS scheduling without reproducing generic C++ mechanisms. Preserve deterministic regeneration for generated regions and revalidate affected correspondence/build/original-test evidence after refactoring. Documentation and refactoring are required completion work, not optional work after declaring the Goal complete.

<a id="acceptance"></a>

## 14. Complete acceptance

Evaluate these predicates against one frozen candidate and required Linux applicability set. Each predicate links exact source/configuration IDs, current evidence, outcomes and approved exceptions. “Implemented,” “reviewed,” “compiled,” “original tests passed,” “packaged,” and “published” remain separate facts. Aggregate completion requires every applicable predicate, not an average score or percentage of names mapped.

The frozen candidate includes the adopted objective/contract hash and decisions, source pins/overlays, applicability/configuration denominator, semantic input closure, Blue/Bevy/dependency pins and final version observation, host/interpreter/GIL identity, build/installed artifacts, committed record generation and actual integrated remote content. Reconcile all gates to that candidate; individually green receipts from incompatible candidates do not compose into acceptance. Apply the current-state completion audit and terminal handshake in [section 2](#goals) after this reconciliation.

| ID | Predicate |
| --- | --- |
| A01 | **Authority and scope closed:** original Destiny, consumed original Blue/BlueExposure, overlays, files/bodies/macros/templates/configurations and finite provider closure are pinned and accounted for; no required unresolved region or silent denominator reduction remains. |
| A02 | **Bijection and naming satisfied:** all required source entities/responsibilities have exactly one real canonical counterpart; actual declarations and expansions reconcile both ways; mechanical names, properties/fields/constants/registrations and logical/concrete owners are correct; auxiliary items are classified. |
| A03 | **Relationship and identity semantics satisfied:** complete base/interface/override graphs, inherited behavior, shared state, runtime identity, queries, copying and lifecycle have actual source-compatible paths, including the `Ball`, `Ballpark` and `IEveReferencePoint` examples. |
| A04 | **All Destiny behavior implemented:** every world/host/client/server/private/configuration obligation has a real body and correct responsibility owner. No TODO, missing delegate, unconditional success, disabled required feature, empty shell or state-only facade remains. |
| A05 | **Current Blue integration complete:** reproducible current Blue dependency, consumed providers, bounded fixes, actual registration/exposure/runtime access and one runtime/state authority across Python, interfaces, Destiny and Bevy are complete. No older nested baseline or undocumented sibling input remains. |
| A06 | **Bevy integration complete:** all subsystem vertical/horizontal records point to real production execution/state, with compatible versions, final finite version gate, headless Linux operation, clock/schedule/callback/resource semantics and no duplicate physical-state authority. |
| A07 | **Python and concurrency contracts complete:** free-threaded default and actual GIL state after required imports, canonical synchronous completion, public type graph, receiver contention, reentrancy, loop/task context, identity/weakrefs/GC, errors/cancellation, interpreter ownership and shutdown are implemented and reviewed with explicit original-test coverage/limits. |
| A08 | **Public boundaries and implementation quality complete:** stable canonical public APIs, private providers/plumbing, native Rust mechanisms, idiomatic Rust/Bevy refactoring and reproducible generation/recorded handwritten ownership are complete. |
| A09 | **Production builds and formats complete:** required actual-host configurations and artifact modes compile; stream/snapshot/replay/wire formats and references preserve required semantics; dependency/toolchain/ABI identities and future-platform obligations are accurate. |
| A10 | **Original-test accounting complete:** every source occurrence has a justified disposition; every required applicable executable case passes against the intended installed Rust/Blue candidate or has an exact execution exception. Missing/zero execution, failures, unapproved skips, timeouts and unresolved C++ adapter routes cannot pass. |
| A11 | **Evidence and decisions current:** source review, reconciliation, build, original-test, package and publication receipts form a continuous current chain; no required pending decision, stale inherited credit or fabricated proof result remains. Additional verification exists only within its authorization. |
| A12 | **Installed deliverables complete:** reproducible packages, native/Python interfaces, data, licenses, build/use instructions and original-test execution use the real installed candidate, with no original C++ production runtime dependency or stale import shadowing. |
| A13 | **Guidance and architecture complete:** exact root-byte mirrors and CI sync/check operate under the maintained-directory boundary; references/user work are preserved; architecture views/ADRs reflect actual code and accurately state ISO alignment and evidence limits. |
| A14 | **Integrated publication complete:** verified Destiny milestones are integrated into `destiny-rs-dev`; required bounded Blue contributions are separately reviewed/integrated into `blue-rs-dev`; actual remote content matches validated semantic inputs; local/remote/visible-checkout state and any exact publication exception are reported. |
| A15 | **Operational closure complete:** canonical queue/generation and continuation reconcile all required obligations; no required `planned`, `partial`, `unresolved`, stale or blocked item remains; native Goal is bound to the adopted contract and only then marked complete under supported lifecycle rules. |

For A10, do not confuse an approved original skip's execution disposition with behavioral acceptance. For A07/A09 and any uncovered behavior, use source/correspondence review and the exact human decision required by [section 9](#tests); do not claim unexecuted paths were exercised or demand an unauthorized new campaign. Historic formal evidence is supplemental and separately scoped.

The final implementation report states candidate/source/Blue revisions and overlays, Linux host and version observation boundary, required/implemented/unresolved counts by entity/body/configuration, original test source/discovery/selection/start/result counts, exact exceptions and their effect, evidence channels/limits, package identities, publication states, future-platform obligations, architecture locations and native Goal status/usage. Never call compilation, one batch, an old proof total or this authoring exercise the completed migration.


<a id="naming"></a>

## Appendix A. Mechanical identity and naming specification

This is mapping-rule version 2. Apply it uniformly to original entities and actual Rust declarations. Preserve existing compliant names and IDs through explicit aliases/migration history where the record format changes; do not silently reinterpret previous mappings.

### A1. Canonical source identity

Use a stable repository identifier, source-qualified declaring owner/name, declaration kind and canonical signature/specialization descriptor. Keep revision, path/span, macro provenance and configuration as linked provenance/variant information. For internal-linkage or anonymous/local entities, add the original relative path and a deterministic owner-local discriminator; line numbers alone are never sufficient. Declaration/definition references for one entity share its ID.

Serialize descriptors as UTF-8 JSON without a BOM or trailing newline, with object keys sorted by Unicode code point, no insignificant whitespace, preserved case, and ordered arrays. Emit non-ASCII characters literally; escape JSON quotes, backslashes and control characters using a fixed serializer recipe. Use decimal integer strings and typed exact bit/value representations rather than host-dependent floating-point JSON numbers. Freeze that recipe with the rule version. Normalize text only to the source language's identifier semantics and record the original spelling. Never normalize raw source bytes for provenance.

A callable descriptor contains these fields, with explicit empty lists or null only when genuinely inapplicable:

| Field | Normalization |
| --- | --- |
| `owner`, `name`, `kind` | Fully qualified source owner; original member/operator spelling; function, method, constructor, destructor or conversion kind. |
| `template_parameters`, `specialization_arguments` | Ordered parameter kind/position and canonical argument forms; parameter names become position identities within the descriptor. |
| `return_type`, `parameter_types` | Canonical fully qualified source types with pointer/reference/array/function structure and qualifiers preserved. Expand typedef aliases for signature equality while retaining spelled aliases separately. |
| `receiver` | Static versus instance, cv/ref qualification and applicable source receiver details. |
| `variadic`, `calling_contract`, `exception_specification` | Source varargs, relevant calling convention/ABI boundary and exception specification; no inferred empty value. |
| `constraints` | Ordered canonical source constraints where applicable. |

For C++ signatures, remove parameter variable names, comments, source whitespace and default argument expressions from signature identity. Defaults remain mandatory call-contract data. Preserve a canonical language-token rendering of type/constraint expressions and the extractor/version/normalization recipe. Do not infer unresolved canonical types with a different parser spelling and give them credit; resolve the descriptor by source review first.

For Destiny-specific Python callables, retain ordered positional-only, positional-or-keyword, keyword-only and variadic parameters, their observable names, and binding mode. Preserve default expressions/values in the call contract and annotation spelling where present; use an explicit dynamic-type marker where the source has no static type. Do not apply C++ parameter-name erasure or invent static type information for Python signatures. Original test definitions retain their own execution identities instead of becoming new Rust tests.

Use recursive C++ type nodes with these fixed fields; nested type operands use the same encoding:

| Node kind | Fields besides `kind` |
| --- | --- |
| `builtin` | `name`: canonical language spelling, including `int` for `signed int` and `unsigned int` for `unsigned`; preserve distinct character and sized language types. |
| `named` | `declaration`: fully qualified source declaration identity; `arguments`: ordered type/value/template argument nodes. |
| `qualified` | `of`: qualified type; `qualifiers`: fixed const/volatile/restrict order, retaining only present qualifiers. Omit empty qualifier nodes. |
| `pointer`, `lvalue_reference`, `rvalue_reference` | `to`: referenced type. |
| `array` | `element`: element type; `extent`: exact constant/dependent expression, or null for unspecified extent. |
| `function` | `return_type`, ordered `parameter_types`, `variadic`, `calling_contract`, and `exception_specification`. |
| `member_pointer` | `owner`: declaring class type; `to`: member type. |
| `template_parameter` | `parameter_kind` and zero-based owner-local `position`. |
| `type_argument`, `template_argument` | `value`: canonical type node or fully qualified template identity, respectively. |
| `constant` | `type`: canonical type; `value`: exact canonical value representation. Use decimal strings for integers, true/false for booleans, and typed exact bit/value representations for other kinds. |
| `dependent` | `category`, ordered language `tokens`, and ordered `bindings` linking referenced names/parameter positions to their source identities. Remove comments/whitespace; canonicalize parameter references to positions. |
| `extension` | Compiler-defined `category`, complete structured/token `form`, and `provider` identity. It remains unresolved until reviewed and its encoding fixed under this rule version. |

Unknown node fields or alternate encodings require an explicit rule-version extension; do not let separate extractors silently choose different spellings. Keep original declarations as provenance alongside canonical values.

Apply C++ semantic function-parameter adjustments before identity encoding, including array/function parameter adjustment and removal of irrelevant top-level value-parameter qualification. Preserve the spelled declaration and any behavior-relevant qualifiers separately. Canonicalize true/false exception expressions when evaluable; preserve dependent expression tokens otherwise. Freeze the node-field serialization recipe with the rule version so two extractors cannot silently choose different encodings.

Do not replace symbolic platform-sized source types with host-only widths in identity. Record their concrete width/signedness per configuration as semantics. Configuration variants attach to the entity when they describe the same logical declaration; distinct signatures/specializations remain distinct entities. Incompatible conditional bodies retain separate variant obligations even when they share a callable identity.

### A2. Rust identifiers and collisions

Apply the following in order:

1. Preserve the original identifier and case wherever valid for the selected Rust edition. Use raw identifiers for keywords where supported.
2. When raw spelling is not legal, encode the original UTF-8 bytes as lowercase hexadecimal prefixed by `__destiny_`. Record the original spelling and escape. This covers otherwise unsupported keyword/nested/operator spellings without arbitrary names.
3. Preserve namespace paths as module paths. When Rust cannot directly express a nested type, put it in an auxiliary sibling module named `<mapped-owner-name>__types`, recursively applying this rule for deeper type nesting and rule 9 for collisions. The original declaring-owner edge remains explicit; the auxiliary module is not a second canonical owner type.
4. Within each source overload family, give every overload the base name followed by `__sig_` and the first 12 lowercase hexadecimal digits of SHA-256 of its canonical callable descriptor. Do not select one arbitrary overload to keep an unsuffixed canonical name.
5. Constructors use `new` when unique, or `new__sig_<digest-prefix>` for an overload family. Preserve construction variants, defaults, errors and source links. Convenience constructors are auxiliary.
6. A source destructor maps to the corresponding lifecycle/Drop implementation and its explicit source effects; implicit field destruction and helper functions are recorded mechanics. A source-visible explicit destruction operation remains its own canonical callable.
7. Operators map to the appropriate native Rust trait method when its signature and behavior fit. Otherwise use a named method with a base formed by the escape in rule 2 and the same overload rule. Conversion operators include the conversion target in their descriptor. Additional operator convenience implementations are infrastructure.
8. Non-callable templates/specializations preserve their generic owner; distinct nominal specializations that need separate Rust types use `__spec_` plus the descriptor digest prefix. Do not invent separate types for ordinary uses of the same generic contract.
9. Resolve collisions in the actual Rust symbol namespace against the complete candidate set. A transformed/generated name yields to an otherwise valid preserved original name. Extend existing digest prefixes by four hexadecimal digits until unique. If a colliding transformed name has no digest yet, append `__sig_` plus the descriptor digest for a callable, or `__id_` plus the stable-identity descriptor digest for another item, starting with 12 digits and extending by four. For normalization collisions between preserved spellings, use their reversible byte escapes and apply the same collision rule. If the full digest still collides, append `__id_` and the hexadecimal UTF-8 encoding of the complete stable source identity; repeat that complete identity suffix if a literal original name occupies the resulting spelling. Resolve generated candidates in stable-source-identity order. Never silently merge.
10. Preserve Python-visible source names/signatures independently through PyO3 facilities. Rust overload suffixes do not leak into Python APIs unless the source exposed them.

Apply suffixes and nested-module construction to the logical identifier spelling, not to the Rust `r#` token prefix. Render raw-identifier syntax only after constructing the final identifier; escape any remaining invalid spelling. Auxiliary nested modules use a stable identity derived from their owner and module role for collision resolution. The record provides reversibility; a hash by itself does not. Check all candidate names against the complete known namespace before publishing the mapping. Newly discovered collisions trigger explicit rule/application migration and affected reconciliation. Keep prior names as optional compatibility aliases only when they preserve the canonical distinction.

### A3. Logical and concrete target identity

Record each actual Rust item's qualified path, kind, source span/generated origin, visibility, translated signature and configuration. For methods, record both:

- Logical owner: canonical self type, declaring trait where applicable, and the original declaring/override owners.
- Concrete impl item: complete self/trait arguments, generics/where constraints, cfg conditions, module/file and deterministic item discriminator.

Do not force a one-to-one relationship between C++ classes and the number of Rust impl blocks. Preserve their types, contracts and method ownership through actual Rust constructs.

A property counterpart is the corresponding owner-bound Rust/PyO3 property implementation, with actual accessor/descriptor paths and state effects, not a registry-only marker. Source-declared accessors retain their own method mappings. Namespace/relationship metadata must likewise reference real declarations.

For runtime objects, one source-visible object identity corresponds to one canonical Rust instance identity. Multiple interface views or Python wrappers are aliases to it where the source requires aliasing. Copying/creation that produces a new source identity must produce the corresponding distinct instance; reference-wrapper creation must not accidentally clone state.

### A4. Relationship and naming review

Record and reconcile declaration ownership, type/base/interface graphs, implementation/override origin, property/accessor links, physical and logical state ownership, visibility and Python exposure. Review all source-discovered overload and constructor families, `Ball` and `Ballpark` interface/base views, `IEveBallpark` ancestry, and their actual corresponding original cases against these exact rules. Do not import Blue-specific fixture names into the Destiny denominator.

Generated and handwritten code follow the same mapping. A rule-version change records which entities, aliases, generated output and reviews are affected. This appendix supplies deterministic mapping policy; it does not require an additional behavioral test suite.

<a id="record-spec"></a>

## Appendix B. Record and receipt contract

These are minimum logical fields, not a demand to replace compatible existing infrastructure. Reuse existing field names through a documented schema mapping; otherwise use the names below. Record `contract_version: 2` and advance the existing record's `format_version` only as its schema requires; do not downgrade an existing schema to match the contract number. Retain prior snapshots and update readers/writers together. Tools that still write an older schema must not silently erase new fields.

### B1. Canonical correspondence record

| Field group | Required content |
| --- | --- |
| `format_version`, `generation`, `previous_generation` | Schema and committed progress identity, with parent linkage. |
| `contract_binding` | Native chat/objective, V2 path/hash/version, adopted amendments and decision references; observed lifecycle/accounting fields, observation time and actual capability/schema identity. Never replace native accounting with local counters. |
| `source_pins`, `source_files` | Origins, revisions/archive identities, raw digests, path/mode/encoding provenance, overlays, extraction/configuration coverage and exclusions. |
| `mapping_rules` | Naming/normalization version, extractor/tool identity and explicit application history. |
| `entities` | Stable source identity/signature, owners, source references, role, visibility, fields/state, relationships, responsibility set, applicability, canonical target and auxiliary/provider links. |
| `python_identity` on affected entities | Exposed names, bases/protocols, wrapper/object identity, callable/property behavior and owning interpreter boundary. |
| `integration` on affected entities/subsystems | Real Python/Blue/Destiny/Bevy paths, canonical owners, state authority, provider/version identity, schedule/clock/callback/resource/concurrency policies, completion points and source-linked review. |
| `blue_dependencies` | Finite consumed original contracts, current implementation pin/overlay, missing capabilities, bounded patch ownership, separate review/integration and final reproducible dependency. |
| `original_tests` | Source occurrences, discovered/selected/executed identities, configuration, applicability, terminal status and receipts. |
| `decisions` | Exact human approval provenance, scope, affected IDs, replacements and acceptance consequences; pending decisions remain pending. |
| `receipts`, `acceptance` | Immutable receipt references and separate per-obligation review/build/test/package/publication outcomes and limits. |
| `turn_observations`, `operations` | Actual turn IDs/classifications, affected obligations/new evidence, operation input identity, owning tool and recoverable handle, current liveness evidence, finite deadline and recovery action. |
| `terminal_transition` | Prepared acceptance/candidate identity, last live Goal observation, attempted supported transition and actual response/confirmation; pending, failed, ambiguous and confirmed outcomes remain distinct. |

Each Destiny-specific responsibility has an identifier within its original owner's responsibility set and exactly one target responsibility under the corresponding owner. Several responsibilities implemented by one source method remain distinct annotations on that method's counterpart; they are not an excuse to invent extra canonical methods or merge unrelated owners.

Implementation status distinguishes `unresolved`, `planned`, `partial`, and `implemented`. Review status distinguishes unreviewed, current reviewed, discrepancy and stale. Compilation, original-test, packaging and publication statuses remain separate. `implemented` alone never means accepted. Source applicability and mechanism replacement are separate from all of these statuses.

### B2. Queue and checkpoint

A batch records its ID, source/configuration/relationship obligations, dependencies, owned paths/writer, expected parent/input identity, implementation and validation work, receipts, unresolved decisions, publication status and exact next action.

A blocker records its fingerprint, affected obligations, condition/evidence, first and consecutive distinct Goal-turn observations, last material change, attempted alternatives, live handles, independent work remaining and exact unblock requirement. A resumed blocked Goal starts a new observation sequence.

The checkpoint records the committed generation, live Goal binding last observed, branch/worktree, source/dependency/host changes, current batch, successful and incomplete operations, previous-turn classification, verified live handles and deadlines, unresolved symbols/decisions, publication state and the next command. It remains concise; detailed data stays in the canonical record/receipts. These fields extend the existing queue/record system, not a separate Goal controller.

### B3. Receipts

Every receipt has a type, unique ID, timestamp, candidate/batch identity, producer/tool identity, command or review method, relevant inputs, outcome and evidence locations/digests.

- Build: before/after or immutable-snapshot input identity, features/environment/target, toolchain/dependencies, exit code, complete log identity and exact outputs.
- Original tests: successful parent build receipt, installed/loaded artifact and module identities, interpreter/GIL/host/configuration, source tests/fixtures/adapters, requested/discovered/started/terminal cases, skips/blockers, timeout/process handle and logs.
- Reconciliation: source and actual target declaration identities, extraction/review method, required counts, discrepancies, resolved ownership/relationship checks and unresolved regions.
- Packaging: build receipts, package contents/digests, compatibility metadata, installation environment and identity used by original tests.
- Publication: tested inputs/receipts, local commit, expected remote parent, actual remote/integration commit/tree, PR state if applicable and visible checkout evidence.
- Transaction: previous/new generations and expected parent digests, durable run receipts, recoverable before/after progress payloads and commit-point identity.

Receipts are immutable observations. Supersede or invalidate them by reference, preserving failure/staleness history. Unknown fields, unavailable logs or interrupted results cannot be filled with invented success. Cache reuse requires the semantic input/artifact relationship in [section 10](#records), not a green flag.

### B4. Acceptance and exceptions

Each acceptance predicate links original required IDs, configuration/candidate identity, evidence channels, result and exact approved exception if any. Preserve counts for replaced generic mechanisms, future platforms, unresolved items and test-only versus behavioral exceptions.

Retain the existing canonical queue/writer and extend its schema; no new custom database, parallel lifecycle engine or separate subsystem catalogs are required. Extend the existing records and use small deterministic serialization/reconciliation tools only where they save work.

<a id="supplied-guidance"></a>

## Appendix C. Preserved supplied guidance

The following block reproduces the supplied document's exact UTF-8 bytes between the opening and closing fences, including its final newline. Its instructions are preserved as reference material; the activation boundary and D01–D06 determine their operative application. Do not execute this appendix merely because it is quoted here.

Source: [supplied AGENTS.MD](</home/astral/Projects/destiny agentsmd/AGENTS.MD>). SHA-256: `9e4ae50fe10d3b846ef7def04d7cf84bb965838f655515b147f832a594367e46`.

```markdown
# AGENTS.MD

## Project Goals:

1. Reimplement Carbon Engine's Destiny in Rust on top of Bevy.

2. There should be precise one to one correspondence between Original destiny objects, methods, etc. and the Rust equivalents. struct names, struct hierarchy, impl block hierarchy and names, trait names, and hierarchy, etc. must be mechanically mapped one to one with the original. Therefore one to one equivalence is simultaneously Behavioral, structural, and nominal.

3. destiny-rs must be deeply integrated with newest implementation of blue-rs, which will have direct one to one correspondence between original blue object model, object/method hierarchy, structure and relationships. Make sure not to model destiny's architecture against older versions of blue-rs. to ensure highest accuracy, look up the implementation of original blue developed by fenris creations's engineers, but do not assume a need for C++ integration. just Python integration, as all C++ code will be replaced by Rust equivalents in Bevy.

4. AGGRESSIVELY use Metaprogramming and Automation to accelerate and simplify development. AGGRESSIVELY use CGP-Oriented metaprogramming, and metaprogramming with proc macro 2, proc macro 2 attribute, and proc macro 2 derive and proc macro 2 delegate, derive deftly and arcane macros to Automate, simplify and accelerate development.

5. Use CGP and derive-deftly and comprende and better_comprehension, proc macro 2, proc macro 2 attribute, and proc macro 2 derive and proc macro 2 delegate and arcane macros AGGRESSIVELY, to accelerate development and reduce boilerplate, and make the project look Pythonic and familiar to python developers: https://github.com/contextgeneric/cgp.git, https://gitlab.torproject.org/Diziet/rust-derive-deftly, https://github.com/QuasarRay/comprende.git, https://github.com/Natural-selection1/better-comprehension-in-rust.git, https://github.com/arcane-rs/arcane, CGP should own the application logic. The project should be designed around CGP-Oriented programming paradigm and design philosophy.

6. This AGENTS.MD file must exist in every directory of this project (The exact text, not an instruction to the agent to go and read the original. With each update in the root directory AGENTS.MD, the AGENTS.MD files in all other directories must be automatically updated. make it part of the CI/CD pipelines)

7. Do not modify main branch. always work in destiny-rs-dev branch.

8. Make stackable pull requests and/or pushes incrementally to ensure that no work is duplicated or lost. turn my github account into your workspace. merge into destiny-rs-dev after each milestone.

9. The purpose of Metaprogramming is to accelerate development, if metaprogramming slowed you down, don't do it. Always choose the faster path for finishing the project.

10. Existing Rust Ecosystem must be used to the fullest potential. Do NOT try to recreate C++ semantics in destiny's Rust reimplementation. Application behavior and semantics must only correspond to original destiny exclusively in destiny-specific semantics, all traces of C++ semantics must be fully removed and replaced with Rust Semantics in Rust reimplementation of destiny.

11. The Rust Reimplementation of destiny MUST have Deep and Broad, Vertical and Horizontal integration with bevy. (Use newest release of Bevy)

12. The original destiny does not cleanly separate the module of public api and the private internals implemenetation. The Rust Reimplementation must fix that flaw and cleanly and surgically separate destiny public API and private internals. Also, CGP must be used to ensure that internal changes can happen effortlessly with ZERO need for API Redesign.

Target Project Repo: https://github.com/QuasarRay/destiny.git
```

The root file's adopted bytes are the future propagation authority under D06. The preserved attachment is historical source material if the user has since intentionally changed that authority. This appendix does not install guidance or erase those changes.

<a id="launcher"></a>

## Appendix D. Copyable Goal launcher

Invoke this only when ready to activate or explicitly adopt the implementation objective. Reading or delivering it does not activate implementation. The [standalone launcher](/home/astral/Projects/destiny/DESTINY_RS_REIMPLEMENTATION_GOAL_V2.txt) contains the identical command. Inspect/reuse the native Goal and bind the contract's actual version/hash under [section 2](#goals). No token budget is implied. The earlier prompts and launchers remain preserved.

```text
/goal Reimplement Carbon Engine's Destiny completely in Rust on Bevy in /home/astral/Projects/destiny, following /home/astral/Projects/destiny/DESTINY_RS_REIMPLEMENTATION_GOAL_PROMPT_V2.md in full. Preserve simultaneous behavioral, structural, and nominal one-to-one correspondence, mechanical names, canonical declaring owners, complete base/interface/override relationships, shared state and object identity, and every required private/public/configuration responsibility. Establish early Python -> current /home/astral/Projects/blue blue-rs -> Destiny -> shared Bevy execution and complete every subsystem through it, with free-threaded Python by default and canonical synchronous behavior. Prefer CGP/metaprogramming, but use simpler or handwritten Rust when it reduces total time to faithful completion; preserve deterministic regeneration for generated regions. Complete Linux acceptance on the actual host, keep the core portable and Windows/macOS obligations explicit, align dependencies to newest stable Bevy under the finite version policy, and permit only bounded separately reviewed required Blue fixes. Use production compilation, applicable unchanged original tests and correspondence review; preserve existing proofs separately and obtain a concrete human decision before additional behavioral verification or semantic test changes. Reuse the canonical queue and evidence records, preserve sources, main branches and other work, mirror exact root AGENTS.MD bytes only through maintained directories, produce idiomatic Rust/Bevy and ISO-aligned architecture descriptions/decision records, package the actual artifacts and publish verified incremental milestones into destiny-rs-dev with required Blue contributions integrated separately into blue-rs-dev. Inspect/reuse the live native Goal and bind this contract version/hash and actual adoption without replacing another objective or resetting accounting. On each continuation, reconcile authoritative state, classify progress or verified live waits, recover the canonical generation and operation handles, respect pause/clear/limits and exact decisions, and continue dependency-ready work. Before completion, audit the full objective and all V2 predicates against current evidence, then use only the supported native completion operation and record its actual returned status/accounting. Partial implementation, first generation, a passing subset, and a checkpoint are not completion.
```

Authoring completion means the V2 contract, launcher and coverage audit have been produced and checked. It does not mean Destiny has been reimplemented, original suites have passed, architecture conformance has been certified, milestones have been published, guidance has been installed, or an implementation Goal has been activated. A separately authorized authoring Goal may now be completed after its own full audit.
