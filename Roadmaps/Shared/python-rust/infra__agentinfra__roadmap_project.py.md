# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 275. Inventory digest: `33b297ab08a13e0dd4dc394da1ed88593063ea74bd1c1bba420963ce42a246ab`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/roadmap_project.py::module::root::Module

Source: `infra/agentinfra/roadmap_project.py:1`; AST `5f25ab4a26840246c9544a0769b9577e68d5f3e6dbbd4c74aa246a2b9448881f`.

Rust module: `infra::agentinfra::roadmap_project`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: AEGIS_RECORD_WRITER, BudgetLedger, FileLock, FileTransaction, INTERFACE_VERSION, Mutation, Path, ProjectProfileV1, WorkspaceLease, a, adopt_managed_runner, allow_create, any, artifacts, authorization_id, before, bind_goal, binding, bool, candidate, canonical, changed, classmethod, cls, confined_path, created, current, dataclass, dict, digest, execution, expected_digest, fields, inspect_process, int, isinstance, k, key, lease, lease_before, len, loads, lock, managed, new_execution, observation, observe_native_owner, observed, old, old_history, owner, path, pid, previous, prior_binding, process_handle, profile, profiles, project, protocol, read_json, record, repository, require, root, self, state, staticmethod, str, tuple, type, updated, user_authorized, uuid, validate_record, value. Outputs/bindings: AEGIS_RECORD_WRITER, INTERFACE_VERSION, a, before, binding, branch, candidate, canonical_record, changed, created, current, declared_repository, execution, k, key, language_boundary, lease, lease_before, lock, managed, new_execution, observation, observed, old, old_history, owner, path, previous, prior_binding, profile, profiles, project, record, repository, root, state, updated, value.
Calls/effect boundaries: BudgetLedger, BudgetLedger(self.root).read, FileLock, FileTransaction, FileTransaction(self.root, [*artifacts, Mutation(path, canonical(updated) + b'\n', expected_exists=before is not None, expected_sha256=expected_digest)], state_dir=self.root / '.aegis/state/transactions', name=AEGIS_RECORD_WRITER).commit, FileTransaction(self.root, [Mutation(lease.path, canonical(state) + b'\n', expected_exists=True, expected_sha256=digest(lease_before)), Mutation(self.profile.path(), canonical(record) + b'\n', expected_exists=True, expected_sha256=digest(before))], state_dir=self.root / '.aegis/state/transactions', name=AEGIS_RECORD_WRITER).commit, Mutation, Path, ProjectProfileV1.from_registry, WorkspaceLease, WorkspaceLease(self.root).assert_owner, adopt_managed_runner, any, before.decode, bind_goal, binding.get, binding.get('observation', {}).get, bool, canonical, changed.get, changed.get('observation', {}).get, cls, confined_path, current.get, dataclass, dict, digest, execution.get, execution.pop, execution.setdefault, execution.setdefault('binding_history', []).append, fields.get, inspect_process, isinstance, lease.path.read_bytes, lease.read, len, loads, lock.acquire, lock.release, managed.get, new_execution.get, observation['goal'].get, observe_native_owner, owner.get, path.exists, path.read_bytes, prior_binding.get, prior_binding.get('observation', {}).get, process_handle, read_json, record.get, require, root.resolve, self._validate_aegis, self.profile.path, self.profile.path().read_bytes, self.read, state['history'].append, str, type, updated.get, updated.get('execution', {}).get, uuid.uuid4, validate_record.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::root.body[0]::Expr

Source: `infra/agentinfra/roadmap_project.py:1`; AST `2aee5f4523788defa856806743ff17f815b1a9619f9ac7e76100f820b48ddcfb`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::root.body[1]::ImportFrom

Source: `infra/agentinfra/roadmap_project.py:7`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::root.body[2]::ImportFrom

Source: `infra/agentinfra/roadmap_project.py:9`; AST `321ed2ed3afceb74be547c9905ed4c676e453b1a68fe7cb2d3e214caeac2624d`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::root.body[3]::ImportFrom

Source: `infra/agentinfra/roadmap_project.py:10`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::root.body[4]::Import

Source: `infra/agentinfra/roadmap_project.py:11`; AST `db14cae1a81ee06a1930fa9f46771b454957916d2bbbc048661adf0613fd70de`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Import evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::root.body[5]::ImportFrom

Source: `infra/agentinfra/roadmap_project.py:13`; AST `f49eec2be7586a81b0fa34570d7cbaa58bc5eeaa5e471a05fac611f36b0ee7bd`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::root.body[6]::ImportFrom

Source: `infra/agentinfra/roadmap_project.py:14`; AST `09d8e9e8f6fd64b1de599cd7bc89a5b39b492565154c1945944f226444aab849`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::root.body[7]::ImportFrom

Source: `infra/agentinfra/roadmap_project.py:15`; AST `01f51128853e6dbb0ff4d0ab5ead27e38e10d07244cf63b3a3c2fef1ef988a5b`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::root.body[8]::ImportFrom

Source: `infra/agentinfra/roadmap_project.py:16`; AST `c77b99ce1220eaeadd24d0d2eb90624f8e6b280576577774ee57598a0f5eef8f`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::root.body[9]::ImportFrom

Source: `infra/agentinfra/roadmap_project.py:17`; AST `c2a64003604dd1da38b622b02ca5190bea13e78ec6647b9f914f7257516a593e`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::root.body[10]::Assign

Source: `infra/agentinfra/roadmap_project.py:20`; AST `450386d2b05707b77cb785f3c9c72b49c8717abae76f79b264237aee79ca0820`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: INTERFACE_VERSION.
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::root.body[11]::Assign

Source: `infra/agentinfra/roadmap_project.py:21`; AST `2a9a7a57751e02a2d3b29d52efc20cb0353895206cf862be5e948f11d5968d8e`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: AEGIS_RECORD_WRITER.
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::root.body[12]::ClassDef

Source: `infra/agentinfra/roadmap_project.py:25`; AST `a4b800e04b45befe9cf2aa04645113b0e8487a2f665c26d69fc3adafc8729865`.

Rust module: `infra::agentinfra::roadmap_project`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: Path, ProjectProfileV1, classmethod, cls, confined_path, dataclass, dict, profile, profiles, project, read_json, repository, require, root, self, str, validate_record. Outputs/bindings: branch, canonical_record, declared_repository, language_boundary, profile, profiles, project, repository, root.
Calls/effect boundaries: Path, cls, confined_path, dataclass, read_json, require, root.resolve, validate_record.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered ClassDef evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::root.body[12].body[0]::AnnAssign

Source: `infra/agentinfra/roadmap_project.py:26`; AST `197b340a07f8e9ef2feb63e72d6ef223ced2a2ef2175eefe6a66ab19abfaa668`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: str. Outputs/bindings: project.
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::root.body[12].body[1]::AnnAssign

Source: `infra/agentinfra/roadmap_project.py:27`; AST `78e7d5541a862d32b751fc45dd4f529c85f532020acd5c392a0b8084e5582311`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: str. Outputs/bindings: declared_repository.
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[12].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::root.body[12].body[2]::AnnAssign

Source: `infra/agentinfra/roadmap_project.py:28`; AST `483ebd0d02ca9d2604287add0eeb2b5b62cef89dfa4ecf5375cfb329feefa898`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path. Outputs/bindings: repository.
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[12].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::root.body[12].body[3]::AnnAssign

Source: `infra/agentinfra/roadmap_project.py:29`; AST `1b775d016e839515a2ae3c3a5e7dbf8d89f90f2a8aa67cbbd09fc162fc9f8d19`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: str. Outputs/bindings: branch.
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[12].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::root.body[12].body[4]::AnnAssign

Source: `infra/agentinfra/roadmap_project.py:30`; AST `fd04b3a40d256a23e6db87818a042486ce0f68ab02d8d8a0e27c3f9bc7ed38b5`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: str. Outputs/bindings: canonical_record.
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[12].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::root.body[12].body[5]::AnnAssign

Source: `infra/agentinfra/roadmap_project.py:31`; AST `8df71f3332103551ecd5fcc941376aea25e5ddfd0f061f07350fe9e804351754`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: str. Outputs/bindings: language_boundary.
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[12].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::from_registry::root.body[12].body[6]::FunctionDef

Source: `infra/agentinfra/roadmap_project.py:34`; AST `5fb1b1291add74db30664da314fb496a0be14abd4a60fcff3174cf43c59f1ad5`.

Rust module: `infra::agentinfra::roadmap_project`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, ProjectProfileV1, classmethod, cls, dict, profile, profiles, project, read_json, repository, require, root, str, validate_record. Outputs/bindings: profile, profiles, repository, root.
Calls/effect boundaries: Path, cls, read_json, require, root.resolve, validate_record.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::from_registry::root.body[12].body[6].body[0]::Assign

Source: `infra/agentinfra/roadmap_project.py:35`; AST `7b881662a93f1cabda6daa8de666cd56431dd47a61da7e3a5a8856defd752ca2`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: root.
Calls/effect boundaries: root.resolve.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::from_registry::root.body[12].body[6].body[0].value::Call

Source: `infra/agentinfra/roadmap_project.py:35`; AST `b97f3f463d4724206af2869ad4674d5eb373167f052507971a722ecc8f771a87`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::from_registry::root.body[12].body[6].body[1]::Assign

Source: `infra/agentinfra/roadmap_project.py:36`; AST `021f6eca041a0a0fa0513a1fccdb93990bb217885976cda46ca8cce7b5476bca`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: profiles, read_json, root. Outputs/bindings: profiles.
Calls/effect boundaries: read_json.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::from_registry::root.body[12].body[6].body[1].value.body.value::Call

Source: `infra/agentinfra/roadmap_project.py:36`; AST `8e7e5aa59eb3d5aad4383ca406ca14418b9e912a465b4f7a0ac32e45ae51a19a`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: read_json, root. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[1].value.body.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::from_registry::root.body[12].body[6].body[2]::Expr

Source: `infra/agentinfra/roadmap_project.py:37`; AST `1451aea661a1b5608c1afb771d83fc520b6f348eb621a6c42945c407bd64ebcc`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: profiles, project, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::from_registry::root.body[12].body[6].body[2].value::Call

Source: `infra/agentinfra/roadmap_project.py:37`; AST `59424e348ed9154663450320bc7d2ad6babe48e35c7e4e3c5fe320fe5e037e0e`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: profiles, project, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::from_registry::root.body[12].body[6].body[3]::Assign

Source: `infra/agentinfra/roadmap_project.py:38`; AST `293d4c7c3d1a384eb85a76e0ae9ddcc73a29da5f35eb2b003134e9db65739a5d`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: profiles, project. Outputs/bindings: profile.
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[6].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::from_registry::root.body[12].body[6].body[4]::Expr

Source: `infra/agentinfra/roadmap_project.py:39`; AST `680e40669754d128f7308c98ce1782aa59aedd157758501f9bdab4043eb74461`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: profile, root, validate_record. Outputs/bindings: (none).
Calls/effect boundaries: validate_record.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::from_registry::root.body[12].body[6].body[4].value::Call

Source: `infra/agentinfra/roadmap_project.py:39`; AST `f062319fbd72194e8e55a8eaf50c321a21daf2a88a3140f1163bcc0c6b2cbc6a`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: profile, root, validate_record. Outputs/bindings: (none).
Calls/effect boundaries: validate_record.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::from_registry::root.body[12].body[6].body[5]::Expr

Source: `infra/agentinfra/roadmap_project.py:40`; AST `636c69b498cd09a08565bec21f2c668dd53d39dbb34c113c523db3bdc3f1e326`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: profile, project, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::from_registry::root.body[12].body[6].body[5].value::Call

Source: `infra/agentinfra/roadmap_project.py:40`; AST `934a468fbde5c00d75f13d546f8ac353264f65312aced72c1cc055c82616b86e`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: profile, project, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::from_registry::root.body[12].body[6].body[6]::Assign

