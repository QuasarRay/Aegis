# Rust agent-orchestration ecosystem for Aegis

## Executive conclusion

After looking beyond the obvious “Rust port of LangChain” projects, I would **not** build Aegis around a single Rust LangChain/LangGraph clone.

Your requirements point to a different architecture:

**Codex should remain the actual coding-agent harness. Aegis should become the deterministic orchestration, policy, evidence, context, skill, and verification layer around Codex.**

That distinction materially changes which Rust projects are attractive.

OpenAI now exposes the same Codex harness that powers its first-party experiences through **Codex app-server**, a documented bidirectional protocol. A client can create and resume threads, start and steer turns, stream events, interrupt work, and answer approval requests. The server speaks a JSON-RPC-style protocol over local stdio/JSONL by default; the protocol is generated from the Rust implementation in the open-source Codex repository. citeturn642379search0turn642379search2turn642379search3

For Aegis, my recommended stack is therefore:

| Layer | Recommendation | Confidence |
|---|---|---:|
| Coding agent / reasoning harness | **Codex app-server** | **Very high** |
| Aegis orchestration state machine | **A small Aegis-owned Rust state machine**, borrowing ideas from **Swiftide Tasks** and **graph-flow** | **Very high** |
| General Rust LLM/agent primitives | **Rig** | **Very high** |
| RAG/indexing infrastructure | **Swiftide**, selectively | **High** |
| Skill/tool discovery layer | **OpenAI Skills + MCP**, optionally borrowing ideas/code from **Thulp** | **High** |
| Direct LangChain compatibility | **langchain-rust** only if actually needed | Medium |
| Direct LangGraph compatibility | **Juncture** as a reference implementation, not Aegis's foundation | Medium |
| Large all-in-one LangChain/LangGraph clone | Avoid as Aegis's central dependency for now | High |

There is one particularly important finding: **Rig has evolved into something unusually well aligned with Aegis.** Its current agent runner executes tool calls with concurrency **one by default**, has serializable/resumable agent runs, lifecycle hooks, usage accounting, persisted memory, recording/replay, `AGENTS.md` support, and native discovery of Agent Skills stored under `.agents/skills`. citeturn741182search0turn741182search2turn741182search8turn741182search9

However, because the real target is *Codex-assisted migration work*, I would still place Rig **below Codex app-server**, rather than replacing Codex with a Rig agent.

The architecture I would pursue is roughly:

```text
                          AEGIS
                            │
          ┌─────────────────┴─────────────────┐
          │                                   │
   deterministic workflow               policy engine
          │                                   │
          ├── phase/state machine              ├── one active worker
          ├── artifact ledger                 ├── token budgets
          ├── evidence ledger                 ├── allowed transitions
          ├── migration map                   ├── tool permissions
          └── verification ledger             └── completion gates
                    │
                    ▼
             Codex app-server
                    │
               one thread/turn
                    │
                 Codex
                    │
        ┌───────────┴────────────┐
        │                        │
     Skills/MCP             repository tools
        │                        │
   exact references          Kani / Cargo /
   source corpus             tests / git / CPG
```

The most important recommendation from this research is consequently:

> **Do not make LangGraph the brain of Aegis. Make Aegis a deterministic Rust controller whose graph contains agentic nodes, and use Codex as the agent executing those nodes.**

That architecture matches your serial-agent requirement, makes discarded work preventable, allows token budgets to be enforced outside the model, makes every phase resumable, and avoids duplicating functionality that Codex already implements.

## What Aegis actually requires from an orchestration framework

Most agent frameworks optimize for capabilities that are almost the opposite of your project.

LangGraph itself is designed as a durable engine for stateful agent workflows and explicitly supports multi-agent coordination, parallel graph execution, persistence, human intervention, and fault tolerance. citeturn263497search2turn263497search3 Aegis needs only a subset of those properties.

For Aegis, I would prioritize these characteristics, in this order.

