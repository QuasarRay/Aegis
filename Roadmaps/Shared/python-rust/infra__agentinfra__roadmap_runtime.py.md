# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 190. Inventory digest: `970c3eadcf96469c0e1ea5385a7613f9f4554a12e8d99756e064ea632c0e48ad`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/roadmap_runtime.py::module::root::Module

Source: `infra/agentinfra/roadmap_runtime.py:1`; AST `6f7d54ee2e2678434ab637414879a916825ca42d881f30578c6356a024d281a3`.

Rust module: `infra::agentinfra::roadmap_runtime`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: BaseException, BudgetLedger, FileLock, Path, a, all, any, argv, atomic_write_json, attempt, bindings_current, bool, compiled, confined_path, diagnosis, dict, digest, event_id, exc, ident, inputs, int, isinstance, lease, ledger, len, list, lock, matches, max_attempts, name, ok, os, outcome, prior, read_json, receipt, recipe, record, require, result, root, run_process, seconds, self, str, sum, sys, thread_id, time, total, total_seconds, type, usage, work_id, x. Outputs/bindings: a, argv, attempt, inputs, lease, ledger, lock, matches, ok, prior, receipt, recipe, record, result, usage, work_id, x.
Calls/effect boundaries: BudgetLedger, FileLock, all, any, atomic_write_json, bindings_current, bool, confined_path, diagnosis.strip, dict, digest, isinstance, lease.acquire, lease.release, ledger.close, ledger.reserve, len, lock.acquire, lock.release, matches[0].update, os.getpid, read_json, record.get, record['attempts'].append, record['usage'].setdefault, require, root.resolve, run_process, self.path.exists, self.path.with_suffix, self.read, str, sum, time.time_ns, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered ImportFrom evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::root.body[10]::ClassDef

Source: `infra/agentinfra/roadmap_runtime.py:15`; AST `0464e5b394702bdc09a8d193f294762b680e06b5d902fa96bd491aa2bebbc73f`.

Rust module: `infra::agentinfra::roadmap_runtime`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: FileLock, Path, a, any, atomic_write_json, attempt, bool, confined_path, diagnosis, dict, digest, event_id, ident, inputs, int, isinstance, len, list, lock, matches, max_attempts, os, outcome, prior, read_json, receipt, record, require, root, seconds, self, str, sum, thread_id, time, total, total_seconds, type, usage, work_id. Outputs/bindings: a, attempt, lock, matches, prior, record, usage.
Calls/effect boundaries: FileLock, any, atomic_write_json, bool, confined_path, diagnosis.strip, dict, digest, isinstance, len, lock.acquire, lock.release, matches[0].update, os.getpid, read_json, record.get, record['attempts'].append, record['usage'].setdefault, require, root.resolve, self.path.exists, self.path.with_suffix, self.read, sum, time.time_ns, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered ClassDef evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::__init__::root.body[10].body[0]::FunctionDef

Source: `infra/agentinfra/roadmap_runtime.py:16`; AST `9bb02373b582dc831e70fc4fa4cd90792c32e6d8e0d7785e08df726578a682dd`.

Rust module: `infra::agentinfra::roadmap_runtime`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, confined_path, root, self. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, root.resolve, self.path.with_suffix.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::__init__::root.body[10].body[0].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:17`; AST `eac70191d36cd330a975a12be514d4a5f58088087cc2acfa2746cafe468cc8ae`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root, self. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::__init__::root.body[10].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:17`; AST `b97f3f463d4724206af2869ad4674d5eb373167f052507971a722ecc8f771a87`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::__init__::root.body[10].body[0].body[1]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:18`; AST `d7c0d76a0a372e03aeee66707c691374e60f76edfd240270d47898754eb23586`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, self. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::__init__::root.body[10].body[0].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:18`; AST `7d3ec00caae052142f9eafaf7e819afec6aee67b95327ec1d924450faaa8dd1d`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, self. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::__init__::root.body[10].body[0].body[2]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:19`; AST `c2afb1ebc402604bd7895515b0a0018025d44af2cbae841656670af5f84ca0bc`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.with_suffix.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::__init__::root.body[10].body[0].body[2].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:19`; AST `46aa1e96394d83d78ce0650ffed08f0cb1281604c533bd7f0a9f1922de6c6239`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.with_suffix.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::read::root.body[10].body[1]::FunctionDef

Source: `infra/agentinfra/roadmap_runtime.py:21`; AST `891edfe851c10127a331e1b2eea82f8b17f181d6a30472cf5f9e3ee3286f4903`.

Rust module: `infra::agentinfra::roadmap_runtime`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: dict, isinstance, list, read_json, record, require, self. Outputs/bindings: record.
Calls/effect boundaries: isinstance, read_json, record.get, require, self.path.exists.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::read::root.body[10].body[1].body[0]::If

Source: `infra/agentinfra/roadmap_runtime.py:22`; AST `67bf55701541534e06b51219f8a02cfa9e5985f005d4a76efd8c094c26b0efae`.

Rust module: `infra::agentinfra::roadmap_runtime`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.exists.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered If evaluation at root.body[10].body[1].body[0]; no call, error or mutation may be omitted. Condition: not self.path.exists()
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::read::root.body[10].body[1].body[0].test.operand::Call

Source: `infra/agentinfra/roadmap_runtime.py:22`; AST `5a0ab509baad619ec2a1ec684d6882dd1595eead8f620b398322ae10eeaa6916`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.exists.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[0].test.operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::read::root.body[10].body[1].body[0].body[0]::Return