Source: `infra/agentinfra/roadmap_project.py:43`; AST `9256f52473e77c68e3ba45a316f7a26c40feaaebd27597f6d6a832366759edb1`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, profile, project, root. Outputs/bindings: repository.
Calls/effect boundaries: Path.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[6].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::from_registry::root.body[12].body[6].body[6].value.orelse::Call

Source: `infra/agentinfra/roadmap_project.py:43`; AST `5ba539d7090a511f6cbdb65bb42a5130aaa3c8032df20301498f801af84c0a67`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, profile. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[6].value.orelse; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::from_registry::root.body[12].body[6].body[7]::Return

Source: `infra/agentinfra/roadmap_project.py:44`; AST `4da8a12e58e62d99dd724c46baa92c31b2e5e41c2b49dc612099cdad4dabf1d1`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cls, profile, project, repository. Outputs/bindings: (none).
Calls/effect boundaries: cls.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Return evaluation at root.body[12].body[6].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::from_registry::root.body[12].body[6].body[7].value::Call

Source: `infra/agentinfra/roadmap_project.py:44`; AST `c410caaac8bb048f7e8d41905ff803065005874bda4a588789cd9d02761c128a`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cls, profile, project, repository. Outputs/bindings: (none).
Calls/effect boundaries: cls.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::path::root.body[12].body[7]::FunctionDef

Source: `infra/agentinfra/roadmap_project.py:47`; AST `0a0fe44c593624bc76248470746d55bf2cfb0468a1cf350ee063e1bfc119382d`.

Rust module: `infra::agentinfra::roadmap_project`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, confined_path, self. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::path::root.body[12].body[7].body[0]::Return

Source: `infra/agentinfra/roadmap_project.py:48`; AST `f425479f17c0999578f69d5ae6d30a6fc752a75e9f42b3b7b7a23c2e415828be`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, self. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Return evaluation at root.body[12].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::path::root.body[12].body[7].body[0].value::Call

Source: `infra/agentinfra/roadmap_project.py:48`; AST `cbb6171a280332be2728518030b3e1a5b9a66a2c792e799256b968a670f70914`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, self. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::root.body[12].decorator_list[0]::Call

Source: `infra/agentinfra/roadmap_project.py:24`; AST `fc70015bf40dfb1bdf9c74c7ec3567232b79ad9aa1cd1edc6c02254994330803`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dataclass. Outputs/bindings: (none).
Calls/effect boundaries: dataclass.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[12].decorator_list[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::root.body[13]::ClassDef

Source: `infra/agentinfra/roadmap_project.py:51`; AST `f3b347ee5d573e67a706798c2aca284c4f9ae87911a73e4a9949c20f3c3c9055`.

Rust module: `infra::agentinfra::roadmap_project`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: AEGIS_RECORD_WRITER, BudgetLedger, FileLock, FileTransaction, INTERFACE_VERSION, Mutation, Path, ProjectProfileV1, WorkspaceLease, a, adopt_managed_runner, allow_create, any, artifacts, authorization_id, before, bind_goal, binding, bool, candidate, canonical, changed, created, current, dict, digest, execution, expected_digest, fields, inspect_process, int, isinstance, k, key, lease, lease_before, len, loads, lock, managed, new_execution, observation, observe_native_owner, observed, old, old_history, owner, path, pid, previous, prior_binding, process_handle, profile, profiles, project, protocol, read_json, record, require, root, self, state, staticmethod, str, tuple, type, updated, user_authorized, uuid, value. Outputs/bindings: a, before, binding, candidate, changed, created, current, execution, k, key, lease, lease_before, lock, managed, new_execution, observation, observed, old, old_history, owner, path, previous, prior_binding, profile, record, state, updated, value.
Calls/effect boundaries: BudgetLedger, BudgetLedger(self.root).read, FileLock, FileTransaction, FileTransaction(self.root, [*artifacts, Mutation(path, canonical(updated) + b'\n', expected_exists=before is not None, expected_sha256=expected_digest)], state_dir=self.root / '.aegis/state/transactions', name=AEGIS_RECORD_WRITER).commit, FileTransaction(self.root, [Mutation(lease.path, canonical(state) + b'\n', expected_exists=True, expected_sha256=digest(lease_before)), Mutation(self.profile.path(), canonical(record) + b'\n', expected_exists=True, expected_sha256=digest(before))], state_dir=self.root / '.aegis/state/transactions', name=AEGIS_RECORD_WRITER).commit, Mutation, ProjectProfileV1.from_registry, WorkspaceLease, WorkspaceLease(self.root).assert_owner, adopt_managed_runner, any, before.decode, bind_goal, binding.get, binding.get('observation', {}).get, bool, canonical, changed.get, changed.get('observation', {}).get, current.get, dict, digest, execution.get, execution.pop, execution.setdefault, execution.setdefault('binding_history', []).append, fields.get, inspect_process, isinstance, lease.path.read_bytes, lease.read, len, loads, lock.acquire, lock.release, managed.get, new_execution.get, observation['goal'].get, observe_native_owner, owner.get, path.exists, path.read_bytes, prior_binding.get, prior_binding.get('observation', {}).get, process_handle, read_json, record.get, require, root.resolve, self._validate_aegis, self.profile.path, self.profile.path().read_bytes, self.read, state['history'].append, str, type, updated.get, updated.get('execution', {}).get, uuid.uuid4.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered ClassDef evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::__init__::root.body[13].body[0]::FunctionDef

Source: `infra/agentinfra/roadmap_project.py:52`; AST `49ddb9a9695c876979ffeadb1bd76ca302ac02ed6c1e04c9176bc97b3eb4ee97`.

Rust module: `infra::agentinfra::roadmap_project`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, ProjectProfileV1, dict, profiles, project, root, self, str. Outputs/bindings: (none).
Calls/effect boundaries: ProjectProfileV1.from_registry, root.resolve.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::__init__::root.body[13].body[0].body[0]::Assign

Source: `infra/agentinfra/roadmap_project.py:53`; AST `eac70191d36cd330a975a12be514d4a5f58088087cc2acfa2746cafe468cc8ae`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root, self. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::__init__::root.body[13].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_project.py:53`; AST `b97f3f463d4724206af2869ad4674d5eb373167f052507971a722ecc8f771a87`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::__init__::root.body[13].body[0].body[1]::Assign

Source: `infra/agentinfra/roadmap_project.py:54`; AST `52823bc4496d4c48cdd8711c2a09d26a5df370b7ad17fc84256d05ef9ee9ab6d`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ProjectProfileV1, profiles, project, self. Outputs/bindings: (none).
Calls/effect boundaries: ProjectProfileV1.from_registry.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::__init__::root.body[13].body[0].body[1].value::Call

Source: `infra/agentinfra/roadmap_project.py:54`; AST `d881c7ec4a0f0d4c25999739e55f0ac23ba55fe627b05709fd2c23592d4d5010`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ProjectProfileV1, profiles, project, self. Outputs/bindings: (none).
Calls/effect boundaries: ProjectProfileV1.from_registry.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::read::root.body[13].body[1]::FunctionDef

Source: `infra/agentinfra/roadmap_project.py:56`; AST `b0311bf2d58de3caf42eb96615ae03baa036b6a23552c7379409763d2ecc86e1`.

Rust module: `infra::agentinfra::roadmap_project`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: dict, isinstance, read_json, require, self, value. Outputs/bindings: value.
Calls/effect boundaries: isinstance, read_json, require, self._validate_aegis, self.profile.path.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::read::root.body[13].body[1].body[0]::Assign

Source: `infra/agentinfra/roadmap_project.py:57`; AST `b90b26c8b4bc992269598dcf7b5eb867ec1cce28c8e747226cde3a913e499130`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: read_json, self. Outputs/bindings: value.
Calls/effect boundaries: read_json, self.profile.path.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::read::root.body[13].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_project.py:57`; AST `258856238abae70e774a798573cc489832b628753746d99426d048fd4174ed08`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: read_json, self. Outputs/bindings: (none).
Calls/effect boundaries: read_json, self.profile.path.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::read::root.body[13].body[1].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_project.py:57`; AST `5aff035e159349b40c99cc1e24ee69d81660511f1625d432552cda0b0afab929`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.profile.path.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::read::root.body[13].body[1].body[1]::Expr

Source: `infra/agentinfra/roadmap_project.py:58`; AST `f924433f2113ea8716bd5f29442c084e4c75c5132563e5b0c29a76f6b9119265`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, isinstance, require, value. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::read::root.body[13].body[1].body[1].value::Call

Source: `infra/agentinfra/roadmap_project.py:58`; AST `a0e3a25fcc22c702dfe515bed966ec7469f66791090ea26725283f2fed2742f6`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, isinstance, require, value. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::read::root.body[13].body[1].body[1].value.args[0]::Call

Source: `infra/agentinfra/roadmap_project.py:58`; AST `a0df6caeebecae97cf305403969f3b48f16842ceba977c5f53441f25fd65637d`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, isinstance, value. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::read::root.body[13].body[1].body[2]::If

Source: `infra/agentinfra/roadmap_project.py:59`; AST `2c038c4a222f1315040aedd628f9fcea5904264798b481914d7d3305f6945704`.

Rust module: `infra::agentinfra::roadmap_project`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: self, value. Outputs/bindings: (none).
Calls/effect boundaries: self._validate_aegis.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered If evaluation at root.body[13].body[1].body[2]; no call, error or mutation may be omitted. Condition: self.profile.project == 'Aegis'
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::read::root.body[13].body[1].body[2].body[0]::Expr

Source: `infra/agentinfra/roadmap_project.py:60`; AST `fe5a81842ed8cfbb7f4db589dda4e430cc69dda8a9d29f31bbc62c138bdaa1fe`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, value. Outputs/bindings: (none).
Calls/effect boundaries: self._validate_aegis.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[1].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::read::root.body[13].body[1].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_project.py:60`; AST `598cef4ebbcac07b1926e9cb671452da88e3e60b4d2b44435d5f78da3133ec9a`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, value. Outputs/bindings: (none).
Calls/effect boundaries: self._validate_aegis.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::read::root.body[13].body[1].body[3]::Return

Source: `infra/agentinfra/roadmap_project.py:61`; AST `88b203970aef225f077e527420a8aa37d7bea48c022a704b48a144448b80ec78`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: value. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Return evaluation at root.body[13].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::_validate_aegis::root.body[13].body[2]::FunctionDef

Source: `infra/agentinfra/roadmap_project.py:64`; AST `8bc20e98ac10a79d23e7e2324c018c5287ce47e280b5ac19a2c2f2e923f07e38`.

Rust module: `infra::agentinfra::roadmap_project`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: AEGIS_RECORD_WRITER, dict, int, record, require, staticmethod, type. Outputs/bindings: (none).
Calls/effect boundaries: record.get, require, type.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::_validate_aegis::root.body[13].body[2].body[0]::Expr

Source: `infra/agentinfra/roadmap_project.py:65`; AST `f691d6ac120bb2fa6be819bda7c0478104a1b0e2435722979460d37f274912df`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: int, record, require, type. Outputs/bindings: (none).
Calls/effect boundaries: record.get, require, type.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::_validate_aegis::root.body[13].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_project.py:65`; AST `be85d796c56e917d5f13314d075084b3df6c0bf3f2de02ac013bed86bc30bda4`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: int, record, require, type. Outputs/bindings: (none).
Calls/effect boundaries: record.get, require, type.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::_validate_aegis::root.body[13].body[2].body[0].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_project.py:65`; AST `039ee65eccc54cc8b054f5abf5ca3f80662d7756c1255a108b80cd8ce73d52ac`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record, type. Outputs/bindings: (none).
Calls/effect boundaries: record.get, type.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].body[0].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::_validate_aegis::root.body[13].body[2].body[0].value.args[0].values[0].left.args[0]::Call

Source: `infra/agentinfra/roadmap_project.py:65`; AST `d1e3876e5f2eab25e6fd365f06eea6e829f195ef666744ac41314682d8aa382c`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].body[0].value.args[0].values[0].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::_validate_aegis::root.body[13].body[2].body[0].value.args[0].values[2].left::Call

