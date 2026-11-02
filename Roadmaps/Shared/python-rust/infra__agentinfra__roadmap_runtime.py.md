# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 529. Inventory digest: `88f981315d6621367290099c2b239ecbcbebaaee8fd0142db62e4486348ee648`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/roadmap_runtime.py::module::root::Module

Source: `infra/agentinfra/roadmap_runtime.py:1`; AST `2006120f04864b7d575c26d657fedad84df1d795515cd818adc332521108f4a7`.

Rust module: `infra::agentinfra::roadmap_runtime`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: BaseException, BudgetLedger, FileLock, Path, WorkspaceLease, a, all, ancestor, any, argv, atomic_write_json, attempt, attempts, binding, bindings_current, bool, bounded_prior, by_id, canonical_record, compiled, confined_path, continuation, created, diagnosis, dict, digest, event_id, exc, execution, f, field, fields, generation, generation_parent, goal, ident, inherited, inherited_attempt_ids, inputs, int, isinstance, k, lease, ledger, legacy, len, list, lock, matches, max_attempts, measured, milestone, name, native_control, ok, old, operation, origin, os, outcome, owner, path, pending, previous, prior, read_json, receipt, recipe, recipe_scope, record, require, result, reusable, reversed, root, run_process, run_work, s, sample, seconds, selected, self, series, set, sorted, spec, spec_binding, started, str, successful, sum, supersedes, sys, thread, thread_id, time, total, total_seconds, totals, tuple, type, usage, user_authorized, v, validate_record, validate_tool_receipt, value, work_id, x. Outputs/bindings: a, ancestor, argv, attempt, attempts, binding, bounded_prior, by_id, canonical_record, continuation, created, execution, f, field, fields, generation, generation_parent, goal, ident, inherited, inputs, k, lease, ledger, legacy, lock, matches, measured, ok, old, owner, path, pending, previous, prior, receipt, recipe, record, result, reusable, s, sample, selected, series, spec, spec_binding, started, successful, supersedes, thread, usage, v, value, work_id, x.
Calls/effect boundaries: BudgetLedger, FileLock, WorkspaceLease, WorkspaceLease(root).assert_owner, a.get, a.get('operation', {}).get, a.get('receipt', {}).get, all, any, atomic_write_json, attempt.get, attempt.get('receipt', {}).get, attempt.update, binding.get, bindings_current, bool, by_id[ident].get, canonical_record.exists, confined_path, continuation.get, diagnosis.strip, dict, digest, execution.get, goal.get, isinstance, lease.acquire, lease.release, ledger.close, ledger.read, ledger.reserve, len, list, lock.acquire, lock.release, matches[0].update, old.get, operation.get, os.getpid, owner.get, pending.append, pending.pop, previous.get, previous.get('operation', {}).get, prior[-1].get, read_json, read_json(canonical_record).get, receipt.get, recipe_scope, record.get, record.get('continuation', {}).get, record['attempts'].append, record['usage'].items, record['usage'].setdefault, require, reversed, root.resolve, run_process, run_work, s.items, sample['totals'].items, selected.add, selected.update, self._reserve, self.path.exists, self.path.with_suffix, self.read, set, sorted, spec.get, spec.items, str, successful.get, successful.setdefault, successful['reuse_consumers'].append, sum, time.time_ns, totals.get, totals.values, tuple, type, validate_record, validate_tool_receipt.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered ImportFrom evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::root.body[11]::ClassDef

Source: `infra/agentinfra/roadmap_runtime.py:16`; AST `ff013e4da30def2e7451169364d7d2e045f25d01b3513df32133e625cfbdb499`.

Rust module: `infra::agentinfra::roadmap_runtime`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: FileLock, Path, a, all, ancestor, any, atomic_write_json, attempt, attempts, bindings_current, bool, bounded_prior, by_id, confined_path, diagnosis, dict, digest, event_id, f, field, fields, generation, generation_parent, ident, inherited_attempt_ids, inputs, int, isinstance, k, len, list, lock, matches, max_attempts, measured, native_control, old, operation, origin, os, outcome, pending, previous, prior, read_json, receipt, record, require, reusable, reversed, root, s, sample, seconds, selected, self, series, set, sorted, spec, spec_binding, str, successful, sum, supersedes, thread_id, time, total, total_seconds, totals, tuple, type, usage, user_authorized, v, validate_record, validate_tool_receipt, value, work_id. Outputs/bindings: a, ancestor, attempt, attempts, bounded_prior, by_id, f, field, fields, generation, generation_parent, ident, k, lock, matches, measured, old, pending, previous, prior, receipt, record, reusable, s, sample, selected, series, spec, spec_binding, successful, supersedes, usage, v, value.
Calls/effect boundaries: FileLock, a.get, a.get('operation', {}).get, a.get('receipt', {}).get, all, any, atomic_write_json, attempt.get, attempt.get('receipt', {}).get, attempt.update, bindings_current, bool, by_id[ident].get, confined_path, diagnosis.strip, dict, digest, isinstance, len, list, lock.acquire, lock.release, matches[0].update, old.get, operation.get, os.getpid, pending.append, pending.pop, previous.get, previous.get('operation', {}).get, prior[-1].get, read_json, receipt.get, record.get, record['attempts'].append, record['usage'].items, record['usage'].setdefault, require, reversed, root.resolve, s.items, sample['totals'].items, selected.add, selected.update, self._reserve, self.path.exists, self.path.with_suffix, self.read, set, sorted, spec.get, spec.items, successful.get, successful.setdefault, successful['reuse_consumers'].append, sum, time.time_ns, totals.get, totals.values, type, validate_record, validate_tool_receipt.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

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
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Return evaluation at root.body[11].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2]::FunctionDef

Source: `infra/agentinfra/roadmap_runtime.py:30`; AST `d435bd6bd23b6129780cdd0ac43603391c14c37c818fcd91e9594581c2368976`.

Rust module: `infra::agentinfra::roadmap_runtime`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: diagnosis, dict, inherited_attempt_ids, inputs, int, max_attempts, seconds, self, str, total_seconds, tuple, work_id. Outputs/bindings: (none).
Calls/effect boundaries: self._reserve.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[0]::Return

Source: `infra/agentinfra/roadmap_runtime.py:33`; AST `34f44f3f5a6e6e8931a9dfa15952ed9d09e4d0e5628ad8f68933d730aaedae90`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: diagnosis, inherited_attempt_ids, inputs, max_attempts, seconds, self, total_seconds, work_id. Outputs/bindings: (none).
Calls/effect boundaries: self._reserve.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Return evaluation at root.body[11].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve::root.body[11].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:33`; AST `c0e137332759aa10a10dbde805f45261c15316bf6ef3026e4f12ecdb1956a793`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: diagnosis, inherited_attempt_ids, inputs, max_attempts, seconds, self, total_seconds, work_id. Outputs/bindings: (none).
Calls/effect boundaries: self._reserve.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve_operation::root.body[11].body[3]::FunctionDef

Source: `infra/agentinfra/roadmap_runtime.py:36`; AST `75811c47618786811ecdfd254e0656803317bc371f241fa234d3751561281ea0`.

Rust module: `infra::agentinfra::roadmap_runtime`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: diagnosis, dict, inherited_attempt_ids, inputs, int, max_attempts, operation, seconds, self, str, total_seconds, tuple, work_id. Outputs/bindings: (none).
Calls/effect boundaries: self._reserve.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve_operation::root.body[11].body[3].body[0]::Return

Source: `infra/agentinfra/roadmap_runtime.py:39`; AST `a5251adf7fa405c8d9961b77cd6d231e2bc4ce2f801ecfa1c5d8ea6d93a4947c`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: diagnosis, inherited_attempt_ids, inputs, max_attempts, operation, seconds, self, total_seconds, work_id. Outputs/bindings: (none).
Calls/effect boundaries: self._reserve.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Return evaluation at root.body[11].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve_operation::root.body[11].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:39`; AST `ea747e211551d424cc5c1667ee60abb45d17ecdf386edb53eb5f8dd4369463fa`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: diagnosis, inherited_attempt_ids, inputs, max_attempts, operation, seconds, self, total_seconds, work_id. Outputs/bindings: (none).
Calls/effect boundaries: self._reserve.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve_control::root.body[11].body[4]::FunctionDef

Source: `infra/agentinfra/roadmap_runtime.py:42`; AST `0bcfbba27873f692d852321353eb3902ce3c12fe3c325b15ba0b175ae133ba46`.

Rust module: `infra::agentinfra::roadmap_runtime`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: bool, diagnosis, dict, inputs, int, operation, require, seconds, self, str, user_authorized, work_id. Outputs/bindings: (none).
Calls/effect boundaries: operation.get, require, self._reserve.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve_control::root.body[11].body[4].body[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:44`; AST `058fcd83634f15674157b13fc79579a2a32585bb10b5829a4e8767db9095aa0c`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: operation, require, user_authorized. Outputs/bindings: (none).
Calls/effect boundaries: operation.get, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve_control::root.body[11].body[4].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:44`; AST `ad12785854cd5beb1de4d384059ef6135092bb8c1ba263481d271d5b6f1ab328`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: operation, require, user_authorized. Outputs/bindings: (none).
Calls/effect boundaries: operation.get, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve_control::root.body[11].body[4].body[0].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:44`; AST `9921b55f7e8e3b57ec046d6a4c420a5e48b6340d2c48eb169f4288f87ac2b4ee`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: operation. Outputs/bindings: (none).
Calls/effect boundaries: operation.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[0].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve_control::root.body[11].body[4].body[0].value.args[0].values[2]::Call

Source: `infra/agentinfra/roadmap_runtime.py:45`; AST `8deed6378753f7ca53da2b562bbb1063ececc4937895220b4ec7152873fad165`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: operation. Outputs/bindings: (none).
Calls/effect boundaries: operation.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[0].value.args[0].values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve_control::root.body[11].body[4].body[0].value.args[0].values[3]::Call

Source: `infra/agentinfra/roadmap_runtime.py:45`; AST `b59ef8dba701734464b916a177f0e4d543f798778161a626c82547bf4b7a41d3`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: operation. Outputs/bindings: (none).
Calls/effect boundaries: operation.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[0].value.args[0].values[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve_control::root.body[11].body[4].body[1]::Return

Source: `infra/agentinfra/roadmap_runtime.py:46`; AST `c1f5c33806ce906988bf868e7c7b92bd1ced1a8b86edc8e6993226bc9cfbf069`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: diagnosis, inputs, operation, seconds, self, work_id. Outputs/bindings: (none).
Calls/effect boundaries: self._reserve.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Return evaluation at root.body[11].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reserve_control::root.body[11].body[4].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:46`; AST `c560296b3a3debcaf11780e958b7e6d08f8d9ea142f09b3831561ffb8c0a4af8`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: diagnosis, inputs, operation, seconds, self, work_id. Outputs/bindings: (none).
Calls/effect boundaries: self._reserve.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5]::FunctionDef

Source: `infra/agentinfra/roadmap_runtime.py:49`; AST `4658f0d0c43187f8da8faac99177d3905d02fbd292be980eea07c867ac5d9042`.

Rust module: `infra::agentinfra::roadmap_runtime`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileLock, a, ancestor, any, atomic_write_json, attempt, bindings_current, bool, bounded_prior, by_id, confined_path, diagnosis, dict, digest, generation, generation_parent, ident, inherited_attempt_ids, inputs, int, k, len, list, lock, max_attempts, native_control, operation, os, pending, previous, prior, read_json, receipt, record, require, reusable, reversed, seconds, selected, self, sorted, spec, spec_binding, str, successful, sum, supersedes, time, total_seconds, tuple, type, v, validate_tool_receipt, work_id. Outputs/bindings: a, ancestor, attempt, bounded_prior, by_id, generation, generation_parent, ident, k, lock, pending, previous, prior, receipt, record, reusable, selected, spec, spec_binding, successful, supersedes, v.
Calls/effect boundaries: FileLock, a.get, a.get('operation', {}).get, any, atomic_write_json, attempt.update, bindings_current, bool, by_id[ident].get, confined_path, diagnosis.strip, dict, digest, len, list, lock.acquire, lock.release, operation.get, os.getpid, pending.append, pending.pop, previous.get, previous.get('operation', {}).get, prior[-1].get, read_json, receipt.get, record['attempts'].append, require, reversed, selected.add, selected.update, self.read, sorted, spec.get, spec.items, successful.get, successful.setdefault, successful['reuse_consumers'].append, sum, time.time_ns, type, validate_tool_receipt.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:53`; AST `a80b87227f28c252d080ff907f0af172651ba555453e5745036155ccbed82667`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, inputs, require, work_id. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:53`; AST `532953187feeb5f720f2ac24f265350e761291ca3c3371a87306da52fd106c62`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, inputs, require, work_id. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[0].value.args[0].values[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:53`; AST `3ae74bfd2d999bef6297b9369a4b32c07c4f1e16d67071fa19213358511f6e29`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, work_id. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[0].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[0].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_runtime.py:53`; AST `ef3364368f11bf503a705b81744c2ee700a977c2e5437c3aaea2668cf13f26be`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, inputs. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[0].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[1]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:54`; AST `b17e586799a16bc6b953646c5e90047a0ed227893cce89fb6b5801148f41fe1e`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: int, require, seconds, total_seconds, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:54`; AST `2a0b826e831477b300b2dac3c5c0290c63800c7feb79d5cdbf29c6474b70eff8`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: int, require, seconds, total_seconds, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[1].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:54`; AST `e29d63a9a86ffc4d5ce9bfd619e61c5b9fafe7809d4fc5ad33dc1f04fb7a317a`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: seconds, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[1].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[2]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:55`; AST `c1ad9285eea94c0876760996a56b011eb7953a8001fa649860e9c5cba67e257f`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: int, max_attempts, require, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[2].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:55`; AST `9964a427f27faa188a06a2f6599c6e308cc37023ed6a1f3819565fd56914c6f3`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: int, max_attempts, require, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[2].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:55`; AST `5c1b9a2cbf1ccfb06e1a4aa0120d70b689774d68a32ac6662ddfca17331a8660`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: max_attempts, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[2].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[3]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:56`; AST `3bc0ac9d6fad6dac6fff38a4fd1f20dc4110bccf5d9eb479aaa386890f32ebf7`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileLock, self. Outputs/bindings: lock.
Calls/effect boundaries: FileLock.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[5].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[3].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:56`; AST `822547b3f0bdc60054653afca1074c32c8ad0902a2bcd405ce481643eccfcaed`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileLock, self. Outputs/bindings: (none).
Calls/effect boundaries: FileLock.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[4]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:57`; AST `2bcfe51cf785ee29160140309ca2724ded506c99a694a1cd40da99965fea32f6`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[4].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:57`; AST `19f113b1ff996d6a4e1349d4f629dcb1414895f291ae11a26e3a1c7c22771cf0`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5]::Try

Source: `infra/agentinfra/roadmap_runtime.py:58`; AST `6c832cf0fdaee2a84b8dd4e9d6c686722e7bc3b2f7b0a4ef9b7c17301d5990df`.

Rust module: `infra::agentinfra::roadmap_runtime`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: a, ancestor, any, atomic_write_json, attempt, bindings_current, bool, bounded_prior, by_id, confined_path, diagnosis, dict, digest, generation, generation_parent, ident, inherited_attempt_ids, inputs, k, len, list, lock, max_attempts, native_control, operation, os, pending, previous, prior, read_json, receipt, record, require, reusable, reversed, seconds, selected, self, sorted, spec, spec_binding, successful, sum, supersedes, time, total_seconds, v, validate_tool_receipt, work_id. Outputs/bindings: a, ancestor, attempt, bounded_prior, by_id, generation, generation_parent, ident, k, pending, previous, prior, receipt, record, reusable, selected, spec, spec_binding, successful, supersedes, v.
Calls/effect boundaries: a.get, a.get('operation', {}).get, any, atomic_write_json, attempt.update, bindings_current, bool, by_id[ident].get, confined_path, diagnosis.strip, dict, digest, len, list, lock.release, operation.get, os.getpid, pending.append, pending.pop, previous.get, previous.get('operation', {}).get, prior[-1].get, read_json, receipt.get, record['attempts'].append, require, reversed, selected.add, selected.update, self.read, sorted, spec.get, spec.items, successful.get, successful.setdefault, successful['reuse_consumers'].append, sum, time.time_ns, validate_tool_receipt.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Try evaluation at root.body[11].body[5].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:59`; AST `8d60c6cf06a37f3a21e36d8d4fc569b1d94d00284e5e8e23781c46e0c0bd8c8b`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: record.
Calls/effect boundaries: self.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[5].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:59`; AST `1a6cd88d33383d245bb90e4e5f924f99f090d6bd29a5c43fab9e8ffb18d19d91`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[1]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:60`; AST `b31d233fda4cb0b2984bcaaa2ce3998b5b11d4ae88bd877f9ff7c904c90b2ab6`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, any, native_control, record, require. Outputs/bindings: a.
Calls/effect boundaries: a.get, a.get('operation', {}).get, any, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:60`; AST `393561e6be361104f48ad6dd6e02a2066206001151cdb4ccb1b15c70badd3d7f`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, any, native_control, record, require. Outputs/bindings: a.
Calls/effect boundaries: a.get, a.get('operation', {}).get, any, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[1].value.args[0].operand::Call

Source: `infra/agentinfra/roadmap_runtime.py:60`; AST `f4a43454fbce589d1a2932ffb4a0a2b7dd31ae028a85859a9f0d925c2a7c777a`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, any, native_control, record. Outputs/bindings: a.
Calls/effect boundaries: a.get, a.get('operation', {}).get, any.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[1].value.args[0].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[1].value.args[0].operand.args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_runtime.py:60`; AST `ada53e6c243087412988f1dc6856a3ef776e1a16257725179d097b9c7f422fd2`.

Rust module: `infra::agentinfra::roadmap_runtime`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: a, native_control, record. Outputs/bindings: a.
Calls/effect boundaries: a.get, a.get('operation', {}).get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[11].body[5].body[5].body[1].value.args[0].operand.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[1].value.args[0].operand.args[0].elt.values[1].values[1].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:61`; AST `e83ae7be321c2f421032ef93357c3703b194488d6b748ef2ebaba14360f6272e`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.get, a.get('operation', {}).get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[1].value.args[0].operand.args[0].elt.values[1].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[1].value.args[0].operand.args[0].elt.values[1].values[1].left.func.value::Call