| Requirement | Importance |
|---|---:|
| Absolutely deterministic **single-worker execution** | Critical |
| Persistent phase/checkpoint state | Critical |
| Exact provenance of outputs | Critical |
| Idempotent/resumable steps | Critical |
| Explicit token/tool/iteration budgets | Critical |
| Ability to prevent model calls before prerequisites exist | Critical |
| Structured output / schemas | Critical |
| Tool-call interception before side effects | Critical |
| Strong observability and audit log | Critical |
| Context assembly under an explicit budget | Critical |
| Skill discovery with progressive disclosure | Critical |
| Local-first persistence | Very high |
| MCP support | Very high |
| RAG over large documentation corpora | Very high |
| Human approval / interrupt | High |
| LangGraph API compatibility | Low |
| LCEL compatibility | Low |
| Parallel agents | **Negative feature for Aegis** |
| Supervisor/swarm orchestration | **Negative feature for Aegis** |

That last point is important. A framework advertising sophisticated fan-out, supervisor agents, autonomous delegation, or swarm coordination is not necessarily better for Aegis. In several cases it is additional behavior you would need to disable or prevent.

Your orchestration problem is closer to a **durable compiler pipeline** than to a general multi-agent platform:

```text
discover
   ↓
extract-original-model
   ↓
freeze-mapping
   ↓
derive-specifications
   ↓
approve-specifications
   ↓
implement-one-unit
   ↓
verify-one-unit
   ↓
record-equivalence
   ↓
advance
```

The model should choose details *inside* permitted states. It should not choose the workflow itself.

That is why Swiftide's `ConcurrencyModel::Sequential`, graph-flow's one-step-at-a-time execution, and Rig's default single-tool execution are unusually relevant to your design. Swiftide explicitly provides `Sequential` and `Parallel` scheduling modes, with `Sequential` completing one branch before another is allowed to run. citeturn519699search10turn519699search11 graph-flow lets each node return `Continue`, which advances a single edge and returns control to the caller, allowing state to be persisted after every operation. citeturn595891view0 Rig's `AgentRunner::tool_concurrency` defaults to one, making its normal tool execution serial rather than concurrent. citeturn741182search0

Those semantics are far more useful to Aegis than maximum fan-out throughput.

## The Rust ecosystem ranked for Aegis

I would divide the ecosystem into four classes rather than putting everything into one leaderboard.

### Foundation-quality candidates

| Project | Maturity | Aegis fit | Role I would assign |
|---|---:|---:|---|
| **Rig** | Very high | **Excellent** | Agent/model/tool primitives |
| **Swiftide** | High | **Excellent** | Typed sequential workflows + RAG |
| **graph-flow** | Medium-high | **Excellent for workflow control** | Durable explicit state machine |
| **langchain-rust** | High | Moderate | LangChain compatibility |
| **Codex's own Rust harness/app-server** | Very high for your actual target | **Exceptional** | Primary coding-agent runtime |

Rig currently has about 9,000 GitHub stars, millions of reported crate downloads, more than 200 contributors, an active release cadence, and released `0.46.0` on October 31, 2026. citeturn349693search0turn448480search0 Its CI includes a fast pull-request gate, nightly all-feature builds, minimum-dependency checks, cassette-based provider tests, and security-advisory work. citeturn448480search3 These are unusually strong maturity signals for a Rust LLM framework.

Swiftide is much smaller but still established: the repository currently shows roughly 790 stars, 70 forks, and nearly 900 commits, with v0.33.0 published October 14, 2026. citeturn448480search4turn448480search5 It combines agents, typed task graphs, and streaming indexing/query pipelines rather than focusing only on chat agents. citeturn349693search2

graph-flow is narrower. It has around 380 stars and under 100 commits, but its implementation is particularly relevant to Aegis because workflows can deliberately stop after each node, serialize their state, and resume later. It also validates graph construction, has task timeouts, execution-step limits, conditional transitions, and optimistic concurrency protection. citeturn595891view0

The older `langchain-rust` remains the most established direct LangChain-style implementation, with approximately 1,300 stars and more than 570 commits. It supports chains, agents, persistent SQLite/PostgreSQL memory, vector stores, document loaders, tracing, and provider-neutral tool calls. citeturn178998search1turn194654search0turn194654search1 It is a sensible library when compatibility with familiar LangChain abstractions matters, but it does not give Aegis the most useful workflow semantics.

### Technically impressive but not yet foundation-quality