Source: `infra/agentinfra/roadmap_project.py:66`; AST `d0a98983fb019a589d6e758de84d4e0770904ddc3da7d42d506d12396e7ac5ca`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].body[0].value.args[0].values[2].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::_validate_aegis::root.body[13].body[2].body[1]::Expr

Source: `infra/agentinfra/roadmap_project.py:67`; AST `677268ba69ed744e363e2b24baacd6e82dd695947cbe9a119ad1c9f80fe6ab88`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: AEGIS_RECORD_WRITER, record, require. Outputs/bindings: (none).
Calls/effect boundaries: record.get, require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::_validate_aegis::root.body[13].body[2].body[1].value::Call

Source: `infra/agentinfra/roadmap_project.py:67`; AST `d539cd8d5ac9fd077a2fad43a5d057a0f1b1cb4b7ee704dfd517f20100165892`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: AEGIS_RECORD_WRITER, record, require. Outputs/bindings: (none).
Calls/effect boundaries: record.get, require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::_validate_aegis::root.body[13].body[2].body[1].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_project.py:67`; AST `2ff7c89e5efe914e0bc6c555cf4900c80abd2000c541210a327481acef370769`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: AEGIS_RECORD_WRITER, record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].body[1].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3]::FunctionDef

Source: `infra/agentinfra/roadmap_project.py:70`; AST `29f98c3ac29c6cd811d005a703008a41f705a68011dad8532ce7c02ef0d9aa40`.

Rust module: `infra::agentinfra::roadmap_project`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: AEGIS_RECORD_WRITER, FileTransaction, Mutation, WorkspaceLease, allow_create, artifacts, before, binding, bool, canonical, changed, created, current, dict, digest, execution, expected_digest, fields, int, isinstance, key, len, loads, new_execution, observed, old_history, owner, path, previous, require, self, str, tuple, type, updated. Outputs/bindings: before, binding, changed, created, current, execution, key, new_execution, observed, old_history, owner, path, previous, updated.
Calls/effect boundaries: FileTransaction, FileTransaction(self.root, [*artifacts, Mutation(path, canonical(updated) + b'\n', expected_exists=before is not None, expected_sha256=expected_digest)], state_dir=self.root / '.aegis/state/transactions', name=AEGIS_RECORD_WRITER).commit, Mutation, WorkspaceLease, WorkspaceLease(self.root).assert_owner, before.decode, binding.get, binding.get('observation', {}).get, bool, canonical, changed.get, changed.get('observation', {}).get, current.get, dict, digest, execution.get, fields.get, isinstance, len, loads, new_execution.get, owner.get, path.exists, path.read_bytes, require, self._validate_aegis, self.profile.path, type, updated.get, updated.get('execution', {}).get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[0]::Expr

Source: `infra/agentinfra/roadmap_project.py:72`; AST `732bc246ac7aba568736b479dfbe5d0dfe027ce70ccd3789e169e7ffae50c20c`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, self. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_project.py:72`; AST `7fdd50e4b59fdf195ad61b18b2621e360becb7be8902b2f27dde0fcbca5f87b3`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, self. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[1]::Expr

Source: `infra/agentinfra/roadmap_project.py:73`; AST `c87a0ee9d93b5e844f997d6bef57e19a18af018f112ec7b4ab370806a8b54cfd`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, fields, isinstance, require. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[1].value::Call

Source: `infra/agentinfra/roadmap_project.py:73`; AST `f396b06f2fcca1612a36e22a9d950e2fd58dd838624131b771893a016a314c61`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, fields, isinstance, require. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[1].value.args[0]::Call

Source: `infra/agentinfra/roadmap_project.py:73`; AST `156733c732f0b8d972873efbb33d15ba5f8c4c11c97e23ef37f146a111996973`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, fields, isinstance. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[2]::Assign

Source: `infra/agentinfra/roadmap_project.py:74`; AST `9af500de7189cd969bd2b82769cf7ba54b23254d4f9ab23c19e892b413f8d606`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: path.
Calls/effect boundaries: self.profile.path.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[2].value::Call

Source: `infra/agentinfra/roadmap_project.py:74`; AST `5aff035e159349b40c99cc1e24ee69d81660511f1625d432552cda0b0afab929`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.profile.path.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[3]::Assign

Source: `infra/agentinfra/roadmap_project.py:75`; AST `364d0fe982fb1e9a6aaf875395a3ff50afbc7a163dde40b7c13e3188964c3c13`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: before.
Calls/effect boundaries: path.exists, path.read_bytes.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[3].value.test::Call

Source: `infra/agentinfra/roadmap_project.py:75`; AST `2cac3ec82b344023c57b4bbfcae282698ef12842cbda26a14724eacbefb97016`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.exists.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[3].value.test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[3].value.body::Call

Source: `infra/agentinfra/roadmap_project.py:75`; AST `f35916bc21a833a57a0dd89398b2dab5479cd1f3ef04b46f456d03ce95b67eac`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[3].value.body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[4]::Expr

Source: `infra/agentinfra/roadmap_project.py:76`; AST `8e8e8f1cd57137dd32e614b48177ce00a733e8f42cb438fa823c8222a2723257`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: allow_create, before, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[3].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[4].value::Call

Source: `infra/agentinfra/roadmap_project.py:76`; AST `4c751a4a27485da58a79a9511c9a498ec84e70ec081db51f09a513e3f7aedc6f`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: allow_create, before, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[5]::Expr

Source: `infra/agentinfra/roadmap_project.py:77`; AST `784b530e21d2bd703072f78a3fd3214eae1753a204fae8daaa85ceeacedf7e12`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: before, digest, expected_digest, require. Outputs/bindings: (none).
Calls/effect boundaries: digest, require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[3].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[5].value::Call

Source: `infra/agentinfra/roadmap_project.py:77`; AST `08e1cd827253645876cade89d6f0735005908c733e5fd1f51fe32b711fe7efc8`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before, digest, expected_digest, require. Outputs/bindings: (none).
Calls/effect boundaries: digest, require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[5].value.args[0].left.body::Call

Source: `infra/agentinfra/roadmap_project.py:77`; AST `4a63ff00fb497e1d094ddb9e4f8ada535aacd403c14cfceee7fc8dd669fbee57`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before, digest. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[5].value.args[0].left.body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[6]::Assign

Source: `infra/agentinfra/roadmap_project.py:79`; AST `92d200e267e0e5669e452d334e8c4bcb3cdafe97ce3c7988af666cb5363da2f7`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: before, loads. Outputs/bindings: current.
Calls/effect boundaries: before.decode, loads.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[3].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[6].value.body::Call

Source: `infra/agentinfra/roadmap_project.py:79`; AST `1bdeb6848cd90df0a771ae4e779d89aed864d15bc2917c477a4084431f9beebf`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before, loads. Outputs/bindings: (none).
Calls/effect boundaries: before.decode, loads.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[6].value.body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[6].value.body.args[0]::Call

Source: `infra/agentinfra/roadmap_project.py:79`; AST `797b7f1e852c5adfb7f77d47f99dd7b7483943b0928c21cd3aea703a3d98f4fb`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before. Outputs/bindings: (none).
Calls/effect boundaries: before.decode.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[6].value.body.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[7]::Expr

Source: `infra/agentinfra/roadmap_project.py:80`; AST `d937d61cecaaa97fe4d096612eb646c2dcdc9fa83a7a1e8b4b0554ed8bb91a75`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current, self. Outputs/bindings: (none).
Calls/effect boundaries: self._validate_aegis.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[3].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[7].value::Call

Source: `infra/agentinfra/roadmap_project.py:80`; AST `674f06f97ebcaff4393536f7238443226e5d497dcea2a58d778989305516e814`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current, self. Outputs/bindings: (none).
Calls/effect boundaries: self._validate_aegis.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[8]::Expr

Source: `infra/agentinfra/roadmap_project.py:81`; AST `7a0e40f3067d2d1a4acc38668330a798f24865a950bf94d9f1041c6e04560bbc`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: AEGIS_RECORD_WRITER, fields, require. Outputs/bindings: (none).
Calls/effect boundaries: fields.get, require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[3].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[8].value::Call