Source: `infra/agentinfra/roadmap_runtime.py:23`; AST `be4cd20c06d06226bfa38334fbb62cfee292b75aae8dd88d66a9a0bd98e0d6ba`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Return evaluation at root.body[10].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::read::root.body[10].body[1].body[1]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:24`; AST `fb8294180bf4926dc986b94d7c34f40164ef851af315e01b0f6fd302cd4b9f4d`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: read_json, self. Outputs/bindings: record.
Calls/effect boundaries: read_json.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::read::root.body[10].body[1].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:24`; AST `e3a79a25f0eadc251da7129b90e21b22224f14b35a0ef4a713b53e9a67e688de`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: read_json, self. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::read::root.body[10].body[1].body[2]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:25`; AST `97b23c59b694d728ff16e61242d7f308eeb2f0cbee09abc17cf144d4fcb422be`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, isinstance, list, record, require. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, record.get, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::read::root.body[10].body[1].body[2].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:25`; AST `0ef8fbb5b29675ed996376eea9c4daed481a02c77fb64032de311d5686dd141c`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, isinstance, list, record, require. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, record.get, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::read::root.body[10].body[1].body[2].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:25`; AST `d1e3876e5f2eab25e6fd365f06eea6e829f195ef666744ac41314682d8aa382c`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[2].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::read::root.body[10].body[1].body[2].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_runtime.py:25`; AST `6eee454d38c6564b55c0aa4f32f87833e740d6719ce68783e5be1391f7aef128`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, list, record. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, record.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[2].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::read::root.body[10].body[1].body[2].value.args[0].values[1].args[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:25`; AST `6f7099dbd1e70fd0200a10e43c3d57441c66d9313a8346facf963c2376729b31`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[2].value.args[0].values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::read::root.body[10].body[1].body[2].value.args[0].values[2]::Call

Source: `infra/agentinfra/roadmap_runtime.py:26`; AST `c48049e81f7d1a6ec319ee66f15165d82368e235328d4c13bde6af9c3945a493`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, isinstance, record. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, record.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[2].value.args[0].values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::read::root.body[10].body[1].body[2].value.args[0].values[2].args[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:26`; AST `971d3eeb847e43400f978a1445d095c0a202e2f066e7915796b8aca6493c5afb`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[2].value.args[0].values[2].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::read::root.body[10].body[1].body[3]::Return

Source: `infra/agentinfra/roadmap_runtime.py:27`; AST `1d8c2c2be64d23c31c6eec0ccb160ec416867628655492a485c3d996da1d58bc`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Return evaluation at root.body[10].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2]::FunctionDef

Source: `infra/agentinfra/roadmap_runtime.py:29`; AST `e03e5cd3a0b7383a82b059b8256e388d75ac1b86317afd3fa7fd531b762bc503`.

Rust module: `infra::agentinfra::roadmap_runtime`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileLock, a, any, atomic_write_json, attempt, bool, diagnosis, dict, digest, inputs, int, len, lock, max_attempts, os, prior, record, require, seconds, self, str, sum, time, total_seconds, type, work_id. Outputs/bindings: a, attempt, lock, prior, record.
Calls/effect boundaries: FileLock, any, atomic_write_json, bool, diagnosis.strip, digest, len, lock.acquire, lock.release, os.getpid, record['attempts'].append, require, self.read, sum, time.time_ns, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:31`; AST `a80b87227f28c252d080ff907f0af172651ba555453e5745036155ccbed82667`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, inputs, require, work_id. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:31`; AST `532953187feeb5f720f2ac24f265350e761291ca3c3371a87306da52fd106c62`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, inputs, require, work_id. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[0].value.args[0].values[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:31`; AST `3ae74bfd2d999bef6297b9369a4b32c07c4f1e16d67071fa19213358511f6e29`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, work_id. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[0].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[0].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_runtime.py:31`; AST `ef3364368f11bf503a705b81744c2ee700a977c2e5437c3aaea2668cf13f26be`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, inputs. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[0].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[1]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:32`; AST `b17e586799a16bc6b953646c5e90047a0ed227893cce89fb6b5801148f41fe1e`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: int, require, seconds, total_seconds, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:32`; AST `2a0b826e831477b300b2dac3c5c0290c63800c7feb79d5cdbf29c6474b70eff8`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: int, require, seconds, total_seconds, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[1].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:32`; AST `e29d63a9a86ffc4d5ce9bfd619e61c5b9fafe7809d4fc5ad33dc1f04fb7a317a`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: seconds, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[1].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[2]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:33`; AST `c1ad9285eea94c0876760996a56b011eb7953a8001fa649860e9c5cba67e257f`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: int, max_attempts, require, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[2].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:33`; AST `9964a427f27faa188a06a2f6599c6e308cc37023ed6a1f3819565fd56914c6f3`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: int, max_attempts, require, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[2].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:33`; AST `5c1b9a2cbf1ccfb06e1a4aa0120d70b689774d68a32ac6662ddfca17331a8660`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: max_attempts, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[2].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[3]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:34`; AST `3bc0ac9d6fad6dac6fff38a4fd1f20dc4110bccf5d9eb479aaa386890f32ebf7`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileLock, self. Outputs/bindings: lock.
Calls/effect boundaries: FileLock.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[2].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[3].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:34`; AST `822547b3f0bdc60054653afca1074c32c8ad0902a2bcd405ce481643eccfcaed`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileLock, self. Outputs/bindings: (none).
Calls/effect boundaries: FileLock.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[4]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:35`; AST `2bcfe51cf785ee29160140309ca2724ded506c99a694a1cd40da99965fea32f6`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[4].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:35`; AST `19f113b1ff996d6a4e1349d4f629dcb1414895f291ae11a26e3a1c7c22771cf0`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5]::Try

Source: `infra/agentinfra/roadmap_runtime.py:36`; AST `267abaf47d3f11c1e0d13651607b667e9df0f71f3319af7876857e5bf70b4b59`.