| Project | Why interesting | Why I would not build Aegis on it yet |
|---|---|---|
| **Juncture** | Probably the strongest direct LangGraph semantic port | Explicitly describes itself as early-stage |
| **langchainrust** | Extremely broad LangChain + LangGraph surface | Small adoption, aggressive release churn |
| **Synaptic** | LCEL + StateGraph + RAG + middleware + MCP | Only a handful of GitHub users/stars |
| **TinyAgents** | Durable graph + budgets + SQLite + testkit | GPL and contradictory maturity documentation |
| **atomr-agents** | Extremely complete architecture | Tiny community/adoption |
| **agent-framework-rs** | Impressive Microsoft Agent Framework port | Very new, virtually no external adoption |
| **metalcraft** | Clean LangGraph-style Rust graph | Very small and early |

Juncture implements a genuine Pregel-style execution model, typed state reducers, checkpointing, human interrupts, `Send` fanout, subgraphs, streaming modes, SQLite/PostgreSQL savers and observability. citeturn695099search4 Its own roadmap, however, still lists “production hardening” and error recovery/resource limits as unfinished work. citeturn695099search4 That makes it an excellent **design/reference repository** for Aegis, but a questionable core dependency.

`langchainrust` is unusually broad. Its v0.28.0 release contains separate crates for agents, LangGraph, MCP, guardrails, sessions, evaluation, RAG, A2A and vector stores, and advertises durable SQLite/PostgreSQL/Redis graph checkpoints, interrupts, time travel, plan-execute agents and context compaction. citeturn360612search0turn360612search1 However, the project has around only twenty GitHub stars according to docs.rs metadata, and the latest v0.28.0 documentation build currently fails on docs.rs. citeturn360612search0 Its release velocity is remarkable—versions moved from 0.1 in January to 0.28 by late October 2026—but that also indicates significant API churn. citeturn360612search0

Synaptic has perhaps the most attractive *paper feature set*: LCEL composition, `StateGraph`, serial and parallel tool executors, persistent graph checkpoints, human-in-the-loop, RAG, evaluation, MCP, context condensation and interceptors. citeturn943016view0 But the repository currently has only four GitHub stars and one fork. citeturn943016view0 For a project where reliability is valued over experimentation, I would treat it as a source of ideas rather than foundational infrastructure.

TinyAgents deserves a closer look because its requirements line up surprisingly well with Aegis. It includes token and dollar budgets, model/tool-call limits, deterministic test utilities, context/cache controls, durable graph runs, SQLite storage and a host-controlled policy boundary. citeturn365152search0turn365152search3 Its tool execution is also conservative: tool concurrency is opt-in, with tools reporting whether they are concurrency-safe, while the trait defaults to false. citeturn365152search2 However, the repository is GPL-3.0-only, its crates are not published to crates.io, and its own documentation includes a graph specification describing parts of the runtime as a “milestone-1 scaffold,” while other documents describe a much fuller graph implementation. citeturn365152search0turn365152search6 I would therefore audit the actual code before depending on it.

`atomr-agents` is architecturally fascinating. It has token/time/money/iteration budgets, context assembly under a `TokenBudget`, skills, checkpointed channel state, retrieval, memories, evaluation suites, artifact registries and many agent strategies. citeturn741158search1 It released binaries and Python wheels as v0.21.0 in June 2026, but the repository currently has only two stars and no forks. citeturn695099search2turn695099search3 It is closer to an advanced research platform than a conservative dependency choice.

The independent Rust port of Microsoft's Agent Framework is also worth watching. It implements Pregel-style workflows, checkpointing, human-in-the-loop, sequential orchestration, MCP, Responses API support, middleware, retries and many other features. citeturn279092search0turn279092search2 Its authors maintain a detailed parity matrix and explicitly separate stable and experimental features. citeturn279092search3 But it currently has essentially no community adoption, despite nine releases through v0.8.0. citeturn279092search1turn279092search4 I would study its workflow engine, not place Aegis on top of it yet.

### Useful auxiliary projects

Two projects outside the LangChain/LangGraph clone category deserve special mention for Aegis.

**Thulp** is a Rust execution-context/tool framework. It provides tool discovery, JSON-Schema validation, MCP/OpenAPI adapters, multi-step skill workflows, `SKILL.md` parsing, query-based capability filtering, hooks, retry logic and file-backed sessions. Its repository reports explicit test counts across its individual crates. citeturn349693search7 It could be useful if you decide that Aegis should own a generic capability registry independent of whichever agent runtime is active.