Source: `infra/agentinfra/roadmap_project.py:81`; AST `00955ee5974acbdbd5d7624e35f7c928df06abd3bf93aa3678684a0a3d9e935b`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: AEGIS_RECORD_WRITER, fields, require. Outputs/bindings: (none).
Calls/effect boundaries: fields.get, require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[8].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_project.py:81`; AST `5fa495e4531ca71e17c6cfaedd2d3da193f405ad65464fce6520ebdc0b862af1`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: AEGIS_RECORD_WRITER, fields. Outputs/bindings: (none).
Calls/effect boundaries: fields.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[8].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[9]::Assign

Source: `infra/agentinfra/roadmap_project.py:83`; AST `a63289e01324fa74fda3a1f1be3042959b6a5cb28afc02adf5a125e4dc9ca770`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current, dict, fields. Outputs/bindings: updated.
Calls/effect boundaries: dict.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[3].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[9].value::Call

Source: `infra/agentinfra/roadmap_project.py:83`; AST `97bace9cd1ada76e2c72281e79924de49013d53a229a45e0f2d133959fe7facc`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current, dict, fields. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[10]::Assign

Source: `infra/agentinfra/roadmap_project.py:84`; AST `a9ba7d516fc29c81e83606864315598f0b87f3348eeda595809ab0006287fe5c`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: AEGIS_RECORD_WRITER, updated. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[3].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[11]::Expr

Source: `infra/agentinfra/roadmap_project.py:85`; AST `9b0f872487e43303dac8e71f3974dc2e55798685b48b595ba9c9b7b7094a156b`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, updated. Outputs/bindings: (none).
Calls/effect boundaries: self._validate_aegis.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[3].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[11].value::Call

Source: `infra/agentinfra/roadmap_project.py:85`; AST `a2c97ffbbb446036f5794be21a64969710c087bdbad7a9415cde4988529638c4`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, updated. Outputs/bindings: (none).
Calls/effect boundaries: self._validate_aegis.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[12]::Assign

Source: `infra/agentinfra/roadmap_project.py:86`; AST `a78f1dd400cf058093eda7b5c30a8b05ebea7a9aad84da840c3d46ce5cb0dacc`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current, updated. Outputs/bindings: execution.
Calls/effect boundaries: current.get, updated.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[3].body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[12].value.values[0]::Call

Source: `infra/agentinfra/roadmap_project.py:86`; AST `a328de23047ce40417fc57ba191190571e062464ebe01ba998e2891fc9809be1`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current. Outputs/bindings: (none).
Calls/effect boundaries: current.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[12].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[12].value.values[1]::Call

Source: `infra/agentinfra/roadmap_project.py:86`; AST `15b079f2654fa7e884ed6710665b447d7ace034007062211786cedceab0ea605`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: updated. Outputs/bindings: (none).
Calls/effect boundaries: updated.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[12].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13]::If

Source: `infra/agentinfra/roadmap_project.py:87`; AST `7d8f1c46b8eea083c736c50cebfd80c706ed27825df00b770cec3aa18a446a61`.

Rust module: `infra::agentinfra::roadmap_project`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: WorkspaceLease, binding, bool, changed, created, execution, int, key, len, new_execution, observed, old_history, owner, previous, require, self, type, updated. Outputs/bindings: binding, changed, created, key, new_execution, observed, old_history, owner, previous.
Calls/effect boundaries: WorkspaceLease, WorkspaceLease(self.root).assert_owner, binding.get, binding.get('observation', {}).get, bool, changed.get, changed.get('observation', {}).get, execution.get, len, new_execution.get, owner.get, require, type, updated.get, updated.get('execution', {}).get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered If evaluation at root.body[13].body[3].body[13]; no call, error or mutation may be omitted. Condition: execution
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[0]::Assign

Source: `infra/agentinfra/roadmap_project.py:88`; AST `3143d476a50e13911b81b08cc9f4475a21e61266a736348376774270436548e6`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: execution. Outputs/bindings: owner.
Calls/effect boundaries: execution.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[3].body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[0].value::Call

Source: `infra/agentinfra/roadmap_project.py:88`; AST `94ea54adee6fc3e52b8da6da4b7ad4c1f66ad0fe66dcebf5eb64a5f9b2021753`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: execution. Outputs/bindings: (none).
Calls/effect boundaries: execution.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[1]::Assign

Source: `infra/agentinfra/roadmap_project.py:89`; AST `8d966d61e8f4fe7fb915b27fb56de3eb1cea5416f6e3c84de1a6bca872634ea8`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: execution. Outputs/bindings: binding.
Calls/effect boundaries: execution.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[3].body[13].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[1].value::Call

Source: `infra/agentinfra/roadmap_project.py:89`; AST `9d07ed4a2c148f4183b707ac830e883b5c33ba96dcd1e134c547f727d92f1312`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: execution. Outputs/bindings: (none).
Calls/effect boundaries: execution.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[2]::Expr

Source: `infra/agentinfra/roadmap_project.py:90`; AST `efaa1634b4c186b43946e4a46df8d821197fdb48e82d21f9a435f223a8ee0bf2`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, bool, owner, require. Outputs/bindings: (none).
Calls/effect boundaries: binding.get, bool, owner.get, require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[3].body[13].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[2].value::Call

Source: `infra/agentinfra/roadmap_project.py:90`; AST `95fd4cbbf935e8aea350a84e37be292a87c6882d033976881b02a30da7dc715e`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, bool, owner, require. Outputs/bindings: (none).
Calls/effect boundaries: binding.get, bool, owner.get, require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[2].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_project.py:90`; AST `27a5b1552929f691a509884265ca66d93c6c63ccce4de6833fab9a141246c47e`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: owner. Outputs/bindings: (none).
Calls/effect boundaries: owner.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[2].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[2].value.args[0].values[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_project.py:90`; AST `63111ba26343241a333d0933cf221435534ec16270d2f49ca57741efb6c4fa1a`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding. Outputs/bindings: (none).
Calls/effect boundaries: binding.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[2].value.args[0].values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[2].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_project.py:90`; AST `6b44386f9fcb7cd39dade6d2cfe0643c1f2a4cd60d8a108ee30fb4c545470682`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, owner. Outputs/bindings: (none).
Calls/effect boundaries: bool, owner.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[2].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[2].value.args[0].values[1].args[0]::Call

Source: `infra/agentinfra/roadmap_project.py:90`; AST `27a5b1552929f691a509884265ca66d93c6c63ccce4de6833fab9a141246c47e`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: owner. Outputs/bindings: (none).
Calls/effect boundaries: owner.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[2].value.args[0].values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[3]::Expr

Source: `infra/agentinfra/roadmap_project.py:92`; AST `31609293520c6c913c3148edaec1c1b224d2c5c5d115b243a07abdb36865da75`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: WorkspaceLease, owner, self. Outputs/bindings: (none).
Calls/effect boundaries: WorkspaceLease, WorkspaceLease(self.root).assert_owner.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[3].body[13].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[3].value::Call

Source: `infra/agentinfra/roadmap_project.py:92`; AST `4e57d43a3eafcdc4f4fff3cb17d80d5c81b7b2b14096dcd659ce2aa052c23521`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: WorkspaceLease, owner, self. Outputs/bindings: (none).
Calls/effect boundaries: WorkspaceLease, WorkspaceLease(self.root).assert_owner.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[3].value.func.value::Call

Source: `infra/agentinfra/roadmap_project.py:92`; AST `408829ac552086ff1aa49ed525f89889a9374a77ff0f5e75e1759a09776c7b06`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: WorkspaceLease, self. Outputs/bindings: (none).
Calls/effect boundaries: WorkspaceLease.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[3].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[4]::Assign

Source: `infra/agentinfra/roadmap_project.py:93`; AST `d2aaff65dcf7f77bd4314e829dd76f6969c288152ba8988a092dafc47b7618e4`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: updated. Outputs/bindings: changed.
Calls/effect boundaries: updated.get, updated.get('execution', {}).get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[3].body[13].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[4].value::Call

Source: `infra/agentinfra/roadmap_project.py:93`; AST `22dbd39e10f5e80d8d2c3c48ff7ff7095bdbfd772051f29c0c0e741b6fd06397`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: updated. Outputs/bindings: (none).
Calls/effect boundaries: updated.get, updated.get('execution', {}).get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[4].value.func.value::Call

Source: `infra/agentinfra/roadmap_project.py:93`; AST `a92afd6585cea4ad55608df885b6e22ae9e7f76d42cc34bfdae58d7d2b0aa07d`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: updated. Outputs/bindings: (none).
Calls/effect boundaries: updated.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[4].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[5]::Expr

Source: `infra/agentinfra/roadmap_project.py:94`; AST `90f55cf2ea2f5ce2c77965a680c22cdbc192168e6c3ed4ce63d9df0060d5d3e2`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: owner, require, updated. Outputs/bindings: (none).
Calls/effect boundaries: require, updated.get, updated.get('execution', {}).get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[3].body[13].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[5].value::Call

Source: `infra/agentinfra/roadmap_project.py:94`; AST `4ec4de0d405c14b43ebf68525559fd1e03f3400d6b358a4636626ac04389c25a`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: owner, require, updated. Outputs/bindings: (none).
Calls/effect boundaries: require, updated.get, updated.get('execution', {}).get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[5].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_project.py:94`; AST `1af38ae42bbb3bb40e8dab2bbe705d86f7a1ac4533dce520f39179e1d1300e96`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: updated. Outputs/bindings: (none).
Calls/effect boundaries: updated.get, updated.get('execution', {}).get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[5].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[5].value.args[0].left.func.value::Call

Source: `infra/agentinfra/roadmap_project.py:94`; AST `a92afd6585cea4ad55608df885b6e22ae9e7f76d42cc34bfdae58d7d2b0aa07d`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: updated. Outputs/bindings: (none).
Calls/effect boundaries: updated.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[5].value.args[0].left.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[6]::Expr

Source: `infra/agentinfra/roadmap_project.py:96`; AST `d38a5e7add4d658fdf8c2a071dd99db13bf819c44be57501982a432c78a0b3c3`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, changed, require. Outputs/bindings: (none).
Calls/effect boundaries: binding.get, changed.get, require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[3].body[13].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[6].value::Call

Source: `infra/agentinfra/roadmap_project.py:96`; AST `b5b51946d87cc225146b12392d268d429b19ec33a2e19ee82f55366a4bb45b19`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, changed, require. Outputs/bindings: (none).
Calls/effect boundaries: binding.get, changed.get, require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[6].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_project.py:96`; AST `8015083335b7c0a8dfb44ecb0fc9b34368e73a39209df4c89c1f9ca0174fc90b`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: changed. Outputs/bindings: (none).
Calls/effect boundaries: changed.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[6].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[6].value.args[0].values[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_project.py:96`; AST `63111ba26343241a333d0933cf221435534ec16270d2f49ca57741efb6c4fa1a`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding. Outputs/bindings: (none).
Calls/effect boundaries: binding.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[6].value.args[0].values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[6].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_project.py:97`; AST `b407a3fa7107027af01af23bad58237da099cadc6e2afe1f37e68a5dba913ce4`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: changed. Outputs/bindings: (none).
Calls/effect boundaries: changed.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[6].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[6].value.args[0].values[1].comparators[0]::Call

Source: `infra/agentinfra/roadmap_project.py:97`; AST `c52ca19c779f5d2a2be4d6e23e8b381a8637c14e49af2b3c39e5bc3ee9359726`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding. Outputs/bindings: (none).
Calls/effect boundaries: binding.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[6].value.args[0].values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[7]::If

Source: `infra/agentinfra/roadmap_project.py:99`; AST `972a62d4669d8b9882507e76d613c5e54090ddaedcbc8c48cb1996b7853ad54f`.

Rust module: `infra::agentinfra::roadmap_project`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: binding, changed, require. Outputs/bindings: (none).
Calls/effect boundaries: binding.get, changed.get, require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered If evaluation at root.body[13].body[3].body[13].body[7]; no call, error or mutation may be omitted. Condition: binding.get('native_accounting_preserved') is True
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[7].test.left::Call

Source: `infra/agentinfra/roadmap_project.py:99`; AST `674558e14bf2016edafb9c07a8f6e4b64a570e02d4fda3901f4706493c1f1137`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding. Outputs/bindings: (none).
Calls/effect boundaries: binding.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[7].test.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[7].body[0]::Expr

Source: `infra/agentinfra/roadmap_project.py:100`; AST `cda807d477d9d110a5c49c9a846583a3fe87e84a24c2eb8eddcc1051e8c0c742`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: changed, require. Outputs/bindings: (none).
Calls/effect boundaries: changed.get, require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[3].body[13].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[7].body[0].value::Call

Source: `infra/agentinfra/roadmap_project.py:100`; AST `074731cdf555012a6e292073ef582dc87c362559ac49d1e4038958bd6de656d0`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: changed, require. Outputs/bindings: (none).
Calls/effect boundaries: changed.get, require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[7].body[0].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_project.py:100`; AST `2bc8f7a93dd195d096c10fc849c662555890d6a6d317b5a3edf193d01f0d6f82`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: changed. Outputs/bindings: (none).
Calls/effect boundaries: changed.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[7].body[0].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[8]::Assign

Source: `infra/agentinfra/roadmap_project.py:102`; AST `69d781ba8b3560a9917e281a81fcf20f7b4ed291d38e2876c21d7acc8de78e84`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: updated. Outputs/bindings: new_execution.
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[3].body[13].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[9]::Expr

Source: `infra/agentinfra/roadmap_project.py:103`; AST `4dd963f284c3ae8b5d318104b0e78adffec61ae9b7a95b43f784845481242874`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: execution, new_execution, require. Outputs/bindings: (none).
Calls/effect boundaries: execution.get, new_execution.get, require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[3].body[13].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[9].value::Call

Source: `infra/agentinfra/roadmap_project.py:103`; AST `44ad6746215ed2268abcb171c21bff08ef407df2f98b60b39ae24487d7a4bf3f`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: execution, new_execution, require. Outputs/bindings: (none).
Calls/effect boundaries: execution.get, new_execution.get, require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[9].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_project.py:103`; AST `ab056c463abc38f3d5abfcd42d1bc4ec87c3ad8c336fe0f4c2ccf85c67ab387b`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: new_execution. Outputs/bindings: (none).
Calls/effect boundaries: new_execution.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[9].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[9].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_project.py:103`; AST `fef641b3bb3cde38d9f02b8401e3595791991f68c22f5384fd74bed14ca6ea85`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: execution. Outputs/bindings: (none).
Calls/effect boundaries: execution.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[9].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[10]::Assign

Source: `infra/agentinfra/roadmap_project.py:105`; AST `daccd3d86e1fff75a37e087248b251214965e8b97213654bcf7a207af7ccacad`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: execution. Outputs/bindings: old_history.
Calls/effect boundaries: execution.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[3].body[13].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[10].value::Call

Source: `infra/agentinfra/roadmap_project.py:105`; AST `4c152ba0ddcae5f021c961df5ea040b3875ac8b8553149025b4b23f7569366b6`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: execution. Outputs/bindings: (none).
Calls/effect boundaries: execution.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[11]::Expr

Source: `infra/agentinfra/roadmap_project.py:106`; AST `221e252e12ea3c46fb0244e87f7f1e980779c020a0a772e215e16c01374a7bba`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, new_execution, old_history, require. Outputs/bindings: (none).
Calls/effect boundaries: len, new_execution.get, require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[3].body[13].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[11].value::Call

Source: `infra/agentinfra/roadmap_project.py:106`; AST `5168c10dc58aa2c714a99445155dedef82923a141ee93a4cc8ba89fcb7d2ac77`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, new_execution, old_history, require. Outputs/bindings: (none).
Calls/effect boundaries: len, new_execution.get, require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[11].value.args[0].left.value::Call

Source: `infra/agentinfra/roadmap_project.py:106`; AST `7f32f6cd44f36f9662bda84ed0fc9ac4bda4eca0290a7aeddb2804c2d7852048`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: new_execution. Outputs/bindings: (none).
Calls/effect boundaries: new_execution.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[11].value.args[0].left.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[11].value.args[0].left.slice.upper::Call

Source: `infra/agentinfra/roadmap_project.py:106`; AST `e662c4fe54487e2a2a8c60f1389496f7f0338b41fc2a93d177cdcd0fe3a53a80`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, old_history. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[11].value.args[0].left.slice.upper; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[12]::For

Source: `infra/agentinfra/roadmap_project.py:108`; AST `b5ad228be79ca1d9b8a7057ebff0682e69ce6cd672abecdc87b60ac9b9e49723`.

Rust module: `infra::agentinfra::roadmap_project`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: binding, changed, int, key, observed, previous, require, type. Outputs/bindings: key, observed, previous.
Calls/effect boundaries: binding.get, binding.get('observation', {}).get, changed.get, changed.get('observation', {}).get, require, type.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered For evaluation at root.body[13].body[3].body[13].body[12]; no call, error or mutation may be omitted. Iteration: key in ('tokensUsed', 'timeUsedSeconds')
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[12].body[0]::Assign

Source: `infra/agentinfra/roadmap_project.py:109`; AST `77cc354770f5d38cb46dbb3f206ca2298a0fb7c798b49c7edcf6d8c0ad558da1`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, key. Outputs/bindings: previous.
Calls/effect boundaries: binding.get, binding.get('observation', {}).get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[3].body[13].body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[12].body[0].value::Call

Source: `infra/agentinfra/roadmap_project.py:109`; AST `d5581843908ca08a75b91699c99f723b96225af764d729c7fd80f88896939b01`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, key. Outputs/bindings: (none).
Calls/effect boundaries: binding.get, binding.get('observation', {}).get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[12].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[12].body[0].value.func.value::Call

Source: `infra/agentinfra/roadmap_project.py:109`; AST `19383d3c3a3dd141414e57358091030cb5d155331564962bc5d64e9d2fdca72d`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding. Outputs/bindings: (none).
Calls/effect boundaries: binding.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[12].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[12].body[1]::Assign

Source: `infra/agentinfra/roadmap_project.py:110`; AST `3395784731d1794ab068b2f5f0a66c7496105267228be91fa3dc6f4a846333a1`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: changed, key. Outputs/bindings: observed.
Calls/effect boundaries: changed.get, changed.get('observation', {}).get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[3].body[13].body[12].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[12].body[1].value::Call

Source: `infra/agentinfra/roadmap_project.py:110`; AST `112583c74426f59a41bedaed87455743aad5f147ba9cabed0ccf8b01e35fb75b`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: changed, key. Outputs/bindings: (none).
Calls/effect boundaries: changed.get, changed.get('observation', {}).get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[12].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[12].body[1].value.func.value::Call

Source: `infra/agentinfra/roadmap_project.py:110`; AST `b0368d00393b990a107f1fc23945f7de6abb271bdf23ec31e8e6c117a30b7051`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: changed. Outputs/bindings: (none).
Calls/effect boundaries: changed.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[12].body[1].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[12].body[2]::If

Source: `infra/agentinfra/roadmap_project.py:111`; AST `d84239d8ade54dc10692c530bbf2d6878bc91512731cdd64895b204abe3633c1`.

Rust module: `infra::agentinfra::roadmap_project`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: int, observed, previous, require, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered If evaluation at root.body[13].body[3].body[13].body[12].body[2]; no call, error or mutation may be omitted. Condition: previous is not None
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[12].body[2].body[0]::Expr

Source: `infra/agentinfra/roadmap_project.py:112`; AST `374c412066c2df20710e7348ed726e98bbdd3bec8ff632ee3a53d546a36a48fd`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: int, observed, previous, require, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[3].body[13].body[12].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[12].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_project.py:112`; AST `402a0da9f67962fd524531c4e5d0c14f44c63497cc269d3d288006a001ae20f1`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: int, observed, previous, require, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[12].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[12].body[2].body[0].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_project.py:112`; AST `1fff1a2c7cc92cd31dc58aa88c53c30060970d14138cfb5ee77a48e7ee69f76e`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: previous, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[12].body[2].body[0].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[12].body[2].body[0].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_project.py:112`; AST `820be8eafd64cfce9736efac92793aaf9db6bbebc0da3e85e542506e62f3774e`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observed, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[12].body[2].body[0].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[13]::Assign

Source: `infra/agentinfra/roadmap_project.py:114`; AST `f45e298d28aced084aac5060dedc4d88c5b5fb371c8dffb16e5cbd0e08c4a331`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding. Outputs/bindings: created.
Calls/effect boundaries: binding.get, binding.get('observation', {}).get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[3].body[13].body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[13].value::Call

Source: `infra/agentinfra/roadmap_project.py:114`; AST `3accc663699663fb6a9ba9f2184d89e5c7ddb7fadedd2699afd9d8d5d4f61af9`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding. Outputs/bindings: (none).
Calls/effect boundaries: binding.get, binding.get('observation', {}).get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[13].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[13].value.func.value::Call

Source: `infra/agentinfra/roadmap_project.py:114`; AST `19383d3c3a3dd141414e57358091030cb5d155331564962bc5d64e9d2fdca72d`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding. Outputs/bindings: (none).
Calls/effect boundaries: binding.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[13].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[14]::Expr

Source: `infra/agentinfra/roadmap_project.py:115`; AST `286741f2dca7baae19990eae74a08d78ab06c11c44e343790d2a4baa0f1336cf`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: changed, created, int, require, type. Outputs/bindings: (none).
Calls/effect boundaries: changed.get, changed.get('observation', {}).get, require, type.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[3].body[13].body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[14].value::Call

Source: `infra/agentinfra/roadmap_project.py:115`; AST `94ebff5fb7b70f4546b7388e8a62f350ba3cc5923868e804d7d4b300d6cd49d0`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: changed, created, int, require, type. Outputs/bindings: (none).
Calls/effect boundaries: changed.get, changed.get('observation', {}).get, require, type.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[14].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[14].value.args[0].values[1].values[0].left::Call

Source: `infra/agentinfra/roadmap_project.py:115`; AST `c93741fd485e081b9a072bcb6670c7fcd7e5f8a44d89568b247c54f81e9eb10e`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: created, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[14].value.args[0].values[1].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[14].value.args[0].values[1].values[1].left::Call

Source: `infra/agentinfra/roadmap_project.py:115`; AST `b3202acc4c4992892c188575b83f25aaa4dc75930d133bf633292b882a08ac2d`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: changed, type. Outputs/bindings: (none).
Calls/effect boundaries: changed.get, changed.get('observation', {}).get, type.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[14].value.args[0].values[1].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[14].value.args[0].values[1].values[1].left.args[0]::Call

Source: `infra/agentinfra/roadmap_project.py:115`; AST `a4c89d1eae90c0a548a58fb22b206e12699c1b7bb90f132eed2db19579fbfbb5`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: changed. Outputs/bindings: (none).
Calls/effect boundaries: changed.get, changed.get('observation', {}).get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[14].value.args[0].values[1].values[1].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[13].body[14].value.args[0].values[1].values[1].left.args[0].func.value::Call

Source: `infra/agentinfra/roadmap_project.py:115`; AST `b0368d00393b990a107f1fc23945f7de6abb271bdf23ec31e8e6c117a30b7051`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: changed. Outputs/bindings: (none).
Calls/effect boundaries: changed.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[13].body[14].value.args[0].values[1].values[1].left.args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[14]::Return

Source: `infra/agentinfra/roadmap_project.py:120`; AST `2955caf63494833ee537ba6fa2caf6e855fff2ac2834da5ffd178c20c5befee0`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: AEGIS_RECORD_WRITER, FileTransaction, Mutation, artifacts, before, canonical, expected_digest, path, self, updated. Outputs/bindings: (none).
Calls/effect boundaries: FileTransaction, FileTransaction(self.root, [*artifacts, Mutation(path, canonical(updated) + b'\n', expected_exists=before is not None, expected_sha256=expected_digest)], state_dir=self.root / '.aegis/state/transactions', name=AEGIS_RECORD_WRITER).commit, Mutation, canonical.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Return evaluation at root.body[13].body[3].body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[14].value::Call

Source: `infra/agentinfra/roadmap_project.py:120`; AST `34175f242daf9451bb9c615e044039431fac6bb4bacecf1abb55977c688b43ec`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: AEGIS_RECORD_WRITER, FileTransaction, Mutation, artifacts, before, canonical, expected_digest, path, self, updated. Outputs/bindings: (none).
Calls/effect boundaries: FileTransaction, FileTransaction(self.root, [*artifacts, Mutation(path, canonical(updated) + b'\n', expected_exists=before is not None, expected_sha256=expected_digest)], state_dir=self.root / '.aegis/state/transactions', name=AEGIS_RECORD_WRITER).commit, Mutation, canonical.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[14].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[14].value.func.value::Call

Source: `infra/agentinfra/roadmap_project.py:120`; AST `e3c1fe5123623167d7c169d1e04c9004d71644fb600c84295e06e20bccaacbf4`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: AEGIS_RECORD_WRITER, FileTransaction, Mutation, artifacts, before, canonical, expected_digest, path, self, updated. Outputs/bindings: (none).
Calls/effect boundaries: FileTransaction, Mutation, canonical.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[14].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[14].value.func.value.args[1].elts[1]::Call

Source: `infra/agentinfra/roadmap_project.py:121`; AST `bda8b0651cd11fdeff70c7951f52f6b3b0a42ec06714fefcd3fb87fc9cd6c94c`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Mutation, before, canonical, expected_digest, path, updated. Outputs/bindings: (none).
Calls/effect boundaries: Mutation, canonical.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[14].value.func.value.args[1].elts[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[13].body[3].body[14].value.func.value.args[1].elts[1].args[1].left::Call

Source: `infra/agentinfra/roadmap_project.py:121`; AST `55c97ce00fe8675ff74e1eed48ded4cd22b3be31d967e0ab26715026d67f484e`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, updated. Outputs/bindings: (none).
Calls/effect boundaries: canonical.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[14].value.func.value.args[1].elts[1].args[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4]::FunctionDef

Source: `infra/agentinfra/roadmap_project.py:127`; AST `9f625d64f8d3c901b38d397046371b1772ed44c4fcdecd9076ebc63a34eafe21`.

Rust module: `infra::agentinfra::roadmap_project`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: AEGIS_RECORD_WRITER, BudgetLedger, FileLock, FileTransaction, Mutation, WorkspaceLease, a, any, before, bind_goal, binding, candidate, canonical, created, dict, digest, execution, inspect_process, int, k, key, lease, lease_before, lock, managed, observation, observe_native_owner, old, owner, pid, prior_binding, process_handle, record, require, self, state, type, uuid. Outputs/bindings: a, before, binding, candidate, created, execution, k, key, lease, lease_before, lock, managed, observation, old, owner, prior_binding, record, state.
Calls/effect boundaries: BudgetLedger, BudgetLedger(self.root).read, FileLock, FileTransaction, FileTransaction(self.root, [Mutation(lease.path, canonical(state) + b'\n', expected_exists=True, expected_sha256=digest(lease_before)), Mutation(self.profile.path(), canonical(record) + b'\n', expected_exists=True, expected_sha256=digest(before))], state_dir=self.root / '.aegis/state/transactions', name=AEGIS_RECORD_WRITER).commit, Mutation, WorkspaceLease, any, bind_goal, canonical, dict, digest, execution.get, execution.pop, execution.setdefault, execution.setdefault('binding_history', []).append, inspect_process, lease.path.read_bytes, lease.read, lock.acquire, lock.release, managed.get, observation['goal'].get, observe_native_owner, prior_binding.get, prior_binding.get('observation', {}).get, process_handle, require, self.profile.path, self.profile.path().read_bytes, self.read, state['history'].append, type, uuid.uuid4.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[0]::Expr

Source: `infra/agentinfra/roadmap_project.py:128`; AST `03e4cca2f0f5c8c4e974d59d85ca853b3dc7a52b2b8cd3a39c6e6645d77c87d2`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[1]::ImportFrom

Source: `infra/agentinfra/roadmap_project.py:134`; AST `636534e2245736b0b6e7173b1574c2c9c9350c49ffeb6396e41cc4d5423b0e2b`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[13].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[2]::ImportFrom

Source: `infra/agentinfra/roadmap_project.py:135`; AST `c6ebf3d38646a18850b74119bc808cd5ab82c2080d64057142776338c3e180c7`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[13].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[3]::ImportFrom

Source: `infra/agentinfra/roadmap_project.py:136`; AST `78e17dfe55d7fc70d3c6757906b88225e0003b67c382d61da76725efabb6f8ae`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[13].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[4]::Expr

Source: `infra/agentinfra/roadmap_project.py:138`; AST `aaf4645188e8cbeacdc447e11fbe39277b7b6a610588cc97ab41f20b3ab34d2f`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, self. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[4].value::Call

Source: `infra/agentinfra/roadmap_project.py:138`; AST `b7be9e5ad28cc33bdb237b10a219a686144e718d5beda654171dd221e03cc0ad`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, self. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[5]::Assign

Source: `infra/agentinfra/roadmap_project.py:139`; AST `412626dbce372a362795421fe3888ef6116ecd170c9caccf92a1ff296520a3bf`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: WorkspaceLease, self. Outputs/bindings: lease.
Calls/effect boundaries: WorkspaceLease.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[5].value::Call

Source: `infra/agentinfra/roadmap_project.py:139`; AST `408829ac552086ff1aa49ed525f89889a9374a77ff0f5e75e1759a09776c7b06`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: WorkspaceLease, self. Outputs/bindings: (none).
Calls/effect boundaries: WorkspaceLease.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[6]::Assign

Source: `infra/agentinfra/roadmap_project.py:140`; AST `8dfaec7af9c5198102a850175ca31427f1a58edea70b6a6bf39515281566b9c8`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileLock, lease. Outputs/bindings: lock.
Calls/effect boundaries: FileLock.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[6].value::Call

Source: `infra/agentinfra/roadmap_project.py:140`; AST `505ea8fde03be1c7d2625bd79989fb59e3f8e9ff9cbc6a2ad48485282a2ebeea`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileLock, lease. Outputs/bindings: (none).
Calls/effect boundaries: FileLock.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[7]::Expr

Source: `infra/agentinfra/roadmap_project.py:141`; AST `2bcfe51cf785ee29160140309ca2724ded506c99a694a1cd40da99965fea32f6`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[4].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[7].value::Call

Source: `infra/agentinfra/roadmap_project.py:141`; AST `19f113b1ff996d6a4e1349d4f629dcb1414895f291ae11a26e3a1c7c22771cf0`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8]::Try

Source: `infra/agentinfra/roadmap_project.py:142`; AST `37a16352206e21813f791e33e667b3e84fde9a9d6da4c8528234754ef00c0b76`.

Rust module: `infra::agentinfra::roadmap_project`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: AEGIS_RECORD_WRITER, BudgetLedger, FileTransaction, Mutation, a, any, before, bind_goal, binding, candidate, canonical, created, dict, digest, execution, inspect_process, int, k, key, lease, lease_before, lock, managed, observation, observe_native_owner, old, owner, pid, prior_binding, process_handle, record, require, self, state, type, uuid. Outputs/bindings: a, before, binding, candidate, created, execution, k, key, lease_before, managed, observation, old, owner, prior_binding, record, state.
Calls/effect boundaries: BudgetLedger, BudgetLedger(self.root).read, FileTransaction, FileTransaction(self.root, [Mutation(lease.path, canonical(state) + b'\n', expected_exists=True, expected_sha256=digest(lease_before)), Mutation(self.profile.path(), canonical(record) + b'\n', expected_exists=True, expected_sha256=digest(before))], state_dir=self.root / '.aegis/state/transactions', name=AEGIS_RECORD_WRITER).commit, Mutation, any, bind_goal, canonical, dict, digest, execution.get, execution.pop, execution.setdefault, execution.setdefault('binding_history', []).append, inspect_process, lease.path.read_bytes, lease.read, lock.release, managed.get, observation['goal'].get, observe_native_owner, prior_binding.get, prior_binding.get('observation', {}).get, process_handle, require, self.profile.path, self.profile.path().read_bytes, self.read, state['history'].append, type, uuid.uuid4.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Try evaluation at root.body[13].body[4].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[0]::Assign

Source: `infra/agentinfra/roadmap_project.py:143`; AST `bc3e9b47e27bdd6fea1d502b84bcc551ae8cc1670babea7ee3e7fe83e3dc289a`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: before.
Calls/effect boundaries: self.profile.path, self.profile.path().read_bytes.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[0].value::Call

Source: `infra/agentinfra/roadmap_project.py:143`; AST `414f4aecd4bacd095da0ebd623b88ed9f624539776a8eb14582b84cb0605eaf1`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.profile.path, self.profile.path().read_bytes.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[0].value.func.value::Call

Source: `infra/agentinfra/roadmap_project.py:143`; AST `5aff035e159349b40c99cc1e24ee69d81660511f1625d432552cda0b0afab929`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.profile.path.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[1]::Assign

Source: `infra/agentinfra/roadmap_project.py:144`; AST `8d60c6cf06a37f3a21e36d8d4fc569b1d94d00284e5e8e23781c46e0c0bd8c8b`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: record.
Calls/effect boundaries: self.read.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4].body[8].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[1].value::Call

Source: `infra/agentinfra/roadmap_project.py:144`; AST `1a6cd88d33383d245bb90e4e5f924f99f090d6bd29a5c43fab9e8ffb18d19d91`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.read.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[2]::Assign

Source: `infra/agentinfra/roadmap_project.py:145`; AST `e0e9d6aaa5cae6167af8fa88e07a13a439f9b554d86164a022da676b042fdb2e`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record. Outputs/bindings: execution.
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4].body[8].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[3]::Assign

