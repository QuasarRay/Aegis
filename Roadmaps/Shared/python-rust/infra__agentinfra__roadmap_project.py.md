# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 155. Inventory digest: `234a95bca2b94e76e228f270189b089153d4fa420b0fde989e2398f22c694368`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/roadmap_project.py::module::root::Module

Source: `infra/agentinfra/roadmap_project.py:1`; AST `e47a20028f65f12457c036a0198a8e58ae17580fa08d856f8b7c1fb3522d4f65`.

Rust module: `infra::agentinfra::roadmap_project`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: AEGIS_RECORD_WRITER, FileTransaction, INTERFACE_VERSION, Mutation, Path, ProjectProfileV1, WorkspaceLease, allow_create, artifacts, before, binding, bool, canonical, changed, classmethod, cls, confined_path, current, dataclass, dict, digest, execution, expected_digest, fields, int, isinstance, key, len, loads, new_execution, observed, old_history, owner, path, previous, profile, profiles, project, read_json, record, repository, require, root, self, staticmethod, str, tuple, type, updated, validate_record, value. Outputs/bindings: AEGIS_RECORD_WRITER, INTERFACE_VERSION, before, binding, branch, canonical_record, changed, current, declared_repository, execution, key, language_boundary, new_execution, observed, old_history, owner, path, previous, profile, profiles, project, repository, root, updated, value.
Calls/effect boundaries: FileTransaction, FileTransaction(self.root, [*artifacts, Mutation(path, canonical(updated) + b'\n', expected_exists=before is not None, expected_sha256=expected_digest)], state_dir=self.root / '.aegis/state/transactions', name=AEGIS_RECORD_WRITER).commit, Mutation, Path, ProjectProfileV1.from_registry, WorkspaceLease, WorkspaceLease(self.root).assert_owner, before.decode, binding.get, binding.get('observation', {}).get, bool, canonical, changed.get, changed.get('observation', {}).get, cls, confined_path, current.get, dataclass, dict, digest, execution.get, fields.get, isinstance, len, loads, new_execution.get, owner.get, path.exists, path.read_bytes, read_json, record.get, require, root.resolve, self._validate_aegis, self.profile.path, str, type, updated.get, updated.get('execution', {}).get, validate_record.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

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
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

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
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

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
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

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
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::root.body[4]::ImportFrom

Source: `infra/agentinfra/roadmap_project.py:12`; AST `09d8e9e8f6fd64b1de599cd7bc89a5b39b492565154c1945944f226444aab849`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::root.body[5]::ImportFrom

Source: `infra/agentinfra/roadmap_project.py:13`; AST `01f51128853e6dbb0ff4d0ab5ead27e38e10d07244cf63b3a3c2fef1ef988a5b`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::root.body[6]::ImportFrom

Source: `infra/agentinfra/roadmap_project.py:14`; AST `c77b99ce1220eaeadd24d0d2eb90624f8e6b280576577774ee57598a0f5eef8f`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::root.body[7]::ImportFrom

Source: `infra/agentinfra/roadmap_project.py:15`; AST `c2a64003604dd1da38b622b02ca5190bea13e78ec6647b9f914f7257516a593e`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered ImportFrom evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::root.body[8]::Assign

Source: `infra/agentinfra/roadmap_project.py:18`; AST `450386d2b05707b77cb785f3c9c72b49c8717abae76f79b264237aee79ca0820`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: INTERFACE_VERSION.
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::root.body[9]::Assign

Source: `infra/agentinfra/roadmap_project.py:19`; AST `2a9a7a57751e02a2d3b29d52efc20cb0353895206cf862be5e948f11d5968d8e`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: AEGIS_RECORD_WRITER.
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::root.body[10]::ClassDef

Source: `infra/agentinfra/roadmap_project.py:23`; AST `a4b800e04b45befe9cf2aa04645113b0e8487a2f665c26d69fc3adafc8729865`.

Rust module: `infra::agentinfra::roadmap_project`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: Path, ProjectProfileV1, classmethod, cls, confined_path, dataclass, dict, profile, profiles, project, read_json, repository, require, root, self, str, validate_record. Outputs/bindings: branch, canonical_record, declared_repository, language_boundary, profile, profiles, project, repository, root.
Calls/effect boundaries: Path, cls, confined_path, dataclass, read_json, require, root.resolve, validate_record.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered ClassDef evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::root.body[10].body[0]::AnnAssign

Source: `infra/agentinfra/roadmap_project.py:24`; AST `197b340a07f8e9ef2feb63e72d6ef223ced2a2ef2175eefe6a66ab19abfaa668`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: str. Outputs/bindings: project.
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered AnnAssign evaluation at root.body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::root.body[10].body[1]::AnnAssign

Source: `infra/agentinfra/roadmap_project.py:25`; AST `78e7d5541a862d32b751fc45dd4f529c85f532020acd5c392a0b8084e5582311`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: str. Outputs/bindings: declared_repository.
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered AnnAssign evaluation at root.body[10].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::root.body[10].body[2]::AnnAssign

Source: `infra/agentinfra/roadmap_project.py:26`; AST `483ebd0d02ca9d2604287add0eeb2b5b62cef89dfa4ecf5375cfb329feefa898`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path. Outputs/bindings: repository.
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered AnnAssign evaluation at root.body[10].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::root.body[10].body[3]::AnnAssign

Source: `infra/agentinfra/roadmap_project.py:27`; AST `1b775d016e839515a2ae3c3a5e7dbf8d89f90f2a8aa67cbbd09fc162fc9f8d19`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: str. Outputs/bindings: branch.
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered AnnAssign evaluation at root.body[10].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::root.body[10].body[4]::AnnAssign

Source: `infra/agentinfra/roadmap_project.py:28`; AST `fd04b3a40d256a23e6db87818a042486ce0f68ab02d8d8a0e27c3f9bc7ed38b5`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: str. Outputs/bindings: canonical_record.
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered AnnAssign evaluation at root.body[10].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::root.body[10].body[5]::AnnAssign

Source: `infra/agentinfra/roadmap_project.py:29`; AST `8df71f3332103551ecd5fcc941376aea25e5ddfd0f061f07350fe9e804351754`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: str. Outputs/bindings: language_boundary.
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered AnnAssign evaluation at root.body[10].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::from_registry::root.body[10].body[6]::FunctionDef

Source: `infra/agentinfra/roadmap_project.py:32`; AST `5fb1b1291add74db30664da314fb496a0be14abd4a60fcff3174cf43c59f1ad5`.

