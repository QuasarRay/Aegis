# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 140. Inventory digest: `0ab30e9aade735167bc8639cf742e7c1f71d6b83aa87223757b0d2bf25cd29bc`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/roadmap_lease.py::module::root::Module

Source: `infra/agentinfra/roadmap_lease.py:1`; AST `ae60a24705d2b0080fd0fba549595d71b068d1629ccd3f40e6f638ffec21f462`.

Rust module: `infra::agentinfra::roadmap_lease`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: FileLock, Path, _pid_alive, _process_identity, active, atomic_write_json, binding, bool, canonical, coordination_root, dict, execution, identity, inspect_process, int, lock, native_observation, observation, observe_managed_owner, observe_native_owner, observed, operation, os, owner, pid, read_json, recovery, require, self, session, socket, state, str, type, uuid. Outputs/bindings: active, binding, canonical, execution, identity, lock, observation, observed, pid, state.
Calls/effect boundaries: FileLock, _pid_alive, _process_identity, atomic_write_json, binding.get, bool, canonical.exists, coordination_root.resolve, execution.get, inspect_process, lock.acquire, lock.release, native_observation.get, observe_managed_owner, observe_native_owner, os.getpid, owner.get, read_json, read_json(canonical).get, read_json(canonical).get('execution', {}).get, require, self.assert_owner, self.path.exists, self.path.with_suffix, self.qualify, self.read, self.release, socket.gethostname, state.get, state['history'].append, type, uuid.uuid4.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::root.body[0]::Expr

Source: `infra/agentinfra/roadmap_lease.py:1`; AST `27caae24d589581bc32bb212926d809a1c0b5ff397f7d8d9154159b0a3376190`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::root.body[1]::ImportFrom

Source: `infra/agentinfra/roadmap_lease.py:6`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::root.body[2]::Import

Source: `infra/agentinfra/roadmap_lease.py:8`; AST `ac3a74d6dd975a8e8fe4b7f85fce794793a9355595b850e3926964913948d386`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::root.body[3]::Import

Source: `infra/agentinfra/roadmap_lease.py:9`; AST `9df267ed6eef4f61eaaffaebdf9ac9fe93bcf6d1aab9647b1fd045430624c91e`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::root.body[4]::ImportFrom

Source: `infra/agentinfra/roadmap_lease.py:10`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::root.body[5]::Import

Source: `infra/agentinfra/roadmap_lease.py:11`; AST `db14cae1a81ee06a1930fa9f46771b454957916d2bbbc048661adf0613fd70de`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Import evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::root.body[6]::ImportFrom

Source: `infra/agentinfra/roadmap_lease.py:13`; AST `1b8b71be5203ae66cf696ad7ae023750f023f11fd20fe2501f8e1d56817881e3`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::root.body[7]::ImportFrom

Source: `infra/agentinfra/roadmap_lease.py:14`; AST `dff9fc536e5bcdb8ee1fb6299892d85f102ca351c3ec11fb3c046d0ec4763a0d`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::root.body[8]::ImportFrom

Source: `infra/agentinfra/roadmap_lease.py:15`; AST `b5e6279c55de91499fa862ad0ce886eb5356061a463830d8012ed83b82bab8e1`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::root.body[9]::ClassDef

Source: `infra/agentinfra/roadmap_lease.py:18`; AST `46758e98ef8ac8583a8d01b4674c34348b9650ecd25766eca2a8c3bde000bf7b`.

Rust module: `infra::agentinfra::roadmap_lease`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: FileLock, Path, _pid_alive, _process_identity, active, atomic_write_json, binding, bool, canonical, coordination_root, dict, execution, identity, inspect_process, int, lock, native_observation, observation, observe_managed_owner, observe_native_owner, observed, operation, os, owner, pid, read_json, recovery, require, self, session, socket, state, str, type, uuid. Outputs/bindings: active, binding, canonical, execution, identity, lock, observation, observed, pid, state.
Calls/effect boundaries: FileLock, _pid_alive, _process_identity, atomic_write_json, binding.get, bool, canonical.exists, coordination_root.resolve, execution.get, inspect_process, lock.acquire, lock.release, native_observation.get, observe_managed_owner, observe_native_owner, os.getpid, owner.get, read_json, read_json(canonical).get, read_json(canonical).get('execution', {}).get, require, self.assert_owner, self.path.exists, self.path.with_suffix, self.qualify, self.read, self.release, socket.gethostname, state.get, state['history'].append, type, uuid.uuid4.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered ClassDef evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::__init__::root.body[9].body[0]::FunctionDef

Source: `infra/agentinfra/roadmap_lease.py:19`; AST `11557b65d6fca30aeef6b568e0d54976622cbfc4408694b5725fe2748dc2535a`.

Rust module: `infra::agentinfra::roadmap_lease`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, coordination_root, self. Outputs/bindings: (none).
Calls/effect boundaries: coordination_root.resolve, self.path.with_suffix.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::__init__::root.body[9].body[0].body[0]::Assign