Source: `infra/agentinfra/roadmap_project.py:146`; AST `f925c2b24f17e2219e120a269fca3a649c245239984905f9a46c7fd67112f9c5`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: execution. Outputs/bindings: old.
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4].body[8].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[4]::Assign

Source: `infra/agentinfra/roadmap_project.py:147`; AST `d2584c897badc3af4e2e226fbf08daaaeb8fef3bc4afd282e4532a4bfd5be081`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lease. Outputs/bindings: lease_before.
Calls/effect boundaries: lease.path.read_bytes.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4].body[8].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[4].value::Call

Source: `infra/agentinfra/roadmap_project.py:147`; AST `9301f6417a7b948060b6dc72dac88ee197c9e883d804cc9a825c110c6f2c17ac`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lease. Outputs/bindings: (none).
Calls/effect boundaries: lease.path.read_bytes.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[5]::Assign

Source: `infra/agentinfra/roadmap_project.py:148`; AST `43012a8f742ae5b8eea9ea4876b0c8094782950319d9ffb8f0869fb35a0a2cc0`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lease. Outputs/bindings: state.
Calls/effect boundaries: lease.read.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4].body[8].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[5].value::Call

Source: `infra/agentinfra/roadmap_project.py:148`; AST `08aa80adbe4e0e0a9d90646e112ab278544265b2c243580650be2680c6546650`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lease. Outputs/bindings: (none).
Calls/effect boundaries: lease.read.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[6]::Expr