**Aether** is a Rust coding-agent harness focused on explicit context ownership. Agents start without a fixed prompt/tool set; prompts are composed from Markdown files and tools arrive through MCP. It can operate headlessly or as an ACP server and exposes a Rust library. citeturn349693search5 I would not replace Codex with it, but its context-design philosophy is relevant to your goal of making token consumption deliberate and inspectable.

### Projects I would exclude from the critical path

I would not use RustGraph or Metalcraft as foundational dependencies today. RustGraph currently shows only one commit and a couple of stars, despite implementing many familiar graph concepts. citeturn849900search0 Metalcraft currently has roughly twenty commits and essentially no adoption. citeturn448480search8

Likewise, I would not choose Kalosm as the orchestration layer. It is a substantial Rust AI project with around 2,200 stars, but its primary focus is local pretrained-model execution rather than durable software-engineering agent orchestration. citeturn349693search1

## Rig, Swiftide, and graph-flow in the context of Aegis

### Rig is the strongest general-purpose Rust agent dependency

Rig is the ecosystem project I would most confidently put into Aegis's dependency graph.

The reasons go beyond popularity.

Its current `AgentRunner` is serial by default for tool execution. `.tool_concurrency(n)` exists, but the default is one; sequential runs preserve call order and stop when a terminating failure occurs. citeturn741182search0turn741182search1

That aligns directly with your “only one agent/subagent may work at a time” rule.

It also has a serializable `AgentRun`. An interrupted run can be persisted and resumed; the runtime records message history, usage and run state. citeturn741182search2turn741182search4 Its memory layer supports persistence, detects competing writes, and refuses to silently overwrite a conversation that changed after it was loaded. citeturn741182search7

For cost control, `AgentRun::usage()` reports accumulated model token usage. citeturn741182search4 Rig also exposes typed hooks capable of inspecting or stopping runs before provider/model/tool actions, rewriting requests and handling malformed tool calls. citeturn741182search3turn741182search5 Those are exactly the seams where Aegis can enforce state-machine permissions and budget policy.

There is an even stronger reason: modern Rig's coding-agent layer understands **`AGENTS.md` and Agent Skills directly**. Its `AgentsMdPlugin` loads repository-local instructions, while `SkillsPlugin` discovers `SKILL.md` files from `.rig/skills`, `.agents/skills`, user-level skill directories and related locations. Full skill instructions are loaded only when needed. citeturn741182search9

Rig additionally implements context compaction, structured checkpoints and provider prompt-cache-aware conversation handling. Its default coding-agent logic preserves newer context while summarizing older content when the context window approaches its limit. citeturn741182search9 Recording/replay support through `rig-cassette` provides effect logs and checkpoints, while the coding-agent session system writes activity, usage and compactions incrementally and contains recovery behavior for interrupted tool executions. citeturn741182search10

For Aegis, I would use Rig for things such as:

```text
aegis-rig
├── auxiliary non-Codex model calls
├── cheap classifier calls
├── embeddings
├── structured extraction
├── optional local-model fallback
├── deterministic tool wrappers
└── test doubles / cassette replay
```

I would **not** let Rig autonomously orchestrate the migration. Aegis should own that state machine.

### Swiftide is the strongest complementary framework

Swiftide is particularly attractive because it combines three useful things:

**typed workflows, agent tooling, and ingestion/RAG.**

A `Task` is a typed execution graph and supports pause/resume. Swiftide explicitly offers a `ConcurrencyModel` with a `Sequential` variant that runs one runnable branch to completion before starting another. citeturn519699search0turn519699search11

That means Aegis can define something like:

```text
AnalyzeOriginalProject
        ↓
FreezeObjectInventory
        ↓
ExtractTests
        ↓
DeriveKaniSpecifications
        ↓
ReviewSpecifications
        ↓
GenerateRustObject
        ↓
VerifyCorrespondence
        ↓
CommitArtifactLedger
```

and enforce that only one of these steps can execute at any point.

Swiftide's agent layer also supports lifecycle hooks, stop conditions, MCP tools, local/custom executors, human approval and explicit message history. citeturn519699search3turn519699search7

Its other major advantage for Aegis is ingestion. Swiftide has streaming loaders, chunkers, transformations, embeddings, retrieval pipelines, Qdrant, Redis, LanceDB, PgVector, DuckDB and Redb integrations. citeturn349693search2 You therefore do not need a Python Haystack/RAGFlow service merely to index Rust documentation.