Source: `infra/agentinfra/roadmap_lease.py:20`; AST `52a97f8b4f8d9b236bac9f67ff0ca6835f57b483b28b072e148f3fdafd3139e6`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: coordination_root, self. Outputs/bindings: (none).
Calls/effect boundaries: coordination_root.resolve.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::__init__::root.body[9].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_lease.py:20`; AST `9813da44ab93f86c140111b145c491fc97af5160b04f2ef147c34b534cf58d5e`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: coordination_root. Outputs/bindings: (none).
Calls/effect boundaries: coordination_root.resolve.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::__init__::root.body[9].body[0].body[1]::Assign

Source: `infra/agentinfra/roadmap_lease.py:21`; AST `e8143ab35a528b61dd6a780271da0d37b6cfb3ea604f2ed37b2cb8f83effd2cc`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::__init__::root.body[9].body[0].body[2]::Assign

Source: `infra/agentinfra/roadmap_lease.py:22`; AST `82c74d3c1f0d6394870ff61fd939abdd5c18d47c0867328e755e5b35fe6f5e33`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.with_suffix.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::__init__::root.body[9].body[0].body[2].value::Call

Source: `infra/agentinfra/roadmap_lease.py:22`; AST `46aa1e96394d83d78ce0650ffed08f0cb1281604c533bd7f0a9f1922de6c6239`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.with_suffix.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::read::root.body[9].body[1]::FunctionDef

Source: `infra/agentinfra/roadmap_lease.py:24`; AST `f34912c609dce8c51a46790f08dda300c614787a518f613ef35b7be45936e2bf`.

Rust module: `infra::agentinfra::roadmap_lease`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: dict, int, read_json, require, self, state, type. Outputs/bindings: state.
Calls/effect boundaries: read_json, require, self.path.exists, state.get, type.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[9].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::read::root.body[9].body[1].body[0]::If

Source: `infra/agentinfra/roadmap_lease.py:25`; AST `dc6ff8e2805e57398333401fca57721323e1e0d18f7f196b9d0bbadc09adff3c`.

Rust module: `infra::agentinfra::roadmap_lease`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.exists.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered If evaluation at root.body[9].body[1].body[0]; no call, error or mutation may be omitted. Condition: not self.path.exists()
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::read::root.body[9].body[1].body[0].test.operand::Call

Source: `infra/agentinfra/roadmap_lease.py:25`; AST `5a0ab509baad619ec2a1ec684d6882dd1595eead8f620b398322ae10eeaa6916`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.exists.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[1].body[0].test.operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::read::root.body[9].body[1].body[0].body[0]::Return

Source: `infra/agentinfra/roadmap_lease.py:25`; AST `593e48325cc6c6fc22c5f1d882f8894815e7e7fc101168df1fce25fa6d767356`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Return evaluation at root.body[9].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::read::root.body[9].body[1].body[1]::Assign

Source: `infra/agentinfra/roadmap_lease.py:26`; AST `eedb12e86c008c5d4e026adb4cac97c66e0696366a0fbf4bbbe16a62a1515453`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: read_json, self. Outputs/bindings: state.
Calls/effect boundaries: read_json.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::read::root.body[9].body[1].body[1].value::Call

Source: `infra/agentinfra/roadmap_lease.py:26`; AST `e3a79a25f0eadc251da7129b90e21b22224f14b35a0ef4a713b53e9a67e688de`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: read_json, self. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::read::root.body[9].body[1].body[2]::Expr

Source: `infra/agentinfra/roadmap_lease.py:27`; AST `bac5ec10ee8059f36aeb652801a3aaaf9912abd2db49fd463e57506867908bad`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: int, require, state, type. Outputs/bindings: (none).
Calls/effect boundaries: require, state.get, type.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::read::root.body[9].body[1].body[2].value::Call

Source: `infra/agentinfra/roadmap_lease.py:27`; AST `9f4daaac15cb3aa8a9baae349ae7a003dcae8c3a3f919a4d120dee8038fd8b95`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: int, require, state, type. Outputs/bindings: (none).
Calls/effect boundaries: require, state.get, type.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[1].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::read::root.body[9].body[1].body[2].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_lease.py:27`; AST `e3d16e1edd2313a98028a536dbf7d28c6dac3f2a79679ed02ce9a6bf83d0fc26`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: state. Outputs/bindings: (none).
Calls/effect boundaries: state.get.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[1].body[2].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::read::root.body[9].body[1].body[2].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_lease.py:27`; AST `f18fd4e9cd51e2d611892dd9a05df8540ba2d3d539a80159e03f05e9edcdcd0a`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: state, type. Outputs/bindings: (none).
Calls/effect boundaries: state.get, type.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[1].body[2].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::read::root.body[9].body[1].body[2].value.args[0].values[1].left.args[0]::Call

Source: `infra/agentinfra/roadmap_lease.py:27`; AST `2a371209bbd4f9487f432678f0e33caeb12a5a244b87021405e330517755b2fb`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: state. Outputs/bindings: (none).
Calls/effect boundaries: state.get.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[1].body[2].value.args[0].values[1].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::read::root.body[9].body[1].body[3]::Return

Source: `infra/agentinfra/roadmap_lease.py:28`; AST `696bf6abaef9788e7945fb5eca5600a1b47e9a45497438e50ce805c5b045cb6c`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: state. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Return evaluation at root.body[9].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::acquire::root.body[9].body[2]::FunctionDef

Source: `infra/agentinfra/roadmap_lease.py:30`; AST `87e8fc4e478d7a6d2b1625fcd1a8cc22425858d41a93abae7fcd511908d31755`.

Rust module: `infra::agentinfra::roadmap_lease`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileLock, _pid_alive, _process_identity, active, atomic_write_json, bool, dict, identity, int, lock, operation, os, pid, require, self, session, socket, state, str, uuid. Outputs/bindings: active, identity, lock, pid, state.
Calls/effect boundaries: FileLock, _pid_alive, _process_identity, atomic_write_json, bool, lock.acquire, lock.release, os.getpid, require, self.read, socket.gethostname, uuid.uuid4.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[9].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::acquire::root.body[9].body[2].body[0]::Expr

Source: `infra/agentinfra/roadmap_lease.py:31`; AST `51fb979c4bd5552455a860b91f311ed6b0efeefce3d8dd94bef72d9103bfffa5`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, operation, require, session. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::acquire::root.body[9].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_lease.py:31`; AST `4e3f6eb48af620a574b686e7d411627eb58beaa4edac71f3abe88216c6c288f3`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, operation, require, session. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::acquire::root.body[9].body[2].body[0].value.args[0].values[0]::Call