Source: `infra/agentinfra/roadmap_project.py:149`; AST `806fd53f4ea553063e746ce5263e211f91c39bac820c77ddc51e109983c59ba9`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: old, require, state. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[4].body[8].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[6].value::Call

Source: `infra/agentinfra/roadmap_project.py:149`; AST `4641bf9de5411a2c06e0bf7e0a8f56357e48e7f5921d62bf3e58cdf3e63eed17`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old, require, state. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[7]::Expr

Source: `infra/agentinfra/roadmap_project.py:150`; AST `8f4ed3d0ca86e581a5a245d42a8ca3d1092586e391c0f91f4f9702fe1df053d7`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: inspect_process, old, require. Outputs/bindings: (none).
Calls/effect boundaries: inspect_process, require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[4].body[8].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[7].value::Call

Source: `infra/agentinfra/roadmap_project.py:150`; AST `fa6cb364d516228f19ec58878c7eee96dc265d26efdcdba8d90d3464d5392ccf`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inspect_process, old, require. Outputs/bindings: (none).
Calls/effect boundaries: inspect_process, require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[7].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_project.py:150`; AST `384d62b5ed5616cea802e1d4bc89cb03369c057cce95e8748897e45e0bd89f47`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inspect_process, old. Outputs/bindings: (none).
Calls/effect boundaries: inspect_process.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[7].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[8]::Expr

Source: `infra/agentinfra/roadmap_project.py:151`; AST `71adb58bba317e459406bd6c8aa458c42a5ea8d1c1fcef09bac713abe1e93ed0`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: BudgetLedger, a, any, require, self. Outputs/bindings: a.
Calls/effect boundaries: BudgetLedger, BudgetLedger(self.root).read, any, require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[4].body[8].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[8].value::Call

Source: `infra/agentinfra/roadmap_project.py:151`; AST `d07370113a3c788ff62b6a636e85b8df1bbb83f8e53a0eabfece249b41ef0547`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: BudgetLedger, a, any, require, self. Outputs/bindings: a.
Calls/effect boundaries: BudgetLedger, BudgetLedger(self.root).read, any, require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[8].value.args[0].operand::Call

Source: `infra/agentinfra/roadmap_project.py:151`; AST `08f7991148e51fc705f190ecfaa740874972cef59a7746ef06ab9bd4d0166977`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: BudgetLedger, a, any, self. Outputs/bindings: a.
Calls/effect boundaries: BudgetLedger, BudgetLedger(self.root).read, any.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[8].value.args[0].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[8].value.args[0].operand.args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_project.py:151`; AST `f7c87e27b1ee0c439c888c3731a4706b764504267c07e67348ae13974563c50c`.

Rust module: `infra::agentinfra::roadmap_project`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: BudgetLedger, a, self. Outputs/bindings: a.
Calls/effect boundaries: BudgetLedger, BudgetLedger(self.root).read.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[13].body[4].body[8].body[8].value.args[0].operand.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[8].value.args[0].operand.args[0].generators[0].iter.value::Call

Source: `infra/agentinfra/roadmap_project.py:151`; AST `142a8dfce79d0ff91a4eb65f132fe4e998b0ac8b93495d5c34cbe56c016541dc`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: BudgetLedger, self. Outputs/bindings: (none).
Calls/effect boundaries: BudgetLedger, BudgetLedger(self.root).read.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[8].value.args[0].operand.args[0].generators[0].iter.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[8].value.args[0].operand.args[0].generators[0].iter.value.func.value::Call

Source: `infra/agentinfra/roadmap_project.py:151`; AST `7284f87df770a43bb43b821afc3c980b7c14f951534180b5361ce68c7aef3690`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: BudgetLedger, self. Outputs/bindings: (none).
Calls/effect boundaries: BudgetLedger.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[8].value.args[0].operand.args[0].generators[0].iter.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[9]::If

Source: `infra/agentinfra/roadmap_project.py:153`; AST `64a9bb2f8477e1ff8627487cde74df3fc177d64f15c5e01f3e9de77ef0290013`.

Rust module: `infra::agentinfra::roadmap_project`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: execution, inspect_process, managed, require. Outputs/bindings: managed.
Calls/effect boundaries: execution.get, execution.pop, inspect_process, managed.get, require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered If evaluation at root.body[13].body[4].body[8].body[9]; no call, error or mutation may be omitted. Condition: execution.get('integration_path') == 'managed_app_server'
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[9].test.left::Call

Source: `infra/agentinfra/roadmap_project.py:153`; AST `ea2fbedf64fbdf2c27b273169e5fb0e5eba266e110561ac4538f727316ad66ca`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: execution. Outputs/bindings: (none).
Calls/effect boundaries: execution.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[9].test.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[9].body[0]::Assign

