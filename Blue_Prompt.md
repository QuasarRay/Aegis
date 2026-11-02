# Blue Rust Reimplementation — Codex Goal Execution Contract V2

Version: 2. Authoring date: 2026-11-02, Australia/Melbourne.

This is the complete execution contract for reimplementing Carbon Engine's Blue and BlueExposure together in Rust. It contains its own operational rules, acceptance conditions, and launcher. The V1 audit is historical context; execution does not require reopening it.

**Every original Blue-specific object, type, interface, method, property, and responsibility MUST have exactly one canonical Rust counterpart. Equivalence MUST be simultaneously behavioral, structural, and nominal. Names, declaring owners, responsibilities, state ownership, and the complete base/interface relationship graph MUST correspond. A matching name, wrapper, manifest entry, or successful compilation alone does not establish equivalence.**

## Contents

- [1. Authority, activation, and objective](#authority)
- [2. Native Codex Goal lifecycle](#goals)
- [3. Source authority, unified repository, and inventory](#sources)
- [4. Canonical correspondence and the Rust object model](#correspondence)
- [5. BlueExposure, PyO3, and Python identity](#exposure)
- [6. Bevy execution and state integration](#bevy)
- [7. Concurrent Python and lifecycle](#python)
- [8. Early feasibility and implementation sequence](#sequence)
- [9. Original tests and bounded execution](#tests)
- [10. Durable records, receipts, and continuation](#records)
- [11. Portable host support, builds, and packaging](#platform)
- [12. Milestone publication and human decisions](#publication)
- [13. Acceptance and completion](#acceptance)
- [Appendix A. Mechanical identity and naming specification](#naming)
- [Appendix B. Record and receipt contract](#record-spec)
- [Appendix C. Finding resolutions F001–F048](#findings)
- [Appendix D. Preserved requirements U01–U22](#requirements)
- [Appendix E. Copyable Goal launcher](#launcher)

<a id="authority"></a>

## 1. Authority, activation, and objective

Execute this contract only when the user explicitly invokes it as the implementation objective. Authoring, reviewing, downloading, or quoting this file does not activate implementation. Respect the current collaboration mode and current tool instructions. This document does not override Plan mode.

V2 governs a migration only after explicit adoption. Do not silently redirect another chat or a running V1 migration. On authorized adoption, preserve the previous contract identity, record the V2 binding and actual user direction, and reconcile affected work and evidence. Preserve the V1 prompt, its launcher, and frozen audit as history.

The objective is a complete unified Linux Rust implementation of Blue and BlueExposure, with the correspondence contract satisfied, substantive Bevy integration, free-threaded Python as the default runtime, successful production compilation and applicable original tests, locally packaged deliverables, and verified milestone integration into `blue-rs-dev`.

The governing decisions are mandatory:

1. Preserve Blue-specific observable behavior and the original object/responsibility graph while replacing obsolete implementation mechanisms.
2. Use one Cargo workspace rooted in Blue. Preserve original sources as reference and import a pinned BlueExposure reference snapshot with licenses and provenance.
3. Reuse PyO3 directly. Do not rebuild generic Python binding machinery that maintained PyO3 already supplies. Retain Blue-specific policy and required identities around those facilities.
4. Bevy MUST own real engine execution and state integration, vertically and horizontally. Use the newest stable release under the finite version-check policy in [section 6](#bevy).
5. Concurrent, parallel, asynchronous, multithreaded Python is the default architecture. Preserve canonical synchronous APIs and required ordering.
6. Optimize time to finish the whole remaining project. CGP, generators, macros, and handwritten Rust are optional implementation choices. No tool is mandatory when it slows completion.
7. Successful compilation and the original Blue and BlueExposure tests are the verification standard. Additional behavioral testing requires a concrete reason and a subsequent human decision.
8. Linux on the actual development host is the first complete acceptance target. Keep the core independent of particular operating systems and distributions. Record Windows/macOS obligations for future acceptance.
9. Publish verified milestones into `blue-rs-dev`. Preserve `main`, the upstream BlueExposure repository, and unrelated work.
10. Report implementation review, compilation, original-test execution, exceptions, packaging, and publication separately. None is formal proof.

Explicit user decisions take precedence over conflicting project guidance, including blanket demands that CGP own all application logic. Preserve the user's root `AGENTS.MD`; apply the decision instead of rewriting guidance to remove a constraint. The specific guidance-propagation boundary in [section 3](#sources) follows the user's preservation and V2 instructions.

This contract authorizes ordinary implementation choices that preserve these requirements. It does not preapprove test changes, removal of behavior, or new behavioral verification. Approval rules in [section 12](#publication) apply throughout, including final acceptance.

<a id="goals"></a>

## 2. Native Codex Goal lifecycle

Use the native Goal service as lifecycle authority. Repository files hold implementation state and evidence, not a competing Goal controller. Goals are persistent objectives scoped to their chat; a checkpoint from another chat cannot establish the active objective. See [Using Goals in Codex](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex). Current tool schemas govern exact operations and transitions, including any supported blocked state.

At activation, inspect available Goal capabilities and call `get_goal` before attempting `create_goal`. Bind the adopted contract in the canonical record to:

- The live chat/thread identifier and native objective as returned.
- This contract's absolute path, version, and SHA-256 of its complete bytes.
- Accepted amendments and the actual user instruction adopting them.
- Source pins, record-schema version, and current worktree owner.

Compute the contract digest at activation and store it outside this document; do not introduce a self-referential embedded digest. The objective must name the complete outcome and V2 path. If the service does not support editing an objective, preserve its returned text and record an explicitly authorized amendment in the binding; do not invent an update operation.

| Returned situation | Required action |
| --- | --- |
| No Goal, or only a completed prior Goal, and implementation is explicitly invoked | Create the complete implementation Goal. Omit `token_budget` unless the user supplies one. |
| Matching active Goal, including one created by the launcher | Reuse it. Do not create milestone Goals or duplicate the objective. |
| Matching paused Goal | Respect the pause. Explicit user resumption is required; use the current user/service-controlled resume mechanism, then confirm state. Do not invent `status: active`. |
| Matching blocked Goal | Respect the recorded blocker until resumption is authorized. On resumption, re-read evidence and start a fresh consecutive-blocker audit. |
| Matching budget-limited or usage-limited Goal | Respect the limit. Only user/system controls can extend or resume it; do not replace the Goal to reset accounting. |
| Matching completed Goal | Do not restart completed work merely because the contract was read. New implementation or reopening requires explicit user direction. |
| Unrelated unfinished Goal | Preserve it. Explain the objective conflict and request direction; do not overwrite it. |
| Native Goal capability unavailable or an unknown state returned | Report the exact capability/state gap, preserve the checkpoint, and follow current tool instructions. Do not emulate continuation with a daemon or invented state. |

A matching objective means the same migration outcome and adopted contract lineage, not merely a similar title. If the contract hash changes, compare the change with actual user steering before depending on affected rules. Preserve prior bindings. A changed file alone does not authorize a scope change.

During execution:

- After a batch, checkpoint its result and continue dependency-ready work while the Goal is active and within its limits.
- When a localized issue needs input, request the exact information and continue independent work.
- Pause only on an explicit user request. If the tool supports `update_goal(status="paused")`, use it, report the returned status, and stop Goal work.
- Use `blocked` only under the available tool contract: the same genuine blocking condition has recurred for at least three consecutive Goal turns, including the original turn, and no meaningful independent progress remains. Persist the condition, distinct turn observations, affected obligations, live operations, alternatives, and independent-work assessment. Multiple polls in one turn are not multiple Goal turns.
- At a budget limit, stop substantive work and preserve the checkpoint within the remaining allowance. Report unfinished work; do not mark complete.
- Mark complete only after every applicable gate in [section 13](#acceptance) is satisfied. Report tool-provided final usage when required, including final token usage for a budgeted Goal.

A resumed blocked Goal starts a new three-turn audit. Difficulty, slow work, an unfinished feature, or a transient tool error does not by itself justify blocked status. Check existing process handles before declaring an impasse or restarting work. Do not claim invisible background continuation after the session stops.

<a id="sources"></a>

## 3. Source authority, unified repository, and inventory

### Repository and preservation boundary

| Role | Location |
| --- | --- |
| Unified repository | `/home/astral/Projects/blue` |
| Authorized remote | `https://github.com/QuasarRay/blue.git` |
| Integration branch | `blue-rs-dev` |
| Original Blue | `src-cpp/`, `include/`, original Python modules, tests, build/configuration files, and their dependencies |
| Initial BlueExposure source | `/home/astral/Projects/blueexposure` |
| Imported reference snapshot | `reference/blueexposure/` |

Revalidate these locations against the actual checkout. Inspect HEAD, branch, remotes, dirty/staged files, existing records, and active writers before changing anything. Reuse compatible implementation and evidence. Authoring-time revision observations are not permanent source pins. Revalidate already-selected source pins; do not silently substitute a newer or easier source base. Resolve material conflicts about the intended original authority with the human before changing that authority.

Keep one root Cargo workspace with canonical public Blue APIs, private implementations, and the PyO3 boundary. Internal crates are permitted when they simplify ownership or builds. Both Rust implementations and their build infrastructure belong in this repository. Production must not depend on a sibling checkout, a BlueExposure gitlink, or original Blue/BlueExposure C++ production bodies.

Preserve original Blue source files and tests. CMake paths that still refer to the former C++ `src/` location may be adapted in build infrastructure; do not mistake Rust `src/` for the C++ authority. Import the selected BlueExposure snapshot with tests, build metadata, license, notice, and provenance, excluding nested Git metadata. Never modify or push the sibling upstream repository.

Guidance mirroring applies to maintained project directories. Exclude immutable source/test reference trees listed in the source manifest, all imported `reference/` snapshots, third-party vendor snapshots, Git metadata, tool installations, caches, virtual environments, generated build/package trees, and ephemeral runtime directories. Do not add or update guidance files inside those excluded trees. Existing guidance there is preserved as source content if part of a pin. Record exact path exclusions and use the same boundaries in mirroring CI and source-snapshot verification. This explicit preservation boundary does not authorize editing the root guidance or omitting mirrors from maintained project directories.

### Source identity and extraction closure

For each authority, record origin, revision or archive identity, license, raw file digest, source path, imported path, file mode/symlink identity where relevant, and configuration identity. Compare imported/current reference bytes against the selected Git object or authenticated archive. Hashing worktree bytes and labeling them with a revision is insufficient.

Record dirty-source overlays separately: parent pin, changed/additional/deleted paths, raw digests, reason, and source-selection decision. Never present an overlay as the untouched revision. Relocation is an explicit path mapping, not permission to normalize line endings or encoding. Preserve raw bytes; decode using identified encodings and flag failures. Replacement-character decoding cannot establish extraction completeness.

Inventory both libraries completely, including:

- Declarations and definitions, private and unused bodies, inline code, templates/specializations, macro-generated declarations and registration.
- Namespaces, types, aliases, constants, fields, methods, properties, interface/base edges, overrides, state ownership, and Python-visible identities.
- Blue-specific behavior inside generic-looking exposure, conversion, registration, copying, persistence, callback, and lifecycle utilities.
- Original Python helpers, source test fixtures, assertion bodies, data, runner/discovery behavior, and configuration branches.
- Build/include/macro dependencies and portable behavior inside platform-oriented files.

For every authoritative file and relevant configuration, track inspected regions, extracted entities/bodies, macro definition and expansion provenance, template definitions and required instantiations, parse failures, and manual resolutions. Start from source build configurations and conditions such as `BLUE_WITH_PYTHON`, `CCP_STACKLESS`, and `PY27_COMPATIBILITY_MODE`; resolve the matrix from source rather than assuming those names are exhaustive. A Linux parse alone cannot discard portable obligations hidden behind another branch.

Use the simplest reliable extraction method: existing compiler/AST information, structured parsing, or explicit source review. Do not make a general translator a prerequisite. A lexical candidate, file count, or export list is not body/relationship coverage. Unresolved regions retain zero completion credit.

Inventory closure requires a disposition for every authoritative file, source region/body, configuration alternative, and required instantiated behavior. Preserve duplicate declarations as provenance for one entity when they denote the same entity; keep genuinely distinct definitions, specializations, test occurrences, and incompatible conditional contracts distinguishable.

### Finite external boundary and applicability

For external contracts, inventory declarations directly consumed by Blue and recursively include only dependencies necessary to understand or supply their signatures, constants, identity/lifecycle behavior, and invoked semantics. For each, name the authoritative source and provider: maintained dependency, Rust/PyO3 primitive, or a minimal Blue-owned adapter. Stop when every consumed contract has a provider and no unresolved transitive semantic dependency remains. Do not port unrelated external bodies or omit inherited obligations such as `IRoot`/`ICcpStream` merely because their definitions live elsewhere.

Use separate dimensions for role, applicability, implementation status, and evidence. The following dispositions do not independently confer acceptance:

| Disposition | Required justification |
| --- | --- |
| `BLUE_SPECIFIC` | Canonical counterpart and retained Blue behavior/relationships. |
| `PYO3_PROVIDED` | Concrete maintained PyO3 facility/version, replaced generic role, and every retained Blue-specific sub-obligation. |
| `NATIVE_RUST_MECHANISM` | Native facility and removed language/bookkeeping role; preserve attached Blue semantics. |
| `EXTERNAL_BOUNDARY` | Consumed contract, finite dependency closure, provider, and required integration. |
| `PLATFORM_DEFERRED` | Source-backed Windows/macOS-only obligation outside Linux acceptance; portable sub-obligations remain required. |
| `HUMAN_APPROVED_EXCEPTION` | Exact decision, affected obligations, authorized change, and effect on acceptance. |
| `UNRESOLVED` | An open obligation; never an exclusion or a successful result. |

Freeze the current applicability set for each acceptance candidate. Changing the set requires a source-backed correction or explicit human scope decision, with previous and new counts visible and affected evidence invalidated. A label, filename, missing dependency, absent test, or replacement mechanism cannot reduce the required set. Split mixed obligations with links to the original owner; do not lose them through classification.

<a id="correspondence"></a>

## 4. Canonical correspondence and the Rust object model

### Domain and exact relation

Let S contain the distinct required Blue-specific production entities in the source inventory, each carrying its explicit set of owned semantic obligations. A declaration and its definition identify one entity. Test assertions are execution obligations, not instructions to create a second Rust test suite. Source fixtures needed to exercise migrated behavior retain their own traceable roles and real implementation path.

Let R contain the canonical Rust counterparts. Maintain a bijection between S and R: exactly one canonical counterpart per source entity, no shared canonical target for distinct entities, and no canonical target without its source entity. Map each owned semantic obligation to exactly one target obligation attached to that corresponding owner. Each type, method, property and state responsibility retains its own identity; multiple responsibility annotations on one method do not require artificial extra Rust methods.

Keep generic C++/binding mechanisms replaced by native Rust or PyO3 outside this canonical Blue-specific domain, with explicit replacement records. For a mixed item, isolate its generic mechanism from its Blue-owned obligations while preserving their common source owner. Never use that split to merge two distinct Blue-specific entities.

Auxiliary adapters, delegation functions, handles, Bevy systems, and PyO3-generated plumbing belong to a separately marked supporting set. Multiple helpers can implement one canonical contract, but there is one authoritative implementation/state responsibility. Two source methods do not become the same canonical method merely because they delegate to a shared primitive.

Preserve graph edges for declaration ownership, field/state ownership, interfaces, interface inheritance, concrete bases, overrides, inherited-method origin, construction/lifecycle, and Python exposure. Composition may replace a concrete inheritance edge only through an explicit base-view/delegation path that retains the source relationship. Removed pure-machinery edges require a documented native/PyO3 replacement. No Blue-specific edge disappears by contraction.

### Required representation rules

| Source construct | Canonical Rust representation and preserved obligation |
| --- | --- |
| Concrete class/struct | Original-named nominal type, authoritative state responsibility, and source-linked lifecycle. |
| Interface/pure abstract contract | Original-named trait with correct declaring methods and supertrait edges. |
| Concrete base | Explicit composition/delegation; preserve base identity, state sharing, inherited behavior, and override dispatch. Auxiliary contract traits are recorded separately. |
| Interface implementation | Explicit trait implementation on the corresponding type or recorded representation boundary; preserve every interface relationship. |
| Inherent/private method | Method on its corresponding owner or explicitly linked private implementation boundary; preserve visibility intent and responsibility. |
| Inherited method | Link to its declaring base/interface and override chain; forwarding must reach the authoritative body instead of copying independently evolving implementations. |
| Field/logical state | One authoritative state owner with ownership, aliasing, lifetime, and concurrency rules. Pure pointer/allocation bookkeeping may have a native replacement. |
| Namespace/nested type/enum/constant/registration | Reversible qualified representation with preserved observable name/value. |
| Property | One source property contract linked to its actual getter/setter/descriptor implementation, mutability, errors, and declaring owner. |

For base/interface views specify identity equality, successful and failed interface queries, root-object resolution, inherited state, cross-interface access, and dispatch from a base method to a derived override. Supertraits and embedded structs alone do not supply those semantics. Address diamond/shared-base paths if the source uses them. Use native Rust mechanisms instead of copying compiler vtables, pointer offsets, or C++ ABI layout.

Rust `impl` blocks have neither independent names nor inheritance. Record two identities: the logical self-type/trait owner of a method, and the concrete impl item identified by full self/trait arguments, generic constraints, configuration and source-item discriminator. Multiple inherent impls may share one logical owner. See the [Rust implementation reference](https://doc.rust-lang.org/reference/items/implementations.html). Follow [Appendix A](#naming) for deterministic naming and signatures.

Derive public Rust and Python surfaces from source declarations, registration, callers and original tests. List exported types/members/signatures and their source visibility; do not simply publish every internal type. Keep implementation machinery private and avoid leaking incidental Bevy/PyO3/provider types into canonical APIs unless an explicit source-boundary decision requires them. Compatibility facades preserve canonical owners; a generic manager or untyped entity wrapper cannot absorb unrelated responsibilities.

### Behavior and boundaries

Preserve defined Blue-specific values, units, conversions, errors, ordering, callback timing, identity, persistence bytes, and lifecycle effects. Rust ownership and synchronization replace raw-pointer tricks, manual C++ allocation, undefined behavior and ABI emulation. A source UB path is not a demand to reproduce UB; identify the valid observable contract and escalate any resulting behavior conflict rather than inventing parity.

For each memory/FFI boundary record owned versus borrowed storage, alias visibility, mutability, lifetime, pinning where needed, lock/unlock rules, integer widths and signedness, overflow/truncation behavior, and safe invalid-input handling. A copied `Vec` is not equivalent to a caller-owned mutable buffer if shared changes are observable. Source review must resolve `SetBuffer`, `LockData`/`UnlockData`, `Read`/`Write`/`Seek` and similar boundaries before their representation is accepted.

Source examples that must survive:

- `src-cpp/BlueMemStream.h` declares `MemStream`. Retain that name and both `IBlueMemStream` and `ICacheable` relationships, including `IBlueMemStream`'s `IBlueStream` ancestry and actual declaring method owners.
- BlueExposure's `TestMultipleInterfaces` fixture retains both `ITestInterfaceOne` and `ITestInterfaceTwo` contracts and common object identity.
- `TestSuperclassMethods` retains its `TestMethods` base relationship and declaring owners; copying methods into an unrelated type is insufficient.

### Reconciliation before correspondence credit

For each batch, reconcile source-to-target and target-to-source using compiler/AST data or explicit source review with recorded locations:

1. Every required source entity/body has its correct canonical counterpart or an explicit mechanism-replacement record.
2. No distinct canonical source entities collide; no source entity has two canonical targets.
3. Actual compiled declarations, signatures, visibility, impl owners and relationship paths agree with the record.
4. Every production target is canonical, an explicit replacement provider, or justified auxiliary infrastructure; orphan bodies are resolved.
5. All required source regions/configurations close, and generated declarations are reconciled after expansion.
6. The public/Python surfaces and state-owner graph agree with the implementation.

Record the review method, input identities, discrepancies and resolutions. This is implementation/mapping infrastructure, not an extra behavioral suite or formal proof. Status fields, comments and aliases cannot stand in for real bodies or relationships.

<a id="exposure"></a>

## 5. BlueExposure, PyO3, and Python identity

Use maintained PyO3 directly for generic Python ownership, attachment, class/module exposure, method/property binding, ordinary conversions, exceptions and supported protocols. Each replacement record names the concrete facility and selected version. Do not recreate a binding framework, reference-count emulation, conversion framework or empty original-named wrapper solely to resemble C++.

Retain an original-named adapter where its name or Blue-specific policy is required. Mixed utilities must preserve their Blue-specific registration, discovery, identity, properties, callbacks, conversion rules, copying, persistence and lifecycle responsibilities. `PYO3_PROVIDED` neither removes those responsibilities nor retires an original test.

Maintain linked, separate graphs for canonical Rust types/interfaces and Python-visible types/objects. For each exposure record include:

- Python module/class/member names, signature, defaults, overload selection and descriptor behavior.
- Python bases, actual MRO/ancestry, `isinstance`/`issubclass` expectations, `BlueWrapper` behavior, and inherited method/property owners.
- Canonical underlying object identity, wrapper identity/reuse, ownership edges and binding-adapter identity.
- Blue class/interface registration IDs, metadata, discovery, creation and failed-query behavior.
- Source-specific conversions, including bool/int distinctions, signedness, range checks, float conversion, strings/bytes, return values and exception types.

A correct Rust trait graph does not establish a correct Python type graph. Use only supported PyO3 class and protocol facilities; choose an explicit adapter representation when a canonical Rust type cannot directly be a pyclass. Preserve one underlying canonical object and record the adapter as infrastructure. Do not claim automatic Python multiple inheritance from multiple Rust traits. Check the selected release's [class guidance](https://pyo3.rs/v0.30.1/class).

Keep source-defined construction, copying, persistence, weak references and deletion policy around reused primitives. Generic PyO3 conversion success is not evidence that Blue's conversion policy is preserved.

Remove deprecated production macro dependencies. Inventory `BlueExposureMacrosDeprecated.h` and other expansion sources, retaining their required semantics through maintained PyO3 attributes, native Rust, or small maintained project macros. Original macro text may remain in immutable references and necessary original test infrastructure. Renaming obsolete internals does not modernize them. External popularity or becoming “mainstream” is not an acceptance condition.

<a id="bevy"></a>

## 6. Bevy execution and state integration

Bevy MUST own engine execution and state integration. Registering a plugin that delegates to an independent legacy runtime is insufficient. Bring Bevy and Python into the first complete object path and retain both in every applicable subsystem batch.

### Version policy

At execution start resolve the newest stable, non-prerelease, non-yanked Bevy release from authoritative [Bevy release information](https://bevy.org/news/) and the [Bevy package registry](https://crates.io/crates/bevy). Record exact version, source response/reference, observation timestamp and compatible Rust/dependency requirements. Pin the selected artifacts and lockfile within a batch. Do not permanently hard-code an authoring-time release family.

Recheck at the final acceptance attempt's version gate. If the observed newest stable differs, select it and rebuild/revalidate affected work before that attempt can succeed. That timestamped observation defines the release target for the bounded attempt; do not poll releases continuously during its validation. Restart the version gate if the attempt is abandoned, resumed after interruption, or its dependency candidate changes for another reason. Report “newest stable as verified at [recorded time]” and the exact accepted version, not a timeless latest claim. An incompatible new release is a concrete implementation/dependency issue, not silent permission to use an older release.

### Subsystem integration record

For each required subsystem, attach an integration entry to the canonical correspondence record. Include source responsibilities, canonical Rust owners, authoritative mutable state, Bevy resources/components/owned values, systems/schedules and ordering, task/asset/reflection use, Python/Rust entry points, completion/callback paths, shutdown behavior, and review/build/original-test evidence.

Cover application/plugin lifecycle; registration and object identity; pumping, clocks, timers and scheduling; streams and paths; resource loading, caches and background work; callbacks and notifications; persistence/copying; reflection/metadata; statistics, logging and diagnostics. The full source inventory determines completeness. Record source-backed non-applicability per Bevy facility rather than requiring rendering or arbitrary entity conversion.

Vertical integration means tracing a real Python or Rust entry point through its canonical Blue owner into Bevy-managed state/work and back to the result. Horizontal integration means the applicable subsystems participate in the same lifecycle, identities and execution model. Each entry must name actual production paths. Inspect the paths and use relevant original tests; an integration matrix alone is not behavioral evidence.

### State access, synchronous completion, and reentrancy

Assign exactly one authoritative owner to each mutable state value. Python wrappers, Blue APIs, Bevy systems and background operations reference or submit work to that state; they must not maintain independently authoritative copies.

For each operation, record its read/write set, synchronization mechanism, point at which effects become visible, completion point, and callback phase. Preserve the original return-time guarantee. A queued request does not satisfy a synchronous method until required effects and immediate callbacks finish.

For ECS-owned state, define the exclusive access phase and owner that applies mutations. A caller already executing on that owner must use a valid synchronous path or a deliberately split execution phase; it cannot queue work and block waiting on itself. Other threads may submit commands and await a result only while releasing the borrows/locks and Python attachment state required for the owner to progress. For canonical objects with synchronized interior state, direct access is permitted only under the recorded ownership protocol; Bevy lifecycle, scheduling, and relevant change visibility must still use that same state.

Before invoking reentrant user/Python code, finish or split exclusive world/object operations so that callbacks can perform all source-permitted operations. Do not hold an incompatible World borrow, pyclass borrow or mutex through that callback. Never solve the problem by returning early from a synchronous method, suppressing callbacks, adding a global interpreter lock, or converting the canonical method to async. If the source requires an irreconcilable reentrant effect, identify it and seek the specific decision.

### Ordering, clocks, resources, and work lifetime

Preserve `SendEvent` immediate completion and `PostEvent` deferred delivery, together with subscriber order, list snapshots, additions/removals during dispatch, nested dispatch and error handling. BlueOS's ordered ticker list is a concrete source case. Explicit system order does not automatically order subscribers observing the same event; [Bevy Observer documentation](https://docs.rs/bevy/latest/bevy/prelude/struct.Observer.html) must be checked for the selected release. Use a source-compatible ordered dispatcher where needed.

Record each source clock's units, epoch, precision, scale, monotonicity, pause/rebase behavior, overflow behavior, update phase and readers. Preserve distinct real/simulation clocks and fractional correction where defined; do not replace them indiscriminately with a generic Bevy Time value. Map pump/timer phases and required ordering explicitly.

For each resource family, record identity, handle ownership, loading/ready/error states, retry/reload behavior, completion/cancellation, cache authority, eviction/recycling and release. Bevy asset/task facilities supply mechanics where compatible; Blue policy and source completion order remain authoritative. Duplicate retention systems cannot silently change lifetime.

Record admission, queue ownership, suspended-task ownership, capacity behavior, cancellation and shutdown drain/join policy. A thread per suspended stack needs an explicit resource policy; a fixed worker pool must not deadlock when all workers suspend waiting for work on that pool. Preserve source-visible capacity/backpressure behavior or request a concrete exception. Do not invent throughput targets or a stress suite.

Headless Linux execution must work without a window or GPU. Broad integration does not add rendering responsibilities that Blue never had.

<a id="python"></a>

## 7. Concurrent Python and lifecycle

Select a current stable free-threaded CPython build supported by maintained PyO3. Record executable, version, build configuration, actual runtime GIL state, PyO3 version and build mode. The default package and run path must select that interpreter configuration.

Free-threaded capability and the currently active GIL state are separate facts. Identify both before and after required imports in execution/test infrastructure, and record later required imports that affect the state. Do not accept a dependency silently re-enabling a GIL-dependent default. Diagnose the exact dependency and fix or replace it within source contracts. See [Python free-threading guidance](https://docs.python.org/3.15/howto/free-threading-python.html); revalidate against the selected interpreter.

### Ownership and borrowing under concurrent calls

Registries, objects, callbacks, counters, caches, cancellation and lifecycle state require appropriate shared ownership and synchronization. Preserve required source ordering; permit independent work to run in parallel. Do not restore blanket single-threaded Python through a substitute global lock.

Attach threads through the selected PyO3 APIs when accessing Python. Use owned Python references across worker boundaries and retain their owning-interpreter identity. An attachment token does not provide exclusive access.

For every shared pyclass/API boundary, specify receiver borrowing and where contention is resolved. A directly exposed mutable pyclass borrow can reject competing calls before an internal mutex is reached. Prefer shared receivers with appropriately synchronized authoritative state when concurrent use is required, or a source-compatible operation protocol. Do not accept new unsourced borrow errors/panics as equivalent behavior merely because storage is Send/Sync. Do not use unjustified unsafe Send/Sync implementations or `unsendable` objects to hide a design failure. Consult [PyO3 free-threading guidance](https://pyo3.rs/v0.30.1/free-threading).

No incompatible World borrow, Python borrow or internal lock may cross an async suspension or reentrant callback. During blocking waits, detach/release what the selected runtime requires for progress, including global runtime synchronization. Keep required references alive without retaining invalid guards.

### Synchronous tasklets, coroutines, and context

Free threading and async futures do not themselves replace arbitrary synchronous stack suspension. Inventory source `Yield`, task switches, suspension/resumption, channels, task identity, timers, tracing and errors before committing to a scheduler representation. Select a maintained mechanism that preserves those contracts and exercise the relevant original cases as early as infrastructure permits. A thread-based substitute must account for scheduling, cancellation, capacity and shutdown; an async adapter cannot require rewriting canonical synchronous callers.

Bevy owns engine scheduling. Python event loops own their coroutines/tasks. Use maintained bridging facilities where available; make cross-thread submission, completion and cancellation loop-safe. Do not manipulate tasks from arbitrary threads or create a competing general executor solely for convenience. Async concurrency alone does not establish parallel Python execution. Follow [Python asyncio threading guidance](https://docs.python.org/3.15/library/asyncio-threading.html).

Task identity is independent of worker identity. Map task-local storage, inherited context, current-task lookup, context propagation, tracing and nested timer stacks through spawn, suspend, resume, callback, cancellation and completion. Restore context at boundaries; do not substitute unqualified thread-local/global state. Preserve source-visible identity/order where defined.

Canonical synchronous methods keep their name, signature, completion and exception contracts. Additional async APIs are explicitly marked infrastructure with a link to the canonical method.

### Object lifetime and interpreter lifetime

Record strong/weak ownership edges across Python objects, Rust objects/handles, callbacks, Bevy state and pending work. Expose Python reference cycles through supported PyO3 GC traversal/clearing protocols where required; Arc/Weak and Drop do not by themselves describe Python's object graph. Preserve wrapper identity and weak-reference behavior.

Separate source-visible logical liveness/destruction effects from physical reclamation. Preserve LiveCount changes, delayed deletion queues, weak-reference visibility and finalization timing where defined. Do not assume either that free threading breaks every immediate-deletion test or that it preserves all such observations automatically. Investigate exact cases and request approval for actual conflicts. Use the selected release's [protocol facilities](https://pyo3.rs/v0.30.1/class/protocols).

Define interpreter ownership and runtime scope for extension import, embedding, worker startup and shutdown. Drain/cancel/join work and clear interpreter-owned references before finalization. Destruction after shutdown must not call into a finalized interpreter. A process-global OnceLock containing Python references is not a restart policy; never reuse interpreter-bound objects with a different interpreter.

Assess the original repeated-initialization fixtures early. Process isolation of independently executable tests is allowed infrastructure only when it preserves their meaning; it cannot remove a same-process restart requirement asserted by a test or source API. Do not assume PyO3 supports every restart pattern. Subinterpreters are not automatically required by multithreading; support them only if source contracts require them, and record the boundary.

### Errors, cancellation, and partial effects

At every Rust/Python/Bevy/worker boundary, map source return codes, false/error results, exception classes, callback error handling, panic propagation and lock-poison handling. Separate recoverable source errors from fatal invariant violations. A recoverable failure cannot silently become a panic, poisoned runtime, or unconditional success.

Record whether cancellation occurs before an effect, after a committed effect, or during an operation with source-defined partial results. Preserve required cleanup and result/exception delivery. Do not report “cancelled with no effect” after mutating authoritative state. Every accepted task needs a terminal result or explicit shutdown disposition; callbacks cannot execute against destroyed state.

<a id="sequence"></a>

## 8. Early feasibility and implementation sequence

### First dependency gate

Before expanding architecture around a disputed assumption, review these known cases from the selected source revisions and create precise dependency entries in the existing work queue:

| Case | Required early result |
| --- | --- |
| Synchronous tasklet suspension and `blue.synchro.Yield()` loops | Source-supported execution strategy, affected original cases, and explicit unresolved semantic questions. |
| `reference/blueexposure/tests/cpp/TestBlueSmartPy.cpp` and related headers | Route from unchanged C++ fixtures/assertions through narrow adapters to actual Rust/PyO3 behavior; no second production binding framework. |
| Its Python initialize/finalize fixture lifecycle | Supported embedding/restart/isolation boundary without changing test meaning. |
| `tests/python/bluetests/test/test_paths.py` | Explicit disposition of `testResolvePath_CaseMismatch`, `testResolvePath_CaseMismatchMultipleCandidates`, their `linux2` guards, and existing unconditional skips. No global platform spoofing. |
| `tests/python/bluetests/test/test_taskletext.py::test_set_exception_notification_handler` | Account for the top-level function and its discovery/signature issue; do not move it into a class or invent execution credit without approval. |
| Carbon core interfaces consumed by streams/classes | Finite source-backed external boundary and providers, including inherited identity/lifecycle obligations. |
| Parallel mutable calls, wrapper identity and weak-reference/deletion cases | Receiver, ownership and lifecycle design capable of preserving the defined contract; identify any concrete evidence gap for a human decision. |

These are feasibility obligations, not claims that every case is impossible. Use source analysis, compilation and existing original tests. Record a supported path or the exact pending decision before dependent broad implementation proceeds. Continue work independent of that decision. Do not postpone these already-visible constraints until final packaging.

### Implementation order

1. Reconcile current work, adopt source/contract bindings, establish safe writer ownership, close the initial applicability/configuration decisions, and complete the feasibility gate for the first path.
2. Establish the unified build and a complete path through object creation, identity, registration, an interface/base relationship, lifecycle, PyO3 exposure and Bevy-managed state, using relevant original tests.
3. Complete dependency-ready subsystem batches, each with canonical owners, required Python exposure, Bevy integration, compilation and applicable original cases.
4. Close remaining source/configuration obligations, build installed packages, run complete applicable original suites/configurations, verify integrated publication and audit every acceptance predicate.

The inventory—not this illustrative list—defines full behavior: metadata/discovery; interfaces/inheritance; copying and lifetime; time/pumping/tasklets/timers; events/callbacks; memory/file/network/remote streams; paths/resources/caches/background loading; marshaling/black/dictionary/YAML persistence and structured rows; statistics, accumulators, logging, diagnostics, process/OS interfaces and private utilities.

No declaration, registry marker, TODO, empty callback, unconditional success, state-only facade or delegate to a missing body receives implementation credit. Required behavior cannot hide behind a disabled optional feature.

### Speed and maintained mechanisms

CGP means Context-Generic Programming. CGP, proc-macro tooling, derive/delegation helpers and generators are optional. Select the approach that minimizes expected time to complete the remaining project, including setup, debugging, repeated use, compilation, correction and maintenance. Do not optimize one quick batch at the expense of recurring manual repair.

Before a substantial optional tooling investment, record a brief cost/reuse estimate, a bounded trial, and a stop condition. Reassess actual cost; sunk cost is not a reason to continue a losing framework. No benchmark campaign is required. Prefer existing tools and small focused scripts; avoid speculative translator frameworks and broad installation work.

For code actually generated, version its inputs, mapping rules and generator, make output deterministic, and fix the generating source rather than only overwritten output. Handwritten Rust remains allowed. Tooling difficulty never reduces feature scope, mapping fidelity or required original-test obligations.

<a id="tests"></a>

## 9. Original tests and bounded execution

**Use successful production compilation and the original Blue and BlueExposure tests. Preserve original assertions, expectations, fixtures and data. Adapt infrastructure around them. Do not add tests, rewrite assertions, weaken expectations, or remove failures merely to make the migration pass.**

Keep the reference tests byte-preserved. Original test code is the default executable material. Permitted infrastructure includes build/link configuration, module loading, fixture registration, Linux execution support, process isolation that preserves test meaning, packaging routes, and narrowly scoped adapters calling actual Rust behavior.

### Preserve the subject and meaning of execution

Separate discovery from execution. Original discovery scripts may install mock modules solely to collect cases; those mocks must not remain on the production execution path. Execute against the intended Rust extension/native artifact and required real helper modules. Record loaded module locations and digests plus relevant adapters; confirm fixture/package imports have not replaced the implementation after its initial import.

Review loader hooks, monkeypatches, fixture changes and transitive shims as semantic changes, even when the test file is unchanged. An adapter must expose real results, not expected answers, substitute implementations, forced outcomes or swallowed errors. A transform that changes what an assertion means requires the same human decision as editing that assertion.

For original C++ suites, record the fixture subject and a concrete adapter/build route to Rust/PyO3. Do not count tests linked to original production bodies as tests of Rust. Do not automatically translate assertions into Rust or rebuild the retired production binding framework. Where unchanged tests cannot reasonably reach the migrated subject, submit the exact conflict for a human decision. Source-preserved C++ fixture infrastructure does not itself authorize a second production implementation.

### Reconcile definitions, discovery, selection, and execution

Keep these distinct sets with explicit links:

1. Source-defined test occurrences, including top-level functions, duplicates, malformed/uncollected definitions, inherited cases and parameterization sites.
2. Cases discovered by the original runner and the reason a source occurrence is shadowed, uncollected or unavailable.
3. Requested executable cases/configurations for this run.
4. Cases actually started and their terminal results.

Use repository, path, fixture/class, name, occurrence, parameter and configuration identities. Line/span data is provenance, not the sole identity. Do not credit two shadowed definitions as two executions. Parameterized instances have distinct runtime identities linked to their original definition.

A nonempty requested selection that executes zero cases is an infrastructure failure even if the runner returns success. Unexpected missing selections, import/discovery errors, truncation or extra substitutions must be diagnosed. An intentionally empty batch has no behavioral credit and cannot satisfy an original-test gate.

Report `passed`, `failed`, `skipped`, `undiscovered`, `blocked`, and `human-approved exception` separately. Track interrupted/timed-out execution explicitly as an incomplete run, not a pass. Every required source test occurrence needs a discovery/applicability disposition, and every selected executable case needs a terminal result. Existing skips stay visible. Platform-only deferrals need source-backed reasons, retaining portable assertions as obligations.

Known `linux2` guards and unconditional skips require the early decisions in [section 8](#sequence). Do not spoof `sys.platform` or suppress skips globally. Missing infrastructure/dependencies never count as passing tests.

### Finite execution and environment failures

Before launching each potentially blocking build/test operation, record its command, selected cases, finite wall-time limit, expected source waits, output/log destination and recoverable process/session handle. Derive a longer limit from source-defined waits or observed legitimate duration; do not leave the limit unspecified. Use an external watchdog when the tested runtime itself may deadlock.

Poll progress through bounded tool calls, normally no longer than 60 seconds, so the agent can report and checkpoint. The process may outlive an individual poll within its recorded limit. At timeout, capture diagnostics, stop or preserve the specifically identified process under a recorded recovery action, and mark the run incomplete. A finite extension needs current evidence of progress or a source-backed duration correction. Re-poll the existing handle before relaunching; never kill unrelated processes.

Record external prerequisites: network endpoints, filesystem conditions, permissions, time/environment assumptions and services. For example, the original network stream test's external HTTP dependency is not controlled by Rust. Distinguish implementation failures from unavailable prerequisites without rewriting responses or asserting success.

Default to no automatic retry of an unchanged failure. One diagnostic retry is permitted when a documented transient environment condition changes or needs confirmation; retain both results. Further identical retries require a changed input or new diagnosis. Do not select only the eventual green result.

### Human decisions and evidence limits

For each incompatibility provide the original identity/path/span, exact assertion or dependency, command/configuration, actual failure or code-level contradiction, relevant Rust path, classification, smallest resolution and consequences. Obtain explicit permission before changing, disabling, removing, replacing or semantically bypassing an original test. Store approved adaptations outside immutable references.

If a concrete scenario makes compilation and original tests insufficient—for example, a required concurrent mutation/lifecycle path that they never exercise—identify the exact obligation and ask what additional verification the human wants. Do not preemptively add unit, stress, fuzz, parity, differential, mutation, benchmark or formal-proof campaigns. Continue independent work while the decision is pending.

Keep implementation/source review, compilation and actual original-test coverage as separate evidence channels for each acceptance requirement. A reviewed-only concurrency obligation is not reported as exercised. Absence of an original test does not waive implementation, and chosen tests do not prove all concurrency interleavings.

<a id="records"></a>

## 10. Durable records, receipts, and continuation

### One canonical record and safe writer ownership

Reuse existing equivalents; otherwise use:

| Artifact | Role |
| --- | --- |
| `migration/correspondence.json` | Canonical source/applicability/mapping/relationship/integration record, decisions and evidence links. |
| `migration/work_queue.json` | One dependency queue with batch ownership, status, blockers and exact next actions. |
| `migration/CONTINUATION.md` | Concise current checkpoint and how to resume. |
| `migration/receipts/` | Immutable compilation, original-test, reconciliation, transaction and publication evidence. |

Extend existing data with a versioned migration; do not discard records or create separate Bevy/Python/platform acceptance catalogs. Views and reports derive from the same identities. [Appendix B](#record-spec) defines required fields and recovery semantics.

Before mutation, determine whether another agent/process owns the worktree or canonical records. Prefer an isolated worktree and scoped milestone branch for concurrent code work; preserve and deliberately reconcile required uncommitted work rather than silently starting from an obsolete HEAD. There remains one authoritative integration queue/record, with scoped contributions merged through its writer.

For shared mutation, use a single-writer lock/ownership record containing chat, worktree, branch, process/session identity and claimed paths. Confirm the previous owner's actual liveness before reclaiming it; elapsed time alone is not permission. Capture expected parent/content digests and recheck before overwriting or staging. Unexpected changes require reconciliation, not a reset. A snapshot isolates builds; cooperative lock files alone do not exclude uncooperative writers.

### Input-to-artifact-to-result chain

Before a run, identify the complete relevant input closure: production source, original helpers, tests/fixtures/data, adapters, generator inputs and rules, build scripts/features/configuration, lockfile and dependencies, compiler/tools, interpreter executable/configuration/GIL state, relevant environment values, host ABI and runtime prerequisites. Record actual values or digests without disclosing secrets. An input affecting semantics cannot be omitted because it is outside Rust `src/`.

Build from an immutable snapshot when concurrent changes cannot be excluded. Otherwise enforce writer ownership and compare the input identity before and after the operation. Before/after hashes alone cannot detect transient edits restored during a run; use a snapshot or reliable exclusion for that case.

A successful build receipt records the inputs, command, tool/configuration identity, exit code, log and exact output digests. A test receipt references that successful build receipt and those loaded/installed artifacts, identifies its own test/runtime inputs, and records actual case results. A stale extension in a runtime directory cannot inherit current source credit merely because it loads successfully.

Check relevant identity after execution. Changed, failed, interrupted, incomplete or truncated runs do not receive current success. Preserve unsuccessful observations with their real status. Acceptance requires a continuous, inspectable relationship from declared source inputs to the built artifact, installed artifact, original-test result and integrated publication.

Reuse success only when its relevant semantic inputs and output artifacts match. Define conservative input sets per recipe; expand them when a newly discovered dependency matters. Do not use HEAD alone or omit Python/bootstrap/fixture dependencies. Progress prose, receipt additions and bookkeeping-only changes are not automatically semantic build inputs; do not create self-invalidating receipts. A contract-policy change requires reevaluating acceptance and affected evidence, not automatically recompiling unrelated unchanged code.

### Atomic updates and recovery

Version schemas and distinguish implementation, review, compilation, tests, packaging and publication statuses. Write immutable run receipts first. Update canonical JSON through validated temporary files and atomic replacement, preserving recoverable committed state. All three progress artifacts carry the same generation identifier.

Use the committed generation in `correspondence.json` as the progress commit point. Before a grouped update, write a durable transaction receipt with previous/new generation, expected parent digests, receipt IDs, and recoverable before/after payloads or snapshot locations. Prepare and validate next queue/checkpoint views, replace those atomically, and replace the canonical record last. Flush files and directory entries where supported. This is file-update infrastructure, not a second lifecycle controller.

On continuation, reconcile mismatched generations before treating status as authoritative. If the canonical record committed the new generation, recover its queue/checkpoint from the transaction payload. If it still has the old generation, restore old committed views; independently valid run receipts remain available for explicit reconciliation. If parent/content identities do not match because another writer intervened, preserve both states and resolve ownership instead of guessing or overwriting. Never infer approval or completion from a prepared transaction.

Schema migrations preserve entity identities, source pins, decisions and receipts, record the migration/version, and are recoverable. Unsupported versions are a concrete infrastructure issue, not permission to initialize an empty catalog.

### Continuation loop

At the beginning of every turn/continuation:

1. Read native Goal state, contract binding, branch/status, writer ownership, source pins, committed generation, checkpoint and relevant queue/mapping slice.
2. Reconcile user steering, changed inputs, interrupted operations and outstanding decisions. Check live process handles and current receipt validity before restarting work.
3. Select a dependency-ready batch with explicit source obligations, acceptance evidence and owned paths. Resolve its early feasibility dependencies first.
4. Implement its canonical behavior and real Bevy/Python path, compile production artifacts and run relevant original cases.
5. Record actual review/build/test outcomes and unresolved symbols; publish a verified milestone when ready.
6. Commit consistent progress state with the exact next command or source responsibility, then continue useful work while the native Goal permits it.

Persist blocker fingerprints, distinct consecutive turn observations, independent-work assessment and live operation handles. Reset the consecutive-blocker sequence after authorized resumption or a material change in the condition. Polling the same live process is not a new independent attempt.

Checkpoint before handoff/compaction or a budget boundary. Keep updates factual and concise. A status question does not cancel the objective. Do not re-read whole catalogs, duplicate completed work, repeat unchanged failures, or repeat broad successful checks without a changed input or unresolved concern.

<a id="platform"></a>

## 11. Portable host support, builds, and packaging

### Linux acceptance without distribution coupling

The first complete acceptance environment is the actual Linux development host. At V2 authoring it is x86_64 CachyOS with GNU libc; those observations are not permanent dependency requirements. At execution record the actual target triple, architecture, distribution snapshot, kernel, libc, filesystem assumptions, toolchain, interpreter and relevant dynamic libraries.

Keep the core independent of OS and distribution identity. Prefer portable Rust/Python APIs and maintained cross-platform facilities. Isolate unavoidable OS behavior behind source-linked adapters with explicit contracts. Avoid CachyOS-specific code, distribution-name/version branches, private system APIs, undocumented layouts, and unnecessary dependencies on newly introduced OS features. Prefer capability checks where a real optional facility must be detected.

If a source obligation cannot be implemented portably with maintained facilities, document the exact requirement, alternatives considered, necessary capability, adapter boundary and compatibility consequences. Support the actual development host at that time. Do not freeze the project to an old CachyOS snapshot as the default solution to rolling updates. An OS-specific mechanism cannot silently change Blue behavior.

Record the environment that passed, not an invented broad Linux compatibility claim. Do not declare the observed glibc/kernel version the minimum supported version merely because it is installed. Determine real ABI/system-library requirements from built artifacts and dependencies; use accurate package compatibility tags. A host-specific binary requirement does not justify putting distribution logic into the portable core.

Use reproducible Rust/dependency/interpreter environments where practical while allowing the host OS to update. A relevant host/runtime/library update changes environment identity and invalidates affected results; refresh the fingerprint, rebuild affected binaries where ABI/linkage changed, and rerun affected original cases. Review the entire input closure when impact cannot be bounded. Do not require a new cross-distribution test matrix without a human decision.

Windows/macOS-only requirements remain recorded future obligations. Portable behavior originating in platform-specific source stays required for Linux. Avoid introducing new platform coupling that would make later support unnecessarily difficult.

### Separate build modes and actual outputs

Derive exact build commands from the maintained toolchain and current source requirements. Record a recipe for each applicable output:

| Mode | Required distinction |
| --- | --- |
| Native Rust library/consumer | Build the actual library and required consuming executable/interface; resolve runtime ownership and linking explicitly. |
| Python extension | Build/install the extension for the selected free-threaded interpreter and correct ABI/platform tags. |
| Embedded Python host | Link/configure the host appropriately for embedding, including initialization/finalization and interpreter location. |
| Original-test adapters | Build narrow fixture/FFI infrastructure against the real corresponding Rust artifacts; keep test-only code identifiable. |

A global extension-only link setting must not accidentally apply to embedding/native consumers. Follow the selected PyO3 release's current [build/distribution guidance](https://pyo3.rs/v0.30.1/building-and-distribution.html); use its supported per-artifact configuration rather than assuming a historical feature flag works for all outputs. Do not claim that `cargo check` or one successful feature combination builds every consumer mode.

Build actual release/package artifacts. Package the unified runtime/library and Python deliverables with required helper modules, data, licenses, notices, public API documentation, build instructions and dependencies. Keep fixtures/adapters distinct from production deliverables. Package registry or deployment publication is not authorized by this contract; local packaging and the Git milestones below are authorized.

For final acceptance, install the actual candidate into an isolated environment and execute applicable original tests through those installed artifacts. Verify import/library identities so the source checkout or a stale runtime copy cannot shadow the package. Development-tree tests remain useful batch evidence; they do not establish installed-package completeness. Native/embedded original cases must likewise consume the candidate outputs. Preserve assertions and fixture meaning.

### Serialization/configuration matrix

For every source serialization family and compatibility mode, record format identity/version, byte order/widths, numeric conversions, object/reference identity, encoding, construction/persistence hooks, malformed-input/error handling and production activation mechanism. Link each to applicable original cases and configurations.

Selecting a test expectation with an environment variable does not prove that the production serializer selected the same mode. Record both build/runtime configuration and the loaded artifact providing it. Include `PY27_COMPATIBILITY_MODE` and other source-defined variants where required. Preserve old data compatibility without adding an obsolete Python runtime. Generic Rust/serde values are not substitutes for exact source bytes or identity semantics.

<a id="publication"></a>

## 12. Milestone publication and human decisions

### Verified integration

Use the authorized Blue remote and `blue-rs-dev` integration branch. Check remote identity, access, branch protections and Git metadata writability early. Leave `main` and upstream BlueExposure untouched.

Prefer scoped verified commits/pushes. If protections or safe concurrent development require branches/PRs, use `codex/blue-<milestone>` branches targeting `blue-rs-dev`, with explicit stacked dependencies, and merge after required checks/reviews. Do not bypass protection or claim an open PR is integrated.

Stage only intended owned changes, preserving unrelated dirty/staged files and the user's guidance edit. Do not force-push, rewrite unrelated history or discard work. Contract invocation authorizes ordinary milestone publication and necessary PR communication; do not ask repeatedly for permission already granted. An actual tool/approval/access restriction must be identified as that restriction.

For each milestone, bind:

- The tested production input/tree identity, affected original-test selection and valid receipts.
- The local commit and publication operation.
- The actual remote integration commit/tree and PR merge state where applicable.
- The visible development checkout and its expected content.

Verify remote state separately from local success. After merge/rebase or intervening changes, compare relevant integrated inputs against the tested inputs. Reuse evidence only when identical; otherwise rebuild/rerun affected original checks. Metadata/receipt-only commits do not require recompiling unchanged production inputs, but their relation to the tested tree must be explicit.

A partial CI badge is batch evidence only. It cannot stand in for complete original-suite acceptance. If publication is blocked, preserve local work and continue useful implementation; full completion still requires integrated remote publication.

### Exact approval and exception accounting

Ask only for missing information, a concrete irreconcilable conflict, or approval explicitly required here. Routine implementation/build/mapping choices that preserve the contract are already authorized.

A decision request must identify source/test obligations, evidence, attempted approaches, smallest proposed change, consequences for behavior/structure/names/tests/platform scope, and independent work that can continue. Do not request a vague waiver for “legacy compatibility.”

Record the user's actual decision with its identifier, provenance, date, affected source/configuration/test IDs and precise authorization:

- A test-only exception changes test accounting, not implementation behavior.
- A behavioral/API/structural exception changes only the explicitly authorized obligation and its final parity qualification.
- A platform/scope exception cannot hide portable behavior without that explicit authorization.
- Permission for additional verification specifies its actual scope; it is not a general new test campaign.

Pending, inferred or assistant-proposed exceptions are not approved. Keep original obligations visible and link approved replacements instead of deleting history. Apply the same exception semantics in mappings, queue, test results, all affected acceptance gates, and the final report.

An authoring-time correction to this contract is not evidence that the runtime issue is resolved. The decisions in [section 8](#sequence) must still be made from current source and execution evidence.

<a id="acceptance"></a>

## 13. Acceptance and completion

Before final acceptance, freeze a candidate identity containing adopted contract/decisions, source/applicability/configuration set, semantic input fingerprints, dependency/version observation, host/runtime identity, artifacts and integrated content. Reconcile all records to that candidate.

For every acceptance obligation, record whether its support comes from implementation/source review, compilation, original tests, packaging inspection or remote publication. Do not merge those channels into an unexplained “verified” flag.

Evaluate the original requirement unless an exact human-approved exception applies. For an approved replacement, evaluate the authorized replacement and qualify the parity claim. A test-only exception never waives the implementation predicate. Pending decisions and unresolved required obligations prevent completion; unrelated work continues under the Goal rules.

| Gate | Required result |
| --- | --- |
| A01 — Unified implementation | Both libraries are implemented in the Blue workspace; no sibling checkout, gitlink or original C++ production dependency. References, licenses and provenance are intact. |
| A02 — Complete source scope | Every file/body/configuration and consumed external contract has a justified disposition. No unresolved required region or silently reduced applicability set remains. |
| A03 — Exact canonical correspondence | Every required Blue-specific entity/responsibility has exactly one canonical Rust counterpart. Behavioral, structural and nominal correspondence all hold, including names, public/private boundaries, owners, interfaces, bases, overrides and shared state. |
| A04 — Actual declaration reconciliation | Forward/reverse source-to-Rust reconciliation is current, with no canonical collisions, missing bodies, unowned production items or unsupported relationship claims. |
| A05 — BlueExposure and Python identity | PyO3 replacements are explicit; Blue-specific discovery, registration, type/object identity, conversion, properties, callbacks, copying, persistence and lifecycle are implemented. |
| A06 — Bevy integration | Every applicable subsystem has a real vertical/horizontal production path with authoritative state, scheduling, resources and callback semantics. Headless Linux works. |
| A07 — Modern concurrency | Default runtime is free-threaded with recorded GIL state after required imports. Ownership, borrowing, tasklet/context behavior, parallel work, async boundaries, cancellation and shutdown preserve required contracts. |
| A08 — Portable host design | The current Linux host/target is identified; the core avoids unnecessary OS/distribution/version coupling. Required platform adapters and future Windows/macOS obligations are explicit. |
| A09 — Maintained versions and mechanisms | The Bevy version meets the timestamped newest-stable gate. Compatible maintained Rust/CPython/PyO3 dependencies are pinned. Deprecated production macros and recreated generic binding machinery are absent. |
| A10 — Build and package | Every required native/extension/embedding/adapter mode builds. Actual final packages install with their required contents and correct artifact identities. |
| A11 — Original tests/configurations | Complete applicable original suites/configurations execute successfully against the candidate, subject only to exact approved exceptions. Required skipped, missing, blocked, zero-case, interrupted or stale results do not count as passes. |
| A12 — Evidence continuity | Review/build/test/package receipts match current semantic inputs and actual artifacts. Discovery, loaded modules, configurations, results and freshness are reconciled. |
| A13 — Verified publication | Completed milestones are integrated into remote blue-rs-dev with evidence valid for that content. Visible checkout, main, upstream BlueExposure and unrelated work are accounted for and preserved. |
| A14 — Truthful terminal state | Queue, checkpoint, committed generation and live Goal agree. No required placeholder, omitted method, empty callback, hidden disabled feature, unapproved exception or unfinished obligation remains. |

**One-to-one equivalence remains behavioral, structural, and nominal at acceptance. A compilation success, matching API list, populated registry, or passed subset of tests is insufficient.** Do not complete merely because a milestone finished, the budget is nearly exhausted, or the prompt's procedures were followed without the required outcome.

On success, use the native completion tool and report implemented scope, mapping/applicability totals, evidence by channel, selected versions and actual Python/host mode, complete original-test results/configurations, exact exceptions, packages, published commits/PRs and visible branch, future platforms, and required tool-reported usage. Describe the result as implementation review, successful compilation and original-test evidence—not formal proof or proof of every concurrency interleaving.

If a gate fails, continue useful work, seek its exact required decision, or follow the genuine blocker policy. Do not fabricate completion.

<a id="naming"></a>

## Appendix A. Mechanical identity and naming specification

This is mapping-rule version 2. Apply it uniformly to original entities and actual Rust declarations. Preserve existing compliant names and IDs through explicit aliases/migration history where the record format changes; do not silently reinterpret previous mappings.

### A1. Canonical source identity

Use a stable repository identifier, source-qualified declaring owner/name, declaration kind and canonical signature/specialization descriptor. Keep revision, path/span, macro provenance and configuration as linked provenance/variant information. For internal-linkage or anonymous/local entities, add the original relative path and a deterministic owner-local discriminator; line numbers alone are never sufficient. Declaration/definition references for one entity share its ID.

Serialize descriptors as UTF-8 JSON with sorted object keys, no insignificant whitespace, preserved case, and ordered arrays. Normalize text to the source language's identifier semantics and record the original spelling. Never normalize raw source bytes for provenance.

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

For Blue-specific Python callables, retain ordered positional-only, positional-or-keyword, keyword-only and variadic parameters, their observable names, and binding mode. Preserve default expressions/values in the call contract and annotation spelling where present; use an explicit dynamic-type marker where the source has no static type. Do not apply C++ parameter-name erasure or invent static type information for Python signatures. Original test definitions retain their own execution identities instead of becoming new Rust tests.

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
2. When raw spelling is not legal, encode the original UTF-8 bytes as lowercase hexadecimal prefixed by `__blue_`. Record the original spelling and escape. This covers otherwise unsupported keyword/nested/operator spellings without arbitrary names.
3. Preserve namespace paths as module paths. When Rust cannot directly express a nested type, put it in an auxiliary sibling module named `<mapped-owner-name>__types`, recursively applying this rule for deeper type nesting and rule 9 for collisions. The original declaring-owner edge remains explicit; the auxiliary module is not a second canonical owner type.
4. Within each source overload family, give every overload the base name followed by `__sig_` and the first 12 lowercase hexadecimal digits of SHA-256 of its canonical callable descriptor. Do not select one arbitrary overload to keep an unsuffixed canonical name.
5. Constructors use `new` when unique, or `new__sig_<digest-prefix>` for an overload family. Preserve construction variants, defaults, errors and source links. Convenience constructors are auxiliary.
6. A source destructor maps to the corresponding lifecycle/Drop implementation and its explicit source effects; implicit field destruction and helper functions are recorded mechanics. A source-visible explicit destruction operation remains its own canonical callable.
7. Operators map to the appropriate native Rust trait method when its signature and behavior fit. Otherwise use a named method with a base formed by the escape in rule 2 and the same overload rule. Conversion operators include the conversion target in their descriptor. Additional operator convenience implementations are infrastructure.
8. Non-callable templates/specializations preserve their generic owner; distinct nominal specializations that need separate Rust types use `__spec_` plus the descriptor digest prefix. Do not invent separate types for ordinary uses of the same generic contract.
9. Resolve collisions in the actual Rust symbol namespace. A generated name yields to an otherwise valid preserved original name. Extend generated digest prefixes by four hexadecimal digits until unique. For normalization collisions between preserved spellings, use their reversible byte escapes. If a full digest still collides, append `__id_` and the hexadecimal UTF-8 encoding of the complete stable source identity. Never silently merge.
10. Preserve Python-visible source names/signatures independently through PyO3 facilities. Rust overload suffixes do not leak into Python APIs unless the source exposed them.

The record provides reversibility; a hash by itself does not. Check all candidate names against the complete known namespace before publishing the mapping. Newly discovered collisions trigger explicit rule/application migration and affected reconciliation. Keep prior names as optional compatibility aliases only when they preserve the canonical distinction.

### A3. Logical and concrete target identity

Record each actual Rust item's qualified path, kind, source span/generated origin, visibility, translated signature and configuration. For methods, record both:

- Logical owner: canonical self type, declaring trait where applicable, and the original declaring/override owners.
- Concrete impl item: complete self/trait arguments, generics/where constraints, cfg conditions, module/file and deterministic item discriminator.

Do not force a one-to-one relationship between C++ classes and the number of Rust impl blocks. Preserve their types, contracts and method ownership through actual Rust constructs.

A property counterpart is the corresponding owner-bound Rust/PyO3 property implementation, with actual accessor/descriptor paths and state effects, not a registry-only marker. Source-declared accessors retain their own method mappings. Namespace/relationship metadata must likewise reference real declarations.

For runtime objects, one source-visible object identity corresponds to one canonical Rust instance identity. Multiple interface views or Python wrappers are aliases to it where the source requires aliasing. Copying/creation that produces a new source identity must produce the corresponding distinct instance; reference-wrapper creation must not accidentally clone state.

### A4. Relationship and naming review

Record and reconcile declaration ownership, type/base/interface graphs, implementation/override origin, property/accessor links, physical and logical state ownership, visibility and Python exposure. Review overloaded `RegisterClasses`, `UnregisterClasses`, `FindClsid`, constructor families and multiple-interface fixtures against these exact rules.

Generated and handwritten code follow the same mapping. A rule-version change records which entities, aliases, generated output and reviews are affected. This appendix supplies deterministic mapping policy; it does not require an additional behavioral test suite.

<a id="record-spec"></a>

## Appendix B. Record and receipt contract

These are minimum logical fields, not a demand to replace compatible existing infrastructure. Reuse existing field names through a documented schema mapping; otherwise use the names below. Adopt `format_version: 2` for a V2 schema, retain prior snapshots, and update readers/writers together. Tools that still write an older schema must not silently erase new fields.

### B1. Canonical correspondence record

| Field group | Required content |
| --- | --- |
| `format_version`, `generation`, `previous_generation` | Schema and committed progress identity, with parent linkage. |
| `contract_binding` | Native chat/objective, V2 path/hash/version, adopted amendments and decision references. |
| `source_pins`, `source_files` | Origins, revisions/archive identities, raw digests, path/mode/encoding provenance, overlays, extraction/configuration coverage and exclusions. |
| `mapping_rules` | Naming/normalization version, extractor/tool identity and explicit application history. |
| `entities` | Stable source identity/signature, owners, source references, role, visibility, fields/state, relationships, responsibility set, applicability, canonical target and auxiliary/provider links. |
| `python_identity` on affected entities | Exposed names, bases/protocols, wrapper/object identity, callable/property behavior and owning interpreter boundary. |
| `integration` on affected entities/subsystems | Real Bevy/Python paths, state authority, schedule/clock/callback/resource/concurrency policies and source-linked review. |
| `original_tests` | Source occurrences, discovered/selected/executed identities, configuration, applicability, terminal status and receipts. |
| `decisions` | Exact human approval provenance, scope, affected IDs, replacements and acceptance consequences; pending decisions remain pending. |
| `receipts`, `acceptance` | Immutable receipt references and separate per-obligation review/build/test/package/publication outcomes and limits. |

Each Blue-specific responsibility has an identifier within its original owner's responsibility set and exactly one target responsibility under the corresponding owner. Several responsibilities implemented by one source method remain distinct annotations on that method's counterpart; they are not an excuse to invent extra canonical methods or merge unrelated owners.

Implementation status distinguishes `unresolved`, `planned`, `partial`, and `implemented`. Review status distinguishes unreviewed, current reviewed, discrepancy and stale. Compilation, original-test, packaging and publication statuses remain separate. `implemented` alone never means accepted. Source applicability and mechanism replacement are separate from all of these statuses.

### B2. Queue and checkpoint

A batch records its ID, source/configuration/relationship obligations, dependencies, owned paths/writer, expected parent/input identity, implementation and validation work, receipts, unresolved decisions, publication status and exact next action.

A blocker records its fingerprint, affected obligations, condition/evidence, first and consecutive distinct Goal-turn observations, last material change, attempted alternatives, live handles, independent work remaining and exact unblock requirement. A resumed blocked Goal starts a new observation sequence.

The checkpoint records the committed generation, live Goal binding last observed, branch/worktree, source/dependency/host changes, current batch, successful and incomplete operations, unresolved symbols/decisions, publication state and the next command. It remains concise; detailed data stays in the canonical record/receipts.

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

No new custom database, parallel lifecycle engine or separate subsystem catalogs are required. Extend the existing records and use small deterministic serialization/reconciliation tools only where they save work.

<a id="findings"></a>

## Appendix C. Finding resolutions F001–F048

These rows map the V1 audit to operative V2 rules. They record corrections to the execution contract, not claims that implementation defects have been repaired. Runtime feasibility questions still require the source/evidence and exact decisions specified above. The complete rule is in the linked section; this table does not replace it.

| Finding | Audited issue | Operative V2 correction |
| --- | --- | --- |
| F001 | The one-to-one relation has no defined domain or allowed transformation algebra | [Rule](#correspondence): Entity bijection, owner-bound obligation mapping, explicit mechanism exclusions and separately marked auxiliary items; no merging of Blue-specific entities. |
| F002 | Composition and supertraits do not specify dispatch and interface identity | [Rule](#correspondence): Base/interface identity, query failure, root identity, shared state and base-to-derived dispatch must have explicit production paths. |
| F003 | The stated identity of an impl block is not a unique Rust item identity | [Rule](#naming): Logical method ownership is distinct from concrete impl identity, including generic constraints, cfg and item discriminators. |
| F004 | Overload and special-member naming is delegated rather than specified | [Rule](#naming): Fixed signature descriptors, language-specific normalization, escapes, overload/constructor/operator rules and deterministic collision resolution. |
| F005 | Native representation changes lack a borrowed-buffer and numeric-boundary contract | [Rule](#correspondence): Owned/borrowed storage, alias visibility, lifetimes, lock/unlock operations, widths, signedness and numeric error behavior are required boundary data. |
| F006 | The public API separation requirement has no public-surface definition | [Rule](#correspondence): Derive and record actual Rust/Python exports, visibility and source owners; keep incidental ecosystem machinery private. |
| F007 | Mechanical mapping can still end as an unverified self-authored manifest | [Rule](#correspondence): Reconcile source entities/bodies and actual Rust declarations in both directions, including relationships and orphan infrastructure. |
| F008 | Source pin recording does not require comparison to the pinned Git object | [Rule](#sources): Compare raw reference bytes with Git/archive authority; separate overlays, relocation, modes and encoding from clean pins. |
| F009 | There is no operational closure method for macros, templates, and configurations | [Rule](#sources): Close file/body/macro/template/configuration coverage with extraction provenance, unresolved regions and lossless raw-byte identities. |
| F010 | External boundary closure has no concrete stopping rule | [Rule](#sources): Bound external work by consumed contracts and necessary transitive semantics, with a source and provider for every obligation. |
| F011 | Reference immutability and AGENTS propagation need an explicit precedence boundary | [Rule](#sources): Explicit guidance-mirroring exclusions protect immutable references, third-party snapshots and generated/cache/tool directories without rewriting root guidance. |
| F012 | Disposition labels do not define when an obligation is required | [Rule](#sources): Separate role, applicability, mechanism and status; freeze candidate applicability and retain portable obligations and authorized scope history. |
| F013 | Deep and broad integration has no subsystem-level completion evidence | [Rule](#bevy): Every subsystem records actual canonical owners, authoritative state, Bevy facilities, schedules, API paths and evidence. |
| F014 | Synchronous calls and Bevy-exclusive state have no linearization protocol | [Rule](#bevy): Record visibility/completion points, exclusive access, owner-local synchronous paths, cross-thread waits and reentrant callback phases. |
| F015 | System ordering alone does not preserve subscriber ordering | [Rule](#bevy): Preserve subscriber order, snapshot/mutation rules, nested dispatch and SendEvent/PostEvent timing; observer order is not assumed. |
| F016 | Clock and pump integration lacks a phase and unit mapping | [Rule](#bevy): Record clock units, epochs, precision, scale, rebase/pause semantics, update phases and pump/timer readers. |
| F017 | Asset/resource integration omits ownership and completion semantics | [Rule](#bevy): Resource identity, handle ownership, load/completion/cancel/reload state, eviction and release share one authority. |
| F018 | Parallel work admission has no capacity or shutdown-drain policy | [Rule](#bevy): Require source-compatible admission, suspended-stack capacity, queue ownership and finite shutdown/drain behavior. |
| F019 | Tasklet replacement feasibility is deferred until after architecture commitment | [Rule](#sequence): Synchronous tasklet strategy and relevant original cases are early dependencies; async/free threading alone cannot replace stack suspension. |
| F020 | Thread-safe pyclass storage can still reject valid parallel calls | [Rule](#python): Shared pyclass receiver/borrow design must resolve contention without introducing unsourced borrow failures or a global interpreter lock. |
| F021 | Task-local context is not distinguished from thread-local state | [Rule](#python): Task identity, inherited context, current-task lookup and timer stacks remain independent of worker-thread identity. |
| F022 | Weak references, cycles, and finalization need an explicit cross-runtime policy | [Rule](#python): Specify cross-runtime strong/weak edges, GC traversal, logical liveness, physical reclamation and source-visible deletion/finalization behavior. |
| F023 | The Python type graph is not independently mapped from the Rust graph | [Rule](#exposure): Map Rust and Python graphs separately and link type/instance identity, ancestry, descriptors, wrappers and real underlying objects. |
| F024 | Interpreter ownership and restart behavior are unspecified | [Rule](#python): Define extension/embedding interpreter ownership and shutdown/restart boundaries; resolve repeated-init original fixtures early. |
| F025 | Error propagation does not define panic, poisoning, and partial-effect boundaries | [Rule](#python): Map source errors, exceptions, panic/poison handling and cancellation/partial-effect outcomes at each execution boundary. |
| F026 | Unchanged test bytes do not guarantee an unchanged validation path | [Rule](#tests): Separate discovery mocks from execution and record transitive loaded modules/adapters; semantic harness changes require exact approval. |
| F027 | The test denominator can miss source cases or accept zero execution | [Rule](#tests): Reconcile definitions, discovery, selection, starts and terminal results; nonempty selections with zero execution fail infrastructure. |
| F028 | The exact-test rule has known Linux applicability conflicts that are not surfaced early | [Rule](#sequence): Known linux2 guards, unconditional skips and uncollected cases become early applicability/approval obligations with no automatic bypass. |
| F029 | Original C++ tests and PyO3 retirement need an early feasibility decision | [Rule](#tests): Each C++ suite needs an unchanged-test adapter route to Rust/PyO3 or a precise human decision; no retired production framework. |
| F030 | The execution loop has no bounded wait or test-process timeout policy | [Rule](#tests): Every blocking run has a finite limit, recoverable handle, bounded polling, watchdog/diagnostic policy and incomplete timeout outcome. |
| F031 | Build and test receipts are not required to prove a continuous artifact chain | [Rule](#records): Build inputs precede execution; successful build receipts bind exact outputs, which parent the loaded/installed original-test receipts. |
| F032 | Acceptance claims lack per-requirement evidence attribution | [Rule](#acceptance): Attribute each acceptance obligation to review, compilation, actual original tests and other specific evidence, preserving their limits. |
| F033 | External test conditions have no reproducibility or failure-classification policy | [Rule](#tests): Record external prerequisites and failure classes; no unchanged automatic retries, fabricated responses or selective green-only reporting. |
| F034 | Freshness-aware reuse lacks a semantic input closure | [Rule](#records): Recipe-specific semantic input closure includes helpers, fixtures, configuration, tools and host/runtime inputs; reuse requires matching artifacts. |
| F035 | The Goal objective is not bound to an immutable contract version | [Rule](#goals): Bind native chat/objective to adopted contract path/version/hash and actual decisions; detect changed contracts and preserve lineage. |
| F036 | Matching paused or blocked Goals fall through the activation instructions | [Rule](#goals): Explicit activation behavior covers absent, active, paused, blocked, completed, limited, unrelated and unavailable/unknown states. |
| F037 | Durable records have no atomic update or schema-migration rules | [Rule](#records): Version schemas, write immutable receipts first, atomically replace progress with a canonical commit point and recover mismatched generations. |
| F038 | Preserving dirty files does not establish ownership of a shared worktree | [Rule](#records): Use isolated worktrees or explicit single-writer ownership, expected-parent checks, immutable build snapshots and deliberate integration. |
| F039 | Three-turn blocker accounting and long-running operation identity are not durable | [Rule](#goals): Persist blocker fingerprints, distinct consecutive turn observations, independent-work assessment, live handles and resumption reset. |
| F040 | Published milestone evidence is not explicitly tied to the tested integration tree | [Rule](#publication): Compare tested inputs with actual remote integrated content; post-merge changes invalidate affected evidence and partial CI stays partial. |
| F041 | Approved exceptions are not reconciled with absolute final parity gates | [Rule](#publication): Apply exact approved exceptions to every affected predicate; test-only exceptions never waive behavior and parity reports remain qualified. |
| F042 | Linux acceptance does not name an architecture or operating-system baseline | [Rule](#platform): Accept the actual Linux host while requiring an OS-independent core, justified adapters and accurate tested-host versus minimum-ABI claims. |
| F043 | Extension and embedded-Python build modes are not separately specified | [Rule](#platform): Separate native, extension, embedding and test-adapter outputs and linking recipes using supported selected-version PyO3 facilities. |
| F044 | Packaging has no installed-artifact execution boundary | [Rule](#platform): Final original tests consume installed candidate artifacts with verified import/library identities and complete package contents. |
| F045 | Newest-release acceptance lacks an explicit finite observation boundary | [Rule](#bevy): Resolve stable releases at start and a timestamped finite final version gate; update/revalidate when that gate observes a newer candidate. |
| F046 | Serialization compatibility has no format/configuration acceptance matrix | [Rule](#platform): Bind each source serialization/data mode to real production configuration, exact format/identity semantics and original cases. |
| F047 | The speed rule optimizes a batch without accounting for whole-project cost | [Rule](#sequence): Optimize total remaining project cost with bounded optional-tool trials, reuse estimates and stop conditions; handwritten Rust remains valid. |
| F048 | The sequence does not prioritize already-visible feasibility blockers | [Rule](#sequence): Place known tasklet, C++ fixture, Linux skip, interpreter-lifetime and external-boundary uncertainties ahead of dependent expansion. |

<a id="requirements"></a>

## Appendix D. Preserved requirements U01–U22

The requirement identifiers preserve the accepted V1 decisions. The host policy also incorporates the user's V2 clarification: avoid OS/distribution/version coupling, and use the actual development host where an OS-specific facility is unavoidable.

| Requirement | Preserved decision | Governing section |
| --- | --- | --- |
| U01 | Every required Blue-specific entity and responsibility has one canonical counterpart. | [Rule](#correspondence) |
| U02 | Behavioral, structural and nominal equivalence apply simultaneously. | [Rule](#acceptance) |
| U03 | Preserve names, state/method owners, interfaces, bases, overrides and responsibilities. | [Rule](#correspondence) |
| U04 | Use Rust structs/traits/supertraits/composition and distinguish logical ownership from actual impl items. | [Rule](#naming) |
| U05 | Inventory both complete libraries, private bodies, configurations and exposure machinery. | [Rule](#sources) |
| U06 | One Blue-rooted Cargo workspace contains both Rust implementations and pinned references. | [Rule](#sources) |
| U07 | Reuse maintained PyO3 directly and retain only required Blue-specific adapters/policy. | [Rule](#exposure) |
| U08 | Modernize mechanisms while preserving defined observable Blue behavior. | [Rule](#correspondence) |
| U09 | Bevy owns substantive vertical/horizontal execution and state integration. | [Rule](#bevy) |
| U10 | Newest stable Bevy is resolved, pinned and rechecked at a dated final gate. | [Rule](#bevy) |
| U11 | Free-threaded concurrent, parallel, async and multithreaded Python is the default. | [Rule](#python) |
| U12 | Canonical synchronous contracts remain; async adapters are additional infrastructure. | [Rule](#python) |
| U13 | Deprecated production macros are replaced with maintained facilities. | [Rule](#exposure) |
| U14 | Tooling serves fastest complete delivery; CGP/generation and handwritten Rust are optional. | [Rule](#sequence) |
| U15 | Successful compilation and original tests remain the verification standard. | [Rule](#tests) |
| U16 | Preserve original tests and require exact approval for semantic changes or retirement. | [Rule](#tests) |
| U17 | Linux/current-host acceptance comes first; portable design remains required and Windows/macOS remain future obligations. | [Rule](#platform) |
| U18 | Use native Goal lifecycle, one queue/checkpoint and durable, current evidence. | [Rule](#goals) |
| U19 | Publish verified milestones to blue-rs-dev while preserving main and upstream BlueExposure. | [Rule](#publication) |
| U20 | Preserve user guidance and unrelated implementation work, including concurrent writers. | [Rule](#records) |
| U21 | Prompt authoring/review does not activate implementation or silently replace an active contract. | [Rule](#authority) |
| U22 | Report evidence channels, exceptions and publication separately; never call them formal proof. | [Rule](#acceptance) |

<a id="launcher"></a>

## Appendix E. Copyable Goal launcher

Invoke this command only to start or explicitly adopt the implementation objective. Reading or delivering it does not activate implementation. It references V2 directly; the preserved V1 launcher is unchanged. Inspect/reuse the live Goal and bind this file's actual hash under [section 2](#goals). No token budget is implied.

```text
/goal Reimplement Carbon Engine's Blue and BlueExposure together in Rust in /home/astral/Projects/blue, following /home/astral/Projects/blue/BLUE_RS_REIMPLEMENTATION_GOAL_PROMPT_V2.md in full. Complete Linux acceptance on the actual development host while keeping the core independent of OS/distribution/version assumptions. Preserve behavioral, structural, and nominal one-to-one correspondence, canonical names and ownership, complete type/interface/base relationships, deep vertical and horizontal Bevy integration using the newest stable release under the contract's version policy, and free-threaded concurrent, parallel, async, multithreaded Python by default. Reuse PyO3, preserve synchronous and observable Blue contracts, resolve early feasibility dependencies, and choose tools for fastest complete delivery. Compile and package actual production artifacts, pass the applicable original tests without unauthorized changes, preserve source and user work, and publish verified milestones into blue-rs-dev. Bind this contract version and evidence to the native Goal, continue dependency-ready work, record exact blockers and human-approved exceptions, and mark complete only after every V2 acceptance gate is satisfied.
```

Authoring completion means this document has been produced and checked. It does not mean Blue has been implemented, its original suites passed, or its milestones published.