Source: `infra/agentinfra/roadmap_runtime.py:61`; AST `1d17b4668c3ec9fdcd025952a68687a28454394a15c49fb432f456618dbba871`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[1].value.args[0].operand.args[0].elt.values[1].values[1].left.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[2]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:63`; AST `3f94d5e396de94be24a697a557aa5b842d9d9f0e0ceb7ef9ae746911cf6a543d`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, record. Outputs/bindings: a, by_id.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[5].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[2].value::DictComp

Source: `infra/agentinfra/roadmap_runtime.py:63`; AST `0af492f53a4f06dd57bc0a462c96632f9d82a37180663e5373914ec37e0068a5`.

Rust module: `infra::agentinfra::roadmap_runtime`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: a, record. Outputs/bindings: a.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered DictComp evaluation at root.body[11].body[5].body[5].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[3]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:64`; AST `f4eeaff93e8425bc3e40e5034fced577e7618659d70e40871271dd147af7b583`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: by_id, len, record, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[5].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[3].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:64`; AST `beee1bab383e0f5afdce56e953b36a9448d7339b38ee1ac39b53642c8df823d9`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: by_id, len, record, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[3].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:64`; AST `fca7519555a1766ecc40eb735a14669b85381de9aec70a807c39a18392a1e9e2`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: by_id, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[3].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[3].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:64`; AST `c05725c5487cf0182a5df9b1cf359aab17b9a274a7574e1eaea12e2c45bfcb0d`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, record. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[3].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[4]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:65`; AST `9995f75d625568b202a5d895d7ea340ca122721c7c855ea2d847f3ea16418d68`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, record, work_id. Outputs/bindings: a, selected.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[5].body[5].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[4].value::SetComp

Source: `infra/agentinfra/roadmap_runtime.py:65`; AST `3feab2de1f629678bc3916e9405bad5b8ff1709d314a18be54c2887efcc61b5a`.

Rust module: `infra::agentinfra::roadmap_runtime`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: a, record, work_id. Outputs/bindings: a.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered SetComp evaluation at root.body[11].body[5].body[5].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[5]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:66`; AST `d93a835165f51f0c01590a1386003c98dd16989de566645b7137f1edc0a5038f`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: inherited_attempt_ids, selected. Outputs/bindings: (none).
Calls/effect boundaries: selected.update.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[5].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[5].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:66`; AST `489abf5a985620f9d5bf4a949c6ff517515efbd40b321eb84cc3a03cffea2e47`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inherited_attempt_ids, selected. Outputs/bindings: (none).
Calls/effect boundaries: selected.update.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[6]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:67`; AST `7990f26d0c3ac3e5ff243f6f29817986c68c08db2968416c4969e47aa3ddc83c`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: list, selected. Outputs/bindings: pending.
Calls/effect boundaries: list.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[5].body[5].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[6].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:67`; AST `0ce818bc2d969dfc1e42388bad21082a934be1abae8978b431f8a4bd8411fda8`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: list, selected. Outputs/bindings: (none).
Calls/effect boundaries: list.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[7]::While

Source: `infra/agentinfra/roadmap_runtime.py:68`; AST `a81932efe292921b095022359e2383938025d43e9766a995e27147bf023c029f`.

Rust module: `infra::agentinfra::roadmap_runtime`. while with explicit truth conversion and a normal-exhaustion flag for loop else

Inputs: ancestor, by_id, ident, pending, require, selected. Outputs/bindings: ancestor, ident.
Calls/effect boundaries: by_id[ident].get, pending.append, pending.pop, require, selected.add.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered While evaluation at root.body[11].body[5].body[5].body[7]; no call, error or mutation may be omitted. Condition: pending
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[7].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:69`; AST `cd29c37b04bb134dfe779600c3ed77c11c577cd4af8f6422efc7626707e31451`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: pending. Outputs/bindings: ident.
Calls/effect boundaries: pending.pop.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[5].body[5].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[7].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:69`; AST `b59b504ea575e0473ea0b5cc17902585c9dde56c94712f38bdafbec0ce738e98`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: pending. Outputs/bindings: (none).
Calls/effect boundaries: pending.pop.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[7].body[1]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:70`; AST `298e078001f96b1f709a7bb4c95fec77c25351a0dd6aafbf186900cd44735f2a`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: by_id, ident, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[5].body[7].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[7].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:70`; AST `af514d5f0dd84d587925dba46fb829699326588b5fad410bc163e6dd5c302ae7`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: by_id, ident, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[7].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[7].body[2]::For

Source: `infra/agentinfra/roadmap_runtime.py:71`; AST `0129a9053ae619ce45e0460dc9c89ddb08d9d941afd50cbddae1bb6fddaab00b`.

Rust module: `infra::agentinfra::roadmap_runtime`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ancestor, by_id, ident, pending, selected. Outputs/bindings: ancestor.
Calls/effect boundaries: by_id[ident].get, pending.append, selected.add.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered For evaluation at root.body[11].body[5].body[5].body[7].body[2]; no call, error or mutation may be omitted. Iteration: ancestor in by_id[ident].get('inherited_attempt_ids', [])
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[7].body[2].iter::Call

Source: `infra/agentinfra/roadmap_runtime.py:71`; AST `b2c30f811df6ec5631268ba55a53c847a07689d33e3a9a0764f8630811872cdc`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: by_id, ident. Outputs/bindings: (none).
Calls/effect boundaries: by_id[ident].get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[7].body[2].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[7].body[2].body[0]::If

Source: `infra/agentinfra/roadmap_runtime.py:72`; AST `fc09a4bed97dc46c99ed744c30f971daaad81bf27be8a733459934d763e1f625`.

Rust module: `infra::agentinfra::roadmap_runtime`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ancestor, pending, selected. Outputs/bindings: (none).
Calls/effect boundaries: pending.append, selected.add.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered If evaluation at root.body[11].body[5].body[5].body[7].body[2].body[0]; no call, error or mutation may be omitted. Condition: ancestor not in selected
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[7].body[2].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:73`; AST `2c682e2f8524ca6b5ce4f91409613a6255b5817ad8a7474ec2481c80e468d2e5`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ancestor, selected. Outputs/bindings: (none).
Calls/effect boundaries: selected.add.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[5].body[7].body[2].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[7].body[2].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:73`; AST `ec99ea1b1aaab3ab414875620660191a2bb130b1499c49b30a4d2fccca28a70c`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ancestor, selected. Outputs/bindings: (none).
Calls/effect boundaries: selected.add.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[7].body[2].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[7].body[2].body[0].body[1]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:74`; AST `c03f05ed75d424f2b2ec867fb7af802a7515d870db2922b6ace3c08ae2a42b3b`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ancestor, pending. Outputs/bindings: (none).
Calls/effect boundaries: pending.append.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[5].body[7].body[2].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[7].body[2].body[0].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:74`; AST `1f4ccbf08b1678df0c7c38f3a544222b1727ed365102028e05856bbca8efb3d9`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ancestor, pending. Outputs/bindings: (none).
Calls/effect boundaries: pending.append.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[7].body[2].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[8]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:75`; AST `5563638ac9b981a191e6c4f760585620e36c277be986945ef5beadf4c5f11316`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, record, selected. Outputs/bindings: a, prior.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[5].body[5].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[8].value::ListComp

Source: `infra/agentinfra/roadmap_runtime.py:75`; AST `4ca34ce9e4d1bc6c69578dc8e02f1fae5d9f9c34c3da7c8af7e7cb24b2e9c862`.

Rust module: `infra::agentinfra::roadmap_runtime`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: a, record, selected. Outputs/bindings: a.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered ListComp evaluation at root.body[11].body[5].body[5].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[9]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:76`; AST `037b140d766aa6136e7e11e92a12eda18f866488ff25ff60bc7791433dc8ed51`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: prior. Outputs/bindings: bounded_prior.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[5].body[5].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[10]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:77`; AST `38895fbbdeada44b277e8723344eebb0bb74a6dd41944172ccec7980e25d134b`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: generation.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[5].body[5].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[11]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:78`; AST `1de20da7789804482f4ad2bd57cb0362185fba298cea1354a49cb88a05c3e7df`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: generation_parent.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[5].body[5].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12]::If

Source: `infra/agentinfra/roadmap_runtime.py:79`; AST `1964e737002a18a9098ccfd08712002361427fe38f11f03d97c94d45f0bec306`.

Rust module: `infra::agentinfra::roadmap_runtime`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, atomic_write_json, bindings_current, confined_path, dict, digest, generation, inputs, k, native_control, operation, previous, prior, read_json, receipt, record, require, reusable, reversed, self, spec, spec_binding, successful, supersedes, v, validate_tool_receipt, work_id. Outputs/bindings: a, bounded_prior, generation, generation_parent, k, previous, receipt, reusable, spec, spec_binding, successful, supersedes, v.
Calls/effect boundaries: a.get, a.get('operation', {}).get, atomic_write_json, bindings_current, confined_path, dict, digest, operation.get, previous.get, previous.get('operation', {}).get, prior[-1].get, read_json, receipt.get, require, reversed, spec.get, spec.items, successful.get, successful.setdefault, successful['reuse_consumers'].append, validate_tool_receipt.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered If evaluation at root.body[11].body[5].body[5].body[12]; no call, error or mutation may be omitted. Condition: operation is not None
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:80`; AST `2dfeda11bd675aa86e9d07a9f0632329754a908f0125226080cb9a7d2c17d6bf`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: inputs, operation, require. Outputs/bindings: (none).
Calls/effect boundaries: operation.get, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[5].body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:80`; AST `3541000dc0c04f5f3751bcc28214277869284463f2c42894880e242df6ced4a3`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inputs, operation, require. Outputs/bindings: (none).
Calls/effect boundaries: operation.get, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[12].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[0].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:80`; AST `464135bbf5bc43d858d4e97bf86c0ddb44a149c00bd3c49c1e2749e3b5eefa03`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: operation. Outputs/bindings: (none).
Calls/effect boundaries: operation.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[12].body[0].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[0].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_runtime.py:80`; AST `e6e06240f8dc45b36481afab20f4c9904fa46c373b009bb586c1b1bbb3838d44`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: operation. Outputs/bindings: (none).
Calls/effect boundaries: operation.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[12].body[0].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[0].value.args[0].values[2].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:81`; AST `4f933458f7d2be92b9c658830428882aa62df4de02da6155fc8502232ce44149`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: operation. Outputs/bindings: (none).
Calls/effect boundaries: operation.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[12].body[0].value.args[0].values[2].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[1]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:82`; AST `f3483c0a76f3550c2661e5f87602a8fe0c92bc763e670540f2a5f877185bcb35`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, inputs, record. Outputs/bindings: a, reusable.
Calls/effect boundaries: a.get, a.get('operation', {}).get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[5].body[5].body[12].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[1].value::ListComp

Source: `infra/agentinfra/roadmap_runtime.py:82`; AST `d31020b5897ccfb659f840b5ca48a5e944e2a9af9dcf4ad80cba645561fb6cb0`.

Rust module: `infra::agentinfra::roadmap_runtime`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: a, inputs, record. Outputs/bindings: a.
Calls/effect boundaries: a.get, a.get('operation', {}).get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered ListComp evaluation at root.body[11].body[5].body[5].body[12].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[1].value.generators[0].ifs[0].values[2].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:83`; AST `82bcd41edb4737254b542942ef5c575c84f1fe74a89f612f8dd5f69ed5ce593c`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.get, a.get('operation', {}).get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[12].body[1].value.generators[0].ifs[0].values[2].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[1].value.generators[0].ifs[0].values[2].left.func.value::Call

Source: `infra/agentinfra/roadmap_runtime.py:83`; AST `1d17b4668c3ec9fdcd025952a68687a28454394a15c49fb432f456618dbba871`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[12].body[1].value.generators[0].ifs[0].values[2].left.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[2]::For

Source: `infra/agentinfra/roadmap_runtime.py:84`; AST `b745e9dde4bd9e81dc3343eaad0dc759111f759f3a32530d4b1c75857a7c37f4`.

Rust module: `infra::agentinfra::roadmap_runtime`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: atomic_write_json, bindings_current, dict, receipt, record, reusable, reversed, self, successful, work_id. Outputs/bindings: receipt, successful.
Calls/effect boundaries: atomic_write_json, bindings_current, dict, receipt.get, reversed, successful.get, successful.setdefault, successful['reuse_consumers'].append.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered For evaluation at root.body[11].body[5].body[5].body[12].body[2]; no call, error or mutation may be omitted. Iteration: successful in reversed(reusable)
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[2].iter::Call

Source: `infra/agentinfra/roadmap_runtime.py:84`; AST `f1a7557a5ead56ba5b5abedeb02eed67ef5cc1e579714ee74d36ef73c2d3cb13`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: reusable, reversed. Outputs/bindings: (none).
Calls/effect boundaries: reversed.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[12].body[2].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[2].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:85`; AST `277dd7d695dcaefdee35df309723027e6e660a020ee27fc5d2f1dd6248802bf9`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: successful. Outputs/bindings: receipt.
Calls/effect boundaries: successful.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[5].body[5].body[12].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:85`; AST `84c5ab4b0436dabeb96637592785102fbd49fa6dd24e4bf18b569f3e58becf2a`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: successful. Outputs/bindings: (none).
Calls/effect boundaries: successful.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[12].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[2].body[1]::If

Source: `infra/agentinfra/roadmap_runtime.py:86`; AST `712c926475b8fdd02b6c426203aa570e1d22aa4a4ff722a527f16be460e70394`.

Rust module: `infra::agentinfra::roadmap_runtime`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: atomic_write_json, bindings_current, dict, receipt, record, self, successful, work_id. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json, bindings_current, dict, receipt.get, successful.setdefault, successful['reuse_consumers'].append.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered If evaluation at root.body[11].body[5].body[5].body[12].body[2].body[1]; no call, error or mutation may be omitted. Condition: bindings_current(self.root, receipt.get('artifacts', []))
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[2].body[1].test::Call

Source: `infra/agentinfra/roadmap_runtime.py:86`; AST `b64e1ff542d5bbd7675e74f9cc7b20734ef937d4434d9f2369340717a2e5e1af`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, receipt, self. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, receipt.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[12].body[2].body[1].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[2].body[1].test.args[1]::Call

Source: `infra/agentinfra/roadmap_runtime.py:86`; AST `096f2d9b15cdf7df0b0beb2ac05443c841e885eefe54ea6594d034111789c847`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: receipt. Outputs/bindings: (none).
Calls/effect boundaries: receipt.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[12].body[2].body[1].test.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[2].body[1].body[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:87`; AST `29cfd3480aa6cd4392f36ce439e233c24a50dab981a5dc3157507db56f546328`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: successful. Outputs/bindings: (none).
Calls/effect boundaries: successful.setdefault.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[5].body[12].body[2].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[2].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:87`; AST `d4f2b2dc1c9c5f2e1bd4b6c4f74f47c0e4a9e498a566cb406c97623dff19cde6`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: successful. Outputs/bindings: (none).
Calls/effect boundaries: successful.setdefault.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[12].body[2].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[2].body[1].body[1]::If

Source: `infra/agentinfra/roadmap_runtime.py:88`; AST `a15c9ec828119ff0a1bf98beffcccfa529bfc04d844c8626db9c49377441c9ea`.

Rust module: `infra::agentinfra::roadmap_runtime`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: successful, work_id. Outputs/bindings: (none).
Calls/effect boundaries: successful['reuse_consumers'].append.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered If evaluation at root.body[11].body[5].body[5].body[12].body[2].body[1].body[1]; no call, error or mutation may be omitted. Condition: work_id not in successful['reuse_consumers']
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[2].body[1].body[1].body[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:89`; AST `9dad778ad75fad019b8d2b03773f8dd0187c8d36f3d5ea44b1efe4ae857fb379`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: successful, work_id. Outputs/bindings: (none).
Calls/effect boundaries: successful['reuse_consumers'].append.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[5].body[12].body[2].body[1].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[2].body[1].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:89`; AST `c3c8fb9f5a6e88d7270da64b5f6c9563e0723ffb2656e9b0c79253908c34ca50`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: successful, work_id. Outputs/bindings: (none).
Calls/effect boundaries: successful['reuse_consumers'].append.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[12].body[2].body[1].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[2].body[1].body[2]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:90`; AST `39653ba93071c48ea5664f41495c0b9b4c456ea6c7027a39f271248d5232ec2e`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_json, record, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[5].body[12].body[2].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[2].body[1].body[2].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:90`; AST `e0ebb6df18f3acd72b73864198de1922264a5591e4adfd3e452231c9bafa9477`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_json, record, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[12].body[2].body[1].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[2].body[1].body[3]::Return

Source: `infra/agentinfra/roadmap_runtime.py:91`; AST `d61f06587ad287a73c2715937781061eb8023f8282e18fe728342ce042fad7fe`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, successful. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Return evaluation at root.body[11].body[5].body[5].body[12].body[2].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[2].body[1].body[3].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:91`; AST `92186335b372f55cdc65bbe00d41d5f14d12963848f0ad267f17bb4010318b17`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, successful. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[12].body[2].body[1].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3]::If

Source: `infra/agentinfra/roadmap_runtime.py:92`; AST `f300e9e926ce8629bd7f56bb90e57f7543c0c1bafe582e5db2af867eb1c62e24`.