A significant limitation is durable graph state. Swiftide tasks retain execution state in the `Task` value, and its docs describe pause/resume, but its task runtime is not presented as a fully transactional durable workflow engine in the same way LangGraph is. citeturn519699search0turn519699search1 You would likely need Aegis-owned persistence around the workflow state.

For your use case that may actually be preferable.

### graph-flow is possibly the best model for the Aegis state machine

graph-flow is much smaller than Swiftide or Rig, but its execution semantics fit Aegis exceptionally well.

A task can return:

- `Continue`: move one edge and return control.
- `ContinueAndExecute`: continue within the same call.
- `WaitForInput`: park.
- `GoTo`: explicit transition.
- `End`: finish. citeturn595891view0

For Aegis I would almost exclusively use **`Continue`**.

That would create this transaction boundary:

```text
load state
    ↓
execute exactly one phase
    ↓
validate output
    ↓
write evidence/artifacts
    ↓
advance state
    ↓
persist
    ↓
return control
```

That is nearly ideal for avoiding duplicated work.

The graph builder validates topology, supports per-task timeouts and maximum chained-step counts, and `FlowRunner` implements load → execute → save semantics. citeturn595891view0 Persistent PostgreSQL storage has optimistic locking, so competing session updates are rejected rather than silently overwriting each other. citeturn595891view0

Its biggest problem for Aegis is that PostgreSQL is the built-in durable backend; in-memory storage is the other included option. citeturn595891view0 For a laptop-first Aegis, I would want SQLite.

Fortunately, `SessionStorage` is an abstraction, so implementing an Aegis-specific SQLite backend would be straightforward in principle. citeturn595891view0

There is also a documented durability issue with `ContinueAndExecute`: the state is written after a chained sequence finishes, meaning a process crash can rerun the first node of the chain. citeturn595891view0 That reinforces my recommendation to never use chained execution inside Aegis. Execute and commit one phase at a time.

### Why I would not start from Juncture

Juncture is probably the project I would study most closely while designing Aegis's graph abstractions.

Its execution model is closer to real LangGraph than graph-flow or Swiftide: it has Pregel scheduling, channels/reducers, typed state, `Command`, `Send`, interrupts, checkpoints, stores, streaming and subgraphs. citeturn849900search5turn695099search4

But Aegis does not actually need Pregel.

Pregel's superstep model is particularly valuable when multiple ready vertices can be executed in the same logical step. Your requirement explicitly forbids that kind of concurrent work.

So the closest LangGraph implementation is **not** necessarily the best Aegis implementation.

Juncture also explicitly identifies production hardening as remaining work. citeturn695099search4

Use it as a specification/reference repository for:

```text
checkpoint identity
state reducers
interrupt semantics
history/time travel
graph compilation
routing validation
state versioning
```

not necessarily as a runtime dependency.

## Codex integration changes the architecture

This is the most consequential finding in the research.

Earlier architectures often treated Codex CLI as something another agent framework would invoke through MCP. That is now outdated. OpenAI notes that the old Codex MCP-server approach was removed/deprecated for new integrations and recommends the SDK or app-server instead. citeturn448174search0turn448174search1

For Aegis, **Codex app-server is the appropriate interface.**

The official documentation says app-server is specifically intended for applications that need persistent conversations, streaming events, interruptions, tools and approval handling. citeturn448174search2turn642379search0

It is especially convenient for Aegis because the implementation itself is Rust. OpenAI's open-source repository includes `codex-app-server` and a separate `codex-app-server-protocol` Rust crate internally. citeturn642379search3turn642379search4

The local protocol flow is simple:

```text
Aegis
  │
  ├── spawn `codex app-server`
  │
  ├── initialize
  │
  ├── thread/start
  │
  ├── turn/start
  │
  ├── consume streamed events
  │
  ├── answer approval requests
  │
  ├── collect artifact/evidence result
  │
  └── persist Aegis phase
```

The standard local transport is newline-delimited JSON over stdio. WebSocket mode exists but remains experimental/unsupported for production workloads, which is irrelevant to your laptop-local design anyway. citeturn642379search1