Source: `infra/agentinfra/roadmap_lease.py:31`; AST `366cba69546422f91701ebd6a06279c02516a3293da00592737fd24a9a91fc22`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, session. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[2].body[0].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::acquire::root.body[9].body[2].body[0].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_lease.py:31`; AST `75aae3e6c3e6c60d6fe78a989851ee2e105590cfdd7bbb3ad375351bc56c7b3c`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, operation. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[2].body[0].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::acquire::root.body[9].body[2].body[1]::Assign

Source: `infra/agentinfra/roadmap_lease.py:32`; AST `42a515937020f238f8142246b08b07c13fa2b8ee0c4e1fee865bcd37ddd62da3`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: os, pid. Outputs/bindings: pid.
Calls/effect boundaries: os.getpid.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::acquire::root.body[9].body[2].body[1].value.body::Call

Source: `infra/agentinfra/roadmap_lease.py:32`; AST `ba1923643b161051a18bf7ae7386addd84146f4ab481f99d56712bc1ce97df2c`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os. Outputs/bindings: (none).
Calls/effect boundaries: os.getpid.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[2].body[1].value.body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::acquire::root.body[9].body[2].body[2]::Assign

Source: `infra/agentinfra/roadmap_lease.py:33`; AST `9b6e3c38b25dab892c88b918e533ff128ccfd81c25a920f6c7aece97c0524cd0`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _process_identity, pid. Outputs/bindings: identity.
Calls/effect boundaries: _process_identity.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::acquire::root.body[9].body[2].body[2].value::Call

Source: `infra/agentinfra/roadmap_lease.py:33`; AST `97ab2fa3d8871bfad69f9576517a3740e9cb2b5f09b34899b3b395aa0a4b4478`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _process_identity, pid. Outputs/bindings: (none).
Calls/effect boundaries: _process_identity.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[2].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::acquire::root.body[9].body[2].body[3]::Expr

Source: `infra/agentinfra/roadmap_lease.py:34`; AST `b7cd66e666dbb7456e0d7fd4b37895c09a8dcd22641a62f8eff425afd8812115`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _pid_alive, identity, pid, require. Outputs/bindings: (none).
Calls/effect boundaries: _pid_alive, require.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[2].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::acquire::root.body[9].body[2].body[3].value::Call

Source: `infra/agentinfra/roadmap_lease.py:34`; AST `8876cbcd4366ac7270f08e54c32a9da34a869068bbc44c062301503cf77887b3`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _pid_alive, identity, pid, require. Outputs/bindings: (none).
Calls/effect boundaries: _pid_alive, require.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[2].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::acquire::root.body[9].body[2].body[3].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_lease.py:34`; AST `fa8c9ebf021b18e6716c336d17172d61d67fac049612447c4f03677af0c7ee2b`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _pid_alive, identity, pid. Outputs/bindings: (none).
Calls/effect boundaries: _pid_alive.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[2].body[3].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::acquire::root.body[9].body[2].body[4]::Assign

Source: `infra/agentinfra/roadmap_lease.py:35`; AST `8cc2026334933174881cc4de48f43b30695397374fd15c460e2285be6819ba6b`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileLock, self. Outputs/bindings: lock.
Calls/effect boundaries: FileLock.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[2].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::acquire::root.body[9].body[2].body[4].value::Call

Source: `infra/agentinfra/roadmap_lease.py:35`; AST `692c0cfe19039a2cf0176eca9b324b889857d15d68972c0e196dd16196c20d4e`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileLock, self. Outputs/bindings: (none).
Calls/effect boundaries: FileLock.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[2].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::acquire::root.body[9].body[2].body[5]::Expr

Source: `infra/agentinfra/roadmap_lease.py:35`; AST `2bcfe51cf785ee29160140309ca2724ded506c99a694a1cd40da99965fea32f6`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[2].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::acquire::root.body[9].body[2].body[5].value::Call

Source: `infra/agentinfra/roadmap_lease.py:35`; AST `19f113b1ff996d6a4e1349d4f629dcb1414895f291ae11a26e3a1c7c22771cf0`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[2].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::acquire::root.body[9].body[2].body[6]::Try

Source: `infra/agentinfra/roadmap_lease.py:36`; AST `ad4893a8490d67306f2151c6f282bea50ec3d006c484e39fc2b1cd5b802ba9c9`.

Rust module: `infra::agentinfra::roadmap_lease`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: active, atomic_write_json, identity, lock, operation, pid, require, self, session, socket, state, uuid. Outputs/bindings: active, state.
Calls/effect boundaries: atomic_write_json, lock.release, require, self.read, socket.gethostname, uuid.uuid4.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Try evaluation at root.body[9].body[2].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::acquire::root.body[9].body[2].body[6].body[0]::Assign

Source: `infra/agentinfra/roadmap_lease.py:37`; AST `f6543f323e041f6b48c301a340bcb4c8ed134a07bd8dedc0e02f4257baeabf5d`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: state.
Calls/effect boundaries: self.read.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[2].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::acquire::root.body[9].body[2].body[6].body[0].value::Call

Source: `infra/agentinfra/roadmap_lease.py:37`; AST `1a6cd88d33383d245bb90e4e5f924f99f090d6bd29a5c43fab9e8ffb18d19d91`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.read.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[2].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::acquire::root.body[9].body[2].body[6].body[1]::Expr

Source: `infra/agentinfra/roadmap_lease.py:38`; AST `9827c6afd817cc35f4b496359e7b8e198b9f5f6da60d12b088cd6de866ebb5ec`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, state. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[2].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::acquire::root.body[9].body[2].body[6].body[1].value::Call

Source: `infra/agentinfra/roadmap_lease.py:38`; AST `84da520383b6dbe5b29738a15d41cb5ba011ee522fd5f41175f513a356c227ef`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, state. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[2].body[6].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::acquire::root.body[9].body[2].body[6].body[2]::AugAssign

Source: `infra/agentinfra/roadmap_lease.py:39`; AST `38db64fc0fd261bcd36fd86519d7be1d4372f5e0b73c6a7eb35466b51ac7e90b`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: state. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered AugAssign evaluation at root.body[9].body[2].body[6].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::acquire::root.body[9].body[2].body[6].body[3]::Assign

Source: `infra/agentinfra/roadmap_lease.py:40`; AST `4657d3299d0c3d117ab85b6a541d93b8195c62481dcdb351506260951a5e55c3`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: identity, operation, pid, session, socket, state, uuid. Outputs/bindings: active.
Calls/effect boundaries: socket.gethostname, uuid.uuid4.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[2].body[6].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::acquire::root.body[9].body[2].body[6].body[3].value.values[1].value::Call

