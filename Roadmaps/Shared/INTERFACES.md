# Version-one controller interfaces

Aegis uses the eleven version-one records in `records.schema.json` at its serialized boundaries. The Python package declares `INTERFACE_VERSION = 1`; its release version follows `framework.toml`. The preserved Destiny CLI and its evidence formats retain their own lineage. A version declaration identifies an interface contract and supplies no proof of behavior.

| Responsibility | Production interface | State and effects |
|---|---|---|
| Project profiles | `roadmap_project.ProjectProfileV1.from_registry` | Validates the existing registered profile; resolves Aegis under the supplied root and retains external projects' declared repositories. |
| Canonical Aegis records | `roadmap_project.ProjectAdapter.read/update` | Uses `.aegis/project.json`, compare-and-swap and the existing `FileTransaction` implementation. Inventory, projection and execution bookkeeping share the `aegis-authority-inventory` transaction-name lock. |
| Compiler and policy | `roadmap.compile_roadmaps`, `roadmap_policy.authorize` | Produces the graph and decisions from preserved requirements and adopted amendments. Does not dispatch a model. |
| Execution | `roadmap_runtime.BudgetLedger`, `roadmap_lease.WorkspaceLease`, `roadmap_work` | Materializes typed source-owned work and retains reservations, native/child creation handles, recovery observations and fencing identity. A scoped local recipe inherits old unscoped attempts only within its current work-unit lifetime; bootstrap A00 can use the native Goal's original creation boundary. |
| Evidence | `roadmap.audit_evidence`, `roadmap_records.validate_record`, `roadmap_verification` | Reconciles actual bound receipts and derives readiness. Producer trust, extraction adequacy and domain verification remain separate obligations. |
| Native Codex | `roadmap_codex`, `roadmap_native` | Observes the actual Goal, turn/configuration, process ancestry and category usage through the existing read-only transport and metadata journal. Full managed dispatch and completed native Plan binding remain A04 work. |
| Knowledge and review | `roadmap_knowledge`, `roadmap_review` | Retains the source corpus, scoped retrieval and review records without adding another project owner. |

`ProjectAdapter.update` merges fields into the registered record and preserves unrelated queue contents. It rejects stale expected bytes, unknown record versions, writer substitution, native objective replacement, scope replacement, lease transfer, erased binding history and decreasing observed native accounting. The adapter verifies a present native owner through the existing workspace lease. `ProjectAdapter.rebind_native_process` transactionally fences a restarted process of the same active native Goal after creation/lifecycle checks; prior owners and native accounting survive. Managed inference lifecycle and Plan integration remain A04 responsibilities.

Blue and Destiny profiles can be inspected through the same typed interface. Their writes require adoption of their actual canonical writer; Aegis does not create replacement Carbon queues. The original Destiny dispatcher and its existing record owners remain available.

## Observing and comparing APIs

`python -B bin/agentctl.py interfaces audit` emits a source-bound observation of every production package module, its declared responsibility, imports, public function/class signatures, lifecycle methods, conditional declaration guards, source hashes and record protocols. Source is parsed and compiled as an AST without importing target modules. Unknown module responsibilities and unsupported interface/schema versions fail explicitly. Private and unused bodies remain in the complete Python/Rust behavioral inventory.

`python -B bin/agentctl.py interfaces compare --baseline-ref COMMIT` binds an immutable baseline commit and reports removed modules/exports, changed signatures or class shape, and changed serialized record contracts. Added modules and added public class methods can be structurally additive. Shadowed declarations remain separate occurrences. These observations establish structural compatibility only. Applicable unchanged original tests supply runtime behavior evidence; current domain proof is required at completion.

`python -B bin/agentctl.py roadmap profile Aegis` shows the effective profile and record writer. Generic record projection remains available, while every normalized spelling of Aegis's registered canonical path routes through the shared adapter. No command above starts a chat or inference turn.

## Python and Rust boundary

The existing typed Python policy, transport, extraction and record facilities are retained. No unused Rust kernel is introduced. `portability build/check` provides the source-bound future Rust proposals described in `PYTHON_RUST.md`; an eventual Rust implementation needs its own semantic and compatibility evidence. Signature observations and migration proposals do not establish cross-language equivalence.

`BudgetLedger.reserve` retains its version-one signature. `reserve_operation`, `journal`, `reservation_record`, `observe_categories` and `metrics` add bound deterministic execution and accounting. `process.observe_process` records the existing supervisor child without replacing its owner. `roadmap_acceptance.assemble_implementation` combines actual current ledger results with a complete scoped output review; its strength remains implementation/runtime acceptance. See [operations](OPERATIONS.md) for lifecycle, usage and recovery boundaries.