Codex can generate a version-specific JSON Schema bundle for the app-server protocol, meaning an Aegis build can generate strongly typed Rust protocol structures rather than maintain handwritten loose JSON. citeturn642379search1turn642379search6

That is the integration I recommend.

### Aegis should not become another coding-agent harness

Codex already has the difficult harness pieces:

- thread state,
- turn state,
- model interaction,
- filesystem/shell tooling,
- streaming,
- approvals,
- context handling,
- conversation persistence,
- agent execution semantics. citeturn642379search0turn642379search2

Reimplementing those in Aegis would produce duplication and create exactly the wasted engineering you want the project to avoid.

Aegis should instead decide:

```text
WHAT MAY HAPPEN NEXT
WHAT EVIDENCE MUST EXIST FIRST
WHAT CONTEXT CODEX RECEIVES
WHAT SKILLS ARE AVAILABLE
WHAT FILES MAY BE CHANGED
WHAT OUTPUT SCHEMA IS REQUIRED
WHAT VALIDATION MUST PASS
WHEN WORK IS CONSIDERED COMPLETE
```

Codex decides:

```text
how to perform the permitted engineering step
```

This is a much cleaner responsibility boundary.

### Goal and Plan integration

Codex Goals are persisted thread-scoped state containing an objective, lifecycle, budget and progress information; completion is intended to be checked against concrete evidence. citeturn491410search1

That maps very closely onto Aegis.

However, Aegis should not make Codex's Goal state its canonical project state.

I would map:

```text
Aegis Migration Goal
        ↓
Aegis immutable objective
        ↓
Current Aegis phase
        ↓
Codex Goal for that phase
```

rather than:

```text
Codex Goal = whole Aegis project state
```

Codex Goals belong to threads rather than being global project-state storage. citeturn491410search1

Similarly, Plan mode should be used as an agent behavior inside a controlled phase. OpenAI describes Plan as selecting/proposing the implementation path, whereas Goals capture the outcome that must be reached. citeturn150072search2

Thus:

```text
AEGIS = authority
GOAL  = phase completion contract
PLAN  = proposed path inside phase
CODEX = executor
```

That separation prevents the model from altering the process that is supposed to constrain it.

## Recommended Aegis architecture

I would design Aegis as a Rust workspace with sharply separated crates.

```text
aegis/
├── crates/
│   ├── aegis-core
│   ├── aegis-workflow
│   ├── aegis-ledger
│   ├── aegis-codex
│   ├── aegis-context
│   ├── aegis-skills
│   ├── aegis-retrieval
│   ├── aegis-policy
│   ├── aegis-migration
│   ├── aegis-kani
│   ├── aegis-cpg
│   ├── aegis-architecture
│   └── aegis-cli
│
├── .agents/
│   ├── skills/
│   ├── rules/
│   └── references/
│
└── AGENTS.md
```

### `aegis-core`

No LLM dependency.

Contains stable identifiers and types:

```rust
ProjectId
SourceArtifactId
TargetArtifactId
OriginalObjectId
RustObjectId
MethodId
TestCaseId
HarnessId
RequirementId
EvidenceId
WorkflowId
PhaseId
CodexThreadId
```

This is critical. Do not let object correspondence live as freeform Markdown.

The strict one-to-one migration relationship should be represented mechanically:

```rust
struct ObjectCorrespondence {
    original: OriginalObjectId,
    rust: RustObjectId,
    mapping_kind: MappingKind,
    evidence: Vec<EvidenceId>,
    status: CorrespondenceStatus,
}
```

No implementation phase should advance unless the expected mapping invariants hold.

### `aegis-workflow`

This should be small.

I would either:

**A. implement it directly**, inspired by graph-flow,

or

**B. use graph-flow initially and replace it later only if necessary.**

The state machine should have no parallel transition primitive.

Do not merely set concurrency to one.

**Do not expose parallel execution in Aegis's public orchestration API at all.**

For example:

```rust
trait AegisStep {
    type Input;
    type Output;

    async fn prepare(...);
    async fn execute(...);
    async fn validate(...);
    async fn commit(...);
}
```

And every operation:

```text
prepare
 ↓
invoke Codex
 ↓
validate
 ↓
commit
 ↓
checkpoint
```

No later state should become reachable until `commit` succeeds.

### `aegis-ledger`

This may ultimately be more important than the graph engine.