Source: `infra/agentinfra/roadmap_lease.py:40`; AST `87eafda000cba758be33f767d487f36fa6a34917ff4cfe4cbd289edd7d07163b`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: uuid. Outputs/bindings: (none).
Calls/effect boundaries: uuid.uuid4.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[2].body[6].body[3].value.values[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::acquire::root.body[9].body[2].body[6].body[3].value.values[6]::Call

Source: `infra/agentinfra/roadmap_lease.py:41`; AST `4263cfe4ff762fbfb73db5540d6d421a621a7fb22318759bc79d367d143d5895`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: socket. Outputs/bindings: (none).
Calls/effect boundaries: socket.gethostname.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[2].body[6].body[3].value.values[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::acquire::root.body[9].body[2].body[6].body[4]::Assign

Source: `infra/agentinfra/roadmap_lease.py:42`; AST `ddd3b3974e0660b1fa160718459591e3872bc955dd05e0c3cf8cf222dd55ba94`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: active, state. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[2].body[6].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::acquire::root.body[9].body[2].body[6].body[5]::Expr

Source: `infra/agentinfra/roadmap_lease.py:43`; AST `47c37f87c4b139eadafb73ff45277e35e0c57b7016e4bb6f83819b74c57bb2de`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_json, self, state. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[2].body[6].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::acquire::root.body[9].body[2].body[6].body[5].value::Call

Source: `infra/agentinfra/roadmap_lease.py:43`; AST `ac7fc12dd27d703341af29ac9171bc58f320270def4f5f2db3279e14dd2f546a`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_json, self, state. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[2].body[6].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::acquire::root.body[9].body[2].body[6].body[6]::Return

Source: `infra/agentinfra/roadmap_lease.py:44`; AST `2582efd8846e95c7607279d34377c5095d107218a4f4b013fbddee69daed317f`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: active. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Return evaluation at root.body[9].body[2].body[6].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::acquire::root.body[9].body[2].body[6].finalbody[0]::Expr

Source: `infra/agentinfra/roadmap_lease.py:45`; AST `9aa6f04fc26ee6b3f6fe1a19158adb3cfde13709dcae4a7cc38bccbb2655afb2`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[2].body[6].finalbody[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::acquire::root.body[9].body[2].body[6].finalbody[0].value::Call

Source: `infra/agentinfra/roadmap_lease.py:45`; AST `107c5710331db61e695f7d71256d48862412d15c223e204da5c71c497352b634`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[2].body[6].finalbody[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::assert_owner::root.body[9].body[3]::FunctionDef

Source: `infra/agentinfra/roadmap_lease.py:47`; AST `ea67ce405392c1af04151d762ea231ebcbb9e75affb4e6a16f74fae5fd945742`.

Rust module: `infra::agentinfra::roadmap_lease`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: _pid_alive, dict, inspect_process, owner, require, self, socket. Outputs/bindings: (none).
Calls/effect boundaries: _pid_alive, inspect_process, owner.get, require, self.read, socket.gethostname.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[9].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::assert_owner::root.body[9].body[3].body[0]::Expr

Source: `infra/agentinfra/roadmap_lease.py:48`; AST `761c5b2a3d0014f615ce6ebafa3075238cef246bd875ec7beb914e9be1277e7f`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: owner, require, self. Outputs/bindings: (none).
Calls/effect boundaries: require, self.read.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::assert_owner::root.body[9].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_lease.py:48`; AST `1a715f638bad93f291c477c2423e00f8f4769a2f6e2319438cc6adc7e00c99f7`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: owner, require, self. Outputs/bindings: (none).
Calls/effect boundaries: require, self.read.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::assert_owner::root.body[9].body[3].body[0].value.args[0].left.value::Call

Source: `infra/agentinfra/roadmap_lease.py:48`; AST `1a6cd88d33383d245bb90e4e5f924f99f090d6bd29a5c43fab9e8ffb18d19d91`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.read.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[3].body[0].value.args[0].left.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::assert_owner::root.body[9].body[3].body[1]::Expr

Source: `infra/agentinfra/roadmap_lease.py:49`; AST `fb3e1b81075a63cb427e2a7ce07c3dddc7dd4ba50d9d7a47188c16c8684f52c6`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _pid_alive, owner, require, socket. Outputs/bindings: (none).
Calls/effect boundaries: _pid_alive, require, socket.gethostname.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::assert_owner::root.body[9].body[3].body[1].value::Call

Source: `infra/agentinfra/roadmap_lease.py:49`; AST `a42950cc34cd7219fb7671d47f6a787d6ffd243a92712b47402c710f8b1b2a92`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _pid_alive, owner, require, socket. Outputs/bindings: (none).
Calls/effect boundaries: _pid_alive, require, socket.gethostname.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::assert_owner::root.body[9].body[3].body[1].value.args[0].values[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_lease.py:49`; AST `4263cfe4ff762fbfb73db5540d6d421a621a7fb22318759bc79d367d143d5895`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: socket. Outputs/bindings: (none).
Calls/effect boundaries: socket.gethostname.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[3].body[1].value.args[0].values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::assert_owner::root.body[9].body[3].body[1].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_lease.py:49`; AST `c102a77d4e9126bd8c1fdd731143cb3a3d9eaaaf3da97c4f68c35b8a3c72a340`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _pid_alive, owner. Outputs/bindings: (none).
Calls/effect boundaries: _pid_alive.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[3].body[1].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::assert_owner::root.body[9].body[3].body[2]::If

Source: `infra/agentinfra/roadmap_lease.py:50`; AST `d220453026674d1cea51113c649e9a696999d5a28bf548a57f0b036736056cc3`.

Rust module: `infra::agentinfra::roadmap_lease`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: inspect_process, owner, require. Outputs/bindings: (none).
Calls/effect boundaries: inspect_process, owner.get, require.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered If evaluation at root.body[9].body[3].body[2]; no call, error or mutation may be omitted. Condition: owner.get('boot_identity') is not None
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::assert_owner::root.body[9].body[3].body[2].test.left::Call

Source: `infra/agentinfra/roadmap_lease.py:50`; AST `e60fd6b0dca89882032965c53af9e7135dbabcd04b82ba8484d7e122c33f7c14`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: owner. Outputs/bindings: (none).
Calls/effect boundaries: owner.get.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[3].body[2].test.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::assert_owner::root.body[9].body[3].body[2].body[0]::ImportFrom

Source: `infra/agentinfra/roadmap_lease.py:51`; AST `2cd7a01c24d6857bd3c23e3cf1018ddf96f4cdeddb150151e99824641cc30222`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[9].body[3].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::assert_owner::root.body[9].body[3].body[2].body[1]::Expr

Source: `infra/agentinfra/roadmap_lease.py:52`; AST `338e8ce398926a8ed7f646b938ceb7263b43e9211c30ef34e328a9cd164c1ecd`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: inspect_process, owner, require. Outputs/bindings: (none).
Calls/effect boundaries: inspect_process, require.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[3].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::assert_owner::root.body[9].body[3].body[2].body[1].value::Call

Source: `infra/agentinfra/roadmap_lease.py:52`; AST `52cabf6735377f7357aaaba1a6b79a4ccf4808d819c204434285c9717634fed4`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inspect_process, owner, require. Outputs/bindings: (none).
Calls/effect boundaries: inspect_process, require.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[3].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::assert_owner::root.body[9].body[3].body[2].body[1].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_lease.py:52`; AST `9cb212d28bdaf842b98926a13f1a78a9141917f3a527e152781c25a7a6339517`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inspect_process, owner. Outputs/bindings: (none).
Calls/effect boundaries: inspect_process.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[3].body[2].body[1].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::qualify::root.body[9].body[4]::FunctionDef

Source: `infra/agentinfra/roadmap_lease.py:54`; AST `6724428c9f17878e6ae34d91fca02eb432634b14d45e32cf80319477de680a84`.

Rust module: `infra::agentinfra::roadmap_lease`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: canonical, dict, execution, observation, observe_managed_owner, observe_native_owner, owner, read_json, self. Outputs/bindings: canonical, execution, observation.
Calls/effect boundaries: canonical.exists, execution.get, observe_managed_owner, observe_native_owner, read_json, read_json(canonical).get, self.assert_owner.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[9].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::qualify::root.body[9].body[4].body[0]::Expr

Source: `infra/agentinfra/roadmap_lease.py:55`; AST `b259e48b31ae7295c90f1cb7d92f728b986f02e63a131ac10fb4fc08d6cb6603`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: owner, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assert_owner.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::qualify::root.body[9].body[4].body[0].value::Call

Source: `infra/agentinfra/roadmap_lease.py:55`; AST `5fc0119096b39cd2396b353da36c7cceb08ce76d361ad2177176ca7ee3116a11`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: owner, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assert_owner.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::qualify::root.body[9].body[4].body[1]::Assign

Source: `infra/agentinfra/roadmap_lease.py:56`; AST `5b13672ebdd5714b01b41469d45628e553af784f72cafc5902e1bd19fb31edf4`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: canonical.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::qualify::root.body[9].body[4].body[2]::Assign

Source: `infra/agentinfra/roadmap_lease.py:57`; AST `0f76c1536c7dacc75a25906fee8fa34df358935fbca5a6728c69eb9a82015966`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: canonical, read_json. Outputs/bindings: execution.
Calls/effect boundaries: canonical.exists, read_json, read_json(canonical).get.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::qualify::root.body[9].body[4].body[2].value.test::Call

Source: `infra/agentinfra/roadmap_lease.py:57`; AST `c1fa978fff3b77a6436fbb45c93af4496409ca1f9341d70e18593b2cea46d5d0`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical. Outputs/bindings: (none).
Calls/effect boundaries: canonical.exists.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[2].value.test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::qualify::root.body[9].body[4].body[2].value.body::Call

Source: `infra/agentinfra/roadmap_lease.py:57`; AST `5a3fc5631384c4b998e5da6be56850ba7307cbe606b39260448f433704a80aba`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json, read_json(canonical).get.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[2].value.body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::qualify::root.body[9].body[4].body[2].value.body.func.value::Call

Source: `infra/agentinfra/roadmap_lease.py:57`; AST `28d751221380b0c0b2aeaf45c4a9ca784e4ca1e55cc75f97e663bce0a020904c`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[2].value.body.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::qualify::root.body[9].body[4].body[3]::If

Source: `infra/agentinfra/roadmap_lease.py:58`; AST `c83010ef7ed98fded2014a409e6a376552ff534f6007fc046095c8bbc96b7dc2`.

Rust module: `infra::agentinfra::roadmap_lease`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: execution, observe_managed_owner, observe_native_owner, owner, self. Outputs/bindings: observation.
Calls/effect boundaries: execution.get, observe_managed_owner, observe_native_owner.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered If evaluation at root.body[9].body[4].body[3]; no call, error or mutation may be omitted. Condition: execution.get('integration_path') == 'managed_app_server'
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::qualify::root.body[9].body[4].body[3].test.left::Call

Source: `infra/agentinfra/roadmap_lease.py:58`; AST `ea2fbedf64fbdf2c27b273169e5fb0e5eba266e110561ac4538f727316ad66ca`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: execution. Outputs/bindings: (none).
Calls/effect boundaries: execution.get.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[3].test.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::qualify::root.body[9].body[4].body[3].body[0]::ImportFrom

Source: `infra/agentinfra/roadmap_lease.py:59`; AST `1c652da500467ca11a668e1e24666bcd76b0abdde81d431f08db38e765123522`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[9].body[4].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::qualify::root.body[9].body[4].body[3].body[1]::Assign

Source: `infra/agentinfra/roadmap_lease.py:60`; AST `9cdf2037cd1564a0cac9342b8c255da5de8e68d5055577b743bbc4c8298e620d`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observe_managed_owner, owner, self. Outputs/bindings: observation.
Calls/effect boundaries: observe_managed_owner.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[4].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::qualify::root.body[9].body[4].body[3].body[1].value::Call

Source: `infra/agentinfra/roadmap_lease.py:60`; AST `46ffe4040771f5d76e248d84fc0ae26b272845b39c36785beb96682fa64b701b`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observe_managed_owner, owner, self. Outputs/bindings: (none).
Calls/effect boundaries: observe_managed_owner.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::qualify::root.body[9].body[4].body[3].orelse[0]::ImportFrom

Source: `infra/agentinfra/roadmap_lease.py:62`; AST `72d2ff6ddcca8d892f0846c05bed804041e6528be66c02b52b4f8e39b21c8158`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[9].body[4].body[3].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::qualify::root.body[9].body[4].body[3].orelse[1]::Assign

Source: `infra/agentinfra/roadmap_lease.py:63`; AST `048f721af00b55f42753142bef4c121b541b3866605de5dfe2695bcd9763a6a4`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observe_native_owner, owner, self. Outputs/bindings: observation.
Calls/effect boundaries: observe_native_owner.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[4].body[3].orelse[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::qualify::root.body[9].body[4].body[3].orelse[1].value::Call

Source: `infra/agentinfra/roadmap_lease.py:63`; AST `66f4a106e007440d5f48ee3def63ffc0a496c3a08bad279b3e82a4e1e10fbdf1`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observe_native_owner, owner, self. Outputs/bindings: (none).
Calls/effect boundaries: observe_native_owner.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[3].orelse[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::qualify::root.body[9].body[4].body[4]::Expr

Source: `infra/agentinfra/roadmap_lease.py:64`; AST `b259e48b31ae7295c90f1cb7d92f728b986f02e63a131ac10fb4fc08d6cb6603`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: owner, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assert_owner.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::qualify::root.body[9].body[4].body[4].value::Call

Source: `infra/agentinfra/roadmap_lease.py:64`; AST `5fc0119096b39cd2396b353da36c7cceb08ce76d361ad2177176ca7ee3116a11`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: owner, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assert_owner.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[4].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::qualify::root.body[9].body[4].body[5]::Return

Source: `infra/agentinfra/roadmap_lease.py:65`; AST `cbdb18d50bf68e75f4a4d559d8a15419d9f8c73cf7a996e25212051c0cc855b1`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observation. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Return evaluation at root.body[9].body[4].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release_observed::root.body[9].body[5]::FunctionDef

Source: `infra/agentinfra/roadmap_lease.py:67`; AST `d9bc73b0aa7fd6a2e4ee94280434927bbb3534ae696160cf75971658f4c0c195`.

Rust module: `infra::agentinfra::roadmap_lease`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: bool, dict, observation, owner, recovery, require, self. Outputs/bindings: observation.
Calls/effect boundaries: require, self.qualify, self.release.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[9].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release_observed::root.body[9].body[5].body[0]::Assign

Source: `infra/agentinfra/roadmap_lease.py:68`; AST `57a341f2238fe65539f5b9de488412be6907c9a304a83ba40e2f7fc7f18e1377`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: owner, self. Outputs/bindings: observation.
Calls/effect boundaries: self.qualify.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release_observed::root.body[9].body[5].body[0].value::Call

Source: `infra/agentinfra/roadmap_lease.py:68`; AST `c16b490f63ed7e0fe2f4bdee4a67c10949eb81164a8fe9016c5f16e0e9f8bd5b`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: owner, self. Outputs/bindings: (none).
Calls/effect boundaries: self.qualify.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release_observed::root.body[9].body[5].body[1]::Expr

Source: `infra/agentinfra/roadmap_lease.py:69`; AST `ce7aa8839b0684761a49b13bf5300dfcff36f8731a0c6a7183c0052ec609f386`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observation, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release_observed::root.body[9].body[5].body[1].value::Call

Source: `infra/agentinfra/roadmap_lease.py:69`; AST `fb7622309d0de794c8f332b05446300c26417669fd2cad0749f1ddec6317227e`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observation, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[5].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release_observed::root.body[9].body[5].body[2]::Expr

Source: `infra/agentinfra/roadmap_lease.py:71`; AST `1daa6c88f7968c8d9c0fee2ea0f604da9ec8e3f53dade137610b7ff0f48fa0f4`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observation, owner, recovery, self. Outputs/bindings: (none).
Calls/effect boundaries: self.release.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release_observed::root.body[9].body[5].body[2].value::Call

Source: `infra/agentinfra/roadmap_lease.py:71`; AST `cb2d540c56c1cfaf149d48681eedc065ae8b0ce5eb8a3c6daa20954d11ebe689`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observation, owner, recovery, self. Outputs/bindings: (none).
Calls/effect boundaries: self.release.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[5].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6]::FunctionDef

Source: `infra/agentinfra/roadmap_lease.py:74`; AST `85cea2ccd8068b1aaedc10c3a65554f7258d63aea9f4a110dbdfbefe2f4cc337`.

Rust module: `infra::agentinfra::roadmap_lease`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileLock, _pid_alive, atomic_write_json, binding, bool, canonical, dict, lock, native_observation, observed, owner, read_json, recovery, require, self, socket, state. Outputs/bindings: binding, canonical, lock, observed, state.
Calls/effect boundaries: FileLock, _pid_alive, atomic_write_json, binding.get, canonical.exists, lock.acquire, lock.release, native_observation.get, read_json, read_json(canonical).get, read_json(canonical).get('execution', {}).get, require, self.qualify, self.read, socket.gethostname, state['history'].append.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[9].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[0]::Assign

Source: `infra/agentinfra/roadmap_lease.py:75`; AST `5b13672ebdd5714b01b41469d45628e553af784f72cafc5902e1bd19fb31edf4`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: canonical.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[1]::Assign

Source: `infra/agentinfra/roadmap_lease.py:76`; AST `b56c715b004ad7947dafc773586fb493f29bb809f8e9f1c6e1c7e942d8e6a0e6`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: canonical, read_json. Outputs/bindings: binding.
Calls/effect boundaries: canonical.exists, read_json, read_json(canonical).get, read_json(canonical).get('execution', {}).get.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[1].value.test::Call

Source: `infra/agentinfra/roadmap_lease.py:76`; AST `c1fa978fff3b77a6436fbb45c93af4496409ca1f9341d70e18593b2cea46d5d0`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical. Outputs/bindings: (none).
Calls/effect boundaries: canonical.exists.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[6].body[1].value.test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[1].value.body::Call

Source: `infra/agentinfra/roadmap_lease.py:76`; AST `a24699aeb6b3c4a8cc3c2d3675b9f6e78cdf22cc5a30dc6e3c1b3619e16c9a92`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json, read_json(canonical).get, read_json(canonical).get('execution', {}).get.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[6].body[1].value.body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[1].value.body.func.value::Call

Source: `infra/agentinfra/roadmap_lease.py:76`; AST `5a3fc5631384c4b998e5da6be56850ba7307cbe606b39260448f433704a80aba`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json, read_json(canonical).get.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[6].body[1].value.body.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[1].value.body.func.value.func.value::Call

Source: `infra/agentinfra/roadmap_lease.py:76`; AST `28d751221380b0c0b2aeaf45c4a9ca784e4ca1e55cc75f97e663bce0a020904c`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[6].body[1].value.body.func.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[2]::If

Source: `infra/agentinfra/roadmap_lease.py:77`; AST `2b0c896402efcb78183a57b43d568aaebd3a9f6ee1a5a92e41824530538fb9f1`.

Rust module: `infra::agentinfra::roadmap_lease`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: binding, observed, owner, require, self. Outputs/bindings: observed.
Calls/effect boundaries: binding.get, require, self.qualify.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered If evaluation at root.body[9].body[6].body[2]; no call, error or mutation may be omitted. Condition: binding.get('thread_id') == owner['session'] and binding.get('native_accounting_preserved') is True
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[2].test.values[0].left::Call

Source: `infra/agentinfra/roadmap_lease.py:77`; AST `63111ba26343241a333d0933cf221435534ec16270d2f49ca57741efb6c4fa1a`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding. Outputs/bindings: (none).
Calls/effect boundaries: binding.get.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[6].body[2].test.values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[2].test.values[1].left::Call

Source: `infra/agentinfra/roadmap_lease.py:77`; AST `674558e14bf2016edafb9c07a8f6e4b64a570e02d4fda3901f4706493c1f1137`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding. Outputs/bindings: (none).
Calls/effect boundaries: binding.get.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[6].body[2].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[2].body[0]::Assign

Source: `infra/agentinfra/roadmap_lease.py:80`; AST `7f6aee44e738d17bf29e25085a28da4793e2a7514c86bae4ba1bf0135c7e1794`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: owner, self. Outputs/bindings: observed.
Calls/effect boundaries: self.qualify.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[6].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_lease.py:80`; AST `c16b490f63ed7e0fe2f4bdee4a67c10949eb81164a8fe9016c5f16e0e9f8bd5b`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: owner, self. Outputs/bindings: (none).
Calls/effect boundaries: self.qualify.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[6].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[2].body[1]::Expr

Source: `infra/agentinfra/roadmap_lease.py:81`; AST `2a87aef15d4bd6e813f837c4559e5276bf3eb7327b79335134be2b8f61beb803`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observed, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[6].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[2].body[1].value::Call

Source: `infra/agentinfra/roadmap_lease.py:81`; AST `d1eb16db8787e1999c79a9c18a426309a06d65998f72e9a883fb254466d38b48`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observed, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[6].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[3]::Assign

Source: `infra/agentinfra/roadmap_lease.py:83`; AST `c74e6a764bc8fbf0b6a669107c897f7fca669e7bcab3a9ec73ef634816a93db6`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileLock, self. Outputs/bindings: lock.
Calls/effect boundaries: FileLock.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[6].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[3].value::Call

Source: `infra/agentinfra/roadmap_lease.py:83`; AST `ea447b203c4a9d0350d1e3bebdc01bf1a9d011e3cedda9a3a361f7e9932dadd2`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileLock, self. Outputs/bindings: (none).
Calls/effect boundaries: FileLock.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[6].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[4]::Expr

Source: `infra/agentinfra/roadmap_lease.py:83`; AST `2bcfe51cf785ee29160140309ca2724ded506c99a694a1cd40da99965fea32f6`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[6].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[4].value::Call

Source: `infra/agentinfra/roadmap_lease.py:83`; AST `19f113b1ff996d6a4e1349d4f629dcb1414895f291ae11a26e3a1c7c22771cf0`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[6].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[5]::Try

Source: `infra/agentinfra/roadmap_lease.py:84`; AST `0aa7e65308559a9c04bb43166f9446081713869225314cecc49187e6e79b509c`.

Rust module: `infra::agentinfra::roadmap_lease`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: _pid_alive, atomic_write_json, lock, native_observation, owner, recovery, require, self, socket, state. Outputs/bindings: state.
Calls/effect boundaries: _pid_alive, atomic_write_json, lock.release, native_observation.get, require, self.read, socket.gethostname, state['history'].append.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Try evaluation at root.body[9].body[6].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[5].body[0]::Assign

Source: `infra/agentinfra/roadmap_lease.py:85`; AST `f6543f323e041f6b48c301a340bcb4c8ed134a07bd8dedc0e02f4257baeabf5d`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: state.
Calls/effect boundaries: self.read.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[6].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[5].body[0].value::Call

Source: `infra/agentinfra/roadmap_lease.py:85`; AST `1a6cd88d33383d245bb90e4e5f924f99f090d6bd29a5c43fab9e8ffb18d19d91`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.read.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[6].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[5].body[1]::Expr

Source: `infra/agentinfra/roadmap_lease.py:85`; AST `2fd08af0a83fd8910b154f0609e3d368fa9ec64f65cc96d57098be1960c6ac80`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: owner, require, state. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[6].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[5].body[1].value::Call

Source: `infra/agentinfra/roadmap_lease.py:85`; AST `fefcde93e54e13556a306e8df7a386c7465f1f3e0ddec83fc88827e5e171f219`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: owner, require, state. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[6].body[5].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[5].body[2]::Expr

Source: `infra/agentinfra/roadmap_lease.py:86`; AST `bfc9dd3ca2a4ab6dac5fc3b7e185162fea75465486bec5c4bfe2cfb7e36bcad2`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: native_observation, owner, require. Outputs/bindings: (none).
Calls/effect boundaries: native_observation.get, require.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[6].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[5].body[2].value::Call

Source: `infra/agentinfra/roadmap_lease.py:86`; AST `7d8d25b13df94578d4b9668f6ecef807a01d3655b5c68f8dcff419bc87a0b5aa`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: native_observation, owner, require. Outputs/bindings: (none).
Calls/effect boundaries: native_observation.get, require.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[6].body[5].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[5].body[2].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_lease.py:86`; AST `602a516995ba5abd9a77756cf7512de7f366ce36f0c7bf5ebf403e87c2e0222e`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: native_observation. Outputs/bindings: (none).
Calls/effect boundaries: native_observation.get.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[6].body[5].body[2].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[5].body[2].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_lease.py:87`; AST `f659dd735e17a70b91af10d02daa62e23da6019b11cff1251c77ebc47362722c`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: native_observation. Outputs/bindings: (none).
Calls/effect boundaries: native_observation.get.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[6].body[5].body[2].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[5].body[2].value.args[0].values[2].left::Call

Source: `infra/agentinfra/roadmap_lease.py:88`; AST `3e58c29dfbe3cc6ea8ee39de32b8beb97108c285e1d1efae061bbcebf04053c1`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: native_observation. Outputs/bindings: (none).
Calls/effect boundaries: native_observation.get.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[6].body[5].body[2].value.args[0].values[2].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[5].body[3]::If

Source: `infra/agentinfra/roadmap_lease.py:90`; AST `88dac23c940168da751d1b178ed431c84a8b36073e4f012a8bf55c38623d888d`.

Rust module: `infra::agentinfra::roadmap_lease`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: _pid_alive, owner, recovery, require, socket. Outputs/bindings: (none).
Calls/effect boundaries: _pid_alive, require, socket.gethostname.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered If evaluation at root.body[9].body[6].body[5].body[3]; no call, error or mutation may be omitted. Condition: recovery
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[5].body[3].body[0]::Expr

Source: `infra/agentinfra/roadmap_lease.py:91`; AST `46645d1d9b0aae6fe726b11aa7c195bfd3ac89ea83dc2e87ed468aa80d4b1996`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _pid_alive, owner, require, socket. Outputs/bindings: (none).
Calls/effect boundaries: _pid_alive, require, socket.gethostname.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[6].body[5].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[5].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_lease.py:91`; AST `82ffc093ff66c35399d6d65985a6b7ddfebdbde07e9331fc923ad49a94c35d40`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _pid_alive, owner, require, socket. Outputs/bindings: (none).
Calls/effect boundaries: _pid_alive, require, socket.gethostname.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[6].body[5].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[5].body[3].body[0].value.args[0].values[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_lease.py:91`; AST `4263cfe4ff762fbfb73db5540d6d421a621a7fb22318759bc79d367d143d5895`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: socket. Outputs/bindings: (none).
Calls/effect boundaries: socket.gethostname.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[6].body[5].body[3].body[0].value.args[0].values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[5].body[3].body[0].value.args[0].values[1].operand::Call

Source: `infra/agentinfra/roadmap_lease.py:92`; AST `c102a77d4e9126bd8c1fdd731143cb3a3d9eaaaf3da97c4f68c35b8a3c72a340`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _pid_alive, owner. Outputs/bindings: (none).
Calls/effect boundaries: _pid_alive.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[6].body[5].body[3].body[0].value.args[0].values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[5].body[4]::Expr

Source: `infra/agentinfra/roadmap_lease.py:93`; AST `eb2dab9fd1824bb7ce17e51cbe0e1e7425203f07dadfd38ec27199a9c68afbdc`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: native_observation, owner, recovery, state. Outputs/bindings: (none).
Calls/effect boundaries: state['history'].append.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[6].body[5].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[5].body[4].value::Call

Source: `infra/agentinfra/roadmap_lease.py:93`; AST `cb15a9eaa9ed1ecefab0b66e56c67b37c028ae531d7a78d68a95dbd9d47a9ef8`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: native_observation, owner, recovery, state. Outputs/bindings: (none).
Calls/effect boundaries: state['history'].append.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[6].body[5].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[5].body[5]::Assign

Source: `infra/agentinfra/roadmap_lease.py:94`; AST `f8b43a9a255d5aba0097fae90add60b1e7cea6b19ecdb8435d92fbde2c5268f7`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: state. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[9].body[6].body[5].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[5].body[6]::Expr

Source: `infra/agentinfra/roadmap_lease.py:95`; AST `47c37f87c4b139eadafb73ff45277e35e0c57b7016e4bb6f83819b74c57bb2de`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_json, self, state. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[6].body[5].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[5].body[6].value::Call

Source: `infra/agentinfra/roadmap_lease.py:95`; AST `ac7fc12dd27d703341af29ac9171bc58f320270def4f5f2db3279e14dd2f546a`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_json, self, state. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[6].body[5].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[5].finalbody[0]::Expr

Source: `infra/agentinfra/roadmap_lease.py:96`; AST `9aa6f04fc26ee6b3f6fe1a19158adb3cfde13709dcae4a7cc38bccbb2655afb2`.

Rust module: `infra::agentinfra::roadmap_lease`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[9].body[6].body[5].finalbody[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_lease.py::module::WorkspaceLease::release::root.body[9].body[6].body[5].finalbody[0].value::Call

Source: `infra/agentinfra/roadmap_lease.py:96`; AST `107c5710331db61e695f7d71256d48862412d15c223e204da5c71c497352b634`.

Rust module: `infra::agentinfra::roadmap_lease`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, atomic, locks, os, pathlib, roadmap_managed, roadmap_native, roadmap_records, socket, uuid.

Invariants: Preserve ordered Call evaluation at root.body[9].body[6].body[5].finalbody[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