Source: `infra/agentinfra/roadmap_project.py:154`; AST `d180a2f6daced111db7b95f62ae531b5793c44cec8c49b87271594320ceb0e70`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: execution. Outputs/bindings: managed.
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4].body[8].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[9].body[1]::Expr

Source: `infra/agentinfra/roadmap_project.py:155`; AST `5763773d6358b905cc8c7616956c9373c67867af5d6ea8f74431e53c0549fe5f`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: inspect_process, managed, require. Outputs/bindings: (none).
Calls/effect boundaries: inspect_process, managed.get, require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[4].body[8].body[9].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[9].body[1].value::Call

Source: `infra/agentinfra/roadmap_project.py:155`; AST `8ac3151b1d95ede6d00a19a082ef823827ea4a850aba0347cb63f2d8c4db8283`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inspect_process, managed, require. Outputs/bindings: (none).
Calls/effect boundaries: inspect_process, managed.get, require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[9].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[9].body[1].value.args[0].values[0].operand::Call

Source: `infra/agentinfra/roadmap_project.py:155`; AST `192c7127a0a0bf798da2cd4590c624ae1532fc82a79516cddf1d0f501597055b`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: managed. Outputs/bindings: (none).
Calls/effect boundaries: managed.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[9].body[1].value.args[0].values[0].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[9].body[1].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_project.py:155`; AST `83d4d5f12970a46f707987cbacda8616011784521838870215d9f36575be22d8`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inspect_process, managed. Outputs/bindings: (none).
Calls/effect boundaries: inspect_process.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[9].body[1].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[9].body[2]::Assign

Source: `infra/agentinfra/roadmap_project.py:157`; AST `77898408e410e207cf1e3c04f1530f12f2ba3455a68d24c1bae54c2be0469710`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: execution, managed. Outputs/bindings: (none).
Calls/effect boundaries: execution.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4].body[8].body[9].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[9].body[2].value.elts[0].value::Call

Source: `infra/agentinfra/roadmap_project.py:157`; AST `13a967cb170892160e8cfd5f9346b1a753d77a871a1aff22c7382c8f4fac8a25`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: execution. Outputs/bindings: (none).
Calls/effect boundaries: execution.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[9].body[2].value.elts[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[9].body[3]::Expr

Source: `infra/agentinfra/roadmap_project.py:158`; AST `28ca94b296d039b2b1f3fe15e429b3975848ff61df10934fa19cc0ec51b8898e`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: execution. Outputs/bindings: (none).
Calls/effect boundaries: execution.pop.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[4].body[8].body[9].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[9].body[3].value::Call

Source: `infra/agentinfra/roadmap_project.py:158`; AST `119277d23f45298e118404ba85d4034f066611807b61e1492ca0384d502ccd67`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: execution. Outputs/bindings: (none).
Calls/effect boundaries: execution.pop.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[9].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[9].body[4]::Assign

Source: `infra/agentinfra/roadmap_project.py:159`; AST `4fe36360fb919589544c81e212fc3aaae53ffa7e199720563db2b7e5547fdb8b`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: execution. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4].body[8].body[9].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[10]::Assign

Source: `infra/agentinfra/roadmap_project.py:160`; AST `e522bab5edcd64fad37936ed5a604c842ce3e3fc65f1cddb57fbc1955e9024a7`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, old, pid, process_handle. Outputs/bindings: candidate.
Calls/effect boundaries: dict, process_handle.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4].body[8].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[10].value::Call

Source: `infra/agentinfra/roadmap_project.py:160`; AST `bc38922586175774ca7a2b7eb1ca7bda39f001cdbc61660a16537904660c463d`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, old, pid, process_handle. Outputs/bindings: (none).
Calls/effect boundaries: dict, process_handle.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[10].value.keywords[0].value::Call

Source: `infra/agentinfra/roadmap_project.py:160`; AST `16480ca8e334f62dda8004139fe9bc1f8c77d9aec01074f0dabd014f7c2623d0`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: pid, process_handle. Outputs/bindings: (none).
Calls/effect boundaries: process_handle.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[10].value.keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[11]::Assign

Source: `infra/agentinfra/roadmap_project.py:161`; AST `07498a5da0cf3ad36670a67774a16960ace3248a50b99ffd779da909224f8bd9`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: candidate, observe_native_owner, self. Outputs/bindings: observation.
Calls/effect boundaries: observe_native_owner.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4].body[8].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[11].value::Call

Source: `infra/agentinfra/roadmap_project.py:161`; AST `5419ded5847d10b163e77c2413634305b660aded66cc06f863f8ef17238e344f`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: candidate, observe_native_owner, self. Outputs/bindings: (none).
Calls/effect boundaries: observe_native_owner.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[12]::Expr

Source: `infra/agentinfra/roadmap_project.py:162`; AST `6673c826873f179d4f8937d7b0bbdcaa2f090854fabed1b05e0066618ef156bd`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observation, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[4].body[8].body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[12].value::Call

Source: `infra/agentinfra/roadmap_project.py:162`; AST `f88f9e9769e9a74f7eb7e488879cb609734dd757bbb07569d9423389411d5bdc`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observation, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[13]::Assign

Source: `infra/agentinfra/roadmap_project.py:165`; AST `7f1ddc32f66f08cfea2d4f761f360cafe537ebe48106b30a09553289ca8e2e8c`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: execution. Outputs/bindings: prior_binding.
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4].body[8].body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[14]::Assign

Source: `infra/agentinfra/roadmap_project.py:166`; AST `06b8ba9f4d038a9493c13433765201e6a9d1119a09010b0b5c9df72200cfa156`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: prior_binding. Outputs/bindings: created.
Calls/effect boundaries: prior_binding.get, prior_binding.get('observation', {}).get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4].body[8].body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[14].value::Call

Source: `infra/agentinfra/roadmap_project.py:166`; AST `557e156df94848d5a82b4a0547a20df327d41ae57bc09c8550e71f4c6c54d875`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: prior_binding. Outputs/bindings: (none).
Calls/effect boundaries: prior_binding.get, prior_binding.get('observation', {}).get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[14].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[14].value.func.value::Call

Source: `infra/agentinfra/roadmap_project.py:166`; AST `20c23494a12e75bfe9e50a20cc836d5df623234865d1a5ce162457413cba59d9`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: prior_binding. Outputs/bindings: (none).
Calls/effect boundaries: prior_binding.get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[14].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[15]::Expr

Source: `infra/agentinfra/roadmap_project.py:167`; AST `9e8808c9ea4d2e46c35eede086b3b0db8c899cef51cdd2444c6b2f3a942644b2`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: created, int, observation, require, type. Outputs/bindings: (none).
Calls/effect boundaries: observation['goal'].get, require, type.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[4].body[8].body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[15].value::Call

Source: `infra/agentinfra/roadmap_project.py:167`; AST `1860cd6647eb7f78e1a95b80d2f4af5087a66cf1bfd0ff732b96eb89eecf560d`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: created, int, observation, require, type. Outputs/bindings: (none).
Calls/effect boundaries: observation['goal'].get, require, type.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[15].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[15].value.args[0].values[1].values[0].left::Call

Source: `infra/agentinfra/roadmap_project.py:167`; AST `c93741fd485e081b9a072bcb6670c7fcd7e5f8a44d89568b247c54f81e9eb10e`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: created, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[15].value.args[0].values[1].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[15].value.args[0].values[1].values[1].left::Call

Source: `infra/agentinfra/roadmap_project.py:167`; AST `64ebca88c6b44391e2bdd3bda1c0c23020467dc3dd6975813a5bb1a785cce51e`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observation, type. Outputs/bindings: (none).
Calls/effect boundaries: observation['goal'].get, type.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[15].value.args[0].values[1].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[15].value.args[0].values[1].values[1].left.args[0]::Call

Source: `infra/agentinfra/roadmap_project.py:167`; AST `cc5afaf8ab83cf6b21d9f29af0f1c0360901185acfb1a5b28468fdd3c2f5857d`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observation. Outputs/bindings: (none).
Calls/effect boundaries: observation['goal'].get.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[15].value.args[0].values[1].values[1].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[16]::Assign

Source: `infra/agentinfra/roadmap_project.py:169`; AST `d9ab3ceff6ebce93e30f4df2c3cc0564d3aa2d94fbae2c2066795334e310d909`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bind_goal, observation, old, prior_binding. Outputs/bindings: binding.
Calls/effect boundaries: bind_goal.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4].body[8].body[16]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[16].value::Call

Source: `infra/agentinfra/roadmap_project.py:169`; AST `fc20cb3a2ae65485c04b5c53105a11e07deed6f753a1f431998a680a87b8943b`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bind_goal, observation, old, prior_binding. Outputs/bindings: (none).
Calls/effect boundaries: bind_goal.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[16].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[17]::For

Source: `infra/agentinfra/roadmap_project.py:171`; AST `f45cc9b3702467b094b2615153db8c92bf60ab454e097cedd2d314249ed9fad1`.

Rust module: `infra::agentinfra::roadmap_project`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: binding, key, prior_binding, require. Outputs/bindings: key.
Calls/effect boundaries: require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered For evaluation at root.body[13].body[4].body[8].body[17]; no call, error or mutation may be omitted. Iteration: key in ('tokensUsed', 'timeUsedSeconds')
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[17].body[0]::Expr

Source: `infra/agentinfra/roadmap_project.py:172`; AST `94194c55b4a652d36c19cd920069ed6ecc4e9cd27ddfa4b86a23317c8a25b621`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, key, prior_binding, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[4].body[8].body[17].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[17].body[0].value::Call

Source: `infra/agentinfra/roadmap_project.py:172`; AST `0e9e21668f10ccea2e3bc7cb0fcf0cfb31923f8e360a13694d02ade82c42e061`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, key, prior_binding, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[17].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[18]::Expr

Source: `infra/agentinfra/roadmap_project.py:174`; AST `1a1c4ace682cb7470d22106062e3a97d877c33ff231dc35b00cbe2f9788e395e`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: inspect_process, old, require. Outputs/bindings: (none).
Calls/effect boundaries: inspect_process, require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[4].body[8].body[18]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[18].value::Call

Source: `infra/agentinfra/roadmap_project.py:174`; AST `386a9dd671a8cc01038ec6a8d3d8ad374509704e33745bbe1588a670814dfde3`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inspect_process, old, require. Outputs/bindings: (none).
Calls/effect boundaries: inspect_process, require.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[18].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[18].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_project.py:174`; AST `384d62b5ed5616cea802e1d4bc89cb03369c057cce95e8748897e45e0bd89f47`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inspect_process, old. Outputs/bindings: (none).
Calls/effect boundaries: inspect_process.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[18].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[19]::AugAssign

Source: `infra/agentinfra/roadmap_project.py:175`; AST `38db64fc0fd261bcd36fd86519d7be1d4372f5e0b73c6a7eb35466b51ac7e90b`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: state. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered AugAssign evaluation at root.body[13].body[4].body[8].body[19]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[20]::Assign

Source: `infra/agentinfra/roadmap_project.py:176`; AST `7404f23caa884c585bba0cf11adcf676265fda0397df57cb51a65290ce527cc1`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: candidate, dict, state, uuid. Outputs/bindings: owner.
Calls/effect boundaries: dict, uuid.uuid4.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4].body[8].body[20]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[20].value::Call

Source: `infra/agentinfra/roadmap_project.py:176`; AST `0ebab40c3e0009f5e45120daa847eecd6352db76c40327c35ad214f7fe16ef56`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: candidate, dict, state, uuid. Outputs/bindings: (none).
Calls/effect boundaries: dict, uuid.uuid4.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[20].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[20].value.keywords[1].value.value::Call

Source: `infra/agentinfra/roadmap_project.py:176`; AST `87eafda000cba758be33f767d487f36fa6a34917ff4cfe4cbd289edd7d07163b`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: uuid. Outputs/bindings: (none).
Calls/effect boundaries: uuid.uuid4.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[20].value.keywords[1].value.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[21]::Expr