Use SQLite.

I would store at least:

```text
projects
source_objects
source_methods
source_tests
target_objects
correspondences
workflow_runs
workflow_steps
codex_threads
codex_turns
artifacts
artifact_hashes
evidence
verification_runs
kani_harnesses
skill_invocations
context_packages
token_usage
decisions
```

Before the agent performs anything expensive:

```text
desired artifact
    ↓
does a valid artifact with matching inputs already exist?
    │
   yes ──► reuse
    │
    no
    ▼
execute
```

This is the mechanism that actually satisfies “prevent duplicated work.”

Prompt instructions cannot reliably guarantee that.

### `aegis-codex`

Implement the app-server client here.

Use stdio, not WebSocket.

The documented app-server protocol begins with `initialize`, then supports thread lifecycle and turn lifecycle operations and emits streamed notifications. citeturn642379search0turn642379search1

Generate the protocol schema from the exact installed Codex version:

```text
codex app-server generate-json-schema --out ...
```

OpenAI explicitly documents this version-specific schema generation. citeturn642379search1

Then generate or validate Aegis Rust structures against that schema.

This gives you a version-pinned integration instead of depending on undocumented behavior.

### `aegis-policy`

This crate should control every expensive or destructive operation.

For example:

```rust
enum Permission {
    ReadSource,
    QuerySkill,
    RunSourceTest,
    WriteTargetFile,
    RunCargoCheck,
    RunKani,
    UpdateMapping,
    AdvancePhase,
}
```

Each state explicitly declares permitted operations.

```text
ExtractSourceModel

allowed:
 ✓ read source
 ✓ run source tests
 ✓ inspect docs
 ✓ write source model database

forbidden:
 ✗ implement Rust
 ✗ modify target source
 ✗ create Kani harness not derived from test
```

This is much stronger than telling an LLM “do not start implementing yet.”

Rig's hook architecture offers comparable interception points for its own runs, including pre-dispatch gating. citeturn741182search3turn741182search5 Codex app-server has an approval flow which Aegis can similarly control at its integration boundary. citeturn642379search0turn642379search2

### `aegis-context`

This should construct the exact context package for each Codex invocation.

Do not let an agent independently “remember what it needs.”

Represent:

```rust
ContextPackage {
    objective,
    phase,
    invariant_set,
    relevant_source_objects,
    relevant_tests,
    mapping_entries,
    relevant_skill_refs,
    previous_evidence,
    output_contract,
    allowed_actions,
}
```

Hash the package.

Store it.

Associate the hash with the turn.

Then every result can be traced to the exact context provided to the agent.

### `aegis-skills`

Here I would follow the modern Agent Skills architecture instead of translating books into giant prompts.

OpenAI Skills use a `SKILL.md` containing metadata and instructions, with optional resources, scripts and references. The agent initially sees metadata and loads full instructions only when the skill applies. citeturn491410search4

This progressive disclosure is directly useful for your context constraint.

However, your “zero information loss” requirement means **the skill cannot merely be a summary of the book**.

I would represent each corpus as:

```text
skill/
├── SKILL.md
├── manifest.json
├── index.sqlite
├── sources/
│   ├── source-0001.md
│   ├── source-0002.md
│   └── ...
├── concepts/
├── examples/
└── scripts/
```

`SKILL.md` teaches *how and when to query the corpus*.

It is **not** the corpus itself.

The full licensed/permitted source corpus remains available through deterministic retrieval.

This avoids:

```text
book
 ↓
LLM summary
 ↓
SKILL.md
 ↓
information permanently lost
```

Instead:

```text
book/docs
    │
    ├──── full normalized source
    │
    ├──── structural index
    │
    ├──── lexical index
    │
    ├──── semantic index
    │
    └──── SKILL.md retrieval instructions
```

When exact wording matters, retrieve original material.

When conceptual navigation matters, use embeddings.

When an identifier or symbol is known, use lexical retrieval.

This is closer to achieving your “no information loss” objective.

Rig already implements Agent Skills progressive discovery in its own coding-agent tooling. citeturn741182search9 Thulp also contains dedicated `SKILL.md` parsing and skill-workflow infrastructure if you need a reusable Rust parser. citeturn349693search7

### `aegis-retrieval`

This is where I would actually use Swiftide heavily.