Rust module: `infra::agentinfra::roadmap_runtime`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, bindings_current, confined_path, digest, generation, inputs, k, native_control, operation, previous, prior, read_json, require, self, spec, spec_binding, supersedes, v, validate_tool_receipt. Outputs/bindings: a, bounded_prior, generation, generation_parent, k, previous, spec, spec_binding, supersedes, v.
Calls/effect boundaries: a.get, bindings_current, confined_path, digest, operation.get, previous.get, previous.get('operation', {}).get, prior[-1].get, read_json, require, spec.get, spec.items, validate_tool_receipt.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered If evaluation at root.body[11].body[5].body[5].body[12].body[3]; no call, error or mutation may be omitted. Condition: not native_control and prior
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:93`; AST `863011bd28cfaf0b3fae7ae31a1e72b37fb631b3eca15cb443536019ff4a894b`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: prior. Outputs/bindings: generation.
Calls/effect boundaries: prior[-1].get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[5].body[5].body[12].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:93`; AST `38c3e4bea138fce9d24596bbf8185843bd8e884dd6e3ae7e3306a5e89f21f476`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: prior. Outputs/bindings: (none).
Calls/effect boundaries: prior[-1].get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[12].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3].body[1]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:94`; AST `8995014b51001beff58927bf5d93af4972b417704cce1ee27dc890493b18ccd3`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: operation. Outputs/bindings: supersedes.
Calls/effect boundaries: operation.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[5].body[5].body[12].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:94`; AST `68e6b0582f728a50779c3141b19eab309262da235bab6e1bfc2c876f53ec373f`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: operation. Outputs/bindings: (none).
Calls/effect boundaries: operation.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[12].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3].body[2]::If

Source: `infra/agentinfra/roadmap_runtime.py:95`; AST `a89116479283bbbaa78b5f8af2ac4a75331ca67b9e204ec11d1acb6febc5c551`.

Rust module: `infra::agentinfra::roadmap_runtime`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: a, bindings_current, confined_path, digest, generation, inputs, k, previous, prior, read_json, require, self, spec, spec_binding, supersedes, v, validate_tool_receipt. Outputs/bindings: a, bounded_prior, generation, generation_parent, k, previous, spec, spec_binding, v.
Calls/effect boundaries: a.get, bindings_current, confined_path, digest, previous.get, previous.get('operation', {}).get, read_json, require, spec.get, spec.items, validate_tool_receipt.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered If evaluation at root.body[11].body[5].body[5].body[12].body[3].body[2]; no call, error or mutation may be omitted. Condition: supersedes
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3].body[2].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:96`; AST `e5970de016d1c91810bb36c6c223c7fe66f67332b07c5d09e0d8383dc377299b`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: prior. Outputs/bindings: previous.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[5].body[5].body[12].body[3].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3].body[2].body[1]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:97`; AST `ab805462ba72ad772e76bfea22ae0f0918a4adb2e2089819c2b0cd66ffc45839`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: inputs, previous, require, supersedes. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[5].body[12].body[3].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3].body[2].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:97`; AST `c1628b50f584c5323a4ff8632b1558d757e7982ec66dbb8f02a8e9617195e3c1`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inputs, previous, require, supersedes. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[12].body[3].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3].body[2].body[2]::ImportFrom

Source: `infra/agentinfra/roadmap_runtime.py:99`; AST `a7922dc8a0d82ef86d47d41024c804cc71a8264999535162870e84029b69ce01`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered ImportFrom evaluation at root.body[11].body[5].body[5].body[12].body[3].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3].body[2].body[3]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:100`; AST `2389dee401f85883e792caa6f1637a3cc390f96b512f3e9034a5e608474f8f00`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: previous. Outputs/bindings: spec_binding.
Calls/effect boundaries: previous.get, previous.get('operation', {}).get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[5].body[5].body[12].body[3].body[2].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3].body[2].body[3].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:100`; AST `04f7bc7a00de4cd8dd509cf1e089ccac179ddf82a317460a77bb104329f217ad`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: previous. Outputs/bindings: (none).
Calls/effect boundaries: previous.get, previous.get('operation', {}).get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[12].body[3].body[2].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3].body[2].body[3].value.func.value::Call

Source: `infra/agentinfra/roadmap_runtime.py:100`; AST `82bc6924daa04229b599861c8c4fb3e00b4f268be1eddd3a622cb4668e6ef385`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: previous. Outputs/bindings: (none).
Calls/effect boundaries: previous.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[12].body[3].body[2].body[3].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3].body[2].body[4]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:101`; AST `b8cef0a97d5050a2a2567e3073fbbfd8cbb4d78ce573b4e35b27837668e28410`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bindings_current, require, self, spec_binding. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[5].body[12].body[3].body[2].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3].body[2].body[4].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:101`; AST `b1b7f89a77f39c5918a943567d45a151047192420d5c7f8f2aac22a242d7741d`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, require, self, spec_binding. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[12].body[3].body[2].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3].body[2].body[4].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_runtime.py:101`; AST `8719e35d19efd5f0901cc62f8e610529d7061522eafa1c3a2878778694d941c5`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, self, spec_binding. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[12].body[3].body[2].body[4].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3].body[2].body[5]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:102`; AST `a11d092a2706ac047f59ef5d6ce613a1c8286e0a8b050f275e18cb2c116db6b8`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, read_json, self, spec_binding. Outputs/bindings: spec.
Calls/effect boundaries: confined_path, read_json.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[5].body[5].body[12].body[3].body[2].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3].body[2].body[5].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:102`; AST `96508da5c22f6e4d20c8174bde6a811f86ea93631b6f84cc765841b6ef4c8b5c`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, read_json, self, spec_binding. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, read_json.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[12].body[3].body[2].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3].body[2].body[5].value.args[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:102`; AST `7e0fd25676c92e27c907d17bf8feac1c334a0b82154ba19233dacd9884cceb7e`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, self, spec_binding. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[12].body[3].body[2].body[5].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3].body[2].body[6]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:103`; AST `cf65721e0d06099bd6491841386a16a406186f6b3e7acdc94e25cee444d7fa0e`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, k, previous, require, spec, v. Outputs/bindings: k, v.
Calls/effect boundaries: digest, require, spec.get, spec.items.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[5].body[12].body[3].body[2].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3].body[2].body[6].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:103`; AST `644849370e26d1d6528ba8e64c7d01f3fbca6ab1e582d06b37edb37c288f896a`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, k, previous, require, spec, v. Outputs/bindings: k, v.
Calls/effect boundaries: digest, require, spec.get, spec.items.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[12].body[3].body[2].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3].body[2].body[6].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:103`; AST `1daebf505b3c7deccc20813a3c7655e38f0769d785c525c8e7b768185ba07030`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: spec. Outputs/bindings: (none).
Calls/effect boundaries: spec.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[12].body[3].body[2].body[6].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3].body[2].body[6].value.args[0].comparators[1]::Call

Source: `infra/agentinfra/roadmap_runtime.py:103`; AST `a3edc4c9024d1b0be963df0d4ef5d05580df1c934cd81bb99aea97e6e77add4e`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, k, spec, v. Outputs/bindings: k, v.
Calls/effect boundaries: digest, spec.items.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[12].body[3].body[2].body[6].value.args[0].comparators[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3].body[2].body[6].value.args[0].comparators[1].args[0]::DictComp

Source: `infra/agentinfra/roadmap_runtime.py:103`; AST `b250ca31563e6ab580c4e0c6b6c261a75ca997bde5df3bf9ce944a0f6531e248`.