Source: `infra/agentinfra/roadmap_project.py:177`; AST `ad1838dd298ca59f08d589e64b968ec20687ce9a2166e9a59fe5c523fe7c1af4`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observation, old, owner, state. Outputs/bindings: (none).
Calls/effect boundaries: state['history'].append.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[4].body[8].body[21]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[21].value::Call

Source: `infra/agentinfra/roadmap_project.py:177`; AST `b975d44096a8f174061e5dfae41d90873edbff1ac27cd9ab75365ce5c19c605f`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observation, old, owner, state. Outputs/bindings: (none).
Calls/effect boundaries: state['history'].append.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[21].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[22]::Assign

Source: `infra/agentinfra/roadmap_project.py:179`; AST `dc38efcf17a8f88757f8735dd9496caa35a3454129aa21833499e4f98c21ac91`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: owner, state. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4].body[8].body[22]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[23]::Assign

Source: `infra/agentinfra/roadmap_project.py:180`; AST `9d908f7e935b20ada5be774054b2d5c939b19cfdceee0baccc2dd000cd9097b0`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: execution, owner. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4].body[8].body[23]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[24]::Expr

Source: `infra/agentinfra/roadmap_project.py:181`; AST `810d9c64a62bdcab1dec43aac2c66d5c8956aa50ace16f2fc9076bc7d02aec5b`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: execution, prior_binding. Outputs/bindings: (none).
Calls/effect boundaries: execution.setdefault, execution.setdefault('binding_history', []).append.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[4].body[8].body[24]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[24].value::Call

Source: `infra/agentinfra/roadmap_project.py:181`; AST `9c683f2a1bbf0c7cd4e2475cede60ff44a5cc0c09b2cd817b95fafbf38815002`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: execution, prior_binding. Outputs/bindings: (none).
Calls/effect boundaries: execution.setdefault, execution.setdefault('binding_history', []).append.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[24].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[24].value.func.value::Call

Source: `infra/agentinfra/roadmap_project.py:181`; AST `3a15a660ba538eae04fa83703a7a8564a1c81d56bccf87237617c5eee063b623`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: execution. Outputs/bindings: (none).
Calls/effect boundaries: execution.setdefault.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[24].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[25]::Assign

Source: `infra/agentinfra/roadmap_project.py:182`; AST `ee85b8710f697cd4b5aaf8ae5a5c311fce8a1fb9cc8f7a294fc4577a66c9f128`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, execution. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4].body[8].body[25]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[26]::Assign

Source: `infra/agentinfra/roadmap_project.py:183`; AST `af55f5d93b15054096b30d4746c0752a8d60ac9e023072d595d26c98b7655cfb`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: execution, k, observation. Outputs/bindings: k.
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4].body[8].body[26]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[26].value::DictComp

Source: `infra/agentinfra/roadmap_project.py:183`; AST `65dbbb7ef6ebe01c3c80c72d46a952cd25c0dee1d19bbfa2e84034788afb1284`.

Rust module: `infra::agentinfra::roadmap_project`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: k, observation. Outputs/bindings: k.
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered DictComp evaluation at root.body[13].body[4].body[8].body[26].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[27]::Assign

Source: `infra/agentinfra/roadmap_project.py:184`; AST `5a7110dfd37dde08a098ed3543f2b7867bfc23e47711ae0f9ca1b22b6bf83f98`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: AEGIS_RECORD_WRITER, record. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4].body[8].body[27]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[28]::Expr

Source: `infra/agentinfra/roadmap_project.py:185`; AST `6f56dadbd8f17eedfe2ad226a7da0b30d713509d850e3f7378058eec11f157cc`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: AEGIS_RECORD_WRITER, FileTransaction, Mutation, before, canonical, digest, lease, lease_before, record, self, state. Outputs/bindings: (none).
Calls/effect boundaries: FileTransaction, FileTransaction(self.root, [Mutation(lease.path, canonical(state) + b'\n', expected_exists=True, expected_sha256=digest(lease_before)), Mutation(self.profile.path(), canonical(record) + b'\n', expected_exists=True, expected_sha256=digest(before))], state_dir=self.root / '.aegis/state/transactions', name=AEGIS_RECORD_WRITER).commit, Mutation, canonical, digest, self.profile.path.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[4].body[8].body[28]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[28].value::Call

Source: `infra/agentinfra/roadmap_project.py:185`; AST `5a1a3597fab3de14ae8c59a4a2d73bcf832bfcfa5a1cdd2b8f714a49ebfaa115`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: AEGIS_RECORD_WRITER, FileTransaction, Mutation, before, canonical, digest, lease, lease_before, record, self, state. Outputs/bindings: (none).
Calls/effect boundaries: FileTransaction, FileTransaction(self.root, [Mutation(lease.path, canonical(state) + b'\n', expected_exists=True, expected_sha256=digest(lease_before)), Mutation(self.profile.path(), canonical(record) + b'\n', expected_exists=True, expected_sha256=digest(before))], state_dir=self.root / '.aegis/state/transactions', name=AEGIS_RECORD_WRITER).commit, Mutation, canonical, digest, self.profile.path.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[28].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[28].value.func.value::Call

Source: `infra/agentinfra/roadmap_project.py:185`; AST `af0c620f38c4f8a91bfecb37b9f422f06272ec5af4bacf8af728a9739433f793`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: AEGIS_RECORD_WRITER, FileTransaction, Mutation, before, canonical, digest, lease, lease_before, record, self, state. Outputs/bindings: (none).
Calls/effect boundaries: FileTransaction, Mutation, canonical, digest, self.profile.path.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[28].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[28].value.func.value.args[1].elts[0]::Call

Source: `infra/agentinfra/roadmap_project.py:185`; AST `94d270008b4c2fb0d71a43601acc33dc45a89726cec99c3d1e083ca649e9b352`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Mutation, canonical, digest, lease, lease_before, state. Outputs/bindings: (none).
Calls/effect boundaries: Mutation, canonical, digest.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[28].value.func.value.args[1].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[28].value.func.value.args[1].elts[0].args[1].left::Call

Source: `infra/agentinfra/roadmap_project.py:185`; AST `4fdaed20db78874f0bcd85d946f6597478be0eaaf66e4f20cde7ed46382c2992`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, state. Outputs/bindings: (none).
Calls/effect boundaries: canonical.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[28].value.func.value.args[1].elts[0].args[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[28].value.func.value.args[1].elts[0].keywords[1].value::Call

Source: `infra/agentinfra/roadmap_project.py:186`; AST `5b0afbd5a70ac35d78c1ac833e6336088a7716fa789f07c04db8e55b1fd02664`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, lease_before. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[28].value.func.value.args[1].elts[0].keywords[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[28].value.func.value.args[1].elts[1]::Call

Source: `infra/agentinfra/roadmap_project.py:187`; AST `80b28ef2172cf8c226eecaa8700ca78888e88215f24c0cff15f96fef69438f17`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Mutation, before, canonical, digest, record, self. Outputs/bindings: (none).
Calls/effect boundaries: Mutation, canonical, digest, self.profile.path.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[28].value.func.value.args[1].elts[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[28].value.func.value.args[1].elts[1].args[0]::Call

Source: `infra/agentinfra/roadmap_project.py:187`; AST `5aff035e159349b40c99cc1e24ee69d81660511f1625d432552cda0b0afab929`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.profile.path.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[28].value.func.value.args[1].elts[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[28].value.func.value.args[1].elts[1].args[1].left::Call

Source: `infra/agentinfra/roadmap_project.py:187`; AST `54f160f3a3abda8314755593356f77dc6e10daab8f07552bdf9b5f9e686d526c`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, record. Outputs/bindings: (none).
Calls/effect boundaries: canonical.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[28].value.func.value.args[1].elts[1].args[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[28].value.func.value.args[1].elts[1].keywords[1].value::Call

Source: `infra/agentinfra/roadmap_project.py:188`; AST `4a63ff00fb497e1d094ddb9e4f8ada535aacd403c14cfceee7fc8dd669fbee57`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before, digest. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].body[28].value.func.value.args[1].elts[1].keywords[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].body[29]::Return

Source: `infra/agentinfra/roadmap_project.py:190`; AST `854dafd97eff386c26152d663b69c1304d77a72a76d93e00784dfbd1ad3f337b`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observation, owner. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Return evaluation at root.body[13].body[4].body[8].body[29]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].finalbody[0]::Expr

Source: `infra/agentinfra/roadmap_project.py:192`; AST `9aa6f04fc26ee6b3f6fe1a19158adb3cfde13709dcae4a7cc38bccbb2655afb2`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[4].body[8].finalbody[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::rebind_native_process::root.body[13].body[4].body[8].finalbody[0].value::Call

Source: `infra/agentinfra/roadmap_project.py:192`; AST `107c5710331db61e695f7d71256d48862412d15c223e204da5c71c497352b634`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[8].finalbody[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::adopt_managed_runner::root.body[13].body[5]::FunctionDef

Source: `infra/agentinfra/roadmap_project.py:194`; AST `af0a7e2ac9d64d7f99a4fe9f92d43438c62b229364b734fa3f20292232c0f7a9`.

Rust module: `infra::agentinfra::roadmap_project`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: adopt_managed_runner, authorization_id, bool, dict, protocol, self, str, user_authorized. Outputs/bindings: (none).
Calls/effect boundaries: adopt_managed_runner.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::adopt_managed_runner::root.body[13].body[5].body[0]::ImportFrom

Source: `infra/agentinfra/roadmap_project.py:195`; AST `4e234d95bb2aaafbe9d27d66789978afd750cf6112ccccc4316c2b03ff1aa084`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[13].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::adopt_managed_runner::root.body[13].body[5].body[1]::Return

Source: `infra/agentinfra/roadmap_project.py:196`; AST `0867960be6a8d8277bde7878e9990d77557f431c9958afc9814077ce91b9b9d8`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: adopt_managed_runner, authorization_id, protocol, self, user_authorized. Outputs/bindings: (none).
Calls/effect boundaries: adopt_managed_runner.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Return evaluation at root.body[13].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::adopt_managed_runner::root.body[13].body[5].body[1].value::Call

Source: `infra/agentinfra/roadmap_project.py:196`; AST `c0f02378c969aa46255ac34896c35e95d103a7f11d9bfbfe7eab12a65e1ec4c1`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: adopt_managed_runner, authorization_id, protocol, self, user_authorized. Outputs/bindings: (none).
Calls/effect boundaries: adopt_managed_runner.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::describe::root.body[13].body[6]::FunctionDef

Source: `infra/agentinfra/roadmap_project.py:198`; AST `be50439862fddc2b431f2eaadd393ee578978e823f09de57649aaa7706cb4e72`.

Rust module: `infra::agentinfra::roadmap_project`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: AEGIS_RECORD_WRITER, INTERFACE_VERSION, dict, profile, self, str. Outputs/bindings: profile.
Calls/effect boundaries: str.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::describe::root.body[13].body[6].body[0]::Assign

Source: `infra/agentinfra/roadmap_project.py:199`; AST `a28fbcf33fb701199f74297ed1430e7ecb69a22057939b4c84da0598d8c0f9ca`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: profile.
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::describe::root.body[13].body[6].body[1]::Return

Source: `infra/agentinfra/roadmap_project.py:200`; AST `93f5f27ac3ab6816223140b0e310cfcdf9442cd5ba8564f6990bf5f1bce06642`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: AEGIS_RECORD_WRITER, INTERFACE_VERSION, profile, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Return evaluation at root.body[13].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::describe::root.body[13].body[6].body[1].value.values[3]::Call

Source: `infra/agentinfra/roadmap_project.py:202`; AST `9136c0e0a63751ee7da8cc0e9796564d610214ec380fd8ea3a44104feaf4cb44`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: profile, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, dataclasses, locks, pathlib, roadmap_codex, roadmap_lease, roadmap_managed, roadmap_native, roadmap_records, roadmap_runtime, security, transaction, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].body[1].value.values[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