Rust module: `infra::agentinfra::roadmap_project`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, ProjectProfileV1, classmethod, cls, dict, profile, profiles, project, read_json, repository, require, root, str, validate_record. Outputs/bindings: profile, profiles, repository, root.
Calls/effect boundaries: Path, cls, read_json, require, root.resolve, validate_record.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::from_registry::root.body[10].body[6].body[0]::Assign

Source: `infra/agentinfra/roadmap_project.py:33`; AST `7b881662a93f1cabda6daa8de666cd56431dd47a61da7e3a5a8856defd752ca2`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: root.
Calls/effect boundaries: root.resolve.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::from_registry::root.body[10].body[6].body[0].value::Call

Source: `infra/agentinfra/roadmap_project.py:33`; AST `b97f3f463d4724206af2869ad4674d5eb373167f052507971a722ecc8f771a87`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::from_registry::root.body[10].body[6].body[1]::Assign

Source: `infra/agentinfra/roadmap_project.py:34`; AST `021f6eca041a0a0fa0513a1fccdb93990bb217885976cda46ca8cce7b5476bca`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: profiles, read_json, root. Outputs/bindings: profiles.
Calls/effect boundaries: read_json.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::from_registry::root.body[10].body[6].body[1].value.body.value::Call

Source: `infra/agentinfra/roadmap_project.py:34`; AST `8e7e5aa59eb3d5aad4383ca406ca14418b9e912a465b4f7a0ac32e45ae51a19a`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: read_json, root. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[1].value.body.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::from_registry::root.body[10].body[6].body[2]::Expr

Source: `infra/agentinfra/roadmap_project.py:35`; AST `1451aea661a1b5608c1afb771d83fc520b6f348eb621a6c42945c407bd64ebcc`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: profiles, project, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[6].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::from_registry::root.body[10].body[6].body[2].value::Call

Source: `infra/agentinfra/roadmap_project.py:35`; AST `59424e348ed9154663450320bc7d2ad6babe48e35c7e4e3c5fe320fe5e037e0e`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: profiles, project, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::from_registry::root.body[10].body[6].body[3]::Assign

Source: `infra/agentinfra/roadmap_project.py:36`; AST `293d4c7c3d1a384eb85a76e0ae9ddcc73a29da5f35eb2b003134e9db65739a5d`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: profiles, project. Outputs/bindings: profile.
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[6].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::from_registry::root.body[10].body[6].body[4]::Expr

Source: `infra/agentinfra/roadmap_project.py:37`; AST `680e40669754d128f7308c98ce1782aa59aedd157758501f9bdab4043eb74461`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: profile, root, validate_record. Outputs/bindings: (none).
Calls/effect boundaries: validate_record.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[6].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::from_registry::root.body[10].body[6].body[4].value::Call

Source: `infra/agentinfra/roadmap_project.py:37`; AST `f062319fbd72194e8e55a8eaf50c321a21daf2a88a3140f1163bcc0c6b2cbc6a`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: profile, root, validate_record. Outputs/bindings: (none).
Calls/effect boundaries: validate_record.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::from_registry::root.body[10].body[6].body[5]::Expr

Source: `infra/agentinfra/roadmap_project.py:38`; AST `636c69b498cd09a08565bec21f2c668dd53d39dbb34c113c523db3bdc3f1e326`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: profile, project, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[6].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::from_registry::root.body[10].body[6].body[5].value::Call

Source: `infra/agentinfra/roadmap_project.py:38`; AST `934a468fbde5c00d75f13d546f8ac353264f65312aced72c1cc055c82616b86e`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: profile, project, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::from_registry::root.body[10].body[6].body[6]::Assign

Source: `infra/agentinfra/roadmap_project.py:41`; AST `9256f52473e77c68e3ba45a316f7a26c40feaaebd27597f6d6a832366759edb1`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, profile, project, root. Outputs/bindings: repository.
Calls/effect boundaries: Path.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[6].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::from_registry::root.body[10].body[6].body[6].value.orelse::Call

Source: `infra/agentinfra/roadmap_project.py:41`; AST `5ba539d7090a511f6cbdb65bb42a5130aaa3c8032df20301498f801af84c0a67`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, profile. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[6].value.orelse; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::from_registry::root.body[10].body[6].body[7]::Return

Source: `infra/agentinfra/roadmap_project.py:42`; AST `4da8a12e58e62d99dd724c46baa92c31b2e5e41c2b49dc612099cdad4dabf1d1`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cls, profile, project, repository. Outputs/bindings: (none).
Calls/effect boundaries: cls.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[10].body[6].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::from_registry::root.body[10].body[6].body[7].value::Call

Source: `infra/agentinfra/roadmap_project.py:42`; AST `c410caaac8bb048f7e8d41905ff803065005874bda4a588789cd9d02761c128a`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cls, profile, project, repository. Outputs/bindings: (none).
Calls/effect boundaries: cls.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::path::root.body[10].body[7]::FunctionDef

Source: `infra/agentinfra/roadmap_project.py:45`; AST `0a0fe44c593624bc76248470746d55bf2cfb0468a1cf350ee063e1bfc119382d`.

Rust module: `infra::agentinfra::roadmap_project`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, confined_path, self. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::path::root.body[10].body[7].body[0]::Return

Source: `infra/agentinfra/roadmap_project.py:46`; AST `f425479f17c0999578f69d5ae6d30a6fc752a75e9f42b3b7b7a23c2e415828be`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, self. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[10].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::path::root.body[10].body[7].body[0].value::Call

Source: `infra/agentinfra/roadmap_project.py:46`; AST `cbb6171a280332be2728518030b3e1a5b9a66a2c792e799256b968a670f70914`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, self. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[10].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectProfileV1::root.body[10].decorator_list[0]::Call