Rust module: `infra::agentinfra::roadmap_runtime`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: k, spec, v. Outputs/bindings: k, v.
Calls/effect boundaries: spec.items.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered DictComp evaluation at root.body[11].body[5].body[5].body[12].body[3].body[2].body[6].value.args[0].comparators[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3].body[2].body[6].value.args[0].comparators[1].args[0].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_runtime.py:103`; AST `5e59911ed4fdf1484be166cd57598539f6a94d16ffb2d4dfd28c4893ec603954`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: spec. Outputs/bindings: (none).
Calls/effect boundaries: spec.items.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[12].body[3].body[2].body[6].value.args[0].comparators[1].args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3].body[2].body[7]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:105`; AST `446324b4c0729c0533a0dfeb6116486c4a2a99ebd9b117e00e6043c7d556116c`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: previous, self, spec, validate_tool_receipt. Outputs/bindings: (none).
Calls/effect boundaries: validate_tool_receipt.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[5].body[12].body[3].body[2].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3].body[2].body[7].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:105`; AST `366da798cddb3dce81d308dfaf99b0ad4d066ea6cf8f8377649e1716a355dbac`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: previous, self, spec, validate_tool_receipt. Outputs/bindings: (none).
Calls/effect boundaries: validate_tool_receipt.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[12].body[3].body[2].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3].body[2].body[8]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:106`; AST `df0a71c6f24811e3616396df380dbc5b84d0ab2064d6776985dfebec1f63cd89`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: previous, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[5].body[12].body[3].body[2].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3].body[2].body[8].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:106`; AST `b0b1f2e0879b02e95f41ff4dbac01161204385ccbcd0f1b1388558cddc05ed1e`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: previous, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[12].body[3].body[2].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3].body[2].body[9]::AugAssign

Source: `infra/agentinfra/roadmap_runtime.py:108`; AST `aaffbb3a825292f0279e280f245c7a98f8f31f87c75bcd45b7180314e1e3c2cc`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: generation.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered AugAssign evaluation at root.body[11].body[5].body[5].body[12].body[3].body[2].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3].body[2].body[10]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:109`; AST `33bb85bb36ff782a74d90090b691b4f16008c9816cfba70e569574fe471ef32f`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: supersedes. Outputs/bindings: generation_parent.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[5].body[5].body[12].body[3].body[2].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3].body[2].body[11]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:110`; AST `1ba458fefa24146c30dfd1fd80ba5a7e7f09449245f5c93a897ff9ac4f9de4b8`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: bounded_prior.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[5].body[5].body[12].body[3].body[2].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3].body[2].orelse[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:112`; AST `4ff9070ab6b10e144a64478750091b42c54d9db2c8f91554e9d00cc104a8b892`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: inputs, prior, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[5].body[12].body[3].body[2].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3].body[2].orelse[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:112`; AST `fb8022fdaefe20f7444aa57376149691b831765e8857273615028abeed1e5964`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inputs, prior, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[12].body[3].body[2].orelse[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3].body[2].orelse[1]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:114`; AST `7e878df634422208bcaa77215d2ab04dae25c927fc3a46e0c47c8e13cd45a506`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, generation, prior. Outputs/bindings: a, bounded_prior.
Calls/effect boundaries: a.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[5].body[5].body[12].body[3].body[2].orelse[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3].body[2].orelse[1].value::ListComp

Source: `infra/agentinfra/roadmap_runtime.py:114`; AST `7f88b44f23b86d4a881a9aae091008964424cb3cdf573f105658b350c826111e`.

Rust module: `infra::agentinfra::roadmap_runtime`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: a, generation, prior. Outputs/bindings: a.
Calls/effect boundaries: a.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered ListComp evaluation at root.body[11].body[5].body[5].body[12].body[3].body[2].orelse[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[12].body[3].body[2].orelse[1].value.generators[0].ifs[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:114`; AST `a8b6eb84d20ef6e37f6388125229d4c528178302c1775be3767296cd75749820`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[12].body[3].body[2].orelse[1].value.generators[0].ifs[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[13]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:115`; AST `9e2e189575ad9c29c56864582f9041b6986912484e2395d8e6e661a3410171f3`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, any, prior, require. Outputs/bindings: a.
Calls/effect boundaries: any, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[5].body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[13].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:115`; AST `3c38a72856553d5c434e909fd4ae145eac7bf8446bca16ad70c3fb45b7b5350c`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, any, prior, require. Outputs/bindings: a.
Calls/effect boundaries: any, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[13].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[13].value.args[0].operand::Call

Source: `infra/agentinfra/roadmap_runtime.py:115`; AST `0c6799aa907ad169146daaee66073b6174234e139128234a79156d4b2ebeda2d`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, any, prior. Outputs/bindings: a.
Calls/effect boundaries: any.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[13].value.args[0].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[13].value.args[0].operand.args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_runtime.py:115`; AST `8a7d5fe1ed41edb414ae9932a9816f5ba59267137bef9f90b7f7dcacce6ceb98`.

Rust module: `infra::agentinfra::roadmap_runtime`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: a, prior. Outputs/bindings: a.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[11].body[5].body[5].body[13].value.args[0].operand.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[14]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:116`; AST `d08faefd03d6489f6ef2ac996dcd9ccebaaf365018efa1c74c918b43bfe0a134`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, any, inputs, prior, require. Outputs/bindings: a.
Calls/effect boundaries: any, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[5].body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[14].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:116`; AST `ac4d1c553a8c47c0f5a5d2d23e8169103c7c28d587178a88a7048ebd50abee20`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, any, inputs, prior, require. Outputs/bindings: a.
Calls/effect boundaries: any, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[14].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[14].value.args[0].operand::Call

Source: `infra/agentinfra/roadmap_runtime.py:116`; AST `fed5ed9c4fb238b253f82e8a7f2a19f3771a6e73715f04ddc0581372625d0b4e`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, any, inputs, prior. Outputs/bindings: a.
Calls/effect boundaries: any.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[14].value.args[0].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[14].value.args[0].operand.args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_runtime.py:116`; AST `13f362874b9ee538d6c9f583dfe103a819c65a15f6b6df4d82432666fe533471`.

Rust module: `infra::agentinfra::roadmap_runtime`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: a, inputs, prior. Outputs/bindings: a.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[11].body[5].body[5].body[14].value.args[0].operand.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[15]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:117`; AST `056b958db10bb6e9e825c5859a65107891162d1e6ee6df84d16ec87d5f1b9b0a`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bounded_prior, len, max_attempts, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[5].body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[15].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:117`; AST `c665a7b2f287b9762a360aa1798f4e1aca293dddb4dbc5851e2164362d7bd64e`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bounded_prior, len, max_attempts, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[15].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[15].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:117`; AST `765fc540ea5cdb4d3c879e5893a828d47e59a9d8bf5104b3378adb6169aa0b4e`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bounded_prior, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[15].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[16]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:118`; AST `5409cdd5b4650430c2a73cacabdc0dbeef01a52c9787f9e4e498c0cb27222392`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, bounded_prior, require, seconds, sum, total_seconds. Outputs/bindings: a.
Calls/effect boundaries: require, sum.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[5].body[16]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[16].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:118`; AST `2a0e0c668df00a9a204c1dfeafa00171d536ad86feca24f6ade8dc1b31c84193`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, bounded_prior, require, seconds, sum, total_seconds. Outputs/bindings: a.
Calls/effect boundaries: require, sum.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[16].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[16].value.args[0].left.left::Call

Source: `infra/agentinfra/roadmap_runtime.py:118`; AST `1b6c9535ea4127f41579c0101e47a3bf4853ab543d60697a1764c334b46711ef`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, bounded_prior, sum. Outputs/bindings: a.
Calls/effect boundaries: sum.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[16].value.args[0].left.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[16].value.args[0].left.left.args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_runtime.py:118`; AST `d81488f6b2e33149bdd995fdbcffaa9a4213529cd3f23c886067d1b5dc6d47bb`.

Rust module: `infra::agentinfra::roadmap_runtime`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: a, bounded_prior. Outputs/bindings: a.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[11].body[5].body[5].body[16].value.args[0].left.left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[17]::If

Source: `infra/agentinfra/roadmap_runtime.py:119`; AST `50623fe0b7e55ea089a6d287113f34b573072fa6690f27f8dfa229ae41304bc9`.

Rust module: `infra::agentinfra::roadmap_runtime`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: bool, bounded_prior, diagnosis, inputs, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, diagnosis.strip, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered If evaluation at root.body[11].body[5].body[5].body[17]; no call, error or mutation may be omitted. Condition: bounded_prior
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[17].body[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:120`; AST `853db2afd8c28c8a33d887e96a83bfc29ef3e7c87665fe0b65ffb9fd150280a6`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, diagnosis, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, diagnosis.strip, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[5].body[17].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[17].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:120`; AST `ee171942fafcee617bf68b88d56acc2131348d87f6dccc06ff90a755a1ee0108`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, diagnosis, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, diagnosis.strip, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[17].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[17].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:120`; AST `5f161d0ee70916206cd6762d78e25cf9148e9debd7f0313e6d473e15d6cbe7ea`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, diagnosis. Outputs/bindings: (none).
Calls/effect boundaries: bool, diagnosis.strip.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[17].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[17].body[0].value.args[0].args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_runtime.py:120`; AST `7ec57aec97069b761eca95116ac27ef7ef1d814f93787c9b53931bd9f521bcd1`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: diagnosis. Outputs/bindings: (none).
Calls/effect boundaries: diagnosis.strip.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[17].body[0].value.args[0].args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[17].body[1]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:121`; AST `cda86ee595c823afe90d02cfaef0ee1c49d1f57ed600a002dacd4affe35eea63`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bounded_prior, inputs, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[5].body[17].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[17].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:121`; AST `0ce2fc1a6718040578cf449b8f220042b0d9e5598d0b4c2341971e0d59eeb70b`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bounded_prior, inputs, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[17].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[18]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:122`; AST `a5e4c849ba3b4fbcee16d01c7e2b2cd85ad1e9a6fbfb11b9b8a24830ecfaa925`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: diagnosis, digest, inputs, len, os, prior, seconds, time, work_id. Outputs/bindings: attempt.
Calls/effect boundaries: digest, len, os.getpid, time.time_ns.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[5].body[5].body[18]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[18].value.values[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:122`; AST `72625daab276fb12642547a5a4363cb6ff2bc5a0f1dd634f089ff1e0ec5de495`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, inputs, len, prior, work_id. Outputs/bindings: (none).
Calls/effect boundaries: digest, len.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[18].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[18].value.values[0].args[0].values[2].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:122`; AST `913efbe5bf6e483de6568a9d688cb27d196675409407cd117ee0c850ad45fa62`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, prior. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[18].value.values[0].args[0].values[2].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[18].value.values[6]::Call

Source: `infra/agentinfra/roadmap_runtime.py:124`; AST `ba1923643b161051a18bf7ae7386addd84146f4ab481f99d56712bc1ce97df2c`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os. Outputs/bindings: (none).
Calls/effect boundaries: os.getpid.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[18].value.values[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[18].value.values[7]::Call

Source: `infra/agentinfra/roadmap_runtime.py:125`; AST `d7bb4f9a8f02ae840b0ecfbf4a0bc46a103c9ee80044d3e746466d336dbaf7ae`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: time. Outputs/bindings: (none).
Calls/effect boundaries: time.time_ns.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[18].value.values[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[19]::If

Source: `infra/agentinfra/roadmap_runtime.py:126`; AST `2e3c0b2733641117cdb80c3b879edb7f5f9be49f9525632448a538394b34672a`.

Rust module: `infra::agentinfra::roadmap_runtime`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: attempt, selected, sorted. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered If evaluation at root.body[11].body[5].body[5].body[19]; no call, error or mutation may be omitted. Condition: selected
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[19].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:127`; AST `ea34d11b7f97d9b8fbb69de922186741b9d0a38b072e14d3f51018b89e855194`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: attempt, selected, sorted. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[5].body[5].body[19].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[19].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:127`; AST `147f6d5e20829fc9a7dc9eb9ad77f8370cf83e0b48d7af6d1bef8e658bbf78af`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: selected, sorted. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[19].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[20]::If

Source: `infra/agentinfra/roadmap_runtime.py:128`; AST `5d458a417ceca109f25937bd1b10781c17fb6d2de5b7537173ffadbc2b982e0b`.

Rust module: `infra::agentinfra::roadmap_runtime`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: attempt, bounded_prior, generation, generation_parent, len, operation. Outputs/bindings: (none).
Calls/effect boundaries: attempt.update, len.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered If evaluation at root.body[11].body[5].body[5].body[20]; no call, error or mutation may be omitted. Condition: operation is not None
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[20].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:129`; AST `0a4b22145e85d4da2757ff2cdd6f57b8483e81e308d6595a3dc68db384420ac5`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: attempt, operation. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[5].body[5].body[20].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[20].body[1]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:130`; AST `0032b35e4e97e240f686b49aab64914f16686e1f36c5bee19ea2521a1488a29f`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: attempt, bounded_prior, generation, generation_parent, len. Outputs/bindings: (none).
Calls/effect boundaries: attempt.update, len.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[5].body[20].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[20].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:130`; AST `ab012df9fa613a219112a9a3fb5e89e88d29226da9e4db672f5fa8ed1f5f5bf3`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: attempt, bounded_prior, generation, generation_parent, len. Outputs/bindings: (none).
Calls/effect boundaries: attempt.update, len.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[20].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[20].body[1].value.keywords[2].value.left::Call

Source: `infra/agentinfra/roadmap_runtime.py:131`; AST `765fc540ea5cdb4d3c879e5893a828d47e59a9d8bf5104b3378adb6169aa0b4e`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bounded_prior, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[20].body[1].value.keywords[2].value.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[21]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:132`; AST `72ad7243e175c897858cde4cb3d89e1c1586fe12d477ff19b5d4b77ea35ae6cd`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: attempt, record. Outputs/bindings: (none).
Calls/effect boundaries: record['attempts'].append.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[5].body[21]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[21].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:132`; AST `876c585b5b90aaeea31ed0ebf97f0192892efe1c54f8971afdc17736d4a0e621`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: attempt, record. Outputs/bindings: (none).
Calls/effect boundaries: record['attempts'].append.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[21].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[22]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:133`; AST `39653ba93071c48ea5664f41495c0b9b4c456ea6c7027a39f271248d5232ec2e`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_json, record, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[5].body[22]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[22].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:133`; AST `e0ebb6df18f3acd72b73864198de1922264a5591e4adfd3e452231c9bafa9477`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_json, record, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].body[22].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].body[23]::Return

Source: `infra/agentinfra/roadmap_runtime.py:134`; AST `e266cd7ee7f5bdfcac0bb2a29b163bd7502edefad7a236c7df360c13dc73bb7e`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: attempt. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Return evaluation at root.body[11].body[5].body[5].body[23]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].finalbody[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:136`; AST `9aa6f04fc26ee6b3f6fe1a19158adb3cfde13709dcae4a7cc38bccbb2655afb2`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[5].body[5].finalbody[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::_reserve::root.body[11].body[5].body[5].finalbody[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:136`; AST `107c5710331db61e695f7d71256d48862412d15c223e204da5c71c497352b634`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].body[5].finalbody[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6]::FunctionDef

Source: `infra/agentinfra/roadmap_runtime.py:138`; AST `b677e9e22f2723bf095aba6a56122837750b593e83708ca452f99ba844865cd5`.

Rust module: `infra::agentinfra::roadmap_runtime`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileLock, a, atomic_write_json, attempt, dict, ident, len, lock, matches, old, operation, record, require, self, str. Outputs/bindings: a, attempt, lock, matches, old, record.
Calls/effect boundaries: FileLock, atomic_write_json, attempt.get, len, lock.acquire, lock.release, old.get, operation.get, require, self.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:139`; AST `0cb69e8d62006f551bc12b04a0252e103958a7fbde12738b296ffff17425ecfc`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[1]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:140`; AST `dab9a4506c3ed452a12e325f5654e03121ff19238e7a1e68bc4529d9c45918f4`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileLock, self. Outputs/bindings: lock.
Calls/effect boundaries: FileLock.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:140`; AST `8bb9d884dbf818fe768f630f0adc7bcd674a3bc7408e6e8aa9f5ddb7c7eeeb79`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileLock, self. Outputs/bindings: (none).
Calls/effect boundaries: FileLock.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[2]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:140`; AST `2bcfe51cf785ee29160140309ca2724ded506c99a694a1cd40da99965fea32f6`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[6].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[2].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:140`; AST `19f113b1ff996d6a4e1349d4f629dcb1414895f291ae11a26e3a1c7c22771cf0`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[3]::Try

Source: `infra/agentinfra/roadmap_runtime.py:141`; AST `89a6944616a6a7ef31e5e25c02bc42c715bdb7bbce1df4fbc9eacd09aa3da24b`.

Rust module: `infra::agentinfra::roadmap_runtime`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: a, atomic_write_json, attempt, ident, len, lock, matches, old, operation, record, require, self. Outputs/bindings: a, attempt, matches, old, record.
Calls/effect boundaries: atomic_write_json, attempt.get, len, lock.release, old.get, operation.get, require, self.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Try evaluation at root.body[11].body[6].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[3].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:142`; AST `8d60c6cf06a37f3a21e36d8d4fc569b1d94d00284e5e8e23781c46e0c0bd8c8b`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: record.
Calls/effect boundaries: self.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[6].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:142`; AST `1a6cd88d33383d245bb90e4e5f924f99f090d6bd29a5c43fab9e8ffb18d19d91`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[3].body[1]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:143`; AST `cf32e9bf9b8a72d66b64531668c804f7085a2f6675610c277caa371b3b7106b2`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, ident, record. Outputs/bindings: a, matches.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[6].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[3].body[1].value::ListComp

Source: `infra/agentinfra/roadmap_runtime.py:143`; AST `fb765ce6077cad522849ac1bfa4314dacb67a58cf6789a9c53a4b0d2d988644b`.

Rust module: `infra::agentinfra::roadmap_runtime`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: a, ident, record. Outputs/bindings: a.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered ListComp evaluation at root.body[11].body[6].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[3].body[2]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:144`; AST `4c34fe2d882e5c297a361680e0a288f39bff8353ef58c0d017cd3baf346331e9`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, matches, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[6].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[3].body[2].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:144`; AST `6848356027a2c11e7a02c9c7b476060e8476929e09e481c989311cf941e283e2`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, matches, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[3].body[2].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:144`; AST `d97f989b8f8f52f8f40688f8e2e1ccaded6f1cf09b4ecf82beecbcc52f1add97`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, matches. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[3].body[2].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[3].body[3]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:145`; AST `ab6dc53f6326db9a8e6dc047bb6479c24e82998dd1e545e1dbe5af6d2a0def5d`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: matches. Outputs/bindings: attempt.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[6].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[3].body[4]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:146`; AST `783f100c9582099efe84a4084f9f8c15d96aa777b92e57dd2cc85e3aafed3994`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: attempt. Outputs/bindings: old.
Calls/effect boundaries: attempt.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[6].body[3].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[3].body[4].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:146`; AST `466051896d4e41d42d5822c25c60cfbbb7ac9f1ff06c930d8c5a32d6501f8708`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: attempt. Outputs/bindings: (none).
Calls/effect boundaries: attempt.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[3].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[3].body[5]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:147`; AST `84be7ee0a13b0b26e1bffe5d910b072247c76426f81b61599700288c26ca30b7`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: old, operation, require. Outputs/bindings: (none).
Calls/effect boundaries: old.get, operation.get, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[6].body[3].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[3].body[5].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:147`; AST `f5c7433514786ae477cd2b3f4ca0b70cde2f01a45dca028ff02fb85f5b565244`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old, operation, require. Outputs/bindings: (none).
Calls/effect boundaries: old.get, operation.get, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[3].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[3].body[5].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:147`; AST `4f933458f7d2be92b9c658830428882aa62df4de02da6155fc8502232ce44149`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: operation. Outputs/bindings: (none).
Calls/effect boundaries: operation.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[3].body[5].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[3].body[5].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:147`; AST `e434ffb815124fd0912c0e9736b882e996db7e709cef9876a72a4f77cbbdaaab`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old. Outputs/bindings: (none).
Calls/effect boundaries: old.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[3].body[5].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[3].body[6]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:149`; AST `4a7796f37d6d8b96b7a4880434af7c62f72dacfb957864ca6cb9c3d58da2ac8c`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: old, operation, require. Outputs/bindings: (none).
Calls/effect boundaries: old.get, operation.get, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[6].body[3].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[3].body[6].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:149`; AST `f2c9c81ddcc3c8e85eb61af4bf69e1a8ae5e9567d0ff75909de8ae08552ea7af`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old, operation, require. Outputs/bindings: (none).
Calls/effect boundaries: old.get, operation.get, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[3].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[3].body[6].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:149`; AST `fdb8cf7974e74d233fcb73061ae995487562fb7243b5519d9eeda0793e7b743a`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old. Outputs/bindings: (none).
Calls/effect boundaries: old.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[3].body[6].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[3].body[6].value.args[0].values[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:149`; AST `464135bbf5bc43d858d4e97bf86c0ddb44a149c00bd3c49c1e2749e3b5eefa03`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: operation. Outputs/bindings: (none).
Calls/effect boundaries: operation.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[3].body[6].value.args[0].values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[3].body[6].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:150`; AST `8964d982a2cf791d60919594eff1e02b1a5771d4ca72a968c9a25896769dea61`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old. Outputs/bindings: (none).
Calls/effect boundaries: old.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[3].body[6].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[3].body[6].value.args[0].values[1].comparators[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:150`; AST `e6e06240f8dc45b36481afab20f4c9904fa46c373b009bb586c1b1bbb3838d44`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: operation. Outputs/bindings: (none).
Calls/effect boundaries: operation.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[3].body[6].value.args[0].values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[3].body[6].value.args[0].values[2].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:150`; AST `684e071226cc0ca572c65119d1d50776043c40e99181184019ff9dea343fdaef`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old. Outputs/bindings: (none).
Calls/effect boundaries: old.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[3].body[6].value.args[0].values[2].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[3].body[6].value.args[0].values[2].comparators[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:150`; AST `43d9eea0ad01f18a014ca904d5c835a4d9a6fb241b485a36a13dc88f722ae908`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: operation. Outputs/bindings: (none).
Calls/effect boundaries: operation.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[3].body[6].value.args[0].values[2].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[3].body[7]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:152`; AST `ef62fb0863fbca4a5091ac18e605ae3864b151c7fd9bfee17f9949895e588765`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: old, operation, require. Outputs/bindings: (none).
Calls/effect boundaries: old.get, operation.get, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[6].body[3].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[3].body[7].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:152`; AST `edfc8c8234c85266fe08d92f339e315e0477ebdb2ef1ee0a2c3342a0eaec072c`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old, operation, require. Outputs/bindings: (none).
Calls/effect boundaries: old.get, operation.get, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[3].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[3].body[7].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:152`; AST `ce55e0d5e7f7603c173546989a862533af9927e3b6377cf915b4fec9fb9a3e6f`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old. Outputs/bindings: (none).
Calls/effect boundaries: old.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[3].body[7].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[3].body[7].value.args[0].values[1].comparators[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:152`; AST `d1b59a1572edcfb63e23cfdc882395a0fb28417ad68cb420e30a424901d2dad2`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: operation. Outputs/bindings: (none).
Calls/effect boundaries: operation.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[3].body[7].value.args[0].values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[3].body[8]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:154`; AST `0a4b22145e85d4da2757ff2cdd6f57b8483e81e308d6595a3dc68db384420ac5`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: attempt, operation. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[6].body[3].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[3].body[9]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:155`; AST `39653ba93071c48ea5664f41495c0b9b4c456ea6c7027a39f271248d5232ec2e`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_json, record, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[6].body[3].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[3].body[9].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:155`; AST `e0ebb6df18f3acd72b73864198de1922264a5591e4adfd3e452231c9bafa9477`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_json, record, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[3].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[3].body[10]::Return

Source: `infra/agentinfra/roadmap_runtime.py:156`; AST `e266cd7ee7f5bdfcac0bb2a29b163bd7502edefad7a236c7df360c13dc73bb7e`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: attempt. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Return evaluation at root.body[11].body[6].body[3].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[3].finalbody[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:158`; AST `9aa6f04fc26ee6b3f6fe1a19158adb3cfde13709dcae4a7cc38bccbb2655afb2`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[6].body[3].finalbody[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::journal::root.body[11].body[6].body[3].finalbody[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:158`; AST `107c5710331db61e695f7d71256d48862412d15c223e204da5c71c497352b634`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[3].finalbody[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7]::FunctionDef

Source: `infra/agentinfra/roadmap_runtime.py:160`; AST `9a2451faf0352a6ffc2457be8bd9d57d2c152c2c360b764b7e5be7abefaae5a7`.

Rust module: `infra::agentinfra::roadmap_runtime`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileLock, all, atomic_write_json, bool, dict, event_id, field, fields, int, k, lock, origin, previous, record, require, sample, self, series, set, sorted, str, thread_id, totals, type, v, value. Outputs/bindings: field, fields, k, lock, previous, record, sample, series, v, value.
Calls/effect boundaries: FileLock, all, atomic_write_json, bool, lock.acquire, lock.release, record['usage'].setdefault, require, sample['totals'].items, self.read, set, sorted, totals.get, totals.values, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:161`; AST `a572648529af09b45dae0426aa0f325c60d190777e6991708481dcacbf33bc76`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[1]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:166`; AST `e9becc91920324cde5033a05c5852b30fadd498dae674f938a0b9e0182938ba6`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: fields.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[7].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[2]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:168`; AST `04912ed0065fe00f1e878c20245fd816a2bac2a773d14245ebb72a8b98a4b618`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, event_id, fields, origin, require, set, thread_id, totals. Outputs/bindings: (none).
Calls/effect boundaries: bool, require, set.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[7].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[2].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:168`; AST `625ba0ac617f48c17b2d1eeb5bf87475a44cb2caace2451514946d6d3820f227`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, event_id, fields, origin, require, set, thread_id, totals. Outputs/bindings: (none).
Calls/effect boundaries: bool, require, set.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[2].value.args[0].values[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:168`; AST `cd37e63e8c7eb3c36062f0fbd5dd0ea6964ef29927b2cb95206c3f8060580755`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, thread_id. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[2].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[2].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_runtime.py:168`; AST `3e92731226f2b51f589da08be39a33e83d597c14fea7e4556613d9a1dbb6d9df`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, event_id. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[2].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[2].value.args[0].values[2]::Call

Source: `infra/agentinfra/roadmap_runtime.py:168`; AST `e1c8441db53cb7008eabc68d3140492a1efad722997fa89dbb62e4aa2328414e`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, origin. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[2].value.args[0].values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[2].value.args[0].values[3].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:168`; AST `0631a7ab711297c2a499a2f1420548869827c217e225e587e796dcd4ca714dab`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: set, totals. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[2].value.args[0].values[3].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[3]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:170`; AST `fafd8b7b882ad4bb63a5be85e920cfee9c94bd7f3d2af7e6834921395881efc8`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, int, require, totals, type, v. Outputs/bindings: v.
Calls/effect boundaries: all, require, totals.values, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[7].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[3].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:170`; AST `b241c05ba82c364a5184918b981ca995a5809adfde3abe31c66273c15bff1f3c`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, int, require, totals, type, v. Outputs/bindings: v.
Calls/effect boundaries: all, require, totals.values, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[3].value.args[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:170`; AST `ab69dbad7dbfbef310845daa79bc1510fafffd03dae917b27a5b18513ee4c24f`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, int, totals, type, v. Outputs/bindings: v.
Calls/effect boundaries: all, totals.values, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[3].value.args[0].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_runtime.py:170`; AST `47a8bf21c667c94c6a1ec58ade14ae47fee6bd904a543c482359e7ee93601890`.

Rust module: `infra::agentinfra::roadmap_runtime`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: int, totals, type, v. Outputs/bindings: v.
Calls/effect boundaries: totals.values, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[11].body[7].body[3].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[3].value.args[0].args[0].elt.values[1].values[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:170`; AST `e048786d0fd27242ac9513214da043edf756617a572829e1cb9725342ed3dd2b`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: type, v. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[3].value.args[0].args[0].elt.values[1].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[3].value.args[0].args[0].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_runtime.py:170`; AST `3871b0b4a69af1fff9abc8804c529ccca7536ce1ce7aa08b753901397f132bbf`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: totals. Outputs/bindings: (none).
Calls/effect boundaries: totals.values.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[3].value.args[0].args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[4]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:171`; AST `72bdbb53fc1c13b5d79ff388de38f223ad13c43dee4a3a184af401300d56029f`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fields, k, origin, sorted, totals. Outputs/bindings: k, sample.
Calls/effect boundaries: sorted, totals.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[7].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[4].value.values[0]::DictComp

Source: `infra/agentinfra/roadmap_runtime.py:171`; AST `4558eb57e9fd6441b356f7f3809d80275fae372b265ab84969a77870f708f7b1`.

Rust module: `infra::agentinfra::roadmap_runtime`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: fields, k, sorted, totals. Outputs/bindings: k.
Calls/effect boundaries: sorted, totals.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered DictComp evaluation at root.body[11].body[7].body[4].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[4].value.values[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:171`; AST `a9350c2171b9a491519feb0efd561aba77e736bc6b442d46c166b52988897b60`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: k, totals. Outputs/bindings: (none).
Calls/effect boundaries: totals.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[4].value.values[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[4].value.values[0].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_runtime.py:171`; AST `2b0a6dd4c8426439a34e6180d12b8864413cd313b56a0f8f70a9175517c78b41`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fields, sorted. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[4].value.values[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[5]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:172`; AST `30cfeaff8693645f6eb60a0c52e4b95f14af5ca6b21b27ff5e8d3725ed5e0586`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileLock, self. Outputs/bindings: lock.
Calls/effect boundaries: FileLock.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[7].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[5].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:172`; AST `6e746ae5ac8c28f57847e70ae31fff7c82ec2eb0aa580929fae13d2361d7c168`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileLock, self. Outputs/bindings: (none).
Calls/effect boundaries: FileLock.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[6]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:172`; AST `2bcfe51cf785ee29160140309ca2724ded506c99a694a1cd40da99965fea32f6`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[7].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[6].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:172`; AST `19f113b1ff996d6a4e1349d4f629dcb1414895f291ae11a26e3a1c7c22771cf0`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[7]::Try

Source: `infra/agentinfra/roadmap_runtime.py:173`; AST `a3f12962c4a6420622ef499bd102f6edcc1d005fc69847249f63760908a5ed24`.

Rust module: `infra::agentinfra::roadmap_runtime`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: atomic_write_json, event_id, field, fields, k, lock, previous, record, require, sample, self, series, sorted, thread_id, value. Outputs/bindings: field, k, previous, record, series, value.
Calls/effect boundaries: atomic_write_json, lock.release, record['usage'].setdefault, require, sample['totals'].items, self.read, sorted.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Try evaluation at root.body[11].body[7].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[7].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:174`; AST `8d60c6cf06a37f3a21e36d8d4fc569b1d94d00284e5e8e23781c46e0c0bd8c8b`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: record.
Calls/effect boundaries: self.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[7].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[7].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:174`; AST `1a6cd88d33383d245bb90e4e5f924f99f090d6bd29a5c43fab9e8ffb18d19d91`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[7].body[1]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:175`; AST `0120b7763499c39196ba084ea20d2f8cb0524b42fcf96ea8181d413660421cd4`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fields, k, record, sorted, thread_id. Outputs/bindings: k, series.
Calls/effect boundaries: record['usage'].setdefault, sorted.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[7].body[7].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[7].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:175`; AST `4cc3a4a231f2544bc03f9cb5b53f838dfac7522839e5e22dd074190eb2eccd7c`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fields, k, record, sorted, thread_id. Outputs/bindings: k.
Calls/effect boundaries: record['usage'].setdefault, sorted.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[7].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[7].body[1].value.args[1].values[2]::DictComp

Source: `infra/agentinfra/roadmap_runtime.py:177`; AST `13ba435387d08ccb378aaf3b98fcd30d6d13a1aac6d3b13cceba99d59809bee8`.

Rust module: `infra::agentinfra::roadmap_runtime`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: fields, k, sorted. Outputs/bindings: k.
Calls/effect boundaries: sorted.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered DictComp evaluation at root.body[11].body[7].body[7].body[1].value.args[1].values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[7].body[1].value.args[1].values[2].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_runtime.py:177`; AST `2b0a6dd4c8426439a34e6180d12b8864413cd313b56a0f8f70a9175517c78b41`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fields, sorted. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[7].body[1].value.args[1].values[2].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[7].body[2]::If

Source: `infra/agentinfra/roadmap_runtime.py:178`; AST `eeaf49059694f67af2197227cc0ed050e4df1e7e5fcde5144bbf41641f0d4790`.

Rust module: `infra::agentinfra::roadmap_runtime`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: event_id, require, sample, series. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered If evaluation at root.body[11].body[7].body[7].body[2]; no call, error or mutation may be omitted. Condition: event_id in series['events']
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[7].body[2].body[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:179`; AST `259ee1fbf8e1258a9b63ae35dedf11bbce6fcebda2687c357e37cd6293c09a67`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: event_id, require, sample, series. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[7].body[7].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[7].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:179`; AST `6966e54d0d5e9b3d05aec4b82aa74ae283b1ba65047bc486c22338593df18b1d`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: event_id, require, sample, series. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[7].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[7].body[2].body[1]::Return

Source: `infra/agentinfra/roadmap_runtime.py:180`; AST `5d94030c03a62be28fd955b239310b9ec02fcdc7f5666a2c8f398f16c18928ed`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: series. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Return evaluation at root.body[11].body[7].body[7].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[7].body[3]::For

Source: `infra/agentinfra/roadmap_runtime.py:181`; AST `580f61f97e97570c02da15ec48b32780412504a532c4b35043f8855f165a3e8a`.

Rust module: `infra::agentinfra::roadmap_runtime`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: field, previous, require, sample, series, value. Outputs/bindings: field, previous, value.
Calls/effect boundaries: require, sample['totals'].items.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered For evaluation at root.body[11].body[7].body[7].body[3]; no call, error or mutation may be omitted. Iteration: (field, value) in sample['totals'].items()
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[7].body[3].iter::Call

Source: `infra/agentinfra/roadmap_runtime.py:181`; AST `cf5b5894e6b3ecd9e15061276317e58205e0934b122b527976352dd49d86b067`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: sample. Outputs/bindings: (none).
Calls/effect boundaries: sample['totals'].items.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[7].body[3].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[7].body[3].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:182`; AST `01a80cc11b8a9179a2051efa42d27e4e772e2f9026665c70d6f45a6b66dd3837`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: field, series. Outputs/bindings: previous.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[7].body[7].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[7].body[3].body[1]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:183`; AST `a0e1ec8cfd615181f2372b77f3f13a91b3c3771a3f07d9be3b173bec5fed9bb0`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: previous, require, value. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[7].body[7].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[7].body[3].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:183`; AST `921c1e4a2e938adb194a89fbc83c18dd71264a707b45c02dce310f01b72577d9`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: previous, require, value. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[7].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[7].body[4]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:185`; AST `18ec54dba4c64fbcd931328b609622385ffbf2e3982b447f18fe9777277217af`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: event_id, sample, series. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[7].body[7].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[7].body[5]::For

Source: `infra/agentinfra/roadmap_runtime.py:186`; AST `83f96d6fb8b7fcae8c3901fd0338f8cc25a54b60def9b4b789e4de649be9eaea`.

Rust module: `infra::agentinfra::roadmap_runtime`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: field, sample, series, value. Outputs/bindings: field, value.
Calls/effect boundaries: sample['totals'].items.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered For evaluation at root.body[11].body[7].body[7].body[5]; no call, error or mutation may be omitted. Iteration: (field, value) in sample['totals'].items()
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[7].body[5].iter::Call

Source: `infra/agentinfra/roadmap_runtime.py:186`; AST `cf5b5894e6b3ecd9e15061276317e58205e0934b122b527976352dd49d86b067`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: sample. Outputs/bindings: (none).
Calls/effect boundaries: sample['totals'].items.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[7].body[5].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[7].body[5].body[0]::If

Source: `infra/agentinfra/roadmap_runtime.py:187`; AST `dc6b31d096cc44b8be5d61d44a3dfce1dbc17835fcb30e6c0c0e29cadc1c586f`.

Rust module: `infra::agentinfra::roadmap_runtime`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: field, series, value. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered If evaluation at root.body[11].body[7].body[7].body[5].body[0]; no call, error or mutation may be omitted. Condition: value is not None
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[7].body[5].body[0].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:188`; AST `93365b890690631629a38dd718b6729f2f5c0b62bd0688dc410eaf9435da5af3`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: field, series, value. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[7].body[7].body[5].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[7].body[6]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:189`; AST `39653ba93071c48ea5664f41495c0b9b4c456ea6c7027a39f271248d5232ec2e`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_json, record, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[7].body[7].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[7].body[6].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:189`; AST `e0ebb6df18f3acd72b73864198de1922264a5591e4adfd3e452231c9bafa9477`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_json, record, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[7].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[7].body[7]::Return

Source: `infra/agentinfra/roadmap_runtime.py:190`; AST `5d94030c03a62be28fd955b239310b9ec02fcdc7f5666a2c8f398f16c18928ed`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: series. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Return evaluation at root.body[11].body[7].body[7].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[7].finalbody[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:192`; AST `9aa6f04fc26ee6b3f6fe1a19158adb3cfde13709dcae4a7cc38bccbb2655afb2`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[7].body[7].finalbody[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_categories::root.body[11].body[7].body[7].finalbody[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:192`; AST `107c5710331db61e695f7d71256d48862412d15c223e204da5c71c497352b634`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[7].body[7].finalbody[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::metrics::root.body[11].body[8]::FunctionDef

Source: `infra/agentinfra/roadmap_runtime.py:194`; AST `ca990b65a54f0bd7cbaf01744a2e3fc20c63fd48393bc437901a52443fbb2de0`.

Rust module: `infra::agentinfra::roadmap_runtime`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: a, attempts, dict, f, int, k, len, measured, record, s, self, sum, type, v. Outputs/bindings: a, attempts, f, k, measured, record, s, v.
Calls/effect boundaries: a.get, a.get('receipt', {}).get, len, record['usage'].items, s.items, self.read, sum, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::metrics::root.body[11].body[8].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:195`; AST `8d60c6cf06a37f3a21e36d8d4fc569b1d94d00284e5e8e23781c46e0c0bd8c8b`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: record.
Calls/effect boundaries: self.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::metrics::root.body[11].body[8].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:195`; AST `1a6cd88d33383d245bb90e4e5f924f99f090d6bd29a5c43fab9e8ffb18d19d91`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[8].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::metrics::root.body[11].body[8].body[1]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:196`; AST `dd53a45002608e0d35803af87ebfb08b2e0cc77203875c46c1a6cdc77eafc2ad`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record. Outputs/bindings: attempts.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[8].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::metrics::root.body[11].body[8].body[2]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:197`; AST `f35f7cd030cc83f8964b6ae1590924c976fc4d06488ebb2162a63a7413b854b0`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, attempts, int, type. Outputs/bindings: a, measured.
Calls/effect boundaries: a.get, a.get('receipt', {}).get, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[8].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::metrics::root.body[11].body[8].body[2].value::ListComp

Source: `infra/agentinfra/roadmap_runtime.py:197`; AST `451cc90a52c10b3a164d5b8dfd241dc782006f0c2dee0a3e88d9ac779ed562b2`.

Rust module: `infra::agentinfra::roadmap_runtime`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: a, attempts, int, type. Outputs/bindings: a.
Calls/effect boundaries: a.get, a.get('receipt', {}).get, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered ListComp evaluation at root.body[11].body[8].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::metrics::root.body[11].body[8].body[2].value.generators[0].ifs[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:198`; AST `f068b76a04fdac543081b68066567663386c667c5da84575c506b0232796d7e4`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, type. Outputs/bindings: (none).
Calls/effect boundaries: a.get, a.get('receipt', {}).get, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[8].body[2].value.generators[0].ifs[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::metrics::root.body[11].body[8].body[2].value.generators[0].ifs[0].left.args[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:198`; AST `0c472a23bf7ef8e4218eb735acff7a688038ede58889a5650e04ae4b53f758ca`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.get, a.get('receipt', {}).get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[8].body[2].value.generators[0].ifs[0].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::metrics::root.body[11].body[8].body[2].value.generators[0].ifs[0].left.args[0].func.value::Call

Source: `infra/agentinfra/roadmap_runtime.py:198`; AST `75581b1aaabd6631c6aa3b77866b15238db132ff961d75593a1f4402cb633f27`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[8].body[2].value.generators[0].ifs[0].left.args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::metrics::root.body[11].body[8].body[3]::Return

Source: `infra/agentinfra/roadmap_runtime.py:199`; AST `15a427171076995bfdd971c8646edede77b2f5b08cd071c87c3a3d42001e6f30`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, attempts, f, k, len, measured, record, s, sum, v. Outputs/bindings: a, f, k, s, v.
Calls/effect boundaries: a.get, len, record['usage'].items, s.items, sum.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Return evaluation at root.body[11].body[8].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::metrics::root.body[11].body[8].body[3].value.values[1]::Call

Source: `infra/agentinfra/roadmap_runtime.py:199`; AST `d96ff57c85b1de5e02701b259745dec95870fd23f436944c4ef0110a889a4cad`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: attempts, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[8].body[3].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::metrics::root.body[11].body[8].body[3].value.values[2]::DictComp

Source: `infra/agentinfra/roadmap_runtime.py:200`; AST `14c843aa64eb02d2fdd1424eaba715fd7ed6b33b81bcdd82ebfea1d68e555fe5`.

Rust module: `infra::agentinfra::roadmap_runtime`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: a, attempts, s, sum. Outputs/bindings: a, s.
Calls/effect boundaries: sum.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered DictComp evaluation at root.body[11].body[8].body[3].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::metrics::root.body[11].body[8].body[3].value.values[2].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:200`; AST `ce83e1254cbc01080838aa9a23ceb0223494b4b4c955e589688add8b7175f283`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, attempts, s, sum. Outputs/bindings: a.
Calls/effect boundaries: sum.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[8].body[3].value.values[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::metrics::root.body[11].body[8].body[3].value.values[2].value.args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_runtime.py:200`; AST `d6535c74c1009a042dfc9308adc6cda1ee02a3cab0285e4b030cab3672c82a7b`.

Rust module: `infra::agentinfra::roadmap_runtime`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: a, attempts, s. Outputs/bindings: a.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[11].body[8].body[3].value.values[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::metrics::root.body[11].body[8].body[3].value.values[3]::Call

Source: `infra/agentinfra/roadmap_runtime.py:202`; AST `137b642961eb56db96a6c98bf7acfbbbefd82101b2edc2bd50d25221a69bfe5b`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, attempts, sum. Outputs/bindings: a.
Calls/effect boundaries: sum.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[8].body[3].value.values[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::metrics::root.body[11].body[8].body[3].value.values[3].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_runtime.py:202`; AST `1ceddb3406fb5a04e2038b55eb316f0cad1304c79b219a8d14cd5925382de110`.

Rust module: `infra::agentinfra::roadmap_runtime`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: a, attempts. Outputs/bindings: a.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[11].body[8].body[3].value.values[3].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::metrics::root.body[11].body[8].body[3].value.values[4].body::Call

Source: `infra/agentinfra/roadmap_runtime.py:203`; AST `82e20c9a59eea54e5be4afe765709c3d654595ef48ea70e60c57ec206afa70a9`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: measured, sum. Outputs/bindings: (none).
Calls/effect boundaries: sum.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[8].body[3].value.values[4].body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::metrics::root.body[11].body[8].body[3].value.values[5].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:204`; AST `d96ff57c85b1de5e02701b259745dec95870fd23f436944c4ef0110a889a4cad`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: attempts, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[8].body[3].value.values[5].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::metrics::root.body[11].body[8].body[3].value.values[5].right::Call

Source: `infra/agentinfra/roadmap_runtime.py:204`; AST `93e57249414727b338c449c16d6cc0cc9d4ffd829b964b1a051d6e97ff92d3aa`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, measured. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[8].body[3].value.values[5].right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::metrics::root.body[11].body[8].body[3].value.values[6]::Call

Source: `infra/agentinfra/roadmap_runtime.py:205`; AST `e3ad621813570ed913952df56523a330752f8c40c18e0238070a199a75cf483d`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, attempts, len, sum. Outputs/bindings: a.
Calls/effect boundaries: a.get, len, sum.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[8].body[3].value.values[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::metrics::root.body[11].body[8].body[3].value.values[6].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_runtime.py:205`; AST `b0f9f6cc7cb87e57af820e9da2db209de42b3642114fecc56d639c7bd18dee59`.

Rust module: `infra::agentinfra::roadmap_runtime`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: a, attempts, len. Outputs/bindings: a.
Calls/effect boundaries: a.get, len.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[11].body[8].body[3].value.values[6].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::metrics::root.body[11].body[8].body[3].value.values[6].args[0].elt::Call

Source: `infra/agentinfra/roadmap_runtime.py:205`; AST `d3cd0639d4ef4aef686b54cbea7c062962bd418eb3aff657d476333ed5203c8d`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, len. Outputs/bindings: (none).
Calls/effect boundaries: a.get, len.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[8].body[3].value.values[6].args[0].elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::metrics::root.body[11].body[8].body[3].value.values[6].args[0].elt.args[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:205`; AST `097f7d77cb7a88df7426607630e059d4ebb4b66e784bb5eda02d82afbfb25c71`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a. Outputs/bindings: (none).
Calls/effect boundaries: a.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[8].body[3].value.values[6].args[0].elt.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::metrics::root.body[11].body[8].body[3].value.values[7]::DictComp

Source: `infra/agentinfra/roadmap_runtime.py:206`; AST `8dde4bf5fc2eda1227abb2bcf9fa3d9603219d93af0c610a71ec6e477dadeb32`.

Rust module: `infra::agentinfra::roadmap_runtime`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: f, k, record, s, v. Outputs/bindings: f, k, s, v.
Calls/effect boundaries: record['usage'].items, s.items.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered DictComp evaluation at root.body[11].body[8].body[3].value.values[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::metrics::root.body[11].body[8].body[3].value.values[7].value::DictComp

Source: `infra/agentinfra/roadmap_runtime.py:206`; AST `b6d178f6e359d6e02a135264e9946b60950dc4134aed9eb3b683c431cdb16409`.

Rust module: `infra::agentinfra::roadmap_runtime`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: f, s, v. Outputs/bindings: f, v.
Calls/effect boundaries: s.items.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered DictComp evaluation at root.body[11].body[8].body[3].value.values[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::metrics::root.body[11].body[8].body[3].value.values[7].value.generators[0].iter::Call

Source: `infra/agentinfra/roadmap_runtime.py:206`; AST `ae05b7e81a409f6152ab1368c42c41c09b2f62bec4aa960bfb2a68d10da0bcaf`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: s. Outputs/bindings: (none).
Calls/effect boundaries: s.items.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[8].body[3].value.values[7].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::metrics::root.body[11].body[8].body[3].value.values[7].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_runtime.py:206`; AST `a77599b17c237f19786b568d5d1d616bd5ebdf47c60853ab98477dcabff27389`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record['usage'].items.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[8].body[3].value.values[7].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reservation_record::root.body[11].body[9]::FunctionDef

Source: `infra/agentinfra/roadmap_runtime.py:212`; AST `d87db6e94b089b8aef63a1b8afddcb94fc137f251a95cd80811d93b5b3bff5ad`.

Rust module: `infra::agentinfra::roadmap_runtime`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: a, attempt, dict, ident, int, len, matches, require, self, str, type, validate_record, value. Outputs/bindings: a, attempt, matches, value.
Calls/effect boundaries: attempt.get, attempt.get('receipt', {}).get, len, require, self.read, type, validate_record.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reservation_record::root.body[11].body[9].body[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:213`; AST `b762ed851697e52df1dda2b6b9566a06ea26d7804442749a288c346daf4ec44b`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reservation_record::root.body[11].body[9].body[1]::ImportFrom

Source: `infra/agentinfra/roadmap_runtime.py:214`; AST `f1f6877549a414631a4db4ccc18f71dd26c0617f1264673848d86c31ac546b2b`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered ImportFrom evaluation at root.body[11].body[9].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reservation_record::root.body[11].body[9].body[2]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:215`; AST `6405994699ee0edc906aebc2e54c1a372d9a3190aadd1065f151b8f4fc6a548a`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, ident, self. Outputs/bindings: a, matches.
Calls/effect boundaries: self.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[9].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reservation_record::root.body[11].body[9].body[2].value::ListComp

Source: `infra/agentinfra/roadmap_runtime.py:215`; AST `aa8927f02d04757215c71802d23e9ee794871aa64af9830103d7b2f090d85a21`.

Rust module: `infra::agentinfra::roadmap_runtime`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: a, ident, self. Outputs/bindings: a.
Calls/effect boundaries: self.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered ListComp evaluation at root.body[11].body[9].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reservation_record::root.body[11].body[9].body[2].value.generators[0].iter.value::Call

Source: `infra/agentinfra/roadmap_runtime.py:215`; AST `1a6cd88d33383d245bb90e4e5f924f99f090d6bd29a5c43fab9e8ffb18d19d91`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[9].body[2].value.generators[0].iter.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reservation_record::root.body[11].body[9].body[3]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:216`; AST `8028f941b6b4b434f65fef827259f5185a9a4aa9b8a1d7683b6f02cb4bc205da`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, matches, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[9].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reservation_record::root.body[11].body[9].body[3].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:216`; AST `f2b596d676fff4f4613d79fec2fcacfb10aa17fbe3480da6a528ee74b5c4dee1`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, matches, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[9].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reservation_record::root.body[11].body[9].body[3].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:216`; AST `d97f989b8f8f52f8f40688f8e2e1ccaded6f1cf09b4ecf82beecbcc52f1add97`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, matches. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[9].body[3].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reservation_record::root.body[11].body[9].body[4]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:217`; AST `ab6dc53f6326db9a8e6dc047bb6479c24e82998dd1e545e1dbe5af6d2a0def5d`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: matches. Outputs/bindings: attempt.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[9].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reservation_record::root.body[11].body[9].body[5]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:218`; AST `a35c4db0969b93c746ed721b267c67424e7ef11203490aca3450126c7a185de6`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: attempt, ident, int, len, type. Outputs/bindings: value.
Calls/effect boundaries: attempt.get, attempt.get('receipt', {}).get, len, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[9].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reservation_record::root.body[11].body[9].body[5].value.values[6].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:220`; AST `f546b9c12b77df0427e8e173914c3d5a5d2b75d0d11f944c7e6d0b80e0b6c5de`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: attempt, type. Outputs/bindings: (none).
Calls/effect boundaries: attempt.get, attempt.get('receipt', {}).get, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[9].body[5].value.values[6].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reservation_record::root.body[11].body[9].body[5].value.values[6].left.args[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:220`; AST `83e8d93ac99f29bbfcc981d62839184ad2e2cd87213326e260b5c0832da540e5`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: attempt. Outputs/bindings: (none).
Calls/effect boundaries: attempt.get, attempt.get('receipt', {}).get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[9].body[5].value.values[6].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reservation_record::root.body[11].body[9].body[5].value.values[6].left.args[0].func.value::Call

Source: `infra/agentinfra/roadmap_runtime.py:220`; AST `9d19ac388db19f6efab948af85aca4b8f678010ebd86c35df29f8be3ec51766a`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: attempt. Outputs/bindings: (none).
Calls/effect boundaries: attempt.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[9].body[5].value.values[6].left.args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reservation_record::root.body[11].body[9].body[5].value.values[7]::Call

Source: `infra/agentinfra/roadmap_runtime.py:221`; AST `f031753f199549435b898257b05a907a97edb78164ca7ed04353ac0486c41caa`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: attempt, len. Outputs/bindings: (none).
Calls/effect boundaries: attempt.get, len.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[9].body[5].value.values[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reservation_record::root.body[11].body[9].body[5].value.values[7].args[1].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:221`; AST `c14ebc1776e45a1e1b5a2c7d0ded2c63c627a566c202fab9ec6fcc354e460788`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: attempt, len. Outputs/bindings: (none).
Calls/effect boundaries: attempt.get, len.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[9].body[5].value.values[7].args[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reservation_record::root.body[11].body[9].body[5].value.values[7].args[1].left.args[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:221`; AST `8c7531442ceb03d7e998fcc2b7ae530dc819cc49044e6c723ca4405dcb01b959`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: attempt. Outputs/bindings: (none).
Calls/effect boundaries: attempt.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[9].body[5].value.values[7].args[1].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reservation_record::root.body[11].body[9].body[6]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:223`; AST `c28201f528a24e91c47ce65e9fd81a1d20b3b9eb4336db883519c9f99d478cc9`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, validate_record, value. Outputs/bindings: (none).
Calls/effect boundaries: validate_record.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[9].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reservation_record::root.body[11].body[9].body[6].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:223`; AST `582e610547c36d887ac2b41bfa5cd7258f9efd94b49c84666898ef057d3b0685`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, validate_record, value. Outputs/bindings: (none).
Calls/effect boundaries: validate_record.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[9].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::reservation_record::root.body[11].body[9].body[7]::Return

Source: `infra/agentinfra/roadmap_runtime.py:224`; AST `88b203970aef225f077e527420a8aa37d7bea48c022a704b48a144448b80ec78`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: value. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Return evaluation at root.body[11].body[9].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[10]::FunctionDef

Source: `infra/agentinfra/roadmap_runtime.py:226`; AST `cf678102d48c77f742b368eb329641a31fa4a47ca6f49b2a4b5b14a8d9ad6197`.

Rust module: `infra::agentinfra::roadmap_runtime`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileLock, a, atomic_write_json, dict, ident, len, lock, matches, outcome, receipt, record, require, self, str, time. Outputs/bindings: a, lock, matches, record.
Calls/effect boundaries: FileLock, atomic_write_json, len, lock.acquire, lock.release, matches[0].update, require, self.read, time.time_ns.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[10].body[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:227`; AST `ff22254ad3521a5de6152891b38da85f22dd101c576a6e0229b2a432bf9aacc7`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: outcome, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[10].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:227`; AST `f8b0617f9b0cada61780dfcbe5e11cb0795448f3c525f4f04f185d7a3eb018f6`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: outcome, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[10].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[10].body[1]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:228`; AST `5ad948bd4807312f2c239602daba24f505bb65e40a43af1bb9af59c5142392a1`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileLock, self. Outputs/bindings: lock.
Calls/effect boundaries: FileLock.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[10].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[10].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:228`; AST `06ed4456c71451913ad10de312800960b64f8327c15985fb8debf4e388eef9d0`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileLock, self. Outputs/bindings: (none).
Calls/effect boundaries: FileLock.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[10].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[10].body[2]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:229`; AST `2bcfe51cf785ee29160140309ca2724ded506c99a694a1cd40da99965fea32f6`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[10].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[10].body[2].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:229`; AST `19f113b1ff996d6a4e1349d4f629dcb1414895f291ae11a26e3a1c7c22771cf0`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[10].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[10].body[3]::Try

Source: `infra/agentinfra/roadmap_runtime.py:230`; AST `69251401fe0d767ce352d17addcd6bf8101dccb325bc2c8ab84841a5555c78c3`.

Rust module: `infra::agentinfra::roadmap_runtime`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: a, atomic_write_json, ident, len, lock, matches, outcome, receipt, record, require, self, time. Outputs/bindings: a, matches, record.
Calls/effect boundaries: atomic_write_json, len, lock.release, matches[0].update, require, self.read, time.time_ns.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Try evaluation at root.body[11].body[10].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[10].body[3].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:231`; AST `8d60c6cf06a37f3a21e36d8d4fc569b1d94d00284e5e8e23781c46e0c0bd8c8b`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: record.
Calls/effect boundaries: self.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[10].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[10].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:231`; AST `1a6cd88d33383d245bb90e4e5f924f99f090d6bd29a5c43fab9e8ffb18d19d91`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[10].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[10].body[3].body[1]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:232`; AST `cf32e9bf9b8a72d66b64531668c804f7085a2f6675610c277caa371b3b7106b2`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, ident, record. Outputs/bindings: a, matches.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[10].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[10].body[3].body[1].value::ListComp

Source: `infra/agentinfra/roadmap_runtime.py:232`; AST `fb765ce6077cad522849ac1bfa4314dacb67a58cf6789a9c53a4b0d2d988644b`.

Rust module: `infra::agentinfra::roadmap_runtime`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: a, ident, record. Outputs/bindings: a.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered ListComp evaluation at root.body[11].body[10].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[10].body[3].body[2]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:233`; AST `c935a24c37b07acc4025897da5181f8b7d3c77f9441b7c12a4a152631ff94abd`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, matches, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[10].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[10].body[3].body[2].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:233`; AST `de82ae7288f3fd876110c4e92da5000b0ea5d5ba25e3a8517d7f9303460023b5`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, matches, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[10].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[10].body[3].body[2].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:233`; AST `d97f989b8f8f52f8f40688f8e2e1ccaded6f1cf09b4ecf82beecbcc52f1add97`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, matches. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[10].body[3].body[2].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[10].body[3].body[3]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:234`; AST `0f4b708072d6f39d8bad5eeee9b8aae8cd819c102d475c75587e7c1abcf8fef8`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: matches, outcome, receipt. Outputs/bindings: (none).
Calls/effect boundaries: matches[0].update.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[10].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[10].body[3].body[3].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:234`; AST `cb028ee3c04d26ae7e343a0dc5e10609863db082fbd882336a75457d2a94abd4`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: matches, outcome, receipt. Outputs/bindings: (none).
Calls/effect boundaries: matches[0].update.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[10].body[3].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[10].body[3].body[4]::If

Source: `infra/agentinfra/roadmap_runtime.py:235`; AST `8f131dd71932b6729f7a92768927f1122889f6760c69c1abcdb76dbaf3b4a530`.

Rust module: `infra::agentinfra::roadmap_runtime`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: matches, outcome, time. Outputs/bindings: (none).
Calls/effect boundaries: time.time_ns.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered If evaluation at root.body[11].body[10].body[3].body[4]; no call, error or mutation may be omitted. Condition: 'operation' in matches[0]
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[10].body[3].body[4].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:236`; AST `f5bb86e888c88be80611134f034c2145997610dd77620ee658ff1040570df2a7`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: matches, outcome. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[10].body[3].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[10].body[3].body[4].body[1]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:237`; AST `85894ca10db0eb9b9bf8fc1a3e1e1443d09a269b4e706124bb568184b8c625c6`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: matches, time. Outputs/bindings: (none).
Calls/effect boundaries: time.time_ns.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[10].body[3].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[10].body[3].body[4].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:237`; AST `d7bb4f9a8f02ae840b0ecfbf4a0bc46a103c9ee80044d3e746466d336dbaf7ae`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: time. Outputs/bindings: (none).
Calls/effect boundaries: time.time_ns.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[10].body[3].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[10].body[3].body[5]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:238`; AST `39653ba93071c48ea5664f41495c0b9b4c456ea6c7027a39f271248d5232ec2e`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_json, record, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[10].body[3].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[10].body[3].body[5].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:238`; AST `e0ebb6df18f3acd72b73864198de1922264a5591e4adfd3e452231c9bafa9477`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_json, record, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[10].body[3].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[10].body[3].finalbody[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:240`; AST `9aa6f04fc26ee6b3f6fe1a19158adb3cfde13709dcae4a7cc38bccbb2655afb2`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[10].body[3].finalbody[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::close::root.body[11].body[10].body[3].finalbody[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:240`; AST `107c5710331db61e695f7d71256d48862412d15c223e204da5c71c497352b634`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[10].body[3].finalbody[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[11]::FunctionDef

Source: `infra/agentinfra/roadmap_runtime.py:242`; AST `b8988c51b7d7a53490248f93800853b5f44fcc82b008cb8f82c28ba23016390c`.

Rust module: `infra::agentinfra::roadmap_runtime`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileLock, atomic_write_json, bool, dict, event_id, int, lock, record, require, self, str, thread_id, total, type, usage. Outputs/bindings: lock, record, usage.
Calls/effect boundaries: FileLock, atomic_write_json, bool, dict, lock.acquire, lock.release, record['usage'].setdefault, require, self.read, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[11].body[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:243`; AST `d799aa76aac235aa02ea343eccecffec1ff0d53ba52ac1e7d2c1fd14f0e671dd`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, event_id, require, thread_id. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[11].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:243`; AST `7a7e76fa5fef3d1ac92cecef7d9e90dcfe3407cc73ec42a8e5a100666799d554`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, event_id, require, thread_id. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[11].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[11].body[0].value.args[0].values[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:243`; AST `cd37e63e8c7eb3c36062f0fbd5dd0ea6964ef29927b2cb95206c3f8060580755`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, thread_id. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[11].body[0].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[11].body[0].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_runtime.py:243`; AST `3e92731226f2b51f589da08be39a33e83d597c14fea7e4556613d9a1dbb6d9df`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, event_id. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[11].body[0].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[11].body[1]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:244`; AST `14b97e4ba59e30f94a1512f471f04d4ec3ccbeb29ff7bd9cbd1fc2984a90b4c3`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: int, require, total, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[11].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[11].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:244`; AST `8f04bdc286ac29f86b50442445b003106f8399a69d6e800a1e7f93573a83cf9b`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: int, require, total, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[11].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[11].body[1].value.args[0].values[1].values[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:244`; AST `1640c40c7f3e5652b4ce485094324d24b71d11f477d89f9370054dc8ab0bcd46`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: total, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[11].body[1].value.args[0].values[1].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[11].body[2]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:245`; AST `0b9cf3f582006dcd9e3bada572669897fb941f81c22a91048b7cca986626b4c6`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileLock, self. Outputs/bindings: lock.
Calls/effect boundaries: FileLock.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[11].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[11].body[2].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:245`; AST `1ee904a2b41404877314b19cf7f0fb6745c76928d8915a51a07c5bcae2fc445b`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileLock, self. Outputs/bindings: (none).
Calls/effect boundaries: FileLock.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[11].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[11].body[3]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:246`; AST `2bcfe51cf785ee29160140309ca2724ded506c99a694a1cd40da99965fea32f6`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[11].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[11].body[3].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:246`; AST `19f113b1ff996d6a4e1349d4f629dcb1414895f291ae11a26e3a1c7c22771cf0`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[11].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[11].body[4]::Try

Source: `infra/agentinfra/roadmap_runtime.py:247`; AST `b121de3fb58456afcb4ffbd65c983c50cdcd461c971cf0aff578440c215bf020`.

Rust module: `infra::agentinfra::roadmap_runtime`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: atomic_write_json, dict, event_id, lock, record, require, self, thread_id, total, usage. Outputs/bindings: record, usage.
Calls/effect boundaries: atomic_write_json, dict, lock.release, record['usage'].setdefault, require, self.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Try evaluation at root.body[11].body[11].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[11].body[4].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:248`; AST `8d60c6cf06a37f3a21e36d8d4fc569b1d94d00284e5e8e23781c46e0c0bd8c8b`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: record.
Calls/effect boundaries: self.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[11].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[11].body[4].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:248`; AST `1a6cd88d33383d245bb90e4e5f924f99f090d6bd29a5c43fab9e8ffb18d19d91`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[11].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[11].body[4].body[1]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:249`; AST `53bcfe909acdecf6389bd1ec4c4194257682702a9c37e4bc185120110b090989`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record, thread_id. Outputs/bindings: usage.
Calls/effect boundaries: record['usage'].setdefault.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[11].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[11].body[4].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:249`; AST `c0683907ccda314c861f238c211afc4a1f6ffa70db9f0eec029d1943eea1cf53`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record, thread_id. Outputs/bindings: (none).
Calls/effect boundaries: record['usage'].setdefault.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[11].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[11].body[4].body[2]::If

Source: `infra/agentinfra/roadmap_runtime.py:250`; AST `f95034d2c8b7eddab9655cc09d7884575c3cab03b52aa5a65da00e05be414c70`.

Rust module: `infra::agentinfra::roadmap_runtime`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: dict, event_id, require, total, usage. Outputs/bindings: (none).
Calls/effect boundaries: dict, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered If evaluation at root.body[11].body[11].body[4].body[2]; no call, error or mutation may be omitted. Condition: event_id in usage['events']
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[11].body[4].body[2].body[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:251`; AST `484a0b9533eae32c71b66c3caa85840f528e80dcd574fccc269e6baaacb62e26`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: event_id, require, total, usage. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[11].body[4].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[11].body[4].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:251`; AST `da3bc31a4b596450a77443fae97fb81fa21166358bacc378bf3de03da2e64dca`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: event_id, require, total, usage. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[11].body[4].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[11].body[4].body[2].body[1]::Return

Source: `infra/agentinfra/roadmap_runtime.py:252`; AST `ed4cf45c6dc70c8fd8da13a6e0eb8b23a7689f702082e00fd2f5f8e1f0a5d564`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, usage. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Return evaluation at root.body[11].body[11].body[4].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[11].body[4].body[2].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:252`; AST `8aa055a140fab9cf553e1183c53bfb2f0a5f5f655a93319e930a19ab5441ec68`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, usage. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[11].body[4].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[11].body[4].body[3]::If

Source: `infra/agentinfra/roadmap_runtime.py:253`; AST `fd88db75cca5888054eec9b4dc2fbe9b4c86f0df9f90dd1bc7af64af556d2203`.

Rust module: `infra::agentinfra::roadmap_runtime`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: require, total, usage. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered If evaluation at root.body[11].body[11].body[4].body[3]; no call, error or mutation may be omitted. Condition: total is not None and usage['total'] is not None
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[11].body[4].body[3].body[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:254`; AST `7240208a29b2feed1eacad1baabf2a3aa383374c146443d08cbe86c0bf715e8a`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, total, usage. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[11].body[4].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[11].body[4].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:254`; AST `5367338754edeaa70ab6f211df26af7f7f60033e003adad9fc20c0442e9e72af`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, total, usage. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[11].body[4].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[11].body[4].body[4]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:255`; AST `36582a4e64162a0874bb43073f8717673f192fd5194a277fa45ec1dd702621ed`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: event_id, total, usage. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[11].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[11].body[4].body[5]::If

Source: `infra/agentinfra/roadmap_runtime.py:256`; AST `937e3ed71edcc16e8369c8af6d5fdb221cd8e1f6175bfbb3f8631273ffd9358c`.

Rust module: `infra::agentinfra::roadmap_runtime`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: total, usage. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered If evaluation at root.body[11].body[11].body[4].body[5]; no call, error or mutation may be omitted. Condition: total is not None
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[11].body[4].body[5].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:257`; AST `fa966965debf4352b7ebfad6de6eb7f1cc1332c3f908442bd356ef0538f4f010`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: total, usage. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[11].body[4].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[11].body[4].body[6]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:258`; AST `39653ba93071c48ea5664f41495c0b9b4c456ea6c7027a39f271248d5232ec2e`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_json, record, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[11].body[4].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[11].body[4].body[6].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:258`; AST `e0ebb6df18f3acd72b73864198de1922264a5591e4adfd3e452231c9bafa9477`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_json, record, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[11].body[4].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[11].body[4].body[7]::Return

Source: `infra/agentinfra/roadmap_runtime.py:259`; AST `ed4cf45c6dc70c8fd8da13a6e0eb8b23a7689f702082e00fd2f5f8e1f0a5d564`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, usage. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Return evaluation at root.body[11].body[11].body[4].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[11].body[4].body[7].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:259`; AST `8aa055a140fab9cf553e1183c53bfb2f0a5f5f655a93319e930a19ab5441ec68`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, usage. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[11].body[4].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[11].body[4].finalbody[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:261`; AST `9aa6f04fc26ee6b3f6fe1a19158adb3cfde13709dcae4a7cc38bccbb2655afb2`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[11].body[4].finalbody[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::BudgetLedger::observe_usage::root.body[11].body[11].body[4].finalbody[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:261`; AST `107c5710331db61e695f7d71256d48862412d15c223e204da5c71c497352b634`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[11].body[4].finalbody[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12]::FunctionDef

Source: `infra/agentinfra/roadmap_runtime.py:264`; AST `e66bf0396a8707d99fee455956fdc7fb8990a735e94525c05c840abbf25325e4`.

Rust module: `infra::agentinfra::roadmap_runtime`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: BudgetLedger, Path, WorkspaceLease, a, binding, bool, compiled, confined_path, continuation, created, dict, digest, execution, goal, inherited, int, ledger, legacy, milestone, name, owner, path, read_json, record, require, root, started, str, thread, tuple, type, work_id. Outputs/bindings: a, binding, continuation, created, execution, goal, inherited, legacy, owner, path, record, started, thread, work_id.
Calls/effect boundaries: WorkspaceLease, WorkspaceLease(root).assert_owner, binding.get, bool, confined_path, continuation.get, digest, execution.get, goal.get, ledger.read, owner.get, read_json, record.get, record.get('continuation', {}).get, require, root.resolve, str, tuple, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:266`; AST `c910188bbd8095f6d234ec9dbb428e32c461b7503d757b1237c8553c2d658883`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[1]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:272`; AST `ff9f7b1b452102574abcb790996ad6100d1ccab24369011a20b807cccd708747`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, milestone, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:272`; AST `c30870bb21ab81837e0b5463012d6133048f1b2dd4100c7411488f762eec09c5`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, milestone, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[2]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:274`; AST `98864eb91502cf19dee35a57c3507c393eb56db4f8cf7bc4f7f63ba19c8ca39c`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, confined_path, root. Outputs/bindings: path.
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[2].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:274`; AST `2411f310ac43c2b4f3c2fac8d1128047c8324665b56e941312032bf564cf1f15`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, confined_path, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[3]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:275`; AST `4c0b40719bd50d8d610b5ba0ec593936db79742bfd3484eeea858809f2b40c7c`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path, read_json. Outputs/bindings: record.
Calls/effect boundaries: read_json.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[3].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:275`; AST `ca2a99ec0b14545aba864c1e6b22415e5a02ad33955de7320b863aa9c805bfcd`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[4]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:276`; AST `f85869b980d0fb25741330a8c16a670c3cb260eb9bce0361055e2192bfba69b1`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record. Outputs/bindings: execution.
Calls/effect boundaries: record.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[4].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:276`; AST `94f294c41d79480919f0ce6955c328ecffa9d2fc269e74d3e6fc9cebeec917d7`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[5]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:277`; AST `8d966d61e8f4fe7fb915b27fb56de3eb1cea5416f6e3c84de1a6bca872634ea8`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: execution. Outputs/bindings: binding.
Calls/effect boundaries: execution.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[5].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:277`; AST `9d07ed4a2c148f4183b707ac830e883b5c33ba96dcd1e134c547f727d92f1312`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: execution. Outputs/bindings: (none).
Calls/effect boundaries: execution.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[6]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:278`; AST `81aca9f5503557b417bc2af78ce8ee8f28bfac449823a648264eb5c819cb7058`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding. Outputs/bindings: goal.
Calls/effect boundaries: binding.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[6].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:278`; AST `19383d3c3a3dd141414e57358091030cb5d155331564962bc5d64e9d2fdca72d`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding. Outputs/bindings: (none).
Calls/effect boundaries: binding.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[7]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:279`; AST `1bfbe0ef6c55dac79248d6cf6e8a349b807d555eade36f876c2a51d6251838a4`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding. Outputs/bindings: thread.
Calls/effect boundaries: binding.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[7].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:279`; AST `63111ba26343241a333d0933cf221435534ec16270d2f49ca57741efb6c4fa1a`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding. Outputs/bindings: (none).
Calls/effect boundaries: binding.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[8]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:280`; AST `670f85d57e1bdbc688d11ba038b5b0b280a41be277563aab1f56458926493883`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, record, require, thread. Outputs/bindings: (none).
Calls/effect boundaries: bool, record.get, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[8].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:280`; AST `6790f037a1a462e1b3ff443660ef5986ded14386843de4e9cfae6a77ca1c92d8`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, record, require, thread. Outputs/bindings: (none).
Calls/effect boundaries: bool, record.get, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[8].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:280`; AST `d1e3876e5f2eab25e6fd365f06eea6e829f195ef666744ac41314682d8aa382c`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[8].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:280`; AST `d0a98983fb019a589d6e758de84d4e0770904ddc3da7d42d506d12396e7ac5ca`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[8].value.args[0].values[2]::Call

Source: `infra/agentinfra/roadmap_runtime.py:280`; AST `7e7f2dee89ebf969b2a85e0869a13de1e700211ebbda1457205ac01cdc2be0d6`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, thread. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].value.args[0].values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[9]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:282`; AST `b5ea1ed7d44eb5365847be873b1be6f5d852826ef4d5bc2dd5bb187572261f46`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, goal, require, thread. Outputs/bindings: (none).
Calls/effect boundaries: binding.get, goal.get, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[9].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:282`; AST `7c1fce64522b83aa1ef05efcb510f0473b02f82cc49876f065584e02c5b69316`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, goal, require, thread. Outputs/bindings: (none).
Calls/effect boundaries: binding.get, goal.get, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[9].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:282`; AST `8882eb7d5b9f4dc8d2105e4953998c448940325a4f4149b97780ded2830a8ee0`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: goal. Outputs/bindings: (none).
Calls/effect boundaries: goal.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[9].value.args[0].values[0].left.args[1]::Call

Source: `infra/agentinfra/roadmap_runtime.py:282`; AST `12a3aafb86d4ac1fabfccdf44687ff589a7892691f5c30c1ec9f07c0e05a13a9`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: goal. Outputs/bindings: (none).
Calls/effect boundaries: goal.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].value.args[0].values[0].left.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[9].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:283`; AST `f63919515d3be4b4c9952f900298cbf76eac49214dedb5f1b96049934fdc731c`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: goal. Outputs/bindings: (none).
Calls/effect boundaries: goal.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[9].value.args[0].values[1].comparators[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:283`; AST `c52ca19c779f5d2a2be4d6e23e8b381a8637c14e49af2b3c39e5bc3ee9359726`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding. Outputs/bindings: (none).
Calls/effect boundaries: binding.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].value.args[0].values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[9].value.args[0].values[2].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:283`; AST `337340fc2dab2135d3885d03c2bb3040fb953c98284ab395c2e6270568db0732`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: goal. Outputs/bindings: (none).
Calls/effect boundaries: goal.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].value.args[0].values[2].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[10]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:285`; AST `9377717ec93ed8c020444988585590b402d03e35300a9e9fa96e3d56a32d1db1`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: execution, milestone, record, require. Outputs/bindings: (none).
Calls/effect boundaries: execution.get, record.get, record.get('continuation', {}).get, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[10].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:285`; AST `9655c5614735abcceb8388fa2b7ed79314d01058096c7c54ed725aadbafbf009`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: execution, milestone, record, require. Outputs/bindings: (none).
Calls/effect boundaries: execution.get, record.get, record.get('continuation', {}).get, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[10].value.args[0].values[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:285`; AST `1d5906c7d6a9e7173e4d5a4677d17ccaba7c71a291cbd487f007d0688de2e211`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: execution. Outputs/bindings: (none).
Calls/effect boundaries: execution.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[10].value.args[0].values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[10].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:286`; AST `1aea51f75485f4d54384e4db631d258f848ec6cbf9df2e80a998ff4773159220`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get, record.get('continuation', {}).get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[10].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[10].value.args[0].values[1].left.func.value::Call

Source: `infra/agentinfra/roadmap_runtime.py:286`; AST `1ac6954672b3424f66695dffe4f844ab9e9cd657bb68329edc66a49dd7cb68ef`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[10].value.args[0].values[1].left.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[11]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:288`; AST `3143d476a50e13911b81b08cc9f4475a21e61266a736348376774270436548e6`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: execution. Outputs/bindings: owner.
Calls/effect boundaries: execution.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[11].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:288`; AST `94ea54adee6fc3e52b8da6da4b7ad4c1f66ad0fe66dcebf5eb64a5f9b2021753`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: execution. Outputs/bindings: (none).
Calls/effect boundaries: execution.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[12]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:289`; AST `94fb5a4b0b19866046013ceb8513e8e312b6239a7ba70b0dff8ddc098cad53f9`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: owner, require, thread. Outputs/bindings: (none).
Calls/effect boundaries: owner.get, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[12].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:289`; AST `d8f75e204e7e55c4c238dd2cdb95826db72f8621abdd77a4eca34ffeb32d8c08`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: owner, require, thread. Outputs/bindings: (none).
Calls/effect boundaries: owner.get, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[12].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:289`; AST `27a5b1552929f691a509884265ca66d93c6c63ccce4de6833fab9a141246c47e`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: owner. Outputs/bindings: (none).
Calls/effect boundaries: owner.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[13]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:290`; AST `d4f115f3a1ad13c15b35dda40721d4df4ac6110395a36304743f1f1998f1e3e3`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: WorkspaceLease, owner, root. Outputs/bindings: (none).
Calls/effect boundaries: WorkspaceLease, WorkspaceLease(root).assert_owner.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[13].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:290`; AST `5a4a7c71898511257607db7d7a64df8ed53c585d29a5b177b02e48bd76fcf6cd`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: WorkspaceLease, owner, root. Outputs/bindings: (none).
Calls/effect boundaries: WorkspaceLease, WorkspaceLease(root).assert_owner.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[13].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[13].value.func.value::Call

Source: `infra/agentinfra/roadmap_runtime.py:290`; AST `9af565e67ae5d334b545886bccb7b0f27fb8d8189b6644c9267610cbdb6cc4e6`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: WorkspaceLease, root. Outputs/bindings: (none).
Calls/effect boundaries: WorkspaceLease.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[13].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[14]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:291`; AST `08ea25a29f190448894e8c3ac615107a7281aea1743f7d9049a43f3034b37171`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: goal. Outputs/bindings: created.
Calls/effect boundaries: goal.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[14].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:291`; AST `6e765ad33f07a626e8e18db3f67a6201ab9cca3273e1f1bacbe3598ea77e0560`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: goal. Outputs/bindings: (none).
Calls/effect boundaries: goal.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[14].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[15]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:292`; AST `cda1666fd0a2b75d6946c9dae6b009b075b76c788e4e6e427dc26ab78720088c`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: created, int, require, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[15].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:292`; AST `1f67d94fdffb4fd139933c6ca4d5445d2d55b02fa48a1de43bb52d47390ab90c`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: created, int, require, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[15].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[15].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:292`; AST `c93741fd485e081b9a072bcb6670c7fcd7e5f8a44d89568b247c54f81e9eb10e`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: created, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[15].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[16]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:293`; AST `ad035630a04854e9df6ca07a8dd6a6fef3f8ac2177a8a3545b2e1fc453668a00`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record. Outputs/bindings: continuation.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[16]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[17]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:294`; AST `7acd7f165404c457fafe90ba5b96ea049dab4c75cf58bc093ed99dfa5f035e6f`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: continuation. Outputs/bindings: started.
Calls/effect boundaries: continuation.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[17]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[17].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:294`; AST `57cc71bb2b55ac413c35405d928b14a17266b08118d615cf2b74cbb7aec654cb`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: continuation. Outputs/bindings: (none).
Calls/effect boundaries: continuation.get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[17].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[18]::If

Source: `infra/agentinfra/roadmap_runtime.py:295`; AST `2fb34f000d123145353d8db13a8f5fc6ce4ae96ade79b1b721c4541b6cbb3906`.

Rust module: `infra::agentinfra::roadmap_runtime`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: created, milestone, started. Outputs/bindings: started.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered If evaluation at root.body[12].body[18]; no call, error or mutation may be omitted. Condition: started is None and milestone == 'A00'
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[18].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:296`; AST `c1968dda3e550b18c2da4fc11624cf95a732776bea508d1f547d5567e6315ae1`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: created. Outputs/bindings: started.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[18].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[19]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:297`; AST `00d8d5f997645d6f196504c8d0e9a5817838d65dbfa82f7168003961c97169f4`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: created, int, require, started, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[19]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[19].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:297`; AST `d242416d912edc3221702b46eb5861b4632501a3fdc8d1efe65196804191162a`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: created, int, require, started, type. Outputs/bindings: (none).
Calls/effect boundaries: require, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[19].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[19].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_runtime.py:297`; AST `33af8700a8edf7a256a3437ba0c9924eb62e34db64d5fef701b2a5548fbb8b39`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: started, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[19].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[20]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:299`; AST `ebe2eff0a25d1a7a307f4c4751c0ec0219e2b07df5fa51edddb8c462a82cdabc`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, name, root, str. Outputs/bindings: legacy.
Calls/effect boundaries: digest, root.resolve, str.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[20]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[20].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:299`; AST `f7eeffad6fe75979b2f5cb21e3b6559a00b62c457e1203bd148a7d8627d441bc`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, name, root, str. Outputs/bindings: (none).
Calls/effect boundaries: digest, root.resolve, str.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[20].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[20].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_runtime.py:299`; AST `29d0b5a674124d6a5dea0e9d83c547c4cebd29502709afd03c4659bd6afedfda`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, str. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve, str.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[20].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[20].value.args[0].values[1].args[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:299`; AST `b97f3f463d4724206af2869ad4674d5eb373167f052507971a722ecc8f771a87`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[20].value.args[0].values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[21]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:300`; AST `d37630148eed6f59476f877a5aed0a7a6747a5657c9db042f04860a46a35375c`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, ledger, legacy, started, tuple. Outputs/bindings: a, inherited.
Calls/effect boundaries: ledger.read, tuple.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[21]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[21].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:300`; AST `0fbceb1ac5915d427e5d67a77397b93b806e2c3941994fabbf91f612345af77b`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, ledger, legacy, started, tuple. Outputs/bindings: a.
Calls/effect boundaries: ledger.read, tuple.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[21].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[21].value.args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_runtime.py:300`; AST `8b86a1b457f264624450953952dd5881883a8923db56d45e7d169fe8ae0abbdf`.

Rust module: `infra::agentinfra::roadmap_runtime`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: a, ledger, legacy, started. Outputs/bindings: a.
Calls/effect boundaries: ledger.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[12].body[21].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[21].value.args[0].generators[0].iter.value::Call

Source: `infra/agentinfra/roadmap_runtime.py:300`; AST `97bf15ee0985708addfb91473f1c9a324eb4e700d9a5a949145f8b93d423dbb2`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ledger. Outputs/bindings: (none).
Calls/effect boundaries: ledger.read.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[21].value.args[0].generators[0].iter.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[22]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:302`; AST `5a0b6ed7782b94b1d816d0b41c12a58b363c43f2210841b200e764786aaf5cb9`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, milestone, name, root, str, thread. Outputs/bindings: work_id.
Calls/effect boundaries: digest, root.resolve, str.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[22]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[22].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:302`; AST `24680cdf1228574942ffbd96b0a4fd3d4c307117247286b73c1e1e9e939121d5`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, milestone, name, root, str, thread. Outputs/bindings: (none).
Calls/effect boundaries: digest, root.resolve, str.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[22].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[22].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_runtime.py:302`; AST `29d0b5a674124d6a5dea0e9d83c547c4cebd29502709afd03c4659bd6afedfda`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, str. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve, str.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[22].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[22].value.args[0].values[1].args[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:302`; AST `b97f3f463d4724206af2869ad4674d5eb373167f052507971a722ecc8f771a87`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[22].value.args[0].values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::recipe_scope::root.body[12].body[23]::Return

Source: `infra/agentinfra/roadmap_runtime.py:304`; AST `bff89ddc70c5bebfa0eb7473c4c0fb168cf8c9b67e526c11da8cb835bbf64988`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: inherited, work_id. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Return evaluation at root.body[12].body[23]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13]::FunctionDef

Source: `infra/agentinfra/roadmap_runtime.py:307`; AST `25cb37e35687ce58a1d2685fcbd0d747efd5a66c9b8bb5730c3b32b3f275b798`.

Rust module: `infra::agentinfra::roadmap_runtime`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: BaseException, BudgetLedger, FileLock, Path, all, argv, attempt, bindings_current, canonical_record, compiled, diagnosis, dict, digest, exc, inherited, inputs, lease, ledger, milestone, name, ok, read_json, receipt, recipe, recipe_scope, require, result, root, run_process, run_work, str, sys, type, work_id, x. Outputs/bindings: argv, attempt, canonical_record, inherited, inputs, lease, ledger, ok, receipt, recipe, result, work_id, x.
Calls/effect boundaries: BudgetLedger, FileLock, all, bindings_current, canonical_record.exists, digest, lease.acquire, lease.release, ledger.close, ledger.reserve, read_json, read_json(canonical_record).get, recipe_scope, require, root.resolve, run_process, run_work, str, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[0]::If

Source: `infra/agentinfra/roadmap_runtime.py:309`; AST `70cecbc719e0fc7d4f4171a4b4a038bde24d397e78563c9c827b679d2a953e04`.

Rust module: `infra::agentinfra::roadmap_runtime`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: compiled, diagnosis, milestone, name, root, run_work. Outputs/bindings: (none).
Calls/effect boundaries: run_work.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered If evaluation at root.body[13].body[0]; no call, error or mutation may be omitted. Condition: milestone is not None
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[0].body[0]::ImportFrom

Source: `infra/agentinfra/roadmap_runtime.py:310`; AST `895553d712176556360f32cd787fda0cee9b80a181a2f2bc9c6298c0cea15c47`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered ImportFrom evaluation at root.body[13].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[0].body[1]::Return

Source: `infra/agentinfra/roadmap_runtime.py:311`; AST `2cd336ee0e3d3de9739a4ff2ac53e30fb4221b5e16f51ab2a6439171b4305473`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, diagnosis, milestone, name, root, run_work. Outputs/bindings: (none).
Calls/effect boundaries: run_work.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Return evaluation at root.body[13].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[0].body[1].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:311`; AST `50aea1d75f4e56a9a7346761e0db0fe5dbc05bc912f526ef0da3a4cbc3ff5211`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, diagnosis, milestone, name, root, run_work. Outputs/bindings: (none).
Calls/effect boundaries: run_work.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[1]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:312`; AST `7308782d2dd92e319b040412b4f7b2fd0b02791d0fbd39a0f6e873f6cc0d3b35`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: canonical_record.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[2]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:313`; AST `31f867b0617a1cacfcba595cbf5e2e0db54cdaf2920f807dd23f00a1a15612d7`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: canonical_record, read_json, require. Outputs/bindings: (none).
Calls/effect boundaries: canonical_record.exists, read_json, read_json(canonical_record).get, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[2].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:313`; AST `372993e7053b827781bdbcf2abc8fedb4937a40cb1be00f34ec729fc0044104a`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical_record, read_json, require. Outputs/bindings: (none).
Calls/effect boundaries: canonical_record.exists, read_json, read_json(canonical_record).get, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[2].value.args[0].values[0].operand::Call

Source: `infra/agentinfra/roadmap_runtime.py:313`; AST `e8cda5fb460f3fae368ea5a6f4238d01dd064f2708e00d114fd8a5efeaa06369`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical_record. Outputs/bindings: (none).
Calls/effect boundaries: canonical_record.exists.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].value.args[0].values[0].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[2].value.args[0].values[1].operand::Call

Source: `infra/agentinfra/roadmap_runtime.py:313`; AST `a8059cace8eb2b277d843238d84d340bc4b86e4bdba4060950a9697f6025460e`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical_record, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json, read_json(canonical_record).get.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].value.args[0].values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[2].value.args[0].values[1].operand.func.value::Call

Source: `infra/agentinfra/roadmap_runtime.py:313`; AST `514d237d65286ca51d2b546278ad5900a8aaf98d518342d1504eda34718ea77e`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical_record, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].value.args[0].values[1].operand.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[3]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:315`; AST `7134076064ca0cc4d6e8bf0df750033455986c45bc4b76108df1e6dd0cf012c7`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bindings_current, compiled, require, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[3].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:315`; AST `1d48ed543f544738992ff8b01172556e0ebe3c3346236bdb93934a175388b6c2`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, compiled, require, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[3].value.args[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:315`; AST `e4376bee10cb5ac58b23e27129b2002e1436b91face64325fcbf8a25771ff8e7`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, compiled, root. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[4]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:316`; AST `64512de268c5e817df30e7dca1f869aa9c2f31bb9f799a4ff54f0f3e6e494ed7`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, name, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[4].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:316`; AST `f78b579b3faa4cc54919bab290adc167932d4b19443dc0853a3b15b21d976cd1`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, name, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[5]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:317`; AST `c6946d992b569719baf8f6b5caeb8843502d56201decee935602a5fe529eba20`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, name. Outputs/bindings: recipe.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[6]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:318`; AST `bc654dbdf9dc5d5642492c41db899552c7f4c7751c6afb9c6138c540f14e0b5a`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: recipe, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[6].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:318`; AST `a15b695faca3256151950dce380c567c0ddb44509ee8a90a9a4e5da25477da06`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: recipe, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[7]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:319`; AST `47b5483b8dd8c381357e24a91032e49c14e8bb5d54ab7923954fdc61efa65649`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: recipe, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[7].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:319`; AST `65aae1c63a647ddbd3502e80205255c1f34e7bca29d35a6c04d8569e8709a5b8`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: recipe, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[8]::Import

Source: `infra/agentinfra/roadmap_runtime.py:320`; AST `f7252e3c1dbe1d5edf1f34c020a58a05b55f706b2c1d9479eae91f9a9d4be275`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Import evaluation at root.body[13].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[9]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:321`; AST `bd9f0f903210947bab774fb108d0c04706d914d59dbd173b0f83f401833a58f0`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: recipe, sys. Outputs/bindings: argv.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[10]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:322`; AST `9d15bb663bddd8cd5cf54a2049a1c82786ab59c32dea73de26fc4cc6e075d1fc`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, argv, require, str, type, x. Outputs/bindings: x.
Calls/effect boundaries: all, require, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[10].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:322`; AST `ca3fb39a85567145d1afae50e4530911662b551f34ac0aad3bcf79f6173bbe24`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, argv, require, str, type, x. Outputs/bindings: x.
Calls/effect boundaries: all, require, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[10].value.args[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:322`; AST `d6765e1f20fcaba0aaeb5595c25d6f47549b94b17938afeeff50e3e72dd87a07`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, argv, str, type, x. Outputs/bindings: x.
Calls/effect boundaries: all, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[10].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[10].value.args[0].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_runtime.py:322`; AST `a43f75bc33ab7a6b7a51cd0aaefe0b517dd36234fa7c8cc09a694d49c78a7a5b`.

Rust module: `infra::agentinfra::roadmap_runtime`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: argv, str, type, x. Outputs/bindings: x.
Calls/effect boundaries: type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[13].body[10].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[10].value.args[0].args[0].elt.left::Call

Source: `infra/agentinfra/roadmap_runtime.py:322`; AST `617245833c9319194f50c6c77baf6916a03ab26dba6a12037ebc1d090f9aebc1`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: type, x. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[10].value.args[0].args[0].elt.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[11]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:323`; AST `67675058a01e0dda8539105929316e0f5649ff01f4106b07914385a579da4201`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, name, root, str. Outputs/bindings: work_id.
Calls/effect boundaries: digest, root.resolve, str.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[11].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:323`; AST `f7eeffad6fe75979b2f5cb21e3b6559a00b62c457e1203bd148a7d8627d441bc`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, name, root, str. Outputs/bindings: (none).
Calls/effect boundaries: digest, root.resolve, str.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[11].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_runtime.py:323`; AST `29d0b5a674124d6a5dea0e9d83c547c4cebd29502709afd03c4659bd6afedfda`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, str. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve, str.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[11].value.args[0].values[1].args[0]::Call

Source: `infra/agentinfra/roadmap_runtime.py:323`; AST `b97f3f463d4724206af2869ad4674d5eb373167f052507971a722ecc8f771a87`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[11].value.args[0].values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[12]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:324`; AST `421b4ed54537fb53288819ed5abaadfbafffa5592ae161b204a201c761a61d4f`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, digest, recipe. Outputs/bindings: inputs.
Calls/effect boundaries: digest.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[12].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:324`; AST `d15b0e2a60dd0d87c5cc653cbf29a5f306cf7cdea9849c6143dc86aaddbcbd0f`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, digest, recipe. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[13]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:325`; AST `dc2fd1ede60c6438c487511f87ef8eedec8bb87e6ab3d1c5380ff1542be015c2`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: BudgetLedger, root. Outputs/bindings: ledger.
Calls/effect boundaries: BudgetLedger.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[13].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:325`; AST `df43247d3e9a1323119ce795d3f01353dada1c7e238477cf98ed400282fae762`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: BudgetLedger, root. Outputs/bindings: (none).
Calls/effect boundaries: BudgetLedger.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[13].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[14]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:326`; AST `f660ab2bd95658c14df241f1bbb042167648bb05826f783cee716951874d9515`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: inherited.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[15]::If

Source: `infra/agentinfra/roadmap_runtime.py:327`; AST `fe7402ebbcb0bdc8a44df0e4cca392c7b97970397493aa99bd3bed8bb3725e2f`.

Rust module: `infra::agentinfra::roadmap_runtime`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: compiled, ledger, milestone, name, recipe_scope, root. Outputs/bindings: inherited, work_id.
Calls/effect boundaries: recipe_scope.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered If evaluation at root.body[13].body[15]; no call, error or mutation may be omitted. Condition: milestone is not None
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[15].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:328`; AST `d87826eb1b04270e73f7665e1d9e591c788d03f29f0dfe7ee46c25a928574981`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, ledger, milestone, name, recipe_scope, root. Outputs/bindings: inherited, work_id.
Calls/effect boundaries: recipe_scope.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[15].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[15].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:328`; AST `73e9e400e7be5a602f49c4f0a53aa44a582e18f2d936c52beddbd466beeb7643`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, ledger, milestone, name, recipe_scope, root. Outputs/bindings: (none).
Calls/effect boundaries: recipe_scope.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[15].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[16]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:329`; AST `597e7c835018aa2ba95b6ca1c6f8fe786ba07ed685b28372355548e344eaf445`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileLock, root. Outputs/bindings: lease.
Calls/effect boundaries: FileLock.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[16]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[16].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:329`; AST `8e00a4bc7d740dc3d04edfbd16ad1f6b400e1685b98654a9adfa0c6508d54b7e`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileLock, root. Outputs/bindings: (none).
Calls/effect boundaries: FileLock.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[16].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[17]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:330`; AST `4d8ec1b6a1b7605da659d3bd4a58e87305084395ac03de474edc83b70229037c`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lease. Outputs/bindings: (none).
Calls/effect boundaries: lease.acquire.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[17]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[17].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:330`; AST `90f35c2c815c72014528f6ee0b25d0d929a0b3c33c0fc7577df4a90ffada1455`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lease. Outputs/bindings: (none).
Calls/effect boundaries: lease.acquire.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[17].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[18]::Try

Source: `infra/agentinfra/roadmap_runtime.py:331`; AST `f64d6ccdba88fcef230737c46531ac6412674fd7f52da402af0eb805b7a14f86`.

Rust module: `infra::agentinfra::roadmap_runtime`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: BaseException, argv, attempt, diagnosis, exc, inherited, inputs, lease, ledger, name, ok, receipt, recipe, result, root, run_process, type, work_id. Outputs/bindings: attempt, ok, receipt, result.
Calls/effect boundaries: lease.release, ledger.close, ledger.reserve, run_process, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Try evaluation at root.body[13].body[18]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[18].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:332`; AST `128797a7ce36658b329d866c778dd19e3a478d826cce7fcf992545a7f80df09d`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: diagnosis, inherited, inputs, ledger, recipe, work_id. Outputs/bindings: attempt.
Calls/effect boundaries: ledger.reserve.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[18].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[18].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:332`; AST `2415374867cea1bb0a0e65d554f08af972d842a8cc384ab877d1bce14a8cabe9`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: diagnosis, inherited, inputs, ledger, recipe, work_id. Outputs/bindings: (none).
Calls/effect boundaries: ledger.reserve.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[18].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[18].body[1]::Try

Source: `infra/agentinfra/roadmap_runtime.py:335`; AST `2451bce5b4525e15091e68b91e30fa1263fa937933c8a6e7ad5b81052d1f67fc`.

Rust module: `infra::agentinfra::roadmap_runtime`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: BaseException, argv, attempt, exc, inputs, ledger, name, receipt, recipe, result, root, run_process, type. Outputs/bindings: ok, receipt, result.
Calls/effect boundaries: ledger.close, run_process, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Try evaluation at root.body[13].body[18].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[18].body[1].body[0]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:336`; AST `5a0a77f443015c25fb8751ff10f33eee995c10fdff134b88b0b44294ad25cb72`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: argv, recipe, root, run_process. Outputs/bindings: result.
Calls/effect boundaries: run_process.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[18].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[18].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:336`; AST `53ff285d5a6f1859d9a7882f6bf78e46dd8216eca3e679bb4cbcdd892fad0866`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: argv, recipe, root, run_process. Outputs/bindings: (none).
Calls/effect boundaries: run_process.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[18].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[18].body[1].body[1]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:337`; AST `2ecbedbd535378ec6e7aa60591b5cafbe87157cfc95e326e92756d72a4d6fd8a`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: argv, inputs, name, result. Outputs/bindings: receipt.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[18].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[18].body[1].body[2]::Assign

Source: `infra/agentinfra/roadmap_runtime.py:341`; AST `b3c1299d30e6607bcfab32352f143a6d494b3a2bcac40a557b7dd1dedbda2b87`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: receipt, result. Outputs/bindings: ok.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[18].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[18].body[1].handlers[0]::ExceptHandler

Source: `infra/agentinfra/roadmap_runtime.py:342`; AST `0693a57bcc28ef82b3a434a4fa88b3109998a167dc0b84fa396ce0f50de3b96b`.

Rust module: `infra::agentinfra::roadmap_runtime`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: BaseException, attempt, exc, ledger, type. Outputs/bindings: (none).
Calls/effect boundaries: ledger.close, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[13].body[18].body[1].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[18].body[1].handlers[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:343`; AST `32155c72452559d63d8f166d88319d50af3edf755312f1917accaffbb9d251a5`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: attempt, exc, ledger, type. Outputs/bindings: (none).
Calls/effect boundaries: ledger.close, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[18].body[1].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[18].body[1].handlers[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:343`; AST `503cdb75c1796ab3efdee8d8c0d1ab0dbb2c3af0eb5a6f4cc156b8cd12b331ce`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: attempt, exc, ledger, type. Outputs/bindings: (none).
Calls/effect boundaries: ledger.close, type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[18].body[1].handlers[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[18].body[1].handlers[0].body[0].value.args[2].values[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:343`; AST `760fdaff1a05c24c8db8bb1ee0c475c11403d48d9ac9c89ec3c062a1494d5d01`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exc, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[18].body[1].handlers[0].body[0].value.args[2].values[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[18].body[1].handlers[0].body[1]::Raise

Source: `infra/agentinfra/roadmap_runtime.py:344`; AST `ba28128c14dfbd0a9062c0dbab42ad6c52ecf0767df6b67576deb1dbbfdd038d`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Raise evaluation at root.body[13].body[18].body[1].handlers[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[18].body[2]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:345`; AST `d3ab36aeed6f03c0c0b1c9d0fb3ca3ba46a4352d5213c05626289b873c0660fd`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: attempt, ledger, ok, receipt. Outputs/bindings: (none).
Calls/effect boundaries: ledger.close.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[18].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[18].body[2].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:345`; AST `7d777545a191c38a43e7ca2aacc371afcf72fabb4f51fdc2087475a41ac96c69`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: attempt, ledger, ok, receipt. Outputs/bindings: (none).
Calls/effect boundaries: ledger.close.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[18].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[18].body[3]::Return

Source: `infra/agentinfra/roadmap_runtime.py:346`; AST `9b378eb582403574e9c02456d9dbe8d3ccc96e049aa98ec3ceee97d8b1bff879`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: receipt. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Return evaluation at root.body[13].body[18].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[18].finalbody[0]::Expr

Source: `infra/agentinfra/roadmap_runtime.py:348`; AST `0324b3e2db1ff1d21a06b04c85a991b516c3896842973d7f654860c5b366eef9`.

Rust module: `infra::agentinfra::roadmap_runtime`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lease. Outputs/bindings: (none).
Calls/effect boundaries: lease.release.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[18].finalbody[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_runtime.py::module::run_recipe::root.body[13].body[18].finalbody[0].value::Call

Source: `infra/agentinfra/roadmap_runtime.py:348`; AST `048afd42289a938d53fdcdbe01fdbf0cfa61c1cf67318f7be9b504d14956c5cf`.

Rust module: `infra::agentinfra::roadmap_runtime`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lease. Outputs/bindings: (none).
Calls/effect boundaries: lease.release.
Dependencies: __future__, atomic, locks, os, pathlib, process, roadmap_lease, roadmap_records, roadmap_work, security, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[18].finalbody[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
