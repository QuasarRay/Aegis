# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 281. Inventory digest: `63d9b4ce678f83477859a5a2a6594f2f075d7513ff6c173c52897d613717dab1`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/roadmap_runtime.py::module::root::Module

Source: `infra/agentinfra/roadmap_runtime.py:1`; AST `d075c6b031660a8933c73a8004283768c144e8b376ade3193a7cef2275b78a9f`.

Rust module: `infra::agentinfra::roadmap_runtime`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: BaseException, BudgetLedger, FileLock, Path, WorkspaceLease, a, all, ancestor, any, argv, atomic_write_json, attempt, binding, bindings_current, bool, by_id, compiled, confined_path, created, diagnosis, dict, digest, event_id, exc, execution, goal, ident, inherited, inherited_attempt_ids, inputs, int, isinstance, lease, ledger, legacy, len, list, lock, matches, max_attempts, milestone, name, ok, os, outcome, owner, path, pending, prior, read_json, receipt, recipe, recipe_scope, record, require, result, root, run_process, seconds, selected, self, sorted, str, sum, sys, thread, thread_id, time, total, total_seconds, tuple, type, usage, work_id, x. Outputs/bindings: a, ancestor, argv, attempt, binding, by_id, created, execution, goal, ident, inherited, inputs, lease, ledger, legacy, lock, matches, ok, owner, path, pending, prior, receipt, recipe, record, result, selected, thread, usage, work_id, x.
Calls/effect boundaries: BudgetLedger, FileLock, WorkspaceLease, WorkspaceLease(root).assert_owner, all, any, atomic_write_json, binding.get, bindings_current, bool, by_id[ident].get, confined_path, diagnosis.strip, dict, digest, execution.get, goal.get, isinstance, lease.acquire, lease.release, ledger.close, ledger.read, ledger.reserve, len, list, lock.acquire, lock.release, matches[0].update, os.getpid, owner.get, pending.append, pending.pop, read_json, recipe_scope, record.get, record.get('continuation', {}).get, record['attempts'].append, record['usage'].setdefault, require, root.resolve, run_process, selected.add, selected.update, self.path.exists, self.path.with_suffix, self.read, sorted, str, sum, time.time_ns, tuple, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::root.body[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:1`; AST `22713275504500a3706dbcd5b882931e335a2c9194ee796a6fc61626333b7e22`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::root.body[1]::ImportFrom

Source: `infra/agentinfra/roadmap_runtime.py:2`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::root.body[2]::Import

Source: `infra/agentinfra/roadmap_runtime.py:4`; AST `ac3a74d6dd975a8e8fe4b7f85fce794793a9355595b850e3926964913948d386`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::root.body[3]::Import

Source: `infra/agentinfra/roadmap_runtime.py:5`; AST `ff05bad0fd9a7212d3cd85fd2726055168be21bc8f6e0d93b29965794b0675d4`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::root.body[4]::ImportFrom

Source: `infra/agentinfra/roadmap_runtime.py:6`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered ImportFrom evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::root.body[5]::ImportFrom

Source: `infra/agentinfra/roadmap_runtime.py:8`; AST `1b8b71be5203ae66cf696ad7ae023750f023f11fd20fe2501f8e1d56817881e3`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered ImportFrom evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::root.body[6]::ImportFrom

Source: `infra/agentinfra/roadmap_runtime.py:9`; AST `f49eec2be7586a81b0fa34570d7cbaa58bc5eeaa5e471a05fac611f36b0ee7bd`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered ImportFrom evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::root.body[7]::ImportFrom

Source: `infra/agentinfra/roadmap_runtime.py:10`; AST `cb4b66aa2a9ba9861af7c0b11d312d64af950034a4b89ff32a7fb710e139fffa`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered ImportFrom evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::root.body[8]::ImportFrom

Source: `infra/agentinfra/roadmap_runtime.py:11`; AST `bc40cff7f4721d6e94a9b7a934f453365503e4faa00b75989946ce9e1e0bd8d4`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered ImportFrom evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::root.body[9]::ImportFrom

Source: `infra/agentinfra/roadmap_runtime.py:12`; AST `c77b99ce1220eaeadd24d0d2eb90624f8e6b280576577774ee57598a0f5eef8f`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered ImportFrom evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::root.body[10]::ImportFrom

Source: `infra/agentinfra/roadmap_runtime.py:13`; AST `09d8e9e8f6fd64b1de599cd7bc89a5b39b492565154c1945944f226444aab849`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered ImportFrom evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::root.body[11]::ClassDef

Source: `infra/agentinfra/roadmap_runtime.py:16`; AST `6aee9c211f35888cce5f2c5d9cd7c47e9e58787769489e32b1902598c677c916`.

Rust module: `infra::agentinfra::roadmap_runtime`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: FileLock, Path, a, ancestor, any, atomic_write_json, attempt, bool, by_id, confined_path, diagnosis, dict, digest, event_id, ident, inherited_attempt_ids, inputs, int, isinstance, len, list, lock, matches, max_attempts, os, outcome, pending, prior, read_json, receipt, record, require, root, seconds, selected, self, sorted, str, sum, thread_id, time, total, total_seconds, tuple, type, usage, work_id. Outputs/bindings: a, ancestor, attempt, by_id, ident, lock, matches, pending, prior, record, selected, usage.
Calls/effect boundaries: FileLock, any, atomic_write_json, bool, by_id[ident].get, confined_path, diagnosis.strip, dict, digest, isinstance, len, list, lock.acquire, lock.release, matches[0].update, os.getpid, pending.append, pending.pop, read_json, record.get, record['attempts'].append, record['usage'].setdefault, require, root.resolve, selected.add, selected.update, self.path.exists, self.path.with_suffix, self.read, sorted, sum, time.time_ns, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered ClassDef evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::__init__::root.body[11].body[0]::FunctionDef

Source: `infra/agentinfra/roadmap_runtime.py:17`; AST `9bb02373b582dc831e70fc4fa4cd90792c32e6d8e0d7785e08df726578a682dd`.

Rust module: `infra::agentinfra::roadmap_runtime`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, confined_path, root, self. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, root.resolve, self.path.with_suffix.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::__init__::root.body[11].body[0].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:18`; AST `eac70191d36cd330a975a12be514d4a5f58088087cc2acfa2746cafe468cc8ae`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root, self. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::__init__::root.body[11].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:18`; AST `b97f3f463d4724206af2869ad4674d5eb373167f052507971a722ecc8f771a87`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::__init__::root.body[11].body[0].body[1]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:19`; AST `d7c0d76a0a372e03aeee66707c691374e60f76edfd240270d47898754eb23586`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, self. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::__init__::root.body[11].body[0].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:19`; AST `7d3ec00caae052142f9eafaf7e819afec6aee67b95327ec1d924450faaa8dd1d`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, self. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::__init__::root.body[11].body[0].body[2]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:20`; AST `c2afb1ebc402604bd7895515b0a0018025d44af2cbae841656670af5f84ca0bc`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.with_suffix.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::__init__::root.body[11].body[0].body[2].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:20`; AST `46aa1e96394d83d78ce0650ffed08f0cb1281604c533bd7f0a9f1922de6c6239`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.with_suffix.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::read::root.body[11].body[1]::FunctionDef

Source: `infra/agentinfra/roadmap_runtime.py:22`; AST `891edfe851c10127a331e1b2eea82f8b17f181d6a30472cf5f9e3ee3286f4903`.

Rust module: `infra::agentinfra::roadmap_runtime`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: dict, isinstance, list, read_json, record, require, self. Outputs/bindings: record.
Calls/effect boundaries: isinstance, read_json, record.get, require, self.path.exists.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::read::root.body[11].body[1].body[0]::If

Source: `infra/agentinfra/roadmap_runtime.py:23`; AST `67bf55701541534e06b51219f8a02cfa9e5985f005d4a76efd8c094c26b0efae`.

Rust module: `infra::agentinfra::roadmap_runtime`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.exists.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered If evaluation at root.body[11].body[1].body[0]; no call, error or mutation may be omitted. Condition: not self.path.exists()
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::read::root.body[11].body[1].body[0].test.operand::Call

Source: `infra/agentinfra/roadmap_runtime.py:23`; AST `5a0ab509baad619ec2a1ec684d6882dd1595eead8f620b398322ae10eeaa6916`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.exists.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[1].body[0].test.operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::read::root.body[11].body[1].body[0].body[0]::Return

Source: `infra/agentinfra/roadmap_runtime.py:24`; AST `be4cd20c06d06226bfa38334fbb62cfee292b75aae8dd88d66a9a0bd98e0d6ba`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Return evaluation at root.body[11].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::read::root.body[11].body[1].body[1]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:25`; AST `fb8294180bf4926dc986b94d7c34f40164ef851af315e01b0f6fd302cd4b9f4d`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: read_json, self. Outputs/bindings: record.
Calls/effect boundaries: read_json.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::read::root.body[11].body[1].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:25`; AST `e3a79a25f0eadc251da7129b90e21b22224f14b35a0ef4a713b53e9a67e688de`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: read_json, self. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::read::root.body[11].body[1].body[2]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:26`; AST `97b23c59b694d728ff16e61242d7f308eeb2f0cbee09abc17cf144d4fcb422be`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, isinstance, list, record, require. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, record.get, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::read::root.body[11].body[1].body[2].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:26`; AST `0ef8fbb5b29675ed996376eea9c4daed481a02c77fb64032de311d5686dd141c`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, isinstance, list, record, require. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, record.get, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[1].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::read::root.body[11].body[1].body[2].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:26`; AST `d1e3876e5f2eab25e6fd365f06eea6e829f195ef666744ac41314682d8aa382c`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[1].body[2].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::read::root.body[11].body[1].body[2].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_runtime.py:26`; AST `6eee454d38c6564b55c0aa4f32f87833e740d6719ce68783e5be1391f7aef128`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, list, record. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, record.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[1].body[2].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::read::root.body[11].body[1].body[2].value.args[0].values[1].args[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:26`; AST `6f7099dbd1e70fd0200a10e43c3d57441c66d9313a8346facf963c2376729b31`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[1].body[2].value.args[0].values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::read::root.body[11].body[1].body[2].value.args[0].values[2]::Call

Source: `infra/agentinfra/roadmap_runtime.py:27`; AST `c48049e81f7d1a6ec319ee66f15165d82368e235328d4c13bde6af9c3945a493`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, isinstance, record. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, record.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[1].body[2].value.args[0].values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::read::root.body[11].body[1].body[2].value.args[0].values[2].args[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:27`; AST `971d3eeb847e43400f978a1445d095c0a202e2f066e7915796b8aca6493c5afb`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[1].body[2].value.args[0].values[2].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::read::root.body[11].body[1].body[3]::Return

Source: `infra/agentinfra/roadmap_runtime.py:28`; AST `1d8c2c2be64d23c31c6eec0ccb160ec416867628655492a485c3d996da1d58bc`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Return evaluation at root.body[11].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2]::FunctionDef

Source: `infra/agentinfra/roadmap_runtime.py:30`; AST `60eb5327c6c99408156447c2b59fc3b638b5b25b2e09ae8d2cef1b0dbc5270d3`.

Rust module: `infra::agentinfra::roadmap_runtime`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileLock, a, ancestor, any, atomic_write_json, attempt, bool, by_id, diagnosis, dict, digest, ident, inherited_attempt_ids, inputs, int, len, list, lock, max_attempts, os, pending, prior, record, require, seconds, selected, self, sorted, str, sum, time, total_seconds, tuple, type, work_id. Outputs/bindings: a, ancestor, attempt, by_id, ident, lock, pending, prior, record, selected.
Calls/effect boundaries: FileLock, any, atomic_write_json, bool, by_id[ident].get, diagnosis.strip, digest, len, list, lock.acquire, lock.release, os.getpid, pending.append, pending.pop, record['attempts'].append, require, selected.add, selected.update, self.read, sorted, sum, time.time_ns, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:33`; AST `a80b87227f28c252d080ff907f0af172651ba555453e5745036155ccbed82667`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, inputs, require, work_id. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:33`; AST `532953187feeb5f720f2ac24f265350e761291ca3c3371a87306da52fd106c62`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, inputs, require, work_id. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[0].value.args[0].values[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:33`; AST `3ae74bfd2d999bef6297b9369a4b32c07c4f1e16d67071fa19213358511f6e29`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, work_id. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[0].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[0].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_runtime.py:33`; AST `ef3364368f11bf503a705b81744c2ee700a977c2e5437c3aaea2668cf13f26be`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, inputs. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[0].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[1]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:34`; AST `b17e586799a16bc6b953646c5e90047a0ed227893cce89fb6b5801148f41fe1e`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: int, require, seconds, total_seconds, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:34`; AST `2a0b826e831477b300b2dac3c5c0290c63800c7feb79d5cdbf29c6474b70eff8`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: int, require, seconds, total_seconds, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[1].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:34`; AST `e29d63a9a86ffc4d5ce9bfd619e61c5b9fafe7809d4fc5ad33dc1f04fb7a317a`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: seconds, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[1].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[2]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:35`; AST `c1ad9285eea94c0876760996a56b011eb7953a8001fa649860e9c5cba67e257f`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: int, max_attempts, require, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[2].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:35`; AST `9964a427f27faa188a06a2f6599c6e308cc37023ed6a1f3819565fd56914c6f3`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: int, max_attempts, require, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[2].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:35`; AST `5c1b9a2cbf1ccfb06e1a4aa0120d70b689774d68a32ac6662ddfca17331a8660`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: max_attempts, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[2].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[3]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:36`; AST `3bc0ac9d6fad6dac6fff38a4fd1f20dc4110bccf5d9eb479aaa386890f32ebf7`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileLock, self. Outputs/bindings: lock.
Calls/effect boundaries: FileLock.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[3].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:36`; AST `822547b3f0bdc60054653afca1074c32c8ad0902a2bcd405ce481643eccfcaed`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileLock, self. Outputs/bindings: (none).
Calls/effect boundaries: FileLock.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[4]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:37`; AST `2bcfe51cf785ee29160140309ca2724ded506c99a694a1cd40da99965fea32f6`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[2].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[4].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:37`; AST `19f113b1ff996d6a4e1349d4f629dcb1414895f291ae11a26e3a1c7c22771cf0`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5]::Try

Source: `infra/agentinfra/roadmap_runtime.py:38`; AST `048054d5fe5386849deb66b59277ce33c5de8db745323eee531d5bcfd0743da8`.

Rust module: `infra::agentinfra::roadmap_runtime`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: a, ancestor, any, atomic_write_json, attempt, bool, by_id, diagnosis, digest, ident, inherited_attempt_ids, inputs, len, list, lock, max_attempts, os, pending, prior, record, require, seconds, selected, self, sorted, sum, time, total_seconds, work_id. Outputs/bindings: a, ancestor, attempt, by_id, ident, pending, prior, record, selected.
Calls/effect boundaries: any, atomic_write_json, bool, by_id[ident].get, diagnosis.strip, digest, len, list, lock.release, os.getpid, pending.append, pending.pop, record['attempts'].append, require, selected.add, selected.update, self.read, sorted, sum, time.time_ns.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Try evaluation at root.body[11].body[2].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:39`; AST `8d60c6cf06a37f3a21e36d8d4fc569b1d94d00284e5e8e23781c46e0c0bd8c8b`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: record.
Calls/effect boundaries: self.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:39`; AST `1a6cd88d33383d245bb90e4e5f924f99f090d6bd29a5c43fab9e8ffb18d19d91`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[1]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:40`; AST `3f94d5e396de94be24a697a557aa5b842d9d9f0e0ceb7ef9ae746911cf6a543d`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, record. Outputs/bindings: a, by_id.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[1].value::DictComp

Source: `infra/agentinfra/roadmap_runtime.py:40`; AST `0af492f53a4f06dd57bc0a462c96632f9d82a37180663e5373914ec37e0068a5`.

Rust module: `infra::agentinfra::roadmap_runtime`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: a, record. Outputs/bindings: a.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered DictComp evaluation at root.body[11].body[2].body[5].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[2]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:41`; AST `f4eeaff93e8425bc3e40e5034fced577e7618659d70e40871271dd147af7b583`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: by_id, len, record, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[2].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[2].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:41`; AST `beee1bab383e0f5afdce56e953b36a9448d7339b38ee1ac39b53642c8df823d9`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: by_id, len, record, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[5].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[2].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:41`; AST `fca7519555a1766ecc40eb735a14669b85381de9aec70a807c39a18392a1e9e2`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: by_id, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[5].body[2].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[2].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:41`; AST `c05725c5487cf0182a5df9b1cf359aab17b9a274a7574e1eaea12e2c45bfcb0d`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, record. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[5].body[2].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[3]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:42`; AST `9995f75d625568b202a5d895d7ea340ca122721c7c855ea2d847f3ea16418d68`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, record, work_id. Outputs/bindings: a, selected.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[5].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[3].value::SetComp

Source: `infra/agentinfra/roadmap_runtime.py:42`; AST `3feab2de1f629678bc3916e9405bad5b8ff1709d314a18be54c2887efcc61b5a`.

Rust module: `infra::agentinfra::roadmap_runtime`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: a, record, work_id. Outputs/bindings: a.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered SetComp evaluation at root.body[11].body[2].body[5].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[4]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:43`; AST `d93a835165f51f0c01590a1386003c98dd16989de566645b7137f1edc0a5038f`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: inherited_attempt_ids, selected. Outputs/bindings: (none).
Calls/effect boundaries: selected.update.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[2].body[5].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[4].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:43`; AST `489abf5a985620f9d5bf4a949c6ff517515efbd40b321eb84cc3a03cffea2e47`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inherited_attempt_ids, selected. Outputs/bindings: (none).
Calls/effect boundaries: selected.update.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[5].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[5]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:44`; AST `7990f26d0c3ac3e5ff243f6f29817986c68c08db2968416c4969e47aa3ddc83c`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: list, selected. Outputs/bindings: pending.
Calls/effect boundaries: list.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[5].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[5].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:44`; AST `0ce818bc2d969dfc1e42388bad21082a934be1abae8978b431f8a4bd8411fda8`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: list, selected. Outputs/bindings: (none).
Calls/effect boundaries: list.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[5].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[6]::While

Source: `infra/agentinfra/roadmap_runtime.py:45`; AST `a81932efe292921b095022359e2383938025d43e9766a995e27147bf023c029f`.

Rust module: `infra::agentinfra::roadmap_runtime`. while with explicit truth conversion and a normal-exhaustion flag for loop else

Inputs: ancestor, by_id, ident, pending, require, selected. Outputs/bindings: ancestor, ident.
Calls/effect boundaries: by_id[ident].get, pending.append, pending.pop, require, selected.add.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered While evaluation at root.body[11].body[2].body[5].body[6]; no call, error or mutation may be omitted. Condition: pending
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[6].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:46`; AST `cd29c37b04bb134dfe779600c3ed77c11c577cd4af8f6422efc7626707e31451`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: pending. Outputs/bindings: ident.
Calls/effect boundaries: pending.pop.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[5].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[6].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:46`; AST `b59b504ea575e0473ea0b5cc17902585c9dde56c94712f38bdafbec0ce738e98`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: pending. Outputs/bindings: (none).
Calls/effect boundaries: pending.pop.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[5].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[6].body[1]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:47`; AST `298e078001f96b1f709a7bb4c95fec77c25351a0dd6aafbf186900cd44735f2a`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: by_id, ident, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[2].body[5].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[6].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:47`; AST `af514d5f0dd84d587925dba46fb829699326588b5fad410bc163e6dd5c302ae7`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: by_id, ident, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[5].body[6].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[6].body[2]::For

Source: `infra/agentinfra/roadmap_runtime.py:48`; AST `0129a9053ae619ce45e0460dc9c89ddb08d9d941afd50cbddae1bb6fddaab00b`.

Rust module: `infra::agentinfra::roadmap_runtime`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ancestor, by_id, ident, pending, selected. Outputs/bindings: ancestor.
Calls/effect boundaries: by_id[ident].get, pending.append, selected.add.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered For evaluation at root.body[11].body[2].body[5].body[6].body[2]; no call, error or mutation may be omitted. Iteration: ancestor in by_id[ident].get('inherited_attempt_ids', [])
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[6].body[2].iter::Call

Source: `infra/agentinfra/roadmap_runtime.py:48`; AST `b2c30f811df6ec5631268ba55a53c847a07689d33e3a9a0764f8630811872cdc`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: by_id, ident. Outputs/bindings: (none).
Calls/effect boundaries: by_id[ident].get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[5].body[6].body[2].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[6].body[2].body[0]::If

Source: `infra/agentinfra/roadmap_runtime.py:49`; AST `fc09a4bed97dc46c99ed744c30f971daaad81bf27be8a733459934d763e1f625`.

Rust module: `infra::agentinfra::roadmap_runtime`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ancestor, pending, selected. Outputs/bindings: (none).
Calls/effect boundaries: pending.append, selected.add.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered If evaluation at root.body[11].body[2].body[5].body[6].body[2].body[0]; no call, error or mutation may be omitted. Condition: ancestor not in selected
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[6].body[2].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:50`; AST `2c682e2f8524ca6b5ce4f91409613a6255b5817ad8a7474ec2481c80e468d2e5`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ancestor, selected. Outputs/bindings: (none).
Calls/effect boundaries: selected.add.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[2].body[5].body[6].body[2].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[6].body[2].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:50`; AST `ec99ea1b1aaab3ab414875620660191a2bb130b1499c49b30a4d2fccca28a70c`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ancestor, selected. Outputs/bindings: (none).
Calls/effect boundaries: selected.add.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[5].body[6].body[2].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[6].body[2].body[0].body[1]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:51`; AST `c03f05ed75d424f2b2ec867fb7af802a7515d870db2922b6ace3c08ae2a42b3b`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ancestor, pending. Outputs/bindings: (none).
Calls/effect boundaries: pending.append.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[2].body[5].body[6].body[2].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[6].body[2].body[0].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:51`; AST `1f4ccbf08b1678df0c7c38f3a544222b1727ed365102028e05856bbca8efb3d9`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ancestor, pending. Outputs/bindings: (none).
Calls/effect boundaries: pending.append.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[5].body[6].body[2].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[7]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:52`; AST `5563638ac9b981a191e6c4f760585620e36c277be986945ef5beadf4c5f11316`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, record, selected. Outputs/bindings: a, prior.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[5].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[7].value::ListComp

Source: `infra/agentinfra/roadmap_runtime.py:52`; AST `4ca34ce9e4d1bc6c69578dc8e02f1fae5d9f9c34c3da7c8af7e7cb24b2e9c862`.

Rust module: `infra::agentinfra::roadmap_runtime`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: a, record, selected. Outputs/bindings: a.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered ListComp evaluation at root.body[11].body[2].body[5].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[8]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:53`; AST `9e2e189575ad9c29c56864582f9041b6986912484e2395d8e6e661a3410171f3`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, any, prior, require. Outputs/bindings: a.
Calls/effect boundaries: any, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[2].body[5].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[8].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:53`; AST `3c38a72856553d5c434e909fd4ae145eac7bf8446bca16ad70c3fb45b7b5350c`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, any, prior, require. Outputs/bindings: a.
Calls/effect boundaries: any, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[5].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[8].value.args[0].operand::Call

Source: `infra/agentinfra/roadmap_runtime.py:53`; AST `0c6799aa907ad169146daaee66073b6174234e139128234a79156d4b2ebeda2d`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, any, prior. Outputs/bindings: a.
Calls/effect boundaries: any.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[5].body[8].value.args[0].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[8].value.args[0].operand.args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_runtime.py:53`; AST `8a7d5fe1ed41edb414ae9932a9816f5ba59267137bef9f90b7f7dcacce6ceb98`.

Rust module: `infra::agentinfra::roadmap_runtime`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: a, prior. Outputs/bindings: a.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[11].body[2].body[5].body[8].value.args[0].operand.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[9]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:54`; AST `d08faefd03d6489f6ef2ac996dcd9ccebaaf365018efa1c74c918b43bfe0a134`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, any, inputs, prior, require. Outputs/bindings: a.
Calls/effect boundaries: any, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[2].body[5].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[9].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:54`; AST `ac4d1c553a8c47c0f5a5d2d23e8169103c7c28d587178a88a7048ebd50abee20`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, any, inputs, prior, require. Outputs/bindings: a.
Calls/effect boundaries: any, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[5].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[9].value.args[0].operand::Call

Source: `infra/agentinfra/roadmap_runtime.py:54`; AST `fed5ed9c4fb238b253f82e8a7f2a19f3771a6e73715f04ddc0581372625d0b4e`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, any, inputs, prior. Outputs/bindings: a.
Calls/effect boundaries: any.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[5].body[9].value.args[0].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[9].value.args[0].operand.args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_runtime.py:54`; AST `13f362874b9ee538d6c9f583dfe103a819c65a15f6b6df4d82432666fe533471`.

Rust module: `infra::agentinfra::roadmap_runtime`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: a, inputs, prior. Outputs/bindings: a.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[11].body[2].body[5].body[9].value.args[0].operand.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[10]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:55`; AST `7391bea7d25413cea2169158057e9dfd3d33a170d458e504311360fb4f859140`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, max_attempts, prior, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[2].body[5].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[10].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:55`; AST `ea5dcffa2aa745f14f54710212bd296f8e87a22aa5a35b29fc65003a4f2dcb1d`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, max_attempts, prior, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[5].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[10].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:55`; AST `913efbe5bf6e483de6568a9d688cb27d196675409407cd117ee0c850ad45fa62`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, prior. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[5].body[10].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[11]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:56`; AST `6ca91224f6f395ad579c50bf96f8a8516cd2bc20de7f8477f7a351740f652eee`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, prior, require, seconds, sum, total_seconds. Outputs/bindings: a.
Calls/effect boundaries: require, sum.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[2].body[5].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[11].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:56`; AST `4f2e717a35193cb0e53391f1d045de41c018111f712e8e01f149475232dc783e`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, prior, require, seconds, sum, total_seconds. Outputs/bindings: a.
Calls/effect boundaries: require, sum.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[5].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[11].value.args[0].left.left::Call

Source: `infra/agentinfra/roadmap_runtime.py:56`; AST `b38b99778247510f3672c27d25c86f1b1b5b33ec826015d24ef67f3500db5098`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, prior, sum. Outputs/bindings: a.
Calls/effect boundaries: sum.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[5].body[11].value.args[0].left.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[11].value.args[0].left.left.args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_runtime.py:56`; AST `a520fd903880e58d6b8700506eefe7632d8c57d438dd4cc7ea61c981e1519e48`.

Rust module: `infra::agentinfra::roadmap_runtime`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: a, prior. Outputs/bindings: a.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[11].body[2].body[5].body[11].value.args[0].left.left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[12]::If

Source: `infra/agentinfra/roadmap_runtime.py:57`; AST `b4dbee7b3606424977851718f53f1684774ad7640f0a279166817736a96978dd`.

Rust module: `infra::agentinfra::roadmap_runtime`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: bool, diagnosis, inputs, prior, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, diagnosis.strip, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered If evaluation at root.body[11].body[2].body[5].body[12]; no call, error or mutation may be omitted. Condition: prior
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[12].body[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:58`; AST `853db2afd8c28c8a33d887e96a83bfc29ef3e7c87665fe0b65ffb9fd150280a6`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, diagnosis, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, diagnosis.strip, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[2].body[5].body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[12].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:58`; AST `ee171942fafcee617bf68b88d56acc2131348d87f6dccc06ff90a755a1ee0108`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, diagnosis, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, diagnosis.strip, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[5].body[12].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[12].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:58`; AST `5f161d0ee70916206cd6762d78e25cf9148e9debd7f0313e6d473e15d6cbe7ea`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, diagnosis. Outputs/bindings: (none).
Calls/effect boundaries: bool, diagnosis.strip.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[5].body[12].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[12].body[0].value.args[0].args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_runtime.py:58`; AST `7ec57aec97069b761eca95116ac27ef7ef1d814f93787c9b53931bd9f521bcd1`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: diagnosis. Outputs/bindings: (none).
Calls/effect boundaries: diagnosis.strip.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[5].body[12].body[0].value.args[0].args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[12].body[1]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:59`; AST `fe7fe2c0aa7b68cc1ea3fbeb1c02aa7c4f81ad6059ad46ce7292e6cdcb94ffdd`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: inputs, prior, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[2].body[5].body[12].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[12].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:59`; AST `1dd71fb4e777ec9c00132d97cce799a33daa63b07e7c6b9bb9ce0e70c0717b0f`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inputs, prior, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[5].body[12].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[13]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:60`; AST `a5e4c849ba3b4fbcee16d01c7e2b2cd85ad1e9a6fbfb11b9b8a24830ecfaa925`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: diagnosis, digest, inputs, len, os, prior, seconds, time, work_id. Outputs/bindings: attempt.
Calls/effect boundaries: digest, len, os.getpid, time.time_ns.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[5].body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[13].value.values[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:60`; AST `72625daab276fb12642547a5a4363cb6ff2bc5a0f1dd634f089ff1e0ec5de495`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, inputs, len, prior, work_id. Outputs/bindings: (none).
Calls/effect boundaries: digest, len.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[5].body[13].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[13].value.values[0].args[0].values[2].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:60`; AST `913efbe5bf6e483de6568a9d688cb27d196675409407cd117ee0c850ad45fa62`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, prior. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[5].body[13].value.values[0].args[0].values[2].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[13].value.values[6]::Call

Source: `infra/agentinfra/roadmap_runtime.py:62`; AST `ba1923643b161051a18bf7ae7386addd84146f4ab481f99d56712bc1ce97df2c`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os. Outputs/bindings: (none).
Calls/effect boundaries: os.getpid.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[5].body[13].value.values[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[13].value.values[7]::Call

Source: `infra/agentinfra/roadmap_runtime.py:63`; AST `d7bb4f9a8f02ae840b0ecfbf4a0bc46a103c9ee80044d3e746466d336dbaf7ae`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: time. Outputs/bindings: (none).
Calls/effect boundaries: time.time_ns.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[5].body[13].value.values[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[14]::If

Source: `infra/agentinfra/roadmap_runtime.py:64`; AST `2e3c0b2733641117cdb80c3b879edb7f5f9be49f9525632448a538394b34672a`.

Rust module: `infra::agentinfra::roadmap_runtime`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: attempt, selected, sorted. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered If evaluation at root.body[11].body[2].body[5].body[14]; no call, error or mutation may be omitted. Condition: selected
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[14].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:65`; AST `ea34d11b7f97d9b8fbb69de922186741b9d0a38b072e14d3f51018b89e855194`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: attempt, selected, sorted. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[5].body[14].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[14].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:65`; AST `147f6d5e20829fc9a7dc9eb9ad77f8370cf83e0b48d7af6d1bef8e658bbf78af`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: selected, sorted. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[5].body[14].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[15]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:66`; AST `72ad7243e175c897858cde4cb3d89e1c1586fe12d477ff19b5d4b77ea35ae6cd`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: attempt, record. Outputs/bindings: (none).
Calls/effect boundaries: record['attempts'].append.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[2].body[5].body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[15].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:66`; AST `876c585b5b90aaeea31ed0ebf97f0192892efe1c54f8971afdc17736d4a0e621`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: attempt, record. Outputs/bindings: (none).
Calls/effect boundaries: record['attempts'].append.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[5].body[15].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[16]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:67`; AST `39653ba93071c48ea5664f41495c0b9b4c456ea6c7027a39f271248d5232ec2e`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_json, record, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[2].body[5].body[16]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[16].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:67`; AST `e0ebb6df18f3acd72b73864198de1922264a5591e4adfd3e452231c9bafa9477`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_json, record, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[5].body[16].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].body[17]::Return

Source: `infra/agentinfra/roadmap_runtime.py:68`; AST `e266cd7ee7f5bdfcac0bb2a29b163bd7502edefad7a236c7df360c13dc73bb7e`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: attempt. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Return evaluation at root.body[11].body[2].body[5].body[17]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].finalbody[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:70`; AST `9aa6f04fc26ee6b3f6fe1a19158adb3cfde13709dcae4a7cc38bccbb2655afb2`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[2].body[5].finalbody[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[5].finalbody[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:70`; AST `107c5710331db61e695f7d71256d48862412d15c223e204da5c71c497352b634`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[5].finalbody[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[3]::FunctionDef

Source: `infra/agentinfra/roadmap_runtime.py:72`; AST `a2393fa0bd59d57498a152c369c0ed2a5ca20b1ffc352bd5da4318b2cc585e6d`.

Rust module: `infra::agentinfra::roadmap_runtime`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileLock, a, atomic_write_json, dict, ident, len, lock, matches, outcome, receipt, record, require, self, str. Outputs/bindings: a, lock, matches, record.
Calls/effect boundaries: FileLock, atomic_write_json, len, lock.acquire, lock.release, matches[0].update, require, self.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[3].body[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:73`; AST `ff22254ad3521a5de6152891b38da85f22dd101c576a6e0229b2a432bf9aacc7`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: outcome, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:73`; AST `f8b0617f9b0cada61780dfcbe5e11cb0795448f3c525f4f04f185d7a3eb018f6`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: outcome, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[3].body[1]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:74`; AST `5ad948bd4807312f2c239602daba24f505bb65e40a43af1bb9af59c5142392a1`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileLock, self. Outputs/bindings: lock.
Calls/effect boundaries: FileLock.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[3].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:74`; AST `06ed4456c71451913ad10de312800960b64f8327c15985fb8debf4e388eef9d0`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileLock, self. Outputs/bindings: (none).
Calls/effect boundaries: FileLock.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[3].body[2]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:75`; AST `2bcfe51cf785ee29160140309ca2724ded506c99a694a1cd40da99965fea32f6`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[3].body[2].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:75`; AST `19f113b1ff996d6a4e1349d4f629dcb1414895f291ae11a26e3a1c7c22771cf0`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[3].body[3]::Try

Source: `infra/agentinfra/roadmap_runtime.py:76`; AST `1685361e6ac80d5ca980d9c91a0a95256ca9a21ac79ed8f43b8d3c5df6c9635d`.

Rust module: `infra::agentinfra::roadmap_runtime`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: a, atomic_write_json, ident, len, lock, matches, outcome, receipt, record, require, self. Outputs/bindings: a, matches, record.
Calls/effect boundaries: atomic_write_json, len, lock.release, matches[0].update, require, self.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Try evaluation at root.body[11].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[3].body[3].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:77`; AST `8d60c6cf06a37f3a21e36d8d4fc569b1d94d00284e5e8e23781c46e0c0bd8c8b`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: record.
Calls/effect boundaries: self.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[3].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[3].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:77`; AST `1a6cd88d33383d245bb90e4e5f924f99f090d6bd29a5c43fab9e8ffb18d19d91`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[3].body[3].body[1]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:78`; AST `cf32e9bf9b8a72d66b64531668c804f7085a2f6675610c277caa371b3b7106b2`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, ident, record. Outputs/bindings: a, matches.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[3].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[3].body[3].body[1].value::ListComp

Source: `infra/agentinfra/roadmap_runtime.py:78`; AST `fb765ce6077cad522849ac1bfa4314dacb67a58cf6789a9c53a4b0d2d988644b`.

Rust module: `infra::agentinfra::roadmap_runtime`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: a, ident, record. Outputs/bindings: a.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered ListComp evaluation at root.body[11].body[3].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[3].body[3].body[2]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:79`; AST `c935a24c37b07acc4025897da5181f8b7d3c77f9441b7c12a4a152631ff94abd`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, matches, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[3].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[3].body[3].body[2].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:79`; AST `de82ae7288f3fd876110c4e92da5000b0ea5d5ba25e3a8517d7f9303460023b5`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, matches, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[3].body[3].body[2].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:79`; AST `d97f989b8f8f52f8f40688f8e2e1ccaded6f1cf09b4ecf82beecbcc52f1add97`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, matches. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[3].body[2].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[3].body[3].body[3]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:80`; AST `0f4b708072d6f39d8bad5eeee9b8aae8cd819c102d475c75587e7c1abcf8fef8`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: matches, outcome, receipt. Outputs/bindings: (none).
Calls/effect boundaries: matches[0].update.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[3].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[3].body[3].body[3].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:80`; AST `cb028ee3c04d26ae7e343a0dc5e10609863db082fbd882336a75457d2a94abd4`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: matches, outcome, receipt. Outputs/bindings: (none).
Calls/effect boundaries: matches[0].update.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[3].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[3].body[3].body[4]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:81`; AST `39653ba93071c48ea5664f41495c0b9b4c456ea6c7027a39f271248d5232ec2e`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_json, record, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[3].body[3].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[3].body[3].body[4].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:81`; AST `e0ebb6df18f3acd72b73864198de1922264a5591e4adfd3e452231c9bafa9477`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_json, record, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[3].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[3].body[3].finalbody[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:83`; AST `9aa6f04fc26ee6b3f6fe1a19158adb3cfde13709dcae4a7cc38bccbb2655afb2`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[3].body[3].finalbody[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[3].body[3].finalbody[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:83`; AST `107c5710331db61e695f7d71256d48862412d15c223e204da5c71c497352b634`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[3].finalbody[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[4]::FunctionDef

Source: `infra/agentinfra/roadmap_runtime.py:85`; AST `b8988c51b7d7a53490248f93800853b5f44fcc82b008cb8f82c28ba23016390c`.

Rust module: `infra::agentinfra::roadmap_runtime`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileLock, atomic_write_json, bool, dict, event_id, int, lock, record, require, self, str, thread_id, total, type, usage. Outputs/bindings: lock, record, usage.
Calls/effect boundaries: FileLock, atomic_write_json, bool, dict, lock.acquire, lock.release, record['usage'].setdefault, require, self.read, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[4].body[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:86`; AST `d799aa76aac235aa02ea343eccecffec1ff0d53ba52ac1e7d2c1fd14f0e671dd`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, event_id, require, thread_id. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[4].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:86`; AST `7a7e76fa5fef3d1ac92cecef7d9e90dcfe3407cc73ec42a8e5a100666799d554`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, event_id, require, thread_id. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[4].body[0].value.args[0].values[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:86`; AST `cd37e63e8c7eb3c36062f0fbd5dd0ea6964ef29927b2cb95206c3f8060580755`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, thread_id. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[0].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[4].body[0].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_runtime.py:86`; AST `3e92731226f2b51f589da08be39a33e83d597c14fea7e4556613d9a1dbb6d9df`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, event_id. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[0].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[4].body[1]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:87`; AST `14b97e4ba59e30f94a1512f471f04d4ec3ccbeb29ff7bd9cbd1fc2984a90b4c3`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: int, require, total, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[4].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:87`; AST `8f04bdc286ac29f86b50442445b003106f8399a69d6e800a1e7f93573a83cf9b`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: int, require, total, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[4].body[1].value.args[0].values[1].values[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:87`; AST `1640c40c7f3e5652b4ce485094324d24b71d11f477d89f9370054dc8ab0bcd46`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: total, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[1].value.args[0].values[1].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[4].body[2]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:88`; AST `0b9cf3f582006dcd9e3bada572669897fb941f81c22a91048b7cca986626b4c6`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileLock, self. Outputs/bindings: lock.
Calls/effect boundaries: FileLock.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[4].body[2].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:88`; AST `1ee904a2b41404877314b19cf7f0fb6745c76928d8915a51a07c5bcae2fc445b`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileLock, self. Outputs/bindings: (none).
Calls/effect boundaries: FileLock.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[4].body[3]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:89`; AST `2bcfe51cf785ee29160140309ca2724ded506c99a694a1cd40da99965fea32f6`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[4].body[3].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:89`; AST `19f113b1ff996d6a4e1349d4f629dcb1414895f291ae11a26e3a1c7c22771cf0`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[4].body[4]::Try

Source: `infra/agentinfra/roadmap_runtime.py:90`; AST `b121de3fb58456afcb4ffbd65c983c50cdcd461c971cf0aff578440c215bf020`.

Rust module: `infra::agentinfra::roadmap_runtime`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: atomic_write_json, dict, event_id, lock, record, require, self, thread_id, total, usage. Outputs/bindings: record, usage.
Calls/effect boundaries: atomic_write_json, dict, lock.release, record['usage'].setdefault, require, self.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Try evaluation at root.body[11].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[4].body[4].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:91`; AST `8d60c6cf06a37f3a21e36d8d4fc569b1d94d00284e5e8e23781c46e0c0bd8c8b`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: record.
Calls/effect boundaries: self.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[4].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[4].body[4].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:91`; AST `1a6cd88d33383d245bb90e4e5f924f99f090d6bd29a5c43fab9e8ffb18d19d91`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[4].body[4].body[1]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:92`; AST `53bcfe909acdecf6389bd1ec4c4194257682702a9c37e4bc185120110b090989`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record, thread_id. Outputs/bindings: usage.
Calls/effect boundaries: record['usage'].setdefault.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[4].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[4].body[4].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:92`; AST `c0683907ccda314c861f238c211afc4a1f6ffa70db9f0eec029d1943eea1cf53`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record, thread_id. Outputs/bindings: (none).
Calls/effect boundaries: record['usage'].setdefault.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[4].body[4].body[2]::If

Source: `infra/agentinfra/roadmap_runtime.py:93`; AST `f95034d2c8b7eddab9655cc09d7884575c3cab03b52aa5a65da00e05be414c70`.

Rust module: `infra::agentinfra::roadmap_runtime`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: dict, event_id, require, total, usage. Outputs/bindings: (none).
Calls/effect boundaries: dict, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered If evaluation at root.body[11].body[4].body[4].body[2]; no call, error or mutation may be omitted. Condition: event_id in usage['events']
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[4].body[4].body[2].body[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:94`; AST `484a0b9533eae32c71b66c3caa85840f528e80dcd574fccc269e6baaacb62e26`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: event_id, require, total, usage. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[4].body[4].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[4].body[4].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:94`; AST `da3bc31a4b596450a77443fae97fb81fa21166358bacc378bf3de03da2e64dca`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: event_id, require, total, usage. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[4].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[4].body[4].body[2].body[1]::Return

Source: `infra/agentinfra/roadmap_runtime.py:95`; AST `ed4cf45c6dc70c8fd8da13a6e0eb8b23a7689f702082e00fd2f5f8e1f0a5d564`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, usage. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Return evaluation at root.body[11].body[4].body[4].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[4].body[4].body[2].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:95`; AST `8aa055a140fab9cf553e1183c53bfb2f0a5f5f655a93319e930a19ab5441ec68`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, usage. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[4].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[4].body[4].body[3]::If

Source: `infra/agentinfra/roadmap_runtime.py:96`; AST `fd88db75cca5888054eec9b4dc2fbe9b4c86f0df9f90dd1bc7af64af556d2203`.

Rust module: `infra::agentinfra::roadmap_runtime`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: require, total, usage. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered If evaluation at root.body[11].body[4].body[4].body[3]; no call, error or mutation may be omitted. Condition: total is not None and usage['total'] is not None
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[4].body[4].body[3].body[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:97`; AST `7240208a29b2feed1eacad1baabf2a3aa383374c146443d08cbe86c0bf715e8a`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, total, usage. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[4].body[4].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[4].body[4].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:97`; AST `5367338754edeaa70ab6f211df26af7f7f60033e003adad9fc20c0442e9e72af`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, total, usage. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[4].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[4].body[4].body[4]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:98`; AST `36582a4e64162a0874bb43073f8717673f192fd5194a277fa45ec1dd702621ed`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: event_id, total, usage. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[4].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[4].body[4].body[5]::If

Source: `infra/agentinfra/roadmap_runtime.py:99`; AST `937e3ed71edcc16e8369c8af6d5fdb221cd8e1f6175bfbb3f8631273ffd9358c`.

Rust module: `infra::agentinfra::roadmap_runtime`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: total, usage. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered If evaluation at root.body[11].body[4].body[4].body[5]; no call, error or mutation may be omitted. Condition: total is not None
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[4].body[4].body[5].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:100`; AST `fa966965debf4352b7ebfad6de6eb7f1cc1332c3f908442bd356ef0538f4f010`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: total, usage. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[4].body[4].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[4].body[4].body[6]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:101`; AST `39653ba93071c48ea5664f41495c0b9b4c456ea6c7027a39f271248d5232ec2e`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_json, record, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[4].body[4].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[4].body[4].body[6].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:101`; AST `e0ebb6df18f3acd72b73864198de1922264a5591e4adfd3e452231c9bafa9477`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_json, record, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[4].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[4].body[4].body[7]::Return

Source: `infra/agentinfra/roadmap_runtime.py:102`; AST `ed4cf45c6dc70c8fd8da13a6e0eb8b23a7689f702082e00fd2f5f8e1f0a5d564`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, usage. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Return evaluation at root.body[11].body[4].body[4].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[4].body[4].body[7].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:102`; AST `8aa055a140fab9cf553e1183c53bfb2f0a5f5f655a93319e930a19ab5441ec68`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, usage. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[4].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[4].body[4].finalbody[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:104`; AST `9aa6f04fc26ee6b3f6fe1a19158adb3cfde13709dcae4a7cc38bccbb2655afb2`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[4].body[4].finalbody[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[4].body[4].finalbody[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:104`; AST `107c5710331db61e695f7d71256d48862412d15c223e204da5c71c497352b634`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[4].finalbody[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12]::FunctionDef

Source: `infra/agentinfra/roadmap_runtime.py:107`; AST `0907c88c9295fde650f1b40f99a88539cf5120ba8aca0f56e2e2f3a74c156f22`.

Rust module: `infra::agentinfra::roadmap_runtime`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: BudgetLedger, Path, WorkspaceLease, a, binding, bool, compiled, confined_path, created, dict, digest, execution, goal, inherited, int, ledger, legacy, milestone, name, owner, path, read_json, record, require, root, str, thread, tuple, type, work_id. Outputs/bindings: a, binding, created, execution, goal, inherited, legacy, owner, path, record, thread, work_id.
Calls/effect boundaries: WorkspaceLease, WorkspaceLease(root).assert_owner, binding.get, bool, confined_path, digest, execution.get, goal.get, ledger.read, owner.get, read_json, record.get, record.get('continuation', {}).get, require, root.resolve, str, tuple, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:109`; AST `c910188bbd8095f6d234ec9dbb428e32c461b7503d757b1237c8553c2d658883`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[1]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:115`; AST `ff9f7b1b452102574abcb790996ad6100d1ccab24369011a20b807cccd708747`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, milestone, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:115`; AST `c30870bb21ab81837e0b5463012d6133048f1b2dd4100c7411488f762eec09c5`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, milestone, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[2]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:117`; AST `98864eb91502cf19dee35a57c3507c393eb56db4f8cf7bc4f7f63ba19c8ca39c`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, confined_path, root. Outputs/bindings: path.
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[2].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:117`; AST `2411f310ac43c2b4f3c2fac8d1128047c8324665b56e941312032bf564cf1f15`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, confined_path, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[3]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:118`; AST `4c0b40719bd50d8d610b5ba0ec593936db79742bfd3484eeea858809f2b40c7c`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path, read_json. Outputs/bindings: record.
Calls/effect boundaries: read_json.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[3].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:118`; AST `ca2a99ec0b14545aba864c1e6b22415e5a02ad33955de7320b863aa9c805bfcd`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[4]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:119`; AST `f85869b980d0fb25741330a8c16a670c3cb260eb9bce0361055e2192bfba69b1`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record. Outputs/bindings: execution.
Calls/effect boundaries: record.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[4].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:119`; AST `94f294c41d79480919f0ce6955c328ecffa9d2fc269e74d3e6fc9cebeec917d7`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[5]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:120`; AST `8d966d61e8f4fe7fb915b27fb56de3eb1cea5416f6e3c84de1a6bca872634ea8`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: execution. Outputs/bindings: binding.
Calls/effect boundaries: execution.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[5].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:120`; AST `9d07ed4a2c148f4183b707ac830e883b5c33ba96dcd1e134c547f727d92f1312`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: execution. Outputs/bindings: (none).
Calls/effect boundaries: execution.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[6]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:121`; AST `81aca9f5503557b417bc2af78ce8ee8f28bfac449823a648264eb5c819cb7058`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding. Outputs/bindings: goal.
Calls/effect boundaries: binding.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[6].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:121`; AST `19383d3c3a3dd141414e57358091030cb5d155331564962bc5d64e9d2fdca72d`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding. Outputs/bindings: (none).
Calls/effect boundaries: binding.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[7]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:122`; AST `1bfbe0ef6c55dac79248d6cf6e8a349b807d555eade36f876c2a51d6251838a4`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding. Outputs/bindings: thread.
Calls/effect boundaries: binding.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[7].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:122`; AST `63111ba26343241a333d0933cf221435534ec16270d2f49ca57741efb6c4fa1a`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding. Outputs/bindings: (none).
Calls/effect boundaries: binding.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[8]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:123`; AST `670f85d57e1bdbc688d11ba038b5b0b280a41be277563aab1f56458926493883`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, record, require, thread. Outputs/bindings: (none).
Calls/effect boundaries: bool, record.get, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[8].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:123`; AST `6790f037a1a462e1b3ff443660ef5986ded14386843de4e9cfae6a77ca1c92d8`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, record, require, thread. Outputs/bindings: (none).
Calls/effect boundaries: bool, record.get, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[8].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:123`; AST `d1e3876e5f2eab25e6fd365f06eea6e829f195ef666744ac41314682d8aa382c`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[8].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:123`; AST `d0a98983fb019a589d6e758de84d4e0770904ddc3da7d42d506d12396e7ac5ca`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[8].value.args[0].values[2]::Call

Source: `infra/agentinfra/roadmap_runtime.py:123`; AST `7e7f2dee89ebf969b2a85e0869a13de1e700211ebbda1457205ac01cdc2be0d6`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, thread. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].value.args[0].values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[9]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:125`; AST `b5ea1ed7d44eb5365847be873b1be6f5d852826ef4d5bc2dd5bb187572261f46`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, goal, require, thread. Outputs/bindings: (none).
Calls/effect boundaries: binding.get, goal.get, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[9].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:125`; AST `7c1fce64522b83aa1ef05efcb510f0473b02f82cc49876f065584e02c5b69316`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, goal, require, thread. Outputs/bindings: (none).
Calls/effect boundaries: binding.get, goal.get, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[9].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:125`; AST `8882eb7d5b9f4dc8d2105e4953998c448940325a4f4149b97780ded2830a8ee0`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: goal. Outputs/bindings: (none).
Calls/effect boundaries: goal.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[9].value.args[0].values[0].left.args[1]::Call

Source: `infra/agentinfra/roadmap_runtime.py:125`; AST `12a3aafb86d4ac1fabfccdf44687ff589a7892691f5c30c1ec9f07c0e05a13a9`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: goal. Outputs/bindings: (none).
Calls/effect boundaries: goal.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].value.args[0].values[0].left.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[9].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:126`; AST `f63919515d3be4b4c9952f900298cbf76eac49214dedb5f1b96049934fdc731c`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: goal. Outputs/bindings: (none).
Calls/effect boundaries: goal.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[9].value.args[0].values[1].comparators[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:126`; AST `c52ca19c779f5d2a2be4d6e23e8b381a8637c14e49af2b3c39e5bc3ee9359726`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding. Outputs/bindings: (none).
Calls/effect boundaries: binding.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].value.args[0].values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[9].value.args[0].values[2].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:126`; AST `337340fc2dab2135d3885d03c2bb3040fb953c98284ab395c2e6270568db0732`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: goal. Outputs/bindings: (none).
Calls/effect boundaries: goal.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].value.args[0].values[2].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[10]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:128`; AST `9377717ec93ed8c020444988585590b402d03e35300a9e9fa96e3d56a32d1db1`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: execution, milestone, record, require. Outputs/bindings: (none).
Calls/effect boundaries: execution.get, record.get, record.get('continuation', {}).get, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[10].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:128`; AST `9655c5614735abcceb8388fa2b7ed79314d01058096c7c54ed725aadbafbf009`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: execution, milestone, record, require. Outputs/bindings: (none).
Calls/effect boundaries: execution.get, record.get, record.get('continuation', {}).get, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[10].value.args[0].values[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:128`; AST `1d5906c7d6a9e7173e4d5a4677d17ccaba7c71a291cbd487f007d0688de2e211`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: execution. Outputs/bindings: (none).
Calls/effect boundaries: execution.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[10].value.args[0].values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[10].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:129`; AST `1aea51f75485f4d54384e4db631d258f848ec6cbf9df2e80a998ff4773159220`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get, record.get('continuation', {}).get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[10].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[10].value.args[0].values[1].left.func.value::Call

Source: `infra/agentinfra/roadmap_runtime.py:129`; AST `1ac6954672b3424f66695dffe4f844ab9e9cd657bb68329edc66a49dd7cb68ef`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[10].value.args[0].values[1].left.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[11]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:131`; AST `3143d476a50e13911b81b08cc9f4475a21e61266a736348376774270436548e6`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: execution. Outputs/bindings: owner.
Calls/effect boundaries: execution.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[11].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:131`; AST `94ea54adee6fc3e52b8da6da4b7ad4c1f66ad0fe66dcebf5eb64a5f9b2021753`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: execution. Outputs/bindings: (none).
Calls/effect boundaries: execution.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[12]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:132`; AST `94fb5a4b0b19866046013ceb8513e8e312b6239a7ba70b0dff8ddc098cad53f9`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: owner, require, thread. Outputs/bindings: (none).
Calls/effect boundaries: owner.get, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[12].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:132`; AST `d8f75e204e7e55c4c238dd2cdb95826db72f8621abdd77a4eca34ffeb32d8c08`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: owner, require, thread. Outputs/bindings: (none).
Calls/effect boundaries: owner.get, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[12].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:132`; AST `27a5b1552929f691a509884265ca66d93c6c63ccce4de6833fab9a141246c47e`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: owner. Outputs/bindings: (none).
Calls/effect boundaries: owner.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[13]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:133`; AST `d4f115f3a1ad13c15b35dda40721d4df4ac6110395a36304743f1f1998f1e3e3`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: WorkspaceLease, owner, root. Outputs/bindings: (none).
Calls/effect boundaries: WorkspaceLease, WorkspaceLease(root).assert_owner.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[13].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:133`; AST `5a4a7c71898511257607db7d7a64df8ed53c585d29a5b177b02e48bd76fcf6cd`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: WorkspaceLease, owner, root. Outputs/bindings: (none).
Calls/effect boundaries: WorkspaceLease, WorkspaceLease(root).assert_owner.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[13].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[13].value.func.value::Call

Source: `infra/agentinfra/roadmap_runtime.py:133`; AST `9af565e67ae5d334b545886bccb7b0f27fb8d8189b6644c9267610cbdb6cc4e6`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: WorkspaceLease, root. Outputs/bindings: (none).
Calls/effect boundaries: WorkspaceLease.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[13].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[14]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:134`; AST `08ea25a29f190448894e8c3ac615107a7281aea1743f7d9049a43f3034b37171`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: goal. Outputs/bindings: created.
Calls/effect boundaries: goal.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[14].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:134`; AST `6e765ad33f07a626e8e18db3f67a6201ab9cca3273e1f1bacbe3598ea77e0560`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: goal. Outputs/bindings: (none).
Calls/effect boundaries: goal.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[14].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[15]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:135`; AST `cda1666fd0a2b75d6946c9dae6b009b075b76c788e4e6e427dc26ab78720088c`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: created, int, require, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[15].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:135`; AST `1f67d94fdffb4fd139933c6ca4d5445d2d55b02fa48a1de43bb52d47390ab90c`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: created, int, require, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[15].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[15].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:135`; AST `c93741fd485e081b9a072bcb6670c7fcd7e5f8a44d89568b247c54f81e9eb10e`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: created, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[15].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[16]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:136`; AST `ebe2eff0a25d1a7a307f4c4751c0ec0219e2b07df5fa51edddb8c462a82cdabc`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, name, root, str. Outputs/bindings: legacy.
Calls/effect boundaries: digest, root.resolve, str.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[16]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[16].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:136`; AST `f7eeffad6fe75979b2f5cb21e3b6559a00b62c457e1203bd148a7d8627d441bc`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, name, root, str. Outputs/bindings: (none).
Calls/effect boundaries: digest, root.resolve, str.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[16].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[16].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_runtime.py:136`; AST `29d0b5a674124d6a5dea0e9d83c547c4cebd29502709afd03c4659bd6afedfda`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, str. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve, str.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[16].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[16].value.args[0].values[1].args[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:136`; AST `b97f3f463d4724206af2869ad4674d5eb373167f052507971a722ecc8f771a87`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[16].value.args[0].values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[17]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:137`; AST `74e83e98d1b46f4ddce087c83ea8a08ef0343259275ac623c36dd068bc77c512`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, created, ledger, legacy, tuple. Outputs/bindings: a, inherited.
Calls/effect boundaries: ledger.read, tuple.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[17]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[17].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:137`; AST `a4d8355af21780780f5937201bab9dfdd102ff61ce0c3e8f7ce41cf05700bacc`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, created, ledger, legacy, tuple. Outputs/bindings: a.
Calls/effect boundaries: ledger.read, tuple.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[17].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[17].value.args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_runtime.py:137`; AST `92f19097aff4d6fe72e8842d7ba277b276bf1497b87a08e0d6ec46939dc8a9ca`.

Rust module: `infra::agentinfra::roadmap_runtime`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: a, created, ledger, legacy. Outputs/bindings: a.
Calls/effect boundaries: ledger.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[12].body[17].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[17].value.args[0].generators[0].iter.value::Call

Source: `infra/agentinfra/roadmap_runtime.py:137`; AST `97bf15ee0985708addfb91473f1c9a324eb4e700d9a5a949145f8b93d423dbb2`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ledger. Outputs/bindings: (none).
Calls/effect boundaries: ledger.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[17].value.args[0].generators[0].iter.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[18]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:139`; AST `5a0b6ed7782b94b1d816d0b41c12a58b363c43f2210841b200e764786aaf5cb9`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, milestone, name, root, str, thread. Outputs/bindings: work_id.
Calls/effect boundaries: digest, root.resolve, str.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[18]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[18].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:139`; AST `24680cdf1228574942ffbd96b0a4fd3d4c307117247286b73c1e1e9e939121d5`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, milestone, name, root, str, thread. Outputs/bindings: (none).
Calls/effect boundaries: digest, root.resolve, str.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[18].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[18].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_runtime.py:139`; AST `29d0b5a674124d6a5dea0e9d83c547c4cebd29502709afd03c4659bd6afedfda`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, str. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve, str.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[18].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[18].value.args[0].values[1].args[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:139`; AST `b97f3f463d4724206af2869ad4674d5eb373167f052507971a722ecc8f771a87`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[18].value.args[0].values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[19]::Return

Source: `infra/agentinfra/roadmap_runtime.py:141`; AST `bff89ddc70c5bebfa0eb7473c4c0fb168cf8c9b67e526c11da8cb835bbf64988`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: inherited, work_id. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Return evaluation at root.body[12].body[19]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13]::FunctionDef

Source: `infra/agentinfra/roadmap_runtime.py:144`; AST `cb418c57ebbea5c9aef4bb34a4ba1d0ca5183e72f339a4170f45173442107556`.

Rust module: `infra::agentinfra::roadmap_runtime`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: BaseException, BudgetLedger, FileLock, Path, all, argv, attempt, bindings_current, compiled, diagnosis, dict, digest, exc, inherited, inputs, lease, ledger, milestone, name, ok, receipt, recipe, recipe_scope, require, result, root, run_process, str, sys, type, work_id, x. Outputs/bindings: argv, attempt, inherited, inputs, lease, ledger, ok, receipt, recipe, result, work_id, x.
Calls/effect boundaries: BudgetLedger, FileLock, all, bindings_current, digest, lease.acquire, lease.release, ledger.close, ledger.reserve, recipe_scope, require, root.resolve, run_process, str, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:146`; AST `7134076064ca0cc4d6e8bf0df750033455986c45bc4b76108df1e6dd0cf012c7`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bindings_current, compiled, require, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:146`; AST `1d48ed543f544738992ff8b01172556e0ebe3c3346236bdb93934a175388b6c2`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, compiled, require, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:146`; AST `e4376bee10cb5ac58b23e27129b2002e1436b91face64325fcbf8a25771ff8e7`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, compiled, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[1]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:147`; AST `64512de268c5e817df30e7dca1f869aa9c2f31bb9f799a4ff54f0f3e6e494ed7`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, name, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:147`; AST `f78b579b3faa4cc54919bab290adc167932d4b19443dc0853a3b15b21d976cd1`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, name, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[2]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:148`; AST `c6946d992b569719baf8f6b5caeb8843502d56201decee935602a5fe529eba20`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, name. Outputs/bindings: recipe.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[3]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:149`; AST `bc654dbdf9dc5d5642492c41db899552c7f4c7751c6afb9c6138c540f14e0b5a`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: recipe, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[3].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:149`; AST `a15b695faca3256151950dce380c567c0ddb44509ee8a90a9a4e5da25477da06`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: recipe, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[4]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:150`; AST `47b5483b8dd8c381357e24a91032e49c14e8bb5d54ab7923954fdc61efa65649`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: recipe, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[4].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:150`; AST `65aae1c63a647ddbd3502e80205255c1f34e7bca29d35a6c04d8569e8709a5b8`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: recipe, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[5]::Import

Source: `infra/agentinfra/roadmap_runtime.py:151`; AST `f7252e3c1dbe1d5edf1f34c020a58a05b55f706b2c1d9479eae91f9a9d4be275`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Import evaluation at root.body[13].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[6]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:152`; AST `bd9f0f903210947bab774fb108d0c04706d914d59dbd173b0f83f401833a58f0`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: recipe, sys. Outputs/bindings: argv.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[7]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:153`; AST `9d15bb663bddd8cd5cf54a2049a1c82786ab59c32dea73de26fc4cc6e075d1fc`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, argv, require, str, type, x. Outputs/bindings: x.
Calls/effect boundaries: all, require, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[7].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:153`; AST `ca3fb39a85567145d1afae50e4530911662b551f34ac0aad3bcf79f6173bbe24`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, argv, require, str, type, x. Outputs/bindings: x.
Calls/effect boundaries: all, require, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[7].value.args[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:153`; AST `d6765e1f20fcaba0aaeb5595c25d6f47549b94b17938afeeff50e3e72dd87a07`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, argv, str, type, x. Outputs/bindings: x.
Calls/effect boundaries: all, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[7].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[7].value.args[0].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_runtime.py:153`; AST `a43f75bc33ab7a6b7a51cd0aaefe0b517dd36234fa7c8cc09a694d49c78a7a5b`.

Rust module: `infra::agentinfra::roadmap_runtime`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: argv, str, type, x. Outputs/bindings: x.
Calls/effect boundaries: type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[13].body[7].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[7].value.args[0].args[0].elt.left::Call

Source: `infra/agentinfra/roadmap_runtime.py:153`; AST `617245833c9319194f50c6c77baf6916a03ab26dba6a12037ebc1d090f9aebc1`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: type, x. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[7].value.args[0].args[0].elt.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[8]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:154`; AST `67675058a01e0dda8539105929316e0f5649ff01f4106b07914385a579da4201`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, name, root, str. Outputs/bindings: work_id.
Calls/effect boundaries: digest, root.resolve, str.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[8].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:154`; AST `f7eeffad6fe75979b2f5cb21e3b6559a00b62c457e1203bd148a7d8627d441bc`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, name, root, str. Outputs/bindings: (none).
Calls/effect boundaries: digest, root.resolve, str.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[8].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_runtime.py:154`; AST `29d0b5a674124d6a5dea0e9d83c547c4cebd29502709afd03c4659bd6afedfda`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, str. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve, str.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[8].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[8].value.args[0].values[1].args[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:154`; AST `b97f3f463d4724206af2869ad4674d5eb373167f052507971a722ecc8f771a87`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[8].value.args[0].values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[9]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:155`; AST `421b4ed54537fb53288819ed5abaadfbafffa5592ae161b204a201c761a61d4f`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, digest, recipe. Outputs/bindings: inputs.
Calls/effect boundaries: digest.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[9].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:155`; AST `d15b0e2a60dd0d87c5cc653cbf29a5f306cf7cdea9849c6143dc86aaddbcbd0f`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, digest, recipe. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[10]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:156`; AST `dc2fd1ede60c6438c487511f87ef8eedec8bb87e6ab3d1c5380ff1542be015c2`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: BudgetLedger, root. Outputs/bindings: ledger.
Calls/effect boundaries: BudgetLedger.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[10].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:156`; AST `df43247d3e9a1323119ce795d3f01353dada1c7e238477cf98ed400282fae762`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: BudgetLedger, root. Outputs/bindings: (none).
Calls/effect boundaries: BudgetLedger.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[11]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:157`; AST `f660ab2bd95658c14df241f1bbb042167648bb05826f783cee716951874d9515`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: inherited.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[12]::If

Source: `infra/agentinfra/roadmap_runtime.py:158`; AST `fe7402ebbcb0bdc8a44df0e4cca392c7b97970397493aa99bd3bed8bb3725e2f`.

Rust module: `infra::agentinfra::roadmap_runtime`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: compiled, ledger, milestone, name, recipe_scope, root. Outputs/bindings: inherited, work_id.
Calls/effect boundaries: recipe_scope.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered If evaluation at root.body[13].body[12]; no call, error or mutation may be omitted. Condition: milestone is not None
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[12].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:159`; AST `d87826eb1b04270e73f7665e1d9e591c788d03f29f0dfe7ee46c25a928574981`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, ledger, milestone, name, recipe_scope, root. Outputs/bindings: inherited, work_id.
Calls/effect boundaries: recipe_scope.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[12].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:159`; AST `73e9e400e7be5a602f49c4f0a53aa44a582e18f2d936c52beddbd466beeb7643`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, ledger, milestone, name, recipe_scope, root. Outputs/bindings: (none).
Calls/effect boundaries: recipe_scope.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[12].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[13]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:160`; AST `597e7c835018aa2ba95b6ca1c6f8fe786ba07ed685b28372355548e344eaf445`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileLock, root. Outputs/bindings: lease.
Calls/effect boundaries: FileLock.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[13].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:160`; AST `8e00a4bc7d740dc3d04edfbd16ad1f6b400e1685b98654a9adfa0c6508d54b7e`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileLock, root. Outputs/bindings: (none).
Calls/effect boundaries: FileLock.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[13].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[14]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:161`; AST `4d8ec1b6a1b7605da659d3bd4a58e87305084395ac03de474edc83b70229037c`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lease. Outputs/bindings: (none).
Calls/effect boundaries: lease.acquire.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[14].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:161`; AST `90f35c2c815c72014528f6ee0b25d0d929a0b3c33c0fc7577df4a90ffada1455`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lease. Outputs/bindings: (none).
Calls/effect boundaries: lease.acquire.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[14].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[15]::Try

Source: `infra/agentinfra/roadmap_runtime.py:162`; AST `f64d6ccdba88fcef230737c46531ac6412674fd7f52da402af0eb805b7a14f86`.

Rust module: `infra::agentinfra::roadmap_runtime`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: BaseException, argv, attempt, diagnosis, exc, inherited, inputs, lease, ledger, name, ok, receipt, recipe, result, root, run_process, type, work_id. Outputs/bindings: attempt, ok, receipt, result.
Calls/effect boundaries: lease.release, ledger.close, ledger.reserve, run_process, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Try evaluation at root.body[13].body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[15].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:163`; AST `128797a7ce36658b329d866c778dd19e3a478d826cce7fcf992545a7f80df09d`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: diagnosis, inherited, inputs, ledger, recipe, work_id. Outputs/bindings: attempt.
Calls/effect boundaries: ledger.reserve.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[15].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[15].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:163`; AST `2415374867cea1bb0a0e65d554f08af972d842a8cc384ab877d1bce14a8cabe9`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: diagnosis, inherited, inputs, ledger, recipe, work_id. Outputs/bindings: (none).
Calls/effect boundaries: ledger.reserve.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[15].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[15].body[1]::Try

Source: `infra/agentinfra/roadmap_runtime.py:166`; AST `2451bce5b4525e15091e68b91e30fa1263fa937933c8a6e7ad5b81052d1f67fc`.

Rust module: `infra::agentinfra::roadmap_runtime`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: BaseException, argv, attempt, exc, inputs, ledger, name, receipt, recipe, result, root, run_process, type. Outputs/bindings: ok, receipt, result.
Calls/effect boundaries: ledger.close, run_process, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Try evaluation at root.body[13].body[15].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[15].body[1].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:167`; AST `5a0a77f443015c25fb8751ff10f33eee995c10fdff134b88b0b44294ad25cb72`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: argv, recipe, root, run_process. Outputs/bindings: result.
Calls/effect boundaries: run_process.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[15].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[15].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:167`; AST `53ff285d5a6f1859d9a7882f6bf78e46dd8216eca3e679bb4cbcdd892fad0866`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: argv, recipe, root, run_process. Outputs/bindings: (none).
Calls/effect boundaries: run_process.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[15].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[15].body[1].body[1]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:168`; AST `2ecbedbd535378ec6e7aa60591b5cafbe87157cfc95e326e92756d72a4d6fd8a`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: argv, inputs, name, result. Outputs/bindings: receipt.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[15].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[15].body[1].body[2]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:172`; AST `b3c1299d30e6607bcfab32352f143a6d494b3a2bcac40a557b7dd1dedbda2b87`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: receipt, result. Outputs/bindings: ok.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[15].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[15].body[1].handlers[0]::ExceptHandler

Source: `infra/agentinfra/roadmap_runtime.py:173`; AST `0693a57bcc28ef82b3a434a4fa88b3109998a167dc0b84fa396ce0f50de3b96b`.

Rust module: `infra::agentinfra::roadmap_runtime`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: BaseException, attempt, exc, ledger, type. Outputs/bindings: (none).
Calls/effect boundaries: ledger.close, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[13].body[15].body[1].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[15].body[1].handlers[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:174`; AST `32155c72452559d63d8f166d88319d50af3edf755312f1917accaffbb9d251a5`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: attempt, exc, ledger, type. Outputs/bindings: (none).
Calls/effect boundaries: ledger.close, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[15].body[1].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[15].body[1].handlers[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:174`; AST `503cdb75c1796ab3efdee8d8c0d1ab0dbb2c3af0eb5a6f4cc156b8cd12b331ce`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: attempt, exc, ledger, type. Outputs/bindings: (none).
Calls/effect boundaries: ledger.close, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[15].body[1].handlers[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[15].body[1].handlers[0].body[0].value.args[2].values[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:174`; AST `760fdaff1a05c24c8db8bb1ee0c475c11403d48d9ac9c89ec3c062a1494d5d01`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exc, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[15].body[1].handlers[0].body[0].value.args[2].values[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[15].body[1].handlers[0].body[1]::Raise

Source: `infra/agentinfra/roadmap_runtime.py:175`; AST `ba28128c14dfbd0a9062c0dbab42ad6c52ecf0767df6b67576deb1dbbfdd038d`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Raise evaluation at root.body[13].body[15].body[1].handlers[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[15].body[2]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:176`; AST `d3ab36aeed6f03c0c0b1c9d0fb3ca3ba46a4352d5213c05626289b873c0660fd`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: attempt, ledger, ok, receipt. Outputs/bindings: (none).
Calls/effect boundaries: ledger.close.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[15].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[15].body[2].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:176`; AST `7d777545a191c38a43e7ca2aacc371afcf72fabb4f51fdc2087475a41ac96c69`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: attempt, ledger, ok, receipt. Outputs/bindings: (none).
Calls/effect boundaries: ledger.close.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[15].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[15].body[3]::Return

Source: `infra/agentinfra/roadmap_runtime.py:177`; AST `9b378eb582403574e9c02456d9dbe8d3ccc96e049aa98ec3ceee97d8b1bff879`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: receipt. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Return evaluation at root.body[13].body[15].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[15].finalbody[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:179`; AST `0324b3e2db1ff1d21a06b04c85a991b516c3896842973d7f654860c5b366eef9`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lease. Outputs/bindings: (none).
Calls/effect boundaries: lease.release.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[15].finalbody[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[15].finalbody[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:179`; AST `048afd42289a938d53fdcdbe01fdbf0cfa61c1cf67318f7be9b504d14956c5cf`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lease. Outputs/bindings: (none).
Calls/effect boundaries: lease.release.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[15].finalbody[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