Source: `infra/agentinfra/roadmap_project.py:22`; AST `fc70015bf40dfb1bdf9c74c7ec3567232b79ad9aa1cd1edc6c02254994330803`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dataclass. Outputs/bindings: (none).
Calls/effect boundaries: dataclass.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[10].decorator_list[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::root.body[11]::ClassDef

Source: `infra/agentinfra/roadmap_project.py:49`; AST `7a029bee1d2bb0de706e4402f7e52793523a9b1360bc25a86ede4e975b672633`.

Rust module: `infra::agentinfra::roadmap_project`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: AEGIS_RECORD_WRITER, FileTransaction, INTERFACE_VERSION, Mutation, Path, ProjectProfileV1, WorkspaceLease, allow_create, artifacts, before, binding, bool, canonical, changed, current, dict, digest, execution, expected_digest, fields, int, isinstance, key, len, loads, new_execution, observed, old_history, owner, path, previous, profile, profiles, project, read_json, record, require, root, self, staticmethod, str, tuple, type, updated, value. Outputs/bindings: before, binding, changed, current, execution, key, new_execution, observed, old_history, owner, path, previous, profile, updated, value.
Calls/effect boundaries: FileTransaction, FileTransaction(self.root, [*artifacts, Mutation(path, canonical(updated) + b'\n', expected_exists=before is not None, expected_sha256=expected_digest)], state_dir=self.root / '.aegis/state/transactions', name=AEGIS_RECORD_WRITER).commit, Mutation, ProjectProfileV1.from_registry, WorkspaceLease, WorkspaceLease(self.root).assert_owner, before.decode, binding.get, binding.get('observation', {}).get, bool, canonical, changed.get, changed.get('observation', {}).get, current.get, dict, digest, execution.get, fields.get, isinstance, len, loads, new_execution.get, owner.get, path.exists, path.read_bytes, read_json, record.get, require, root.resolve, self._validate_aegis, self.profile.path, str, type, updated.get, updated.get('execution', {}).get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered ClassDef evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::__init__::root.body[11].body[0]::FunctionDef

Source: `infra/agentinfra/roadmap_project.py:50`; AST `49ddb9a9695c876979ffeadb1bd76ca302ac02ed6c1e04c9176bc97b3eb4ee97`.

Rust module: `infra::agentinfra::roadmap_project`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, ProjectProfileV1, dict, profiles, project, root, self, str. Outputs/bindings: (none).
Calls/effect boundaries: ProjectProfileV1.from_registry, root.resolve.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::__init__::root.body[11].body[0].body[0]::Assign

Source: `infra/agentinfra/roadmap_project.py:51`; AST `eac70191d36cd330a975a12be514d4a5f58088087cc2acfa2746cafe468cc8ae`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root, self. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::__init__::root.body[11].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_project.py:51`; AST `b97f3f463d4724206af2869ad4674d5eb373167f052507971a722ecc8f771a87`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::__init__::root.body[11].body[0].body[1]::Assign

Source: `infra/agentinfra/roadmap_project.py:52`; AST `52823bc4496d4c48cdd8711c2a09d26a5df370b7ad17fc84256d05ef9ee9ab6d`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ProjectProfileV1, profiles, project, self. Outputs/bindings: (none).
Calls/effect boundaries: ProjectProfileV1.from_registry.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::__init__::root.body[11].body[0].body[1].value::Call

Source: `infra/agentinfra/roadmap_project.py:52`; AST `d881c7ec4a0f0d4c25999739e55f0ac23ba55fe627b05709fd2c23592d4d5010`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ProjectProfileV1, profiles, project, self. Outputs/bindings: (none).
Calls/effect boundaries: ProjectProfileV1.from_registry.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::read::root.body[11].body[1]::FunctionDef

Source: `infra/agentinfra/roadmap_project.py:54`; AST `b0311bf2d58de3caf42eb96615ae03baa036b6a23552c7379409763d2ecc86e1`.

Rust module: `infra::agentinfra::roadmap_project`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: dict, isinstance, read_json, require, self, value. Outputs/bindings: value.
Calls/effect boundaries: isinstance, read_json, require, self._validate_aegis, self.profile.path.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::read::root.body[11].body[1].body[0]::Assign

Source: `infra/agentinfra/roadmap_project.py:55`; AST `b90b26c8b4bc992269598dcf7b5eb867ec1cce28c8e747226cde3a913e499130`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: read_json, self. Outputs/bindings: value.
Calls/effect boundaries: read_json, self.profile.path.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::read::root.body[11].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_project.py:55`; AST `258856238abae70e774a798573cc489832b628753746d99426d048fd4174ed08`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: read_json, self. Outputs/bindings: (none).
Calls/effect boundaries: read_json, self.profile.path.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::read::root.body[11].body[1].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_project.py:55`; AST `5aff035e159349b40c99cc1e24ee69d81660511f1625d432552cda0b0afab929`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.profile.path.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[1].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::read::root.body[11].body[1].body[1]::Expr

Source: `infra/agentinfra/roadmap_project.py:56`; AST `f924433f2113ea8716bd5f29442c084e4c75c5132563e5b0c29a76f6b9119265`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, isinstance, require, value. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, require.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::read::root.body[11].body[1].body[1].value::Call

Source: `infra/agentinfra/roadmap_project.py:56`; AST `a0e3a25fcc22c702dfe515bed966ec7469f66791090ea26725283f2fed2742f6`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, isinstance, require, value. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, require.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::read::root.body[11].body[1].body[1].value.args[0]::Call

Source: `infra/agentinfra/roadmap_project.py:56`; AST `a0df6caeebecae97cf305403969f3b48f16842ceba977c5f53441f25fd65637d`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, isinstance, value. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[1].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::read::root.body[11].body[1].body[2]::If

Source: `infra/agentinfra/roadmap_project.py:57`; AST `2c038c4a222f1315040aedd628f9fcea5904264798b481914d7d3305f6945704`.

Rust module: `infra::agentinfra::roadmap_project`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: self, value. Outputs/bindings: (none).
Calls/effect boundaries: self._validate_aegis.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[11].body[1].body[2]; no call, error or mutation may be omitted. Condition: self.profile.project == 'Aegis'
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::read::root.body[11].body[1].body[2].body[0]::Expr

Source: `infra/agentinfra/roadmap_project.py:58`; AST `fe5a81842ed8cfbb7f4db589dda4e430cc69dda8a9d29f31bbc62c138bdaa1fe`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, value. Outputs/bindings: (none).
Calls/effect boundaries: self._validate_aegis.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[1].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::read::root.body[11].body[1].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_project.py:58`; AST `598cef4ebbcac07b1926e9cb671452da88e3e60b4d2b44435d5f78da3133ec9a`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, value. Outputs/bindings: (none).
Calls/effect boundaries: self._validate_aegis.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[1].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::read::root.body[11].body[1].body[3]::Return

Source: `infra/agentinfra/roadmap_project.py:59`; AST `88b203970aef225f077e527420a8aa37d7bea48c022a704b48a144448b80ec78`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: value. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[11].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::_validate_aegis::root.body[11].body[2]::FunctionDef

Source: `infra/agentinfra/roadmap_project.py:62`; AST `8bc20e98ac10a79d23e7e2324c018c5287ce47e280b5ac19a2c2f2e923f07e38`.

Rust module: `infra::agentinfra::roadmap_project`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: AEGIS_RECORD_WRITER, dict, int, record, require, staticmethod, type. Outputs/bindings: (none).
Calls/effect boundaries: record.get, require, type.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::_validate_aegis::root.body[11].body[2].body[0]::Expr

Source: `infra/agentinfra/roadmap_project.py:63`; AST `f691d6ac120bb2fa6be819bda7c0478104a1b0e2435722979460d37f274912df`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: int, record, require, type. Outputs/bindings: (none).
Calls/effect boundaries: record.get, require, type.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::_validate_aegis::root.body[11].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_project.py:63`; AST `be85d796c56e917d5f13314d075084b3df6c0bf3f2de02ac013bed86bc30bda4`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: int, record, require, type. Outputs/bindings: (none).
Calls/effect boundaries: record.get, require, type.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::_validate_aegis::root.body[11].body[2].body[0].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_project.py:63`; AST `039ee65eccc54cc8b054f5abf5ca3f80662d7756c1255a108b80cd8ce73d52ac`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record, type. Outputs/bindings: (none).
Calls/effect boundaries: record.get, type.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[0].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::_validate_aegis::root.body[11].body[2].body[0].value.args[0].values[0].left.args[0]::Call

Source: `infra/agentinfra/roadmap_project.py:63`; AST `d1e3876e5f2eab25e6fd365f06eea6e829f195ef666744ac41314682d8aa382c`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[0].value.args[0].values[0].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::_validate_aegis::root.body[11].body[2].body[0].value.args[0].values[2].left::Call

Source: `infra/agentinfra/roadmap_project.py:64`; AST `d0a98983fb019a589d6e758de84d4e0770904ddc3da7d42d506d12396e7ac5ca`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[0].value.args[0].values[2].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::_validate_aegis::root.body[11].body[2].body[1]::Expr

Source: `infra/agentinfra/roadmap_project.py:65`; AST `677268ba69ed744e363e2b24baacd6e82dd695947cbe9a119ad1c9f80fe6ab88`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: AEGIS_RECORD_WRITER, record, require. Outputs/bindings: (none).
Calls/effect boundaries: record.get, require.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::_validate_aegis::root.body[11].body[2].body[1].value::Call

Source: `infra/agentinfra/roadmap_project.py:65`; AST `d539cd8d5ac9fd077a2fad43a5d057a0f1b1cb4b7ee704dfd517f20100165892`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: AEGIS_RECORD_WRITER, record, require. Outputs/bindings: (none).
Calls/effect boundaries: record.get, require.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::_validate_aegis::root.body[11].body[2].body[1].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_project.py:65`; AST `2ff7c89e5efe914e0bc6c555cf4900c80abd2000c541210a327481acef370769`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: AEGIS_RECORD_WRITER, record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[1].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3]::FunctionDef

Source: `infra/agentinfra/roadmap_project.py:68`; AST `702c6071512e920a1d18339c3841844f65ea20f0e5615548688522d0aa92ae53`.

Rust module: `infra::agentinfra::roadmap_project`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: AEGIS_RECORD_WRITER, FileTransaction, Mutation, WorkspaceLease, allow_create, artifacts, before, binding, bool, canonical, changed, current, dict, digest, execution, expected_digest, fields, int, isinstance, key, len, loads, new_execution, observed, old_history, owner, path, previous, require, self, str, tuple, type, updated. Outputs/bindings: before, binding, changed, current, execution, key, new_execution, observed, old_history, owner, path, previous, updated.
Calls/effect boundaries: FileTransaction, FileTransaction(self.root, [*artifacts, Mutation(path, canonical(updated) + b'\n', expected_exists=before is not None, expected_sha256=expected_digest)], state_dir=self.root / '.aegis/state/transactions', name=AEGIS_RECORD_WRITER).commit, Mutation, WorkspaceLease, WorkspaceLease(self.root).assert_owner, before.decode, binding.get, binding.get('observation', {}).get, bool, canonical, changed.get, changed.get('observation', {}).get, current.get, dict, digest, execution.get, fields.get, isinstance, len, loads, new_execution.get, owner.get, path.exists, path.read_bytes, require, self._validate_aegis, self.profile.path, type, updated.get, updated.get('execution', {}).get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[0]::Expr

Source: `infra/agentinfra/roadmap_project.py:70`; AST `732bc246ac7aba568736b479dfbe5d0dfe027ce70ccd3789e169e7ffae50c20c`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, self. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_project.py:70`; AST `7fdd50e4b59fdf195ad61b18b2621e360becb7be8902b2f27dde0fcbca5f87b3`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, self. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[1]::Expr

Source: `infra/agentinfra/roadmap_project.py:71`; AST `c87a0ee9d93b5e844f997d6bef57e19a18af018f112ec7b4ab370806a8b54cfd`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, fields, isinstance, require. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, require.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[1].value::Call

Source: `infra/agentinfra/roadmap_project.py:71`; AST `f396b06f2fcca1612a36e22a9d950e2fd58dd838624131b771893a016a314c61`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, fields, isinstance, require. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, require.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[1].value.args[0]::Call

Source: `infra/agentinfra/roadmap_project.py:71`; AST `156733c732f0b8d972873efbb33d15ba5f8c4c11c97e23ef37f146a111996973`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, fields, isinstance. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[2]::Assign

Source: `infra/agentinfra/roadmap_project.py:72`; AST `9af500de7189cd969bd2b82769cf7ba54b23254d4f9ab23c19e892b413f8d606`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: path.
Calls/effect boundaries: self.profile.path.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[2].value::Call

Source: `infra/agentinfra/roadmap_project.py:72`; AST `5aff035e159349b40c99cc1e24ee69d81660511f1625d432552cda0b0afab929`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.profile.path.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[3]::Assign

Source: `infra/agentinfra/roadmap_project.py:73`; AST `364d0fe982fb1e9a6aaf875395a3ff50afbc7a163dde40b7c13e3188964c3c13`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: before.
Calls/effect boundaries: path.exists, path.read_bytes.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[3].value.test::Call

Source: `infra/agentinfra/roadmap_project.py:73`; AST `2cac3ec82b344023c57b4bbfcae282698ef12842cbda26a14724eacbefb97016`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.exists.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[3].value.test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[3].value.body::Call

Source: `infra/agentinfra/roadmap_project.py:73`; AST `f35916bc21a833a57a0dd89398b2dab5479cd1f3ef04b46f456d03ce95b67eac`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[3].value.body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[4]::Expr

Source: `infra/agentinfra/roadmap_project.py:74`; AST `8e8e8f1cd57137dd32e614b48177ce00a733e8f42cb438fa823c8222a2723257`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: allow_create, before, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[3].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[4].value::Call

Source: `infra/agentinfra/roadmap_project.py:74`; AST `4c751a4a27485da58a79a9511c9a498ec84e70ec081db51f09a513e3f7aedc6f`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: allow_create, before, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[5]::Expr

Source: `infra/agentinfra/roadmap_project.py:75`; AST `784b530e21d2bd703072f78a3fd3214eae1753a204fae8daaa85ceeacedf7e12`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: before, digest, expected_digest, require. Outputs/bindings: (none).
Calls/effect boundaries: digest, require.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[3].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[5].value::Call

Source: `infra/agentinfra/roadmap_project.py:75`; AST `08e1cd827253645876cade89d6f0735005908c733e5fd1f51fe32b711fe7efc8`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before, digest, expected_digest, require. Outputs/bindings: (none).
Calls/effect boundaries: digest, require.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[5].value.args[0].left.body::Call

Source: `infra/agentinfra/roadmap_project.py:75`; AST `4a63ff00fb497e1d094ddb9e4f8ada535aacd403c14cfceee7fc8dd669fbee57`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before, digest. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[5].value.args[0].left.body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[6]::Assign

Source: `infra/agentinfra/roadmap_project.py:77`; AST `92d200e267e0e5669e452d334e8c4bcb3cdafe97ce3c7988af666cb5363da2f7`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: before, loads. Outputs/bindings: current.
Calls/effect boundaries: before.decode, loads.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[3].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[6].value.body::Call

Source: `infra/agentinfra/roadmap_project.py:77`; AST `1bdeb6848cd90df0a771ae4e779d89aed864d15bc2917c477a4084431f9beebf`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before, loads. Outputs/bindings: (none).
Calls/effect boundaries: before.decode, loads.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[6].value.body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[6].value.body.args[0]::Call

Source: `infra/agentinfra/roadmap_project.py:77`; AST `797b7f1e852c5adfb7f77d47f99dd7b7483943b0928c21cd3aea703a3d98f4fb`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before. Outputs/bindings: (none).
Calls/effect boundaries: before.decode.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[6].value.body.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[7]::Expr

Source: `infra/agentinfra/roadmap_project.py:78`; AST `d937d61cecaaa97fe4d096612eb646c2dcdc9fa83a7a1e8b4b0554ed8bb91a75`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current, self. Outputs/bindings: (none).
Calls/effect boundaries: self._validate_aegis.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[3].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[7].value::Call

Source: `infra/agentinfra/roadmap_project.py:78`; AST `674f06f97ebcaff4393536f7238443226e5d497dcea2a58d778989305516e814`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current, self. Outputs/bindings: (none).
Calls/effect boundaries: self._validate_aegis.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[8]::Expr

Source: `infra/agentinfra/roadmap_project.py:79`; AST `7a0e40f3067d2d1a4acc38668330a798f24865a950bf94d9f1041c6e04560bbc`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: AEGIS_RECORD_WRITER, fields, require. Outputs/bindings: (none).
Calls/effect boundaries: fields.get, require.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[3].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[8].value::Call

Source: `infra/agentinfra/roadmap_project.py:79`; AST `00955ee5974acbdbd5d7624e35f7c928df06abd3bf93aa3678684a0a3d9e935b`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: AEGIS_RECORD_WRITER, fields, require. Outputs/bindings: (none).
Calls/effect boundaries: fields.get, require.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[8].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_project.py:79`; AST `5fa495e4531ca71e17c6cfaedd2d3da193f405ad65464fce6520ebdc0b862af1`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: AEGIS_RECORD_WRITER, fields. Outputs/bindings: (none).
Calls/effect boundaries: fields.get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[8].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[9]::Assign

Source: `infra/agentinfra/roadmap_project.py:81`; AST `a63289e01324fa74fda3a1f1be3042959b6a5cb28afc02adf5a125e4dc9ca770`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current, dict, fields. Outputs/bindings: updated.
Calls/effect boundaries: dict.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[3].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[9].value::Call

Source: `infra/agentinfra/roadmap_project.py:81`; AST `97bace9cd1ada76e2c72281e79924de49013d53a229a45e0f2d133959fe7facc`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current, dict, fields. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[10]::Assign

Source: `infra/agentinfra/roadmap_project.py:82`; AST `a9ba7d516fc29c81e83606864315598f0b87f3348eeda595809ab0006287fe5c`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: AEGIS_RECORD_WRITER, updated. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[3].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[11]::Expr

Source: `infra/agentinfra/roadmap_project.py:83`; AST `9b0f872487e43303dac8e71f3974dc2e55798685b48b595ba9c9b7b7094a156b`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, updated. Outputs/bindings: (none).
Calls/effect boundaries: self._validate_aegis.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[3].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[11].value::Call

Source: `infra/agentinfra/roadmap_project.py:83`; AST `a2c97ffbbb446036f5794be21a64969710c087bdbad7a9415cde4988529638c4`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, updated. Outputs/bindings: (none).
Calls/effect boundaries: self._validate_aegis.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[12]::Assign

Source: `infra/agentinfra/roadmap_project.py:84`; AST `a78f1dd400cf058093eda7b5c30a8b05ebea7a9aad84da840c3d46ce5cb0dacc`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current, updated. Outputs/bindings: execution.
Calls/effect boundaries: current.get, updated.get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[3].body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[12].value.values[0]::Call

Source: `infra/agentinfra/roadmap_project.py:84`; AST `a328de23047ce40417fc57ba191190571e062464ebe01ba998e2891fc9809be1`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current. Outputs/bindings: (none).
Calls/effect boundaries: current.get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[12].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[12].value.values[1]::Call

Source: `infra/agentinfra/roadmap_project.py:84`; AST `15b079f2654fa7e884ed6710665b447d7ace034007062211786cedceab0ea605`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: updated. Outputs/bindings: (none).
Calls/effect boundaries: updated.get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[12].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13]::If

Source: `infra/agentinfra/roadmap_project.py:85`; AST `c0c57e7e2071614a4486edfd26474c0faa8a3e147223f6626b67aeb11d87917d`.

Rust module: `infra::agentinfra::roadmap_project`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: WorkspaceLease, binding, bool, changed, execution, int, key, len, new_execution, observed, old_history, owner, previous, require, self, type, updated. Outputs/bindings: binding, changed, key, new_execution, observed, old_history, owner, previous.
Calls/effect boundaries: WorkspaceLease, WorkspaceLease(self.root).assert_owner, binding.get, binding.get('observation', {}).get, bool, changed.get, changed.get('observation', {}).get, execution.get, len, new_execution.get, owner.get, require, type, updated.get, updated.get('execution', {}).get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[11].body[3].body[13]; no call, error or mutation may be omitted. Condition: execution
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[0]::Assign

Source: `infra/agentinfra/roadmap_project.py:86`; AST `3143d476a50e13911b81b08cc9f4475a21e61266a736348376774270436548e6`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: execution. Outputs/bindings: owner.
Calls/effect boundaries: execution.get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[3].body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[0].value::Call

Source: `infra/agentinfra/roadmap_project.py:86`; AST `94ea54adee6fc3e52b8da6da4b7ad4c1f66ad0fe66dcebf5eb64a5f9b2021753`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: execution. Outputs/bindings: (none).
Calls/effect boundaries: execution.get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[13].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[1]::Assign

Source: `infra/agentinfra/roadmap_project.py:87`; AST `8d966d61e8f4fe7fb915b27fb56de3eb1cea5416f6e3c84de1a6bca872634ea8`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: execution. Outputs/bindings: binding.
Calls/effect boundaries: execution.get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[3].body[13].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[1].value::Call

Source: `infra/agentinfra/roadmap_project.py:87`; AST `9d07ed4a2c148f4183b707ac830e883b5c33ba96dcd1e134c547f727d92f1312`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: execution. Outputs/bindings: (none).
Calls/effect boundaries: execution.get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[13].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[2]::Expr

Source: `infra/agentinfra/roadmap_project.py:88`; AST `efaa1634b4c186b43946e4a46df8d821197fdb48e82d21f9a435f223a8ee0bf2`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, bool, owner, require. Outputs/bindings: (none).
Calls/effect boundaries: binding.get, bool, owner.get, require.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[3].body[13].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[2].value::Call

Source: `infra/agentinfra/roadmap_project.py:88`; AST `95fd4cbbf935e8aea350a84e37be292a87c6882d033976881b02a30da7dc715e`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, bool, owner, require. Outputs/bindings: (none).
Calls/effect boundaries: binding.get, bool, owner.get, require.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[13].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[2].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_project.py:88`; AST `27a5b1552929f691a509884265ca66d93c6c63ccce4de6833fab9a141246c47e`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: owner. Outputs/bindings: (none).
Calls/effect boundaries: owner.get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[13].body[2].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[2].value.args[0].values[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_project.py:88`; AST `63111ba26343241a333d0933cf221435534ec16270d2f49ca57741efb6c4fa1a`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding. Outputs/bindings: (none).
Calls/effect boundaries: binding.get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[13].body[2].value.args[0].values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[2].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_project.py:88`; AST `6b44386f9fcb7cd39dade6d2cfe0643c1f2a4cd60d8a108ee30fb4c545470682`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, owner. Outputs/bindings: (none).
Calls/effect boundaries: bool, owner.get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[13].body[2].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[2].value.args[0].values[1].args[0]::Call

Source: `infra/agentinfra/roadmap_project.py:88`; AST `27a5b1552929f691a509884265ca66d93c6c63ccce4de6833fab9a141246c47e`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: owner. Outputs/bindings: (none).
Calls/effect boundaries: owner.get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[13].body[2].value.args[0].values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[3]::Expr

Source: `infra/agentinfra/roadmap_project.py:90`; AST `31609293520c6c913c3148edaec1c1b224d2c5c5d115b243a07abdb36865da75`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: WorkspaceLease, owner, self. Outputs/bindings: (none).
Calls/effect boundaries: WorkspaceLease, WorkspaceLease(self.root).assert_owner.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[3].body[13].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[3].value::Call

Source: `infra/agentinfra/roadmap_project.py:90`; AST `4e57d43a3eafcdc4f4fff3cb17d80d5c81b7b2b14096dcd659ce2aa052c23521`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: WorkspaceLease, owner, self. Outputs/bindings: (none).
Calls/effect boundaries: WorkspaceLease, WorkspaceLease(self.root).assert_owner.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[13].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[3].value.func.value::Call

Source: `infra/agentinfra/roadmap_project.py:90`; AST `408829ac552086ff1aa49ed525f89889a9374a77ff0f5e75e1759a09776c7b06`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: WorkspaceLease, self. Outputs/bindings: (none).
Calls/effect boundaries: WorkspaceLease.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[13].body[3].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[4]::Assign

Source: `infra/agentinfra/roadmap_project.py:91`; AST `d2aaff65dcf7f77bd4314e829dd76f6969c288152ba8988a092dafc47b7618e4`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: updated. Outputs/bindings: changed.
Calls/effect boundaries: updated.get, updated.get('execution', {}).get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[3].body[13].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[4].value::Call

Source: `infra/agentinfra/roadmap_project.py:91`; AST `22dbd39e10f5e80d8d2c3c48ff7ff7095bdbfd772051f29c0c0e741b6fd06397`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: updated. Outputs/bindings: (none).
Calls/effect boundaries: updated.get, updated.get('execution', {}).get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[13].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[4].value.func.value::Call

Source: `infra/agentinfra/roadmap_project.py:91`; AST `a92afd6585cea4ad55608df885b6e22ae9e7f76d42cc34bfdae58d7d2b0aa07d`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: updated. Outputs/bindings: (none).
Calls/effect boundaries: updated.get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[13].body[4].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[5]::Expr

Source: `infra/agentinfra/roadmap_project.py:92`; AST `90f55cf2ea2f5ce2c77965a680c22cdbc192168e6c3ed4ce63d9df0060d5d3e2`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: owner, require, updated. Outputs/bindings: (none).
Calls/effect boundaries: require, updated.get, updated.get('execution', {}).get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[3].body[13].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[5].value::Call

Source: `infra/agentinfra/roadmap_project.py:92`; AST `4ec4de0d405c14b43ebf68525559fd1e03f3400d6b358a4636626ac04389c25a`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: owner, require, updated. Outputs/bindings: (none).
Calls/effect boundaries: require, updated.get, updated.get('execution', {}).get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[13].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[5].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_project.py:92`; AST `1af38ae42bbb3bb40e8dab2bbe705d86f7a1ac4533dce520f39179e1d1300e96`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: updated. Outputs/bindings: (none).
Calls/effect boundaries: updated.get, updated.get('execution', {}).get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[13].body[5].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[5].value.args[0].left.func.value::Call

Source: `infra/agentinfra/roadmap_project.py:92`; AST `a92afd6585cea4ad55608df885b6e22ae9e7f76d42cc34bfdae58d7d2b0aa07d`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: updated. Outputs/bindings: (none).
Calls/effect boundaries: updated.get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[13].body[5].value.args[0].left.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[6]::Expr

Source: `infra/agentinfra/roadmap_project.py:94`; AST `d38a5e7add4d658fdf8c2a071dd99db13bf819c44be57501982a432c78a0b3c3`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, changed, require. Outputs/bindings: (none).
Calls/effect boundaries: binding.get, changed.get, require.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[3].body[13].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[6].value::Call

Source: `infra/agentinfra/roadmap_project.py:94`; AST `b5b51946d87cc225146b12392d268d429b19ec33a2e19ee82f55366a4bb45b19`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, changed, require. Outputs/bindings: (none).
Calls/effect boundaries: binding.get, changed.get, require.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[13].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[6].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_project.py:94`; AST `8015083335b7c0a8dfb44ecb0fc9b34368e73a39209df4c89c1f9ca0174fc90b`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: changed. Outputs/bindings: (none).
Calls/effect boundaries: changed.get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[13].body[6].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[6].value.args[0].values[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_project.py:94`; AST `63111ba26343241a333d0933cf221435534ec16270d2f49ca57741efb6c4fa1a`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding. Outputs/bindings: (none).
Calls/effect boundaries: binding.get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[13].body[6].value.args[0].values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[6].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_project.py:95`; AST `b407a3fa7107027af01af23bad58237da099cadc6e2afe1f37e68a5dba913ce4`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: changed. Outputs/bindings: (none).
Calls/effect boundaries: changed.get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[13].body[6].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[6].value.args[0].values[1].comparators[0]::Call

Source: `infra/agentinfra/roadmap_project.py:95`; AST `c52ca19c779f5d2a2be4d6e23e8b381a8637c14e49af2b3c39e5bc3ee9359726`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding. Outputs/bindings: (none).
Calls/effect boundaries: binding.get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[13].body[6].value.args[0].values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[7]::Assign

Source: `infra/agentinfra/roadmap_project.py:97`; AST `69d781ba8b3560a9917e281a81fcf20f7b4ed291d38e2876c21d7acc8de78e84`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: updated. Outputs/bindings: new_execution.
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[3].body[13].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[8]::Expr

Source: `infra/agentinfra/roadmap_project.py:98`; AST `4dd963f284c3ae8b5d318104b0e78adffec61ae9b7a95b43f784845481242874`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: execution, new_execution, require. Outputs/bindings: (none).
Calls/effect boundaries: execution.get, new_execution.get, require.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[3].body[13].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[8].value::Call

Source: `infra/agentinfra/roadmap_project.py:98`; AST `44ad6746215ed2268abcb171c21bff08ef407df2f98b60b39ae24487d7a4bf3f`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: execution, new_execution, require. Outputs/bindings: (none).
Calls/effect boundaries: execution.get, new_execution.get, require.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[13].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[8].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_project.py:98`; AST `ab056c463abc38f3d5abfcd42d1bc4ec87c3ad8c336fe0f4c2ccf85c67ab387b`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: new_execution. Outputs/bindings: (none).
Calls/effect boundaries: new_execution.get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[13].body[8].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[8].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_project.py:98`; AST `fef641b3bb3cde38d9f02b8401e3595791991f68c22f5384fd74bed14ca6ea85`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: execution. Outputs/bindings: (none).
Calls/effect boundaries: execution.get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[13].body[8].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[9]::Assign

Source: `infra/agentinfra/roadmap_project.py:100`; AST `daccd3d86e1fff75a37e087248b251214965e8b97213654bcf7a207af7ccacad`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: execution. Outputs/bindings: old_history.
Calls/effect boundaries: execution.get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[3].body[13].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[9].value::Call

Source: `infra/agentinfra/roadmap_project.py:100`; AST `4c152ba0ddcae5f021c961df5ea040b3875ac8b8553149025b4b23f7569366b6`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: execution. Outputs/bindings: (none).
Calls/effect boundaries: execution.get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[13].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[10]::Expr

Source: `infra/agentinfra/roadmap_project.py:101`; AST `221e252e12ea3c46fb0244e87f7f1e980779c020a0a772e215e16c01374a7bba`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, new_execution, old_history, require. Outputs/bindings: (none).
Calls/effect boundaries: len, new_execution.get, require.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[3].body[13].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[10].value::Call

Source: `infra/agentinfra/roadmap_project.py:101`; AST `5168c10dc58aa2c714a99445155dedef82923a141ee93a4cc8ba89fcb7d2ac77`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, new_execution, old_history, require. Outputs/bindings: (none).
Calls/effect boundaries: len, new_execution.get, require.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[13].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[10].value.args[0].left.value::Call

Source: `infra/agentinfra/roadmap_project.py:101`; AST `7f32f6cd44f36f9662bda84ed0fc9ac4bda4eca0290a7aeddb2804c2d7852048`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: new_execution. Outputs/bindings: (none).
Calls/effect boundaries: new_execution.get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[13].body[10].value.args[0].left.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[10].value.args[0].left.slice.upper::Call

Source: `infra/agentinfra/roadmap_project.py:101`; AST `e662c4fe54487e2a2a8c60f1389496f7f0338b41fc2a93d177cdcd0fe3a53a80`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, old_history. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[13].body[10].value.args[0].left.slice.upper; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[11]::For

Source: `infra/agentinfra/roadmap_project.py:103`; AST `b5ad228be79ca1d9b8a7057ebff0682e69ce6cd672abecdc87b60ac9b9e49723`.

Rust module: `infra::agentinfra::roadmap_project`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: binding, changed, int, key, observed, previous, require, type. Outputs/bindings: key, observed, previous.
Calls/effect boundaries: binding.get, binding.get('observation', {}).get, changed.get, changed.get('observation', {}).get, require, type.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered For evaluation at root.body[11].body[3].body[13].body[11]; no call, error or mutation may be omitted. Iteration: key in ('tokensUsed', 'timeUsedSeconds')
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[11].body[0]::Assign

Source: `infra/agentinfra/roadmap_project.py:104`; AST `77cc354770f5d38cb46dbb3f206ca2298a0fb7c798b49c7edcf6d8c0ad558da1`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, key. Outputs/bindings: previous.
Calls/effect boundaries: binding.get, binding.get('observation', {}).get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[3].body[13].body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[11].body[0].value::Call

Source: `infra/agentinfra/roadmap_project.py:104`; AST `d5581843908ca08a75b91699c99f723b96225af764d729c7fd80f88896939b01`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, key. Outputs/bindings: (none).
Calls/effect boundaries: binding.get, binding.get('observation', {}).get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[13].body[11].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[11].body[0].value.func.value::Call

Source: `infra/agentinfra/roadmap_project.py:104`; AST `19383d3c3a3dd141414e57358091030cb5d155331564962bc5d64e9d2fdca72d`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding. Outputs/bindings: (none).
Calls/effect boundaries: binding.get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[13].body[11].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[11].body[1]::Assign

Source: `infra/agentinfra/roadmap_project.py:105`; AST `3395784731d1794ab068b2f5f0a66c7496105267228be91fa3dc6f4a846333a1`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: changed, key. Outputs/bindings: observed.
Calls/effect boundaries: changed.get, changed.get('observation', {}).get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[3].body[13].body[11].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[11].body[1].value::Call

Source: `infra/agentinfra/roadmap_project.py:105`; AST `112583c74426f59a41bedaed87455743aad5f147ba9cabed0ccf8b01e35fb75b`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: changed, key. Outputs/bindings: (none).
Calls/effect boundaries: changed.get, changed.get('observation', {}).get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[13].body[11].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[11].body[1].value.func.value::Call

Source: `infra/agentinfra/roadmap_project.py:105`; AST `b0368d00393b990a107f1fc23945f7de6abb271bdf23ec31e8e6c117a30b7051`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: changed. Outputs/bindings: (none).
Calls/effect boundaries: changed.get.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[13].body[11].body[1].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[11].body[2]::If

Source: `infra/agentinfra/roadmap_project.py:106`; AST `d84239d8ade54dc10692c530bbf2d6878bc91512731cdd64895b204abe3633c1`.

Rust module: `infra::agentinfra::roadmap_project`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: int, observed, previous, require, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered If evaluation at root.body[11].body[3].body[13].body[11].body[2]; no call, error or mutation may be omitted. Condition: previous is not None
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[11].body[2].body[0]::Expr

Source: `infra/agentinfra/roadmap_project.py:107`; AST `374c412066c2df20710e7348ed726e98bbdd3bec8ff632ee3a53d546a36a48fd`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: int, observed, previous, require, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[3].body[13].body[11].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[11].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_project.py:107`; AST `402a0da9f67962fd524531c4e5d0c14f44c63497cc269d3d288006a001ae20f1`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: int, observed, previous, require, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[13].body[11].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[11].body[2].body[0].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_project.py:107`; AST `1fff1a2c7cc92cd31dc58aa88c53c30060970d14138cfb5ee77a48e7ee69f76e`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: previous, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[13].body[11].body[2].body[0].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[13].body[11].body[2].body[0].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_project.py:107`; AST `820be8eafd64cfce9736efac92793aaf9db6bbebc0da3e85e542506e62f3774e`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observed, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[13].body[11].body[2].body[0].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[14]::Return

Source: `infra/agentinfra/roadmap_project.py:111`; AST `2955caf63494833ee537ba6fa2caf6e855fff2ac2834da5ffd178c20c5befee0`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: AEGIS_RECORD_WRITER, FileTransaction, Mutation, artifacts, before, canonical, expected_digest, path, self, updated. Outputs/bindings: (none).
Calls/effect boundaries: FileTransaction, FileTransaction(self.root, [*artifacts, Mutation(path, canonical(updated) + b'\n', expected_exists=before is not None, expected_sha256=expected_digest)], state_dir=self.root / '.aegis/state/transactions', name=AEGIS_RECORD_WRITER).commit, Mutation, canonical.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[11].body[3].body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[14].value::Call

Source: `infra/agentinfra/roadmap_project.py:111`; AST `34175f242daf9451bb9c615e044039431fac6bb4bacecf1abb55977c688b43ec`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: AEGIS_RECORD_WRITER, FileTransaction, Mutation, artifacts, before, canonical, expected_digest, path, self, updated. Outputs/bindings: (none).
Calls/effect boundaries: FileTransaction, FileTransaction(self.root, [*artifacts, Mutation(path, canonical(updated) + b'\n', expected_exists=before is not None, expected_sha256=expected_digest)], state_dir=self.root / '.aegis/state/transactions', name=AEGIS_RECORD_WRITER).commit, Mutation, canonical.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[14].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[14].value.func.value::Call

Source: `infra/agentinfra/roadmap_project.py:111`; AST `e3c1fe5123623167d7c169d1e04c9004d71644fb600c84295e06e20bccaacbf4`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: AEGIS_RECORD_WRITER, FileTransaction, Mutation, artifacts, before, canonical, expected_digest, path, self, updated. Outputs/bindings: (none).
Calls/effect boundaries: FileTransaction, Mutation, canonical.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[14].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[14].value.func.value.args[1].elts[1]::Call

Source: `infra/agentinfra/roadmap_project.py:112`; AST `bda8b0651cd11fdeff70c7951f52f6b3b0a42ec06714fefcd3fb87fc9cd6c94c`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Mutation, before, canonical, expected_digest, path, updated. Outputs/bindings: (none).
Calls/effect boundaries: Mutation, canonical.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[14].value.func.value.args[1].elts[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::update::root.body[11].body[3].body[14].value.func.value.args[1].elts[1].args[1].left::Call

Source: `infra/agentinfra/roadmap_project.py:112`; AST `55c97ce00fe8675ff74e1eed48ded4cd22b3be31d967e0ab26715026d67f484e`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, updated. Outputs/bindings: (none).
Calls/effect boundaries: canonical.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[14].value.func.value.args[1].elts[1].args[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::describe::root.body[11].body[4]::FunctionDef

Source: `infra/agentinfra/roadmap_project.py:118`; AST `be50439862fddc2b431f2eaadd393ee578978e823f09de57649aaa7706cb4e72`.

Rust module: `infra::agentinfra::roadmap_project`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: AEGIS_RECORD_WRITER, INTERFACE_VERSION, dict, profile, self, str. Outputs/bindings: profile.
Calls/effect boundaries: str.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::describe::root.body[11].body[4].body[0]::Assign

Source: `infra/agentinfra/roadmap_project.py:119`; AST `a28fbcf33fb701199f74297ed1430e7ecb69a22057939b4c84da0598d8c0f9ca`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: profile.
Calls/effect boundaries: (none).
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::describe::root.body[11].body[4].body[1]::Return

Source: `infra/agentinfra/roadmap_project.py:120`; AST `93f5f27ac3ab6816223140b0e310cfcdf9442cd5ba8564f6990bf5f1bce06642`.

Rust module: `infra::agentinfra::roadmap_project`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: AEGIS_RECORD_WRITER, INTERFACE_VERSION, profile, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Return evaluation at root.body[11].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_project.py::module::ProjectAdapter::describe::root.body[11].body[4].body[1].value.values[3]::Call

Source: `infra/agentinfra/roadmap_project.py:122`; AST `9136c0e0a63751ee7da8cc0e9796564d610214ec380fd8ea3a44104feaf4cb44`.

Rust module: `infra::agentinfra::roadmap_project`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: profile, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, dataclasses, pathlib, roadmap_lease, roadmap_records, security, transaction.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[1].value.values[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