Rust module: `infra::agentinfra::roadmap_runtime`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: a, any, atomic_write_json, attempt, bool, diagnosis, digest, inputs, len, lock, max_attempts, os, prior, record, require, seconds, self, sum, time, total_seconds, work_id. Outputs/bindings: a, attempt, prior, record.
Calls/effect boundaries: any, atomic_write_json, bool, diagnosis.strip, digest, len, lock.release, os.getpid, record['attempts'].append, require, self.read, sum, time.time_ns.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Try evaluation at root.body[10].body[2].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:37`; AST `8d60c6cf06a37f3a21e36d8d4fc569b1d94d00284e5e8e23781c46e0c0bd8c8b`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: record.
Calls/effect boundaries: self.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[2].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:37`; AST `1a6cd88d33383d245bb90e4e5f924f99f090d6bd29a5c43fab9e8ffb18d19d91`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].body[1]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:38`; AST `fb02894e79bd0ac79de95f550b4feb094271bbf4f2b65127fde6aebb7f8a50e0`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, record, work_id. Outputs/bindings: a, prior.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[2].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].body[1].value::ListComp

Source: `infra/agentinfra/roadmap_runtime.py:38`; AST `c3f3c40c97fec8a4120cf8b564950f887d14890d8da492833edbf6e6043e119a`.

Rust module: `infra::agentinfra::roadmap_runtime`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: a, record, work_id. Outputs/bindings: a.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered ListComp evaluation at root.body[10].body[2].body[5].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].body[2]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:39`; AST `9e2e189575ad9c29c56864582f9041b6986912484e2395d8e6e661a3410171f3`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, any, prior, require. Outputs/bindings: a.
Calls/effect boundaries: any, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].body[2].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:39`; AST `3c38a72856553d5c434e909fd4ae145eac7bf8446bca16ad70c3fb45b7b5350c`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, any, prior, require. Outputs/bindings: a.
Calls/effect boundaries: any, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[5].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].body[2].value.args[0].operand::Call

Source: `infra/agentinfra/roadmap_runtime.py:39`; AST `0c6799aa907ad169146daaee66073b6174234e139128234a79156d4b2ebeda2d`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, any, prior. Outputs/bindings: a.
Calls/effect boundaries: any.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[5].body[2].value.args[0].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].body[2].value.args[0].operand.args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_runtime.py:39`; AST `8a7d5fe1ed41edb414ae9932a9816f5ba59267137bef9f90b7f7dcacce6ceb98`.

Rust module: `infra::agentinfra::roadmap_runtime`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: a, prior. Outputs/bindings: a.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[10].body[2].body[5].body[2].value.args[0].operand.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].body[3]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:40`; AST `d08faefd03d6489f6ef2ac996dcd9ccebaaf365018efa1c74c918b43bfe0a134`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, any, inputs, prior, require. Outputs/bindings: a.
Calls/effect boundaries: any, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[5].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].body[3].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:40`; AST `ac4d1c553a8c47c0f5a5d2d23e8169103c7c28d587178a88a7048ebd50abee20`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, any, inputs, prior, require. Outputs/bindings: a.
Calls/effect boundaries: any, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[5].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].body[3].value.args[0].operand::Call

Source: `infra/agentinfra/roadmap_runtime.py:40`; AST `fed5ed9c4fb238b253f82e8a7f2a19f3771a6e73715f04ddc0581372625d0b4e`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, any, inputs, prior. Outputs/bindings: a.
Calls/effect boundaries: any.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[5].body[3].value.args[0].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].body[3].value.args[0].operand.args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_runtime.py:40`; AST `13f362874b9ee538d6c9f583dfe103a819c65a15f6b6df4d82432666fe533471`.

Rust module: `infra::agentinfra::roadmap_runtime`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: a, inputs, prior. Outputs/bindings: a.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[10].body[2].body[5].body[3].value.args[0].operand.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].body[4]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:41`; AST `7391bea7d25413cea2169158057e9dfd3d33a170d458e504311360fb4f859140`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, max_attempts, prior, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[5].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].body[4].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:41`; AST `ea5dcffa2aa745f14f54710212bd296f8e87a22aa5a35b29fc65003a4f2dcb1d`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, max_attempts, prior, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[5].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].body[4].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:41`; AST `913efbe5bf6e483de6568a9d688cb27d196675409407cd117ee0c850ad45fa62`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, prior. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[5].body[4].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].body[5]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:42`; AST `6ca91224f6f395ad579c50bf96f8a8516cd2bc20de7f8477f7a351740f652eee`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, prior, require, seconds, sum, total_seconds. Outputs/bindings: a.
Calls/effect boundaries: require, sum.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[5].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].body[5].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:42`; AST `4f2e717a35193cb0e53391f1d045de41c018111f712e8e01f149475232dc783e`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, prior, require, seconds, sum, total_seconds. Outputs/bindings: a.
Calls/effect boundaries: require, sum.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[5].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].body[5].value.args[0].left.left::Call

Source: `infra/agentinfra/roadmap_runtime.py:42`; AST `b38b99778247510f3672c27d25c86f1b1b5b33ec826015d24ef67f3500db5098`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, prior, sum. Outputs/bindings: a.
Calls/effect boundaries: sum.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[5].body[5].value.args[0].left.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].body[5].value.args[0].left.left.args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_runtime.py:42`; AST `a520fd903880e58d6b8700506eefe7632d8c57d438dd4cc7ea61c981e1519e48`.

Rust module: `infra::agentinfra::roadmap_runtime`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: a, prior. Outputs/bindings: a.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[10].body[2].body[5].body[5].value.args[0].left.left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].body[6]::If

Source: `infra/agentinfra/roadmap_runtime.py:43`; AST `b4dbee7b3606424977851718f53f1684774ad7640f0a279166817736a96978dd`.

Rust module: `infra::agentinfra::roadmap_runtime`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: bool, diagnosis, inputs, prior, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, diagnosis.strip, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered If evaluation at root.body[10].body[2].body[5].body[6]; no call, error or mutation may be omitted. Condition: prior
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].body[6].body[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:44`; AST `853db2afd8c28c8a33d887e96a83bfc29ef3e7c87665fe0b65ffb9fd150280a6`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, diagnosis, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, diagnosis.strip, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[5].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].body[6].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:44`; AST `ee171942fafcee617bf68b88d56acc2131348d87f6dccc06ff90a755a1ee0108`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, diagnosis, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, diagnosis.strip, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[5].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].body[6].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:44`; AST `5f161d0ee70916206cd6762d78e25cf9148e9debd7f0313e6d473e15d6cbe7ea`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, diagnosis. Outputs/bindings: (none).
Calls/effect boundaries: bool, diagnosis.strip.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[5].body[6].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].body[6].body[0].value.args[0].args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_runtime.py:44`; AST `7ec57aec97069b761eca95116ac27ef7ef1d814f93787c9b53931bd9f521bcd1`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: diagnosis. Outputs/bindings: (none).
Calls/effect boundaries: diagnosis.strip.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[5].body[6].body[0].value.args[0].args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].body[6].body[1]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:45`; AST `fe7fe2c0aa7b68cc1ea3fbeb1c02aa7c4f81ad6059ad46ce7292e6cdcb94ffdd`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: inputs, prior, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[5].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].body[6].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:45`; AST `1dd71fb4e777ec9c00132d97cce799a33daa63b07e7c6b9bb9ce0e70c0717b0f`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inputs, prior, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[5].body[6].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].body[7]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:46`; AST `a5e4c849ba3b4fbcee16d01c7e2b2cd85ad1e9a6fbfb11b9b8a24830ecfaa925`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: diagnosis, digest, inputs, len, os, prior, seconds, time, work_id. Outputs/bindings: attempt.
Calls/effect boundaries: digest, len, os.getpid, time.time_ns.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[2].body[5].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].body[7].value.values[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:46`; AST `72625daab276fb12642547a5a4363cb6ff2bc5a0f1dd634f089ff1e0ec5de495`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, inputs, len, prior, work_id. Outputs/bindings: (none).
Calls/effect boundaries: digest, len.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[5].body[7].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].body[7].value.values[0].args[0].values[2].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:46`; AST `913efbe5bf6e483de6568a9d688cb27d196675409407cd117ee0c850ad45fa62`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, prior. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[5].body[7].value.values[0].args[0].values[2].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].body[7].value.values[6]::Call