Its indexing/query model already separates loaders, chunking, transformations, embeddings, retrieval and reranking, with support for local or external stores. citeturn349693search2

But I would not rely on vector search alone.

Use three paths:

```text
exact path / heading / symbol
        ↓
     lexical

concept question
        ↓
     semantic

known documentation hierarchy
        ↓
   structural lookup
```

Then fuse results.

That matters for material such as the Rust Reference or Kani docs because exact terminology and section identity can matter more than semantic similarity.

### `aegis-rig`

This can be an optional adapter rather than core infrastructure.

Use it when a task does **not** require a full Codex coding turn.

Examples:

```text
classify source tests
extract structured metadata
rank documentation sections
check mapping consistency
generate embeddings
cheap schema transformation
```

That could substantially lower Codex-credit consumption.

Rig's provider abstraction covers more than twenty model providers, and its agent primitives expose usage, hooks, persistent memory and structured execution. citeturn849900search8turn349693search0

The key principle would be:

> Codex is used only where Codex-quality engineering reasoning is needed.

Everything else should be deterministic code or, where useful, a cheaper structured model call.

## Production-readiness verdict and adoption order

For Aegis specifically, I would rank the technologies like this:

| Rank | Technology | Use |
|---:|---|---|
| **1** | **Codex app-server** | Main agent execution |
| **2** | **SQLite + Aegis-owned ledger** | Canonical durable state |
| **3** | **Aegis-owned sequential workflow controller** | Pipeline authority |
| **4** | **Rig** | Rust LLM primitives, auxiliary reasoning, skills ideas |
| **5** | **Swiftide** | RAG/indexing and possibly typed tasks |
| **6** | **Thulp** | Optional tool/skill registry |
| **7** | **graph-flow** | Either dependency or architectural reference for workflow control |
| **8** | **langchain-rust** | Only where LangChain compatibility provides concrete value |
| **9** | **Juncture** | LangGraph implementation reference |
| **10** | **agent-framework-rs** | Design reference |
| **11** | **TinyAgents** | Research/reference |
| **12** | **langchainrust / Synaptic / atomr-agents** | Watch, borrow ideas, don't anchor project yet |

The ordering is not based only on GitHub popularity. It reflects your specific invariants.

### A key architectural change I recommend to your `AGENTS.md`

I would change the final goal:

> “if necessary, Langgraph + Langchain + Unpythonic must replace raw python code”

to something conceptually closer to:

> **Aegis orchestration MUST be expressed as explicit, typed, durable state transitions. Agent-framework abstractions may be used only where they improve correctness, inspectability, reuse, or context efficiency. LangChain/LangGraph compatibility is not itself a design objective. Parallel agent execution is forbidden at both the workflow and tool-dispatch layers.**

There is no obvious reason for `unpythonic` to be part of Aegis's Rust architecture. The well-known `Technologicat/unpythonic` project is a Python library adding Lisp/Haskell-inspired functional-programming and macro constructs to Python; it is not an agent orchestration framework. citeturn263497search0

If that is the `Unpythonic` you meant, I would remove it from the Aegis platform requirements.

### The resulting dependency philosophy

I would avoid:

```text
Aegis
  ↓
Huge LangChain clone
  ↓
Huge LangGraph clone
  ↓
Agent
```

and use:

```text
                Aegis core
                    │
          ┌─────────┴────────┐
          │                  │
     workflow/ledger       context
          │                  │
          └─────────┬────────┘
                    │
             Codex app-server
                    │
                  Codex

Optional infrastructure:

Rig ───────── model/tool primitives
Swiftide ──── indexing/retrieval
Thulp ─────── skill/tool registry
SQLite ────── canonical durable state
Kani ──────── specification verification
```

This architecture is substantially smaller than adopting an all-in-one agent framework, but it gives Aegis **more** control over the properties you care about.

It also gives you a very important separation of authority:

```text
Aegis decides what is true.
Aegis decides what may happen.
Aegis decides what constitutes evidence.
Aegis decides when a phase is complete.

Codex reasons about how to accomplish the currently permitted task.
```

For a migration system whose highest priorities are **one-to-one structural equivalence, zero duplicate work, controlled context, evidence-derived Kani specifications, strict serial execution, and minimal wasted model credits**, that is a safer foundation than making LangGraph itself the controlling intelligence.