Source: `infra/agentinfra/roadmap_runtime.py:48`; AST `ba1923643b161051a18bf7ae7386addd84146f4ab481f99d56712bc1ce97df2c`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os. Outputs/bindings: (none).
Calls/effect boundaries: os.getpid.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[5].body[7].value.values[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].body[7].value.values[7]::Call

Source: `infra/agentinfra/roadmap_runtime.py:49`; AST `d7bb4f9a8f02ae840b0ecfbf4a0bc46a103c9ee80044d3e746466d336dbaf7ae`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: time. Outputs/bindings: (none).
Calls/effect boundaries: time.time_ns.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[5].body[7].value.values[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].body[8]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:50`; AST `72ad7243e175c897858cde4cb3d89e1c1586fe12d477ff19b5d4b77ea35ae6cd`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: attempt, record. Outputs/bindings: (none).
Calls/effect boundaries: record['attempts'].append.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[5].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].body[8].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:50`; AST `876c585b5b90aaeea31ed0ebf97f0192892efe1c54f8971afdc17736d4a0e621`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: attempt, record. Outputs/bindings: (none).
Calls/effect boundaries: record['attempts'].append.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[5].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].body[9]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:51`; AST `39653ba93071c48ea5664f41495c0b9b4c456ea6c7027a39f271248d5232ec2e`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_json, record, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[5].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].body[9].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:51`; AST `e0ebb6df18f3acd72b73864198de1922264a5591e4adfd3e452231c9bafa9477`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_json, record, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[5].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].body[10]::Return

Source: `infra/agentinfra/roadmap_runtime.py:52`; AST `e266cd7ee7f5bdfcac0bb2a29b163bd7502edefad7a236c7df360c13dc73bb7e`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: attempt. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Return evaluation at root.body[10].body[2].body[5].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].finalbody[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:54`; AST `9aa6f04fc26ee6b3f6fe1a19158adb3cfde13709dcae4a7cc38bccbb2655afb2`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[5].finalbody[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[10].body[2].body[5].finalbody[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:54`; AST `107c5710331db61e695f7d71256d48862412d15c223e204da5c71c497352b634`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[5].finalbody[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[10].body[3]::FunctionDef

Source: `infra/agentinfra/roadmap_runtime.py:56`; AST `a2393fa0bd59d57498a152c369c0ed2a5ca20b1ffc352bd5da4318b2cc585e6d`.

Rust module: `infra::agentinfra::roadmap_runtime`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileLock, a, atomic_write_json, dict, ident, len, lock, matches, outcome, receipt, record, require, self, str. Outputs/bindings: a, lock, matches, record.
Calls/effect boundaries: FileLock, atomic_write_json, len, lock.acquire, lock.release, matches[0].update, require, self.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[10].body[3].body[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:57`; AST `ff22254ad3521a5de6152891b38da85f22dd101c576a6e0229b2a432bf9aacc7`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: outcome, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[10].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:57`; AST `f8b0617f9b0cada61780dfcbe5e11cb0795448f3c525f4f04f185d7a3eb018f6`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: outcome, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[10].body[3].body[1]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:58`; AST `5ad948bd4807312f2c239602daba24f505bb65e40a43af1bb9af59c5142392a1`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileLock, self. Outputs/bindings: lock.
Calls/effect boundaries: FileLock.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[10].body[3].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:58`; AST `06ed4456c71451913ad10de312800960b64f8327c15985fb8debf4e388eef9d0`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileLock, self. Outputs/bindings: (none).
Calls/effect boundaries: FileLock.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[10].body[3].body[2]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:59`; AST `2bcfe51cf785ee29160140309ca2724ded506c99a694a1cd40da99965fea32f6`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[10].body[3].body[2].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:59`; AST `19f113b1ff996d6a4e1349d4f629dcb1414895f291ae11a26e3a1c7c22771cf0`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[10].body[3].body[3]::Try

Source: `infra/agentinfra/roadmap_runtime.py:60`; AST `1685361e6ac80d5ca980d9c91a0a95256ca9a21ac79ed8f43b8d3c5df6c9635d`.

Rust module: `infra::agentinfra::roadmap_runtime`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: a, atomic_write_json, ident, len, lock, matches, outcome, receipt, record, require, self. Outputs/bindings: a, matches, record.
Calls/effect boundaries: atomic_write_json, len, lock.release, matches[0].update, require, self.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Try evaluation at root.body[10].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[10].body[3].body[3].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:61`; AST `8d60c6cf06a37f3a21e36d8d4fc569b1d94d00284e5e8e23781c46e0c0bd8c8b`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: record.
Calls/effect boundaries: self.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[3].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[10].body[3].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:61`; AST `1a6cd88d33383d245bb90e4e5f924f99f090d6bd29a5c43fab9e8ffb18d19d91`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[10].body[3].body[3].body[1]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:62`; AST `cf32e9bf9b8a72d66b64531668c804f7085a2f6675610c277caa371b3b7106b2`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, ident, record. Outputs/bindings: a, matches.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[3].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[10].body[3].body[3].body[1].value::ListComp

Source: `infra/agentinfra/roadmap_runtime.py:62`; AST `fb765ce6077cad522849ac1bfa4314dacb67a58cf6789a9c53a4b0d2d988644b`.

Rust module: `infra::agentinfra::roadmap_runtime`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: a, ident, record. Outputs/bindings: a.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered ListComp evaluation at root.body[10].body[3].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[10].body[3].body[3].body[2]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:63`; AST `c935a24c37b07acc4025897da5181f8b7d3c77f9441b7c12a4a152631ff94abd`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, matches, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[3].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[10].body[3].body[3].body[2].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:63`; AST `de82ae7288f3fd876110c4e92da5000b0ea5d5ba25e3a8517d7f9303460023b5`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, matches, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[10].body[3].body[3].body[2].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:63`; AST `d97f989b8f8f52f8f40688f8e2e1ccaded6f1cf09b4ecf82beecbcc52f1add97`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, matches. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[3].body[2].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[10].body[3].body[3].body[3]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:64`; AST `0f4b708072d6f39d8bad5eeee9b8aae8cd819c102d475c75587e7c1abcf8fef8`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: matches, outcome, receipt. Outputs/bindings: (none).
Calls/effect boundaries: matches[0].update.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[3].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[10].body[3].body[3].body[3].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:64`; AST `cb028ee3c04d26ae7e343a0dc5e10609863db082fbd882336a75457d2a94abd4`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: matches, outcome, receipt. Outputs/bindings: (none).
Calls/effect boundaries: matches[0].update.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[3].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[10].body[3].body[3].body[4]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:65`; AST `39653ba93071c48ea5664f41495c0b9b4c456ea6c7027a39f271248d5232ec2e`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_json, record, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[3].body[3].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[10].body[3].body[3].body[4].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:65`; AST `e0ebb6df18f3acd72b73864198de1922264a5591e4adfd3e452231c9bafa9477`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_json, record, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[3].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[10].body[3].body[3].finalbody[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:67`; AST `9aa6f04fc26ee6b3f6fe1a19158adb3cfde13709dcae4a7cc38bccbb2655afb2`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[3].body[3].finalbody[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[10].body[3].body[3].finalbody[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:67`; AST `107c5710331db61e695f7d71256d48862412d15c223e204da5c71c497352b634`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[3].finalbody[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[10].body[4]::FunctionDef

Source: `infra/agentinfra/roadmap_runtime.py:69`; AST `b8988c51b7d7a53490248f93800853b5f44fcc82b008cb8f82c28ba23016390c`.

Rust module: `infra::agentinfra::roadmap_runtime`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileLock, atomic_write_json, bool, dict, event_id, int, lock, record, require, self, str, thread_id, total, type, usage. Outputs/bindings: lock, record, usage.
Calls/effect boundaries: FileLock, atomic_write_json, bool, dict, lock.acquire, lock.release, record['usage'].setdefault, require, self.read, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[10].body[4].body[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:70`; AST `d799aa76aac235aa02ea343eccecffec1ff0d53ba52ac1e7d2c1fd14f0e671dd`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, event_id, require, thread_id. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[10].body[4].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:70`; AST `7a7e76fa5fef3d1ac92cecef7d9e90dcfe3407cc73ec42a8e5a100666799d554`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, event_id, require, thread_id. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[10].body[4].body[0].value.args[0].values[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:70`; AST `cd37e63e8c7eb3c36062f0fbd5dd0ea6964ef29927b2cb95206c3f8060580755`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, thread_id. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[0].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[10].body[4].body[0].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_runtime.py:70`; AST `3e92731226f2b51f589da08be39a33e83d597c14fea7e4556613d9a1dbb6d9df`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, event_id. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[0].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[10].body[4].body[1]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:71`; AST `14b97e4ba59e30f94a1512f471f04d4ec3ccbeb29ff7bd9cbd1fc2984a90b4c3`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: int, require, total, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[10].body[4].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:71`; AST `8f04bdc286ac29f86b50442445b003106f8399a69d6e800a1e7f93573a83cf9b`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: int, require, total, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[10].body[4].body[1].value.args[0].values[1].values[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:71`; AST `1640c40c7f3e5652b4ce485094324d24b71d11f477d89f9370054dc8ab0bcd46`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: total, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[1].value.args[0].values[1].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[10].body[4].body[2]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:72`; AST `0b9cf3f582006dcd9e3bada572669897fb941f81c22a91048b7cca986626b4c6`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileLock, self. Outputs/bindings: lock.
Calls/effect boundaries: FileLock.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[10].body[4].body[2].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:72`; AST `1ee904a2b41404877314b19cf7f0fb6745c76928d8915a51a07c5bcae2fc445b`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileLock, self. Outputs/bindings: (none).
Calls/effect boundaries: FileLock.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[10].body[4].body[3]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:73`; AST `2bcfe51cf785ee29160140309ca2724ded506c99a694a1cd40da99965fea32f6`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[10].body[4].body[3].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:73`; AST `19f113b1ff996d6a4e1349d4f629dcb1414895f291ae11a26e3a1c7c22771cf0`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[10].body[4].body[4]::Try

Source: `infra/agentinfra/roadmap_runtime.py:74`; AST `b121de3fb58456afcb4ffbd65c983c50cdcd461c971cf0aff578440c215bf020`.

Rust module: `infra::agentinfra::roadmap_runtime`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: atomic_write_json, dict, event_id, lock, record, require, self, thread_id, total, usage. Outputs/bindings: record, usage.
Calls/effect boundaries: atomic_write_json, dict, lock.release, record['usage'].setdefault, require, self.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Try evaluation at root.body[10].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[10].body[4].body[4].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:75`; AST `8d60c6cf06a37f3a21e36d8d4fc569b1d94d00284e5e8e23781c46e0c0bd8c8b`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: record.
Calls/effect boundaries: self.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[4].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[10].body[4].body[4].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:75`; AST `1a6cd88d33383d245bb90e4e5f924f99f090d6bd29a5c43fab9e8ffb18d19d91`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[10].body[4].body[4].body[1]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:76`; AST `53bcfe909acdecf6389bd1ec4c4194257682702a9c37e4bc185120110b090989`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record, thread_id. Outputs/bindings: usage.
Calls/effect boundaries: record['usage'].setdefault.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[4].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[10].body[4].body[4].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:76`; AST `c0683907ccda314c861f238c211afc4a1f6ffa70db9f0eec029d1943eea1cf53`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record, thread_id. Outputs/bindings: (none).
Calls/effect boundaries: record['usage'].setdefault.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[10].body[4].body[4].body[2]::If

Source: `infra/agentinfra/roadmap_runtime.py:77`; AST `f95034d2c8b7eddab9655cc09d7884575c3cab03b52aa5a65da00e05be414c70`.

Rust module: `infra::agentinfra::roadmap_runtime`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: dict, event_id, require, total, usage. Outputs/bindings: (none).
Calls/effect boundaries: dict, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered If evaluation at root.body[10].body[4].body[4].body[2]; no call, error or mutation may be omitted. Condition: event_id in usage['events']
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[10].body[4].body[4].body[2].body[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:78`; AST `484a0b9533eae32c71b66c3caa85840f528e80dcd574fccc269e6baaacb62e26`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: event_id, require, total, usage. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[4].body[4].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[10].body[4].body[4].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:78`; AST `da3bc31a4b596450a77443fae97fb81fa21166358bacc378bf3de03da2e64dca`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: event_id, require, total, usage. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[4].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[10].body[4].body[4].body[2].body[1]::Return

Source: `infra/agentinfra/roadmap_runtime.py:79`; AST `ed4cf45c6dc70c8fd8da13a6e0eb8b23a7689f702082e00fd2f5f8e1f0a5d564`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, usage. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Return evaluation at root.body[10].body[4].body[4].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[10].body[4].body[4].body[2].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:79`; AST `8aa055a140fab9cf553e1183c53bfb2f0a5f5f655a93319e930a19ab5441ec68`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, usage. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[4].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[10].body[4].body[4].body[3]::If

Source: `infra/agentinfra/roadmap_runtime.py:80`; AST `fd88db75cca5888054eec9b4dc2fbe9b4c86f0df9f90dd1bc7af64af556d2203`.

Rust module: `infra::agentinfra::roadmap_runtime`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: require, total, usage. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered If evaluation at root.body[10].body[4].body[4].body[3]; no call, error or mutation may be omitted. Condition: total is not None and usage['total'] is not None
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[10].body[4].body[4].body[3].body[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:81`; AST `7240208a29b2feed1eacad1baabf2a3aa383374c146443d08cbe86c0bf715e8a`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, total, usage. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[4].body[4].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[10].body[4].body[4].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:81`; AST `5367338754edeaa70ab6f211df26af7f7f60033e003adad9fc20c0442e9e72af`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, total, usage. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[4].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[10].body[4].body[4].body[4]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:82`; AST `36582a4e64162a0874bb43073f8717673f192fd5194a277fa45ec1dd702621ed`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: event_id, total, usage. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[4].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[10].body[4].body[4].body[5]::If

Source: `infra/agentinfra/roadmap_runtime.py:83`; AST `937e3ed71edcc16e8369c8af6d5fdb221cd8e1f6175bfbb3f8631273ffd9358c`.

Rust module: `infra::agentinfra::roadmap_runtime`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: total, usage. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered If evaluation at root.body[10].body[4].body[4].body[5]; no call, error or mutation may be omitted. Condition: total is not None
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[10].body[4].body[4].body[5].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:84`; AST `fa966965debf4352b7ebfad6de6eb7f1cc1332c3f908442bd356ef0538f4f010`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: total, usage. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[4].body[4].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[10].body[4].body[4].body[6]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:85`; AST `39653ba93071c48ea5664f41495c0b9b4c456ea6c7027a39f271248d5232ec2e`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_json, record, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[4].body[4].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[10].body[4].body[4].body[6].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:85`; AST `e0ebb6df18f3acd72b73864198de1922264a5591e4adfd3e452231c9bafa9477`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_json, record, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[4].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[10].body[4].body[4].body[7]::Return

Source: `infra/agentinfra/roadmap_runtime.py:86`; AST `ed4cf45c6dc70c8fd8da13a6e0eb8b23a7689f702082e00fd2f5f8e1f0a5d564`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, usage. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Return evaluation at root.body[10].body[4].body[4].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[10].body[4].body[4].body[7].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:86`; AST `8aa055a140fab9cf553e1183c53bfb2f0a5f5f655a93319e930a19ab5441ec68`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, usage. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[4].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[10].body[4].body[4].finalbody[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:88`; AST `9aa6f04fc26ee6b3f6fe1a19158adb3cfde13709dcae4a7cc38bccbb2655afb2`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[4].body[4].finalbody[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[10].body[4].body[4].finalbody[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:88`; AST `107c5710331db61e695f7d71256d48862412d15c223e204da5c71c497352b634`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[4].finalbody[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11]::FunctionDef

Source: `infra/agentinfra/roadmap_runtime.py:91`; AST `31ffd8b547fdf2b1f4c13b64930fcaf22f1f6dea235db4444fe18ccb94e4ba96`.

Rust module: `infra::agentinfra::roadmap_runtime`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: BaseException, BudgetLedger, FileLock, Path, all, argv, attempt, bindings_current, compiled, diagnosis, dict, digest, exc, inputs, lease, ledger, name, ok, receipt, recipe, require, result, root, run_process, str, sys, type, work_id, x. Outputs/bindings: argv, attempt, inputs, lease, ledger, ok, receipt, recipe, result, work_id, x.
Calls/effect boundaries: BudgetLedger, FileLock, all, bindings_current, digest, lease.acquire, lease.release, ledger.close, ledger.reserve, require, root.resolve, run_process, str, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:92`; AST `7134076064ca0cc4d6e8bf0df750033455986c45bc4b76108df1e6dd0cf012c7`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bindings_current, compiled, require, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:92`; AST `1d48ed543f544738992ff8b01172556e0ebe3c3346236bdb93934a175388b6c2`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, compiled, require, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:92`; AST `e4376bee10cb5ac58b23e27129b2002e1436b91face64325fcbf8a25771ff8e7`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, compiled, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[1]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:93`; AST `64512de268c5e817df30e7dca1f869aa9c2f31bb9f799a4ff54f0f3e6e494ed7`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, name, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:93`; AST `f78b579b3faa4cc54919bab290adc167932d4b19443dc0853a3b15b21d976cd1`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, name, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[2]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:94`; AST `c6946d992b569719baf8f6b5caeb8843502d56201decee935602a5fe529eba20`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, name. Outputs/bindings: recipe.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[3]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:95`; AST `bc654dbdf9dc5d5642492c41db899552c7f4c7751c6afb9c6138c540f14e0b5a`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: recipe, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[3].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:95`; AST `a15b695faca3256151950dce380c567c0ddb44509ee8a90a9a4e5da25477da06`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: recipe, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[4]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:96`; AST `47b5483b8dd8c381357e24a91032e49c14e8bb5d54ab7923954fdc61efa65649`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: recipe, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[4].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:96`; AST `65aae1c63a647ddbd3502e80205255c1f34e7bca29d35a6c04d8569e8709a5b8`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: recipe, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[5]::Import

Source: `infra/agentinfra/roadmap_runtime.py:97`; AST `f7252e3c1dbe1d5edf1f34c020a58a05b55f706b2c1d9479eae91f9a9d4be275`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Import evaluation at root.body[11].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[6]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:98`; AST `0eed2b2afe87fd76205f49998eb944dc25226d40930535b153fbcfca68291fa3`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: recipe, sys. Outputs/bindings: argv.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[7]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:99`; AST `9d15bb663bddd8cd5cf54a2049a1c82786ab59c32dea73de26fc4cc6e075d1fc`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, argv, require, str, type, x. Outputs/bindings: x.
Calls/effect boundaries: all, require, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[7].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:99`; AST `ca3fb39a85567145d1afae50e4530911662b551f34ac0aad3bcf79f6173bbe24`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, argv, require, str, type, x. Outputs/bindings: x.
Calls/effect boundaries: all, require, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[7].value.args[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:99`; AST `d6765e1f20fcaba0aaeb5595c25d6f47549b94b17938afeeff50e3e72dd87a07`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, argv, str, type, x. Outputs/bindings: x.
Calls/effect boundaries: all, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[7].value.args[0].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_runtime.py:99`; AST `a43f75bc33ab7a6b7a51cd0aaefe0b517dd36234fa7c8cc09a694d49c78a7a5b`.

Rust module: `infra::agentinfra::roadmap_runtime`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: argv, str, type, x. Outputs/bindings: x.
Calls/effect boundaries: type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[11].body[7].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[7].value.args[0].args[0].elt.left::Call

Source: `infra/agentinfra/roadmap_runtime.py:99`; AST `617245833c9319194f50c6c77baf6916a03ab26dba6a12037ebc1d090f9aebc1`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: type, x. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].value.args[0].args[0].elt.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[8]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:100`; AST `67675058a01e0dda8539105929316e0f5649ff01f4106b07914385a579da4201`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, name, root, str. Outputs/bindings: work_id.
Calls/effect boundaries: digest, root.resolve, str.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[8].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:100`; AST `f7eeffad6fe75979b2f5cb21e3b6559a00b62c457e1203bd148a7d8627d441bc`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, name, root, str. Outputs/bindings: (none).
Calls/effect boundaries: digest, root.resolve, str.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[8].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_runtime.py:100`; AST `29d0b5a674124d6a5dea0e9d83c547c4cebd29502709afd03c4659bd6afedfda`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, str. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve, str.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[8].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[8].value.args[0].values[1].args[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:100`; AST `b97f3f463d4724206af2869ad4674d5eb373167f052507971a722ecc8f771a87`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[8].value.args[0].values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[9]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:101`; AST `421b4ed54537fb53288819ed5abaadfbafffa5592ae161b204a201c761a61d4f`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, digest, recipe. Outputs/bindings: inputs.
Calls/effect boundaries: digest.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[9].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:101`; AST `d15b0e2a60dd0d87c5cc653cbf29a5f306cf7cdea9849c6143dc86aaddbcbd0f`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, digest, recipe. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[10]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:102`; AST `dc2fd1ede60c6438c487511f87ef8eedec8bb87e6ab3d1c5380ff1542be015c2`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: BudgetLedger, root. Outputs/bindings: ledger.
Calls/effect boundaries: BudgetLedger.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[10].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:102`; AST `df43247d3e9a1323119ce795d3f01353dada1c7e238477cf98ed400282fae762`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: BudgetLedger, root. Outputs/bindings: (none).
Calls/effect boundaries: BudgetLedger.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[11]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:103`; AST `597e7c835018aa2ba95b6ca1c6f8fe786ba07ed685b28372355548e344eaf445`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileLock, root. Outputs/bindings: lease.
Calls/effect boundaries: FileLock.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[11].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:103`; AST `8e00a4bc7d740dc3d04edfbd16ad1f6b400e1685b98654a9adfa0c6508d54b7e`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileLock, root. Outputs/bindings: (none).
Calls/effect boundaries: FileLock.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[12]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:104`; AST `4d8ec1b6a1b7605da659d3bd4a58e87305084395ac03de474edc83b70229037c`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lease. Outputs/bindings: (none).
Calls/effect boundaries: lease.acquire.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[12].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:104`; AST `90f35c2c815c72014528f6ee0b25d0d929a0b3c33c0fc7577df4a90ffada1455`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lease. Outputs/bindings: (none).
Calls/effect boundaries: lease.acquire.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[13]::Try

Source: `infra/agentinfra/roadmap_runtime.py:105`; AST `7e1e7685fe28061c6a95dfea5b06f9dc4c575b2a76f5e8b3400415b783a1046b`.

Rust module: `infra::agentinfra::roadmap_runtime`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: BaseException, argv, attempt, diagnosis, exc, inputs, lease, ledger, name, ok, receipt, recipe, result, root, run_process, type, work_id. Outputs/bindings: attempt, ok, receipt, result.
Calls/effect boundaries: lease.release, ledger.close, ledger.reserve, run_process, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Try evaluation at root.body[11].body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[13].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:106`; AST `68c635bc672c0772316f4c2ea50b67ee2e62598939a7228ac1316d7e461c309c`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: diagnosis, inputs, ledger, recipe, work_id. Outputs/bindings: attempt.
Calls/effect boundaries: ledger.reserve.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[13].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:106`; AST `fa6c33a3e167a94c96bad464822fbe19306f4dccfb3a749b04d848829ce28312`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: diagnosis, inputs, ledger, recipe, work_id. Outputs/bindings: (none).
Calls/effect boundaries: ledger.reserve.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[13].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[13].body[1]::Try

Source: `infra/agentinfra/roadmap_runtime.py:108`; AST `2451bce5b4525e15091e68b91e30fa1263fa937933c8a6e7ad5b81052d1f67fc`.

Rust module: `infra::agentinfra::roadmap_runtime`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: BaseException, argv, attempt, exc, inputs, ledger, name, receipt, recipe, result, root, run_process, type. Outputs/bindings: ok, receipt, result.
Calls/effect boundaries: ledger.close, run_process, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Try evaluation at root.body[11].body[13].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[13].body[1].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:109`; AST `5a0a77f443015c25fb8751ff10f33eee995c10fdff134b88b0b44294ad25cb72`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: argv, recipe, root, run_process. Outputs/bindings: result.
Calls/effect boundaries: run_process.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[13].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[13].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:109`; AST `53ff285d5a6f1859d9a7882f6bf78e46dd8216eca3e679bb4cbcdd892fad0866`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: argv, recipe, root, run_process. Outputs/bindings: (none).
Calls/effect boundaries: run_process.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[13].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[13].body[1].body[1]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:110`; AST `2ecbedbd535378ec6e7aa60591b5cafbe87157cfc95e326e92756d72a4d6fd8a`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: argv, inputs, name, result. Outputs/bindings: receipt.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[13].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[13].body[1].body[2]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:114`; AST `b3c1299d30e6607bcfab32352f143a6d494b3a2bcac40a557b7dd1dedbda2b87`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: receipt, result. Outputs/bindings: ok.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[13].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[13].body[1].handlers[0]::ExceptHandler

Source: `infra/agentinfra/roadmap_runtime.py:115`; AST `0693a57bcc28ef82b3a434a4fa88b3109998a167dc0b84fa396ce0f50de3b96b`.

Rust module: `infra::agentinfra::roadmap_runtime`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: BaseException, attempt, exc, ledger, type. Outputs/bindings: (none).
Calls/effect boundaries: ledger.close, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[11].body[13].body[1].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[13].body[1].handlers[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:116`; AST `32155c72452559d63d8f166d88319d50af3edf755312f1917accaffbb9d251a5`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: attempt, exc, ledger, type. Outputs/bindings: (none).
Calls/effect boundaries: ledger.close, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[13].body[1].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[13].body[1].handlers[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:116`; AST `503cdb75c1796ab3efdee8d8c0d1ab0dbb2c3af0eb5a6f4cc156b8cd12b331ce`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: attempt, exc, ledger, type. Outputs/bindings: (none).
Calls/effect boundaries: ledger.close, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[13].body[1].handlers[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[13].body[1].handlers[0].body[0].value.args[2].values[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:116`; AST `760fdaff1a05c24c8db8bb1ee0c475c11403d48d9ac9c89ec3c062a1494d5d01`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exc, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[13].body[1].handlers[0].body[0].value.args[2].values[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[13].body[1].handlers[0].body[1]::Raise

Source: `infra/agentinfra/roadmap_runtime.py:117`; AST `ba28128c14dfbd0a9062c0dbab42ad6c52ecf0767df6b67576deb1dbbfdd038d`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Raise evaluation at root.body[11].body[13].body[1].handlers[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[13].body[2]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:118`; AST `d3ab36aeed6f03c0c0b1c9d0fb3ca3ba46a4352d5213c05626289b873c0660fd`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: attempt, ledger, ok, receipt. Outputs/bindings: (none).
Calls/effect boundaries: ledger.close.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[13].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[13].body[2].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:118`; AST `7d777545a191c38a43e7ca2aacc371afcf72fabb4f51fdc2087475a41ac96c69`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: attempt, ledger, ok, receipt. Outputs/bindings: (none).
Calls/effect boundaries: ledger.close.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[13].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[13].body[3]::Return

Source: `infra/agentinfra/roadmap_runtime.py:119`; AST `9b378eb582403574e9c02456d9dbe8d3ccc96e049aa98ec3ceee97d8b1bff879`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: receipt. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Return evaluation at root.body[11].body[13].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[13].finalbody[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:121`; AST `0324b3e2db1ff1d21a06b04c85a991b516c3896842973d7f654860c5b366eef9`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lease. Outputs/bindings: (none).
Calls/effect boundaries: lease.release.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[13].finalbody[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[11].body[13].finalbody[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:121`; AST `048afd42289a938d53fdcdbe01fdbf0cfa61c1cf67318f7be9b504d14956c5cf`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lease. Outputs/bindings: (none).
Calls/effect boundaries: lease.release.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_records, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[13].finalbody[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
