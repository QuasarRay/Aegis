# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 193. Inventory digest: `8c5699819d36f2adc0fd5f50f9f544c7d5ee26a0fc1f47823e2d00b30fa5684e`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/atomic.py::module::root::Module

Source: `infra/agentinfra/atomic.py:1`; AST `03028ba176ebd3b5e755a993922f39720359cef9e8f85bca945f00660e4232ad`.

Rust module: `infra::agentinfra::atomic`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: AtomicWriteError, BaseException, Callable, FaultHook, FileNotFoundError, GovernanceViolation, OSError, Path, PermissionError, ValueError, _assert_confined, _call_fault, _directory_fsync, _replace_with_bounded_retry, absolute, assert_mutation_allowed, atomic_write_bytes, atomic_write_text, bool, bytes, current, data, delay, delays, desired_mode, destination, directory, durability, exc, fault, fd, flags, getattr, hasattr, int, is_path_redirect, json, kwargs, last, missing_ok, mode, obj, original_mode, os, path, preserve_mode, reject_symlinks, replaced, required, resolved_root, root, source, stage, stat, str, stream, tempfile, text, time, tmp, tmp_name. Outputs/bindings: FaultHook, absolute, current, delay, delays, desired_mode, fd, flags, last, original_mode, path, replaced, resolved_root, stream, tmp, tmp_name.
Calls/effect boundaries: AtomicWriteError, Path, ValueError, _assert_confined, _call_fault, _directory_fsync, _replace_with_bounded_retry, absolute.relative_to, assert_mutation_allowed, atomic_write_bytes, atomic_write_text, current.resolve, fault, getattr, hasattr, is_path_redirect, json.dumps, os.chmod, os.close, os.fdopen, os.fsync, os.open, os.replace, path.exists, path.parent.absolute, path.parent.mkdir, path.parent.resolve, path.stat, path.unlink, root.resolve, stat.S_IMODE, str, stream.fileno, stream.flush, stream.write, tempfile.mkstemp, text.encode, time.sleep, tmp.unlink.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::root.body[0]::ImportFrom

Source: `infra/agentinfra/atomic.py:1`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered ImportFrom evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::root.body[1]::Import

Source: `infra/agentinfra/atomic.py:3`; AST `211ee42757705c7e350e70e36b762987a737f5e9c268f2a343e2dbfcb8fbea75`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Import evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::root.body[2]::Import

Source: `infra/agentinfra/atomic.py:4`; AST `ac3a74d6dd975a8e8fe4b7f85fce794793a9355595b850e3926964913948d386`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::root.body[3]::Import

Source: `infra/agentinfra/atomic.py:5`; AST `c22b5a111acc3bea9e5136e41e207f1f95083e90d861516ce34d682526721c86`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::root.body[4]::Import

Source: `infra/agentinfra/atomic.py:6`; AST `81dafa7a7cf16b83e7a7cafd7a6702e15f4b4d576a43463dc14beb05d48e72d0`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Import evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::root.body[5]::Import

Source: `infra/agentinfra/atomic.py:7`; AST `ff05bad0fd9a7212d3cd85fd2726055168be21bc8f6e0d93b29965794b0675d4`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Import evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::root.body[6]::ImportFrom

Source: `infra/agentinfra/atomic.py:8`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered ImportFrom evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::root.body[7]::ImportFrom

Source: `infra/agentinfra/atomic.py:9`; AST `7ca2e57c1081976a3ad6ace42b615c28bf66be61f73c8cc557151d12000415bb`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered ImportFrom evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::root.body[8]::ImportFrom

Source: `infra/agentinfra/atomic.py:11`; AST `632a9db15162364f46041598eaf2830d63e78af499728e92644736ad18ec9e6d`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered ImportFrom evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::root.body[9]::ImportFrom

Source: `infra/agentinfra/atomic.py:12`; AST `eb4944c2e741a4a8bcb152b70a25f0d1c5edb1f4f8545b1913283e03370a4605`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered ImportFrom evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::AtomicWriteError::root.body[10]::ClassDef

Source: `infra/agentinfra/atomic.py:15`; AST `e34559af724f9970bc3e6fcd5f0cc073bd0c993e791b8ef4a50c65d926930ed7`.

Rust module: `infra::agentinfra::atomic`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: OSError. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered ClassDef evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::AtomicWriteError::root.body[10].body[0]::Pass

Source: `infra/agentinfra/atomic.py:16`; AST `f8e211bd496e62be79e8542ba1d0a7cebbf2a6143ae07b375ae14ce00a91b69c`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Pass evaluation at root.body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::root.body[11]::Assign

Source: `infra/agentinfra/atomic.py:19`; AST `b09f8a22292846a0bbbe1b6b73a19f42a1391353aadd3c1461ff719b2fab0110`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Callable, Path, str. Outputs/bindings: FaultHook.
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Assign evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_call_fault::root.body[12]::FunctionDef

Source: `infra/agentinfra/atomic.py:22`; AST `6efd9206c2fd7f4c4bb7a5e63741e79cfad185101db1890d9e74ee6d64231aa3`.

Rust module: `infra::agentinfra::atomic`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FaultHook, Path, fault, path, stage, str. Outputs/bindings: (none).
Calls/effect boundaries: fault.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_call_fault::root.body[12].body[0]::If

Source: `infra/agentinfra/atomic.py:23`; AST `a969b3054063328f50bd8a35669532c41f174563ad853af6714bfe44bec4b9e4`.

Rust module: `infra::agentinfra::atomic`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: fault, path, stage. Outputs/bindings: (none).
Calls/effect boundaries: fault.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered If evaluation at root.body[12].body[0]; no call, error or mutation may be omitted. Condition: fault is not None
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_call_fault::root.body[12].body[0].body[0]::Expr

Source: `infra/agentinfra/atomic.py:24`; AST `d0fc8af241266774cef866ec2bceee6c782540c22c52537f433f3bf6e8def751`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fault, path, stage. Outputs/bindings: (none).
Calls/effect boundaries: fault.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_call_fault::root.body[12].body[0].body[0].value::Call

Source: `infra/agentinfra/atomic.py:24`; AST `24fa4b44f0e840f511bcd2b1a03981cd7581b18f68b160a5e72fdffb18323018`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fault, path, stage. Outputs/bindings: (none).
Calls/effect boundaries: fault.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13]::FunctionDef

Source: `infra/agentinfra/atomic.py:27`; AST `eda1664b7e7f59224580b50918b139030229bf031948d27218a7fc879659515f`.

Rust module: `infra::agentinfra::atomic`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: AtomicWriteError, GovernanceViolation, Path, ValueError, absolute, assert_mutation_allowed, bool, current, exc, is_path_redirect, path, reject_symlinks, resolved_root, root, str. Outputs/bindings: absolute, current, resolved_root.
Calls/effect boundaries: AtomicWriteError, absolute.relative_to, assert_mutation_allowed, current.resolve, is_path_redirect, path.parent.absolute, path.parent.resolve, root.resolve, str.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[0]::If

Source: `infra/agentinfra/atomic.py:28`; AST `f5c41848c39e87d01022828c4fe335934a5d7c06ed12571b6534b6baa061c79b`.

Rust module: `infra::agentinfra::atomic`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: AtomicWriteError, path. Outputs/bindings: (none).
Calls/effect boundaries: AtomicWriteError.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered If evaluation at root.body[13].body[0]; no call, error or mutation may be omitted. Condition: '..' in path.parts
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[0].body[0]::Raise

Source: `infra/agentinfra/atomic.py:29`; AST `eedb4e3ea60da18e3544e8d5aea74991d296411b97ac4660f8490b5bd82f06ce`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: AtomicWriteError, path. Outputs/bindings: (none).
Calls/effect boundaries: AtomicWriteError.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Raise evaluation at root.body[13].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[0].body[0].exc::Call

Source: `infra/agentinfra/atomic.py:29`; AST `709cce1c6ef31f8af46e4dce948a1053af7fe2141466efaa1b3208119e2eb2c2`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: AtomicWriteError, path. Outputs/bindings: (none).
Calls/effect boundaries: AtomicWriteError.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[1]::Assign

Source: `infra/agentinfra/atomic.py:30`; AST `47d28e6a04831ba999ad1f45178bca6ca6f5e10487b020851a4e7d9fd4e0e452`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: absolute.
Calls/effect boundaries: path.parent.resolve.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[1].value.left::Call

Source: `infra/agentinfra/atomic.py:30`; AST `6b8de31f5a96bde7404c3405554f559e745b683c7e0c3108269c10c749180333`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.parent.resolve.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[2]::Assign

Source: `infra/agentinfra/atomic.py:31`; AST `ab5b2ec1ea14e72ea99a4c55b516aa40e754644c0684e6f2b686e5f01755e300`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: resolved_root.
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[3]::If

Source: `infra/agentinfra/atomic.py:32`; AST `2c477e5b200c6ef9b67192ff36f6c5c6cde5432f2bb8ba17c26c9dbc2924b1b4`.

Rust module: `infra::agentinfra::atomic`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: AtomicWriteError, GovernanceViolation, ValueError, absolute, assert_mutation_allowed, exc, path, resolved_root, root, str. Outputs/bindings: resolved_root.
Calls/effect boundaries: AtomicWriteError, absolute.relative_to, assert_mutation_allowed, root.resolve, str.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered If evaluation at root.body[13].body[3]; no call, error or mutation may be omitted. Condition: root is not None
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[3].body[0]::Assign

Source: `infra/agentinfra/atomic.py:33`; AST `c3b64e9baf9b24648afa37402d2e93eb7d7e5b710c3fe2a70ff5584090d14340`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: resolved_root.
Calls/effect boundaries: root.resolve.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[3].body[0].value::Call

Source: `infra/agentinfra/atomic.py:33`; AST `56ce091af63844ee93125714af2e994600b88740aa8b9bf3bb1ba7526dba15a7`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[3].body[1]::Try

Source: `infra/agentinfra/atomic.py:34`; AST `73042ebc39bdb0093c95e8b18a2de3ef8597f1c625a0572e37ebb93d2152a87f`.

Rust module: `infra::agentinfra::atomic`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: AtomicWriteError, GovernanceViolation, assert_mutation_allowed, exc, path, resolved_root, str. Outputs/bindings: (none).
Calls/effect boundaries: AtomicWriteError, assert_mutation_allowed, str.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Try evaluation at root.body[13].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[3].body[1].body[0]::Expr

Source: `infra/agentinfra/atomic.py:35`; AST `3d2462bf3a4eef48e6e00a5687e34bd0d576d619a0252ae8ed8c25304d89f3b0`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: assert_mutation_allowed, path, resolved_root. Outputs/bindings: (none).
Calls/effect boundaries: assert_mutation_allowed.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[3].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[3].body[1].body[0].value::Call

Source: `infra/agentinfra/atomic.py:35`; AST `35b8eb7a4fe14e2c68b012c00a119c5b61c2979235ad04bd6114257b0b3065bb`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assert_mutation_allowed, path, resolved_root. Outputs/bindings: (none).
Calls/effect boundaries: assert_mutation_allowed.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[3].body[1].handlers[0]::ExceptHandler

Source: `infra/agentinfra/atomic.py:36`; AST `45249c8b6774c5ec81d6958012bb1c4c56652639abc8971e4089ae06b96f86d3`.

Rust module: `infra::agentinfra::atomic`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: AtomicWriteError, GovernanceViolation, exc, str. Outputs/bindings: (none).
Calls/effect boundaries: AtomicWriteError, str.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[13].body[3].body[1].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[3].body[1].handlers[0].body[0]::Raise

Source: `infra/agentinfra/atomic.py:37`; AST `b71857ba281f05569db717caee3de2fdecc0d1653d3eb99c92de29f689815dd8`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: AtomicWriteError, exc, str. Outputs/bindings: (none).
Calls/effect boundaries: AtomicWriteError, str.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Raise evaluation at root.body[13].body[3].body[1].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[3].body[1].handlers[0].body[0].exc::Call

Source: `infra/agentinfra/atomic.py:37`; AST `de9c2910aa2ebe1a0b8c045bbd5a6ba1d3628344dccf97dbef420f45a6dd343e`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: AtomicWriteError, exc, str. Outputs/bindings: (none).
Calls/effect boundaries: AtomicWriteError, str.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[1].handlers[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[3].body[1].handlers[0].body[0].exc.args[0]::Call

Source: `infra/agentinfra/atomic.py:37`; AST `ed91e0e2c4feb43ad37ba7941b4ee3c7dcc36d3eb80d4a170990c028aa16f027`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exc, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[1].handlers[0].body[0].exc.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[3].body[2]::Try

Source: `infra/agentinfra/atomic.py:38`; AST `1e2a5599d1b521d1c352ed2620c6238d38a8c34f07026881411770ed02c5ffdf`.

Rust module: `infra::agentinfra::atomic`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: AtomicWriteError, ValueError, absolute, exc, path, resolved_root. Outputs/bindings: (none).
Calls/effect boundaries: AtomicWriteError, absolute.relative_to.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Try evaluation at root.body[13].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[3].body[2].body[0]::Expr

Source: `infra/agentinfra/atomic.py:39`; AST `cb16276f53e8e57a14193ae763c55fb82facd9f6025080429f6920e20c4635f3`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: absolute, resolved_root. Outputs/bindings: (none).
Calls/effect boundaries: absolute.relative_to.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[3].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[3].body[2].body[0].value::Call

Source: `infra/agentinfra/atomic.py:39`; AST `d96c25c8a9631b32f20b1669b546e7dedf14bbc508aa6017020005629bf42957`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: absolute, resolved_root. Outputs/bindings: (none).
Calls/effect boundaries: absolute.relative_to.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[3].body[2].handlers[0]::ExceptHandler

Source: `infra/agentinfra/atomic.py:40`; AST `316df402748db635155ac826c61fe8856a079a58c40787ee12ceadf8840e7a2d`.

Rust module: `infra::agentinfra::atomic`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: AtomicWriteError, ValueError, exc, path, resolved_root. Outputs/bindings: (none).
Calls/effect boundaries: AtomicWriteError.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[13].body[3].body[2].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[3].body[2].handlers[0].body[0]::Raise

Source: `infra/agentinfra/atomic.py:41`; AST `69bffe36592a6c6d48d4d40c784c67d3bc15596a39b4fcf7b8659fbc72f9bec8`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: AtomicWriteError, exc, path, resolved_root. Outputs/bindings: (none).
Calls/effect boundaries: AtomicWriteError.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Raise evaluation at root.body[13].body[3].body[2].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[3].body[2].handlers[0].body[0].exc::Call

Source: `infra/agentinfra/atomic.py:41`; AST `dfd39b36d25655f55b1673a46c6b029cb6c64fd26964bd416bbcf098d7c9dc43`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: AtomicWriteError, path, resolved_root. Outputs/bindings: (none).
Calls/effect boundaries: AtomicWriteError.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].body[2].handlers[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[4]::If

Source: `infra/agentinfra/atomic.py:42`; AST `c0b22a26862bfd1e20e4861fc6b43d32a1b2d7b838f300373b146ca14e8e22ab`.

Rust module: `infra::agentinfra::atomic`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: AtomicWriteError, current, is_path_redirect, path, reject_symlinks, resolved_root. Outputs/bindings: current.
Calls/effect boundaries: AtomicWriteError, current.resolve, is_path_redirect, path.parent.absolute.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered If evaluation at root.body[13].body[4]; no call, error or mutation may be omitted. Condition: reject_symlinks
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[4].body[0]::If

Source: `infra/agentinfra/atomic.py:43`; AST `fe74a0005f923c5da9d81f46eb4ef81186f6ba92f7cb5509bd1df95542bc4b21`.

Rust module: `infra::agentinfra::atomic`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: AtomicWriteError, is_path_redirect, path. Outputs/bindings: (none).
Calls/effect boundaries: AtomicWriteError, is_path_redirect.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered If evaluation at root.body[13].body[4].body[0]; no call, error or mutation may be omitted. Condition: is_path_redirect(path)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[4].body[0].test::Call

Source: `infra/agentinfra/atomic.py:43`; AST `d9cac03fb65b00711ae1083fa305b5510d29827fd7fb7d268ae3ec96200e726a`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: is_path_redirect, path. Outputs/bindings: (none).
Calls/effect boundaries: is_path_redirect.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[0].test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[4].body[0].body[0]::Raise

Source: `infra/agentinfra/atomic.py:44`; AST `50a1311341376f1e3a8b247b937573aa5d4cb16148169987efe2ae938711e0d3`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: AtomicWriteError, path. Outputs/bindings: (none).
Calls/effect boundaries: AtomicWriteError.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Raise evaluation at root.body[13].body[4].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[4].body[0].body[0].exc::Call

Source: `infra/agentinfra/atomic.py:44`; AST `86037ed16562a156dc6a4dd7774b48867a417209f3656b82baa33fd83aeaa72a`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: AtomicWriteError, path. Outputs/bindings: (none).
Calls/effect boundaries: AtomicWriteError.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[4].body[1]::Assign

Source: `infra/agentinfra/atomic.py:45`; AST `877b38c3d520bcb93f854317b819d1a206fa151dd5f8081e29fa129ffc428f11`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: current.
Calls/effect boundaries: path.parent.absolute.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[4].body[1].value::Call

Source: `infra/agentinfra/atomic.py:45`; AST `163c65ba2a348e42e40a48d978d05c3ea8347815acc768e46cd15f9d6fe2dcb6`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.parent.absolute.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[4].body[2]::While

Source: `infra/agentinfra/atomic.py:46`; AST `a64941c9b7723ce949503551051cf35a0990756489a9aa07811f1344daed32ff`.

Rust module: `infra::agentinfra::atomic`. while with explicit truth conversion and a normal-exhaustion flag for loop else

Inputs: AtomicWriteError, current, is_path_redirect, path, resolved_root. Outputs/bindings: current.
Calls/effect boundaries: AtomicWriteError, current.resolve, is_path_redirect.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered While evaluation at root.body[13].body[4].body[2]; no call, error or mutation may be omitted. Condition: True
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[4].body[2].body[0]::If

Source: `infra/agentinfra/atomic.py:47`; AST `e234ec9c7d7ca01488e18fe7c2f7bde5b947b08b522ba51e829ed6974bd79433`.

Rust module: `infra::agentinfra::atomic`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: AtomicWriteError, current, is_path_redirect. Outputs/bindings: (none).
Calls/effect boundaries: AtomicWriteError, is_path_redirect.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered If evaluation at root.body[13].body[4].body[2].body[0]; no call, error or mutation may be omitted. Condition: is_path_redirect(current)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[4].body[2].body[0].test::Call

Source: `infra/agentinfra/atomic.py:47`; AST `40016ece3accb20f8c991e15dbde33edb0976b624a9765bc08db3981c15afe10`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current, is_path_redirect. Outputs/bindings: (none).
Calls/effect boundaries: is_path_redirect.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[2].body[0].test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[4].body[2].body[0].body[0]::Raise

Source: `infra/agentinfra/atomic.py:48`; AST `b9bcf15c6e0056b7905f4105e4ec1074434eb4e26e643e0cbc14fe24e742d684`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: AtomicWriteError, current. Outputs/bindings: (none).
Calls/effect boundaries: AtomicWriteError.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Raise evaluation at root.body[13].body[4].body[2].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[4].body[2].body[0].body[0].exc::Call

Source: `infra/agentinfra/atomic.py:48`; AST `5b3c3f8ae118ae07b6a6088cfbc908ba15e1e5b7aa659a6a4221ae822362d0c4`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: AtomicWriteError, current. Outputs/bindings: (none).
Calls/effect boundaries: AtomicWriteError.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[2].body[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[4].body[2].body[1]::If

Source: `infra/agentinfra/atomic.py:53`; AST `88864946e1c4bd0ec9629e2397d9aca89fe4412bf680f280429009b95418b222`.

Rust module: `infra::agentinfra::atomic`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: current, resolved_root. Outputs/bindings: (none).
Calls/effect boundaries: current.resolve.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered If evaluation at root.body[13].body[4].body[2].body[1]; no call, error or mutation may be omitted. Condition: resolved_root is not None and current.resolve(strict=False) == resolved_root
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[4].body[2].body[1].test.values[1].left::Call

Source: `infra/agentinfra/atomic.py:53`; AST `75660c4503b14a163ef89f8fd71005ef913b8a50d4d629b6b2f7824a7d11a9de`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current. Outputs/bindings: (none).
Calls/effect boundaries: current.resolve.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[2].body[1].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[4].body[2].body[1].body[0]::Break

Source: `infra/agentinfra/atomic.py:54`; AST `c0d25d96e6146e7b648417b86bf6bbfedd0a458099247cf2cd469124da4c9fec`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Break evaluation at root.body[13].body[4].body[2].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[4].body[2].body[2]::If

Source: `infra/agentinfra/atomic.py:55`; AST `28af965b07fe4ec353d482793957716ae77ca434121877e1a982ed6ab87fe23a`.

Rust module: `infra::agentinfra::atomic`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: current, resolved_root. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered If evaluation at root.body[13].body[4].body[2].body[2]; no call, error or mutation may be omitted. Condition: resolved_root is None and current.parent == current
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[4].body[2].body[2].body[0]::Break

Source: `infra/agentinfra/atomic.py:56`; AST `c0d25d96e6146e7b648417b86bf6bbfedd0a458099247cf2cd469124da4c9fec`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Break evaluation at root.body[13].body[4].body[2].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[4].body[2].body[3]::If

Source: `infra/agentinfra/atomic.py:57`; AST `efc89bd46d4044927eab454935796cea750ef67673bb8bf7527dd81625bec908`.

Rust module: `infra::agentinfra::atomic`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: AtomicWriteError, current, path, resolved_root. Outputs/bindings: (none).
Calls/effect boundaries: AtomicWriteError.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered If evaluation at root.body[13].body[4].body[2].body[3]; no call, error or mutation may be omitted. Condition: current.parent == current
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[4].body[2].body[3].body[0]::Raise

Source: `infra/agentinfra/atomic.py:58`; AST `fcd43a06ade0949a0885dff038969999a568e649c44f9ea462883c13ed6f2acb`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: AtomicWriteError, path, resolved_root. Outputs/bindings: (none).
Calls/effect boundaries: AtomicWriteError.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Raise evaluation at root.body[13].body[4].body[2].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[4].body[2].body[3].body[0].exc::Call

Source: `infra/agentinfra/atomic.py:58`; AST `fe6194edddaba1713dbd901562166003f14db9baad9ddd62926181bed0d48ca4`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: AtomicWriteError, path, resolved_root. Outputs/bindings: (none).
Calls/effect boundaries: AtomicWriteError.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[2].body[3].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_assert_confined::root.body[13].body[4].body[2].body[4]::Assign

Source: `infra/agentinfra/atomic.py:59`; AST `15acd7d7c7e99f81956b6b67607b11be0af45773df9251b18eb5a4614d523e95`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current. Outputs/bindings: current.
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4].body[2].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_directory_fsync::root.body[14]::FunctionDef

Source: `infra/agentinfra/atomic.py:62`; AST `b93b49e92fdfe8af7c6e17e1fa081f22cf689e8e2ba0b288eea20e1dc370c54f`.

Rust module: `infra::agentinfra::atomic`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: OSError, Path, bool, directory, fd, flags, getattr, hasattr, os, required. Outputs/bindings: fd, flags.
Calls/effect boundaries: getattr, hasattr, os.close, os.fsync, os.open.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_directory_fsync::root.body[14].body[0]::If

Source: `infra/agentinfra/atomic.py:63`; AST `9e326f6332a158eae0b80451838893219355a7ada220204e21312a7f8c1524be`.

Rust module: `infra::agentinfra::atomic`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: hasattr, os, required. Outputs/bindings: (none).
Calls/effect boundaries: hasattr.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered If evaluation at root.body[14].body[0]; no call, error or mutation may be omitted. Condition: os.name == 'nt'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_directory_fsync::root.body[14].body[0].body[0]::If

Source: `infra/agentinfra/atomic.py:66`; AST `0b3e8a74aafb438b87f7b94495a7a49609ab138660ac6fdde6e6d7b3ce5172f6`.

Rust module: `infra::agentinfra::atomic`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: hasattr, os, required. Outputs/bindings: (none).
Calls/effect boundaries: hasattr.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered If evaluation at root.body[14].body[0].body[0]; no call, error or mutation may be omitted. Condition: required and (not hasattr(os, 'O_DIRECTORY'))
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_directory_fsync::root.body[14].body[0].body[0].test.values[1].operand::Call

Source: `infra/agentinfra/atomic.py:66`; AST `055f1f23470d36fca086c6df0bb9c6cc58646d240f821b3c72915736f4d04141`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: hasattr, os. Outputs/bindings: (none).
Calls/effect boundaries: hasattr.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].body[0].test.values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_directory_fsync::root.body[14].body[0].body[0].body[0]::Return

Source: `infra/agentinfra/atomic.py:67`; AST `d3ec646650be52e3f5b5700447f19313b1bab9ed1bd27c2483960d5d0bcaf584`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Return evaluation at root.body[14].body[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_directory_fsync::root.body[14].body[1]::Assign

Source: `infra/agentinfra/atomic.py:68`; AST `84ff88698f76f05433832129ccbb46ceef3a4ae6786ade8dbc4d8a39783be655`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: getattr, os. Outputs/bindings: flags.
Calls/effect boundaries: getattr.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_directory_fsync::root.body[14].body[1].value.right::Call

Source: `infra/agentinfra/atomic.py:68`; AST `2a881ede28f8434651113459fab4182adc43df3395fac06431bc7ab3f4b9a876`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: getattr, os. Outputs/bindings: (none).
Calls/effect boundaries: getattr.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].value.right; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_directory_fsync::root.body[14].body[2]::Try

Source: `infra/agentinfra/atomic.py:69`; AST `35a3e705324204355d523e39f50c33fbec4d9ed8df721ed8d0a054892b5a32c4`.

Rust module: `infra::agentinfra::atomic`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: OSError, directory, flags, os, required. Outputs/bindings: fd.
Calls/effect boundaries: os.open.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Try evaluation at root.body[14].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_directory_fsync::root.body[14].body[2].body[0]::Assign

Source: `infra/agentinfra/atomic.py:70`; AST `1cd1c32c19321e7606ab0ebfc30b54d89e4c715b72bce105f2fcae64c3ef1214`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: directory, flags, os. Outputs/bindings: fd.
Calls/effect boundaries: os.open.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_directory_fsync::root.body[14].body[2].body[0].value::Call

Source: `infra/agentinfra/atomic.py:70`; AST `e710276c49d6c06a24a8538cba0b994ccbe6e7a74e232b68d53e1297337e954c`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: directory, flags, os. Outputs/bindings: (none).
Calls/effect boundaries: os.open.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_directory_fsync::root.body[14].body[2].handlers[0]::ExceptHandler

Source: `infra/agentinfra/atomic.py:71`; AST `af9c54e95a8b93e9f85c133e5c10dc7fce0b544f23358ebbe5133d511420344d`.

Rust module: `infra::agentinfra::atomic`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: OSError, os, required. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[14].body[2].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_directory_fsync::root.body[14].body[2].handlers[0].body[0]::If

Source: `infra/agentinfra/atomic.py:72`; AST `cd182727d5d8305d769c21a87a33ba360f89360e9768c9e5e97c7cacb3f44a45`.

Rust module: `infra::agentinfra::atomic`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: os, required. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered If evaluation at root.body[14].body[2].handlers[0].body[0]; no call, error or mutation may be omitted. Condition: required and os.name != 'nt'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_directory_fsync::root.body[14].body[2].handlers[0].body[0].body[0]::Raise

Source: `infra/agentinfra/atomic.py:73`; AST `ba28128c14dfbd0a9062c0dbab42ad6c52ecf0767df6b67576deb1dbbfdd038d`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Raise evaluation at root.body[14].body[2].handlers[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_directory_fsync::root.body[14].body[2].handlers[0].body[1]::Return

Source: `infra/agentinfra/atomic.py:74`; AST `d3ec646650be52e3f5b5700447f19313b1bab9ed1bd27c2483960d5d0bcaf584`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Return evaluation at root.body[14].body[2].handlers[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_directory_fsync::root.body[14].body[3]::Try

Source: `infra/agentinfra/atomic.py:75`; AST `529ef3348786346baa90d47d5d0ad784bcb854af9964d9724a245a071844ef2d`.

Rust module: `infra::agentinfra::atomic`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: OSError, fd, os, required. Outputs/bindings: (none).
Calls/effect boundaries: os.close, os.fsync.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Try evaluation at root.body[14].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_directory_fsync::root.body[14].body[3].body[0]::Expr

Source: `infra/agentinfra/atomic.py:76`; AST `eedcbe43b38b93d540b012dfe32683f858605c442e1a0c6e2ebf2ab33d969045`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fd, os. Outputs/bindings: (none).
Calls/effect boundaries: os.fsync.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_directory_fsync::root.body[14].body[3].body[0].value::Call

Source: `infra/agentinfra/atomic.py:76`; AST `cc0a9205313b39d7f2cc9a509076711d694bfe64931498c6c65e79aedcf39fa1`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fd, os. Outputs/bindings: (none).
Calls/effect boundaries: os.fsync.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[14].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_directory_fsync::root.body[14].body[3].handlers[0]::ExceptHandler

Source: `infra/agentinfra/atomic.py:77`; AST `3201c85da35a476358e89838187f98dbf8aa02bc684685c627270d63fb3e451f`.

Rust module: `infra::agentinfra::atomic`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: OSError, required. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[14].body[3].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_directory_fsync::root.body[14].body[3].handlers[0].body[0]::If

Source: `infra/agentinfra/atomic.py:78`; AST `3e94b024a922c96c1861256aa3d14042162e2e297cef60eeb93edac2f83bdfcd`.

Rust module: `infra::agentinfra::atomic`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: required. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered If evaluation at root.body[14].body[3].handlers[0].body[0]; no call, error or mutation may be omitted. Condition: required
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_directory_fsync::root.body[14].body[3].handlers[0].body[0].body[0]::Raise

Source: `infra/agentinfra/atomic.py:79`; AST `ba28128c14dfbd0a9062c0dbab42ad6c52ecf0767df6b67576deb1dbbfdd038d`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Raise evaluation at root.body[14].body[3].handlers[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_directory_fsync::root.body[14].body[3].finalbody[0]::Expr

Source: `infra/agentinfra/atomic.py:81`; AST `e3651c239428eac3c5a211e0813f2890d1a9be94a2f9822a2a262c2f1b0dc3de`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fd, os. Outputs/bindings: (none).
Calls/effect boundaries: os.close.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[3].finalbody[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_directory_fsync::root.body[14].body[3].finalbody[0].value::Call

Source: `infra/agentinfra/atomic.py:81`; AST `5e53ed07e4ca5a07b4ea1627e0c8c20d53193bf9a8eca3acdc75bafd1d79af7f`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fd, os. Outputs/bindings: (none).
Calls/effect boundaries: os.close.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[14].body[3].finalbody[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_replace_with_bounded_retry::root.body[15]::FunctionDef

Source: `infra/agentinfra/atomic.py:84`; AST `ea812b27f7c81744c371ba7acf6e640a70816eb1a8f63bbc42c33ec5cbeb719b`.

Rust module: `infra::agentinfra::atomic`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: OSError, Path, PermissionError, delay, delays, destination, exc, last, os, source, time. Outputs/bindings: delay, delays, last.
Calls/effect boundaries: os.replace, time.sleep.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_replace_with_bounded_retry::root.body[15].body[0]::Expr

Source: `infra/agentinfra/atomic.py:85`; AST `43ef89ceecde612a46d4c1e9b1d67bc540fc8cad2fab755aa3b1d4e5bc6b25d5`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_replace_with_bounded_retry::root.body[15].body[1]::Assign

Source: `infra/agentinfra/atomic.py:86`; AST `50bc03dd1e60c5ba8806efcf78ac505068feb89b7631489b696db097d2b71682`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: os. Outputs/bindings: delays.
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_replace_with_bounded_retry::root.body[15].body[2]::AnnAssign

Source: `infra/agentinfra/atomic.py:87`; AST `c9f9f5d66c5da25c509ceebb104d7f36c883fa291382261ad5441f6d5e68a045`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: OSError. Outputs/bindings: last.
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered AnnAssign evaluation at root.body[15].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_replace_with_bounded_retry::root.body[15].body[3]::For

Source: `infra/agentinfra/atomic.py:88`; AST `f2d26efae8137e49c69870e54ff56a52a204db2c69cd15fe5c9a2b2d793d3989`.

Rust module: `infra::agentinfra::atomic`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: PermissionError, delay, delays, destination, exc, os, source, time. Outputs/bindings: delay, last.
Calls/effect boundaries: os.replace, time.sleep.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered For evaluation at root.body[15].body[3]; no call, error or mutation may be omitted. Iteration: delay in delays
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_replace_with_bounded_retry::root.body[15].body[3].body[0]::If

Source: `infra/agentinfra/atomic.py:89`; AST `ffd0ebf7abdb267ef583b1a6577a01ad8579277e2e4a0dc2d4223611de05258e`.

Rust module: `infra::agentinfra::atomic`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: delay, time. Outputs/bindings: (none).
Calls/effect boundaries: time.sleep.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered If evaluation at root.body[15].body[3].body[0]; no call, error or mutation may be omitted. Condition: delay
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_replace_with_bounded_retry::root.body[15].body[3].body[0].body[0]::Expr

Source: `infra/agentinfra/atomic.py:90`; AST `63460f424effbf8b7431cba8d93b061f273993505e5342b990dd6ee91178a9d9`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: delay, time. Outputs/bindings: (none).
Calls/effect boundaries: time.sleep.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[3].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_replace_with_bounded_retry::root.body[15].body[3].body[0].body[0].value::Call

Source: `infra/agentinfra/atomic.py:90`; AST `77933c8d2024856a54243855e5a5ced8ff5fce6afbb828d52c8100a292a2cdf3`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: delay, time. Outputs/bindings: (none).
Calls/effect boundaries: time.sleep.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_replace_with_bounded_retry::root.body[15].body[3].body[1]::Try

Source: `infra/agentinfra/atomic.py:91`; AST `3b8f314cd726891d718ae1f3a64b108ca8a2f439ecf238e128b3c360337f7ba2`.

Rust module: `infra::agentinfra::atomic`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: PermissionError, destination, exc, os, source. Outputs/bindings: last.
Calls/effect boundaries: os.replace.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Try evaluation at root.body[15].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_replace_with_bounded_retry::root.body[15].body[3].body[1].body[0]::Expr

Source: `infra/agentinfra/atomic.py:92`; AST `170006999f3546e88039abf9112a20351e82153ee4f6c097ef65a8c8d9549d96`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: destination, os, source. Outputs/bindings: (none).
Calls/effect boundaries: os.replace.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[3].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_replace_with_bounded_retry::root.body[15].body[3].body[1].body[0].value::Call

Source: `infra/agentinfra/atomic.py:92`; AST `16481509b93b447ff0cd0023faeff35d5aef197a1831e433ed9cde537d25c4aa`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: destination, os, source. Outputs/bindings: (none).
Calls/effect boundaries: os.replace.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_replace_with_bounded_retry::root.body[15].body[3].body[1].body[1]::Return

Source: `infra/agentinfra/atomic.py:93`; AST `d3ec646650be52e3f5b5700447f19313b1bab9ed1bd27c2483960d5d0bcaf584`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Return evaluation at root.body[15].body[3].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_replace_with_bounded_retry::root.body[15].body[3].body[1].handlers[0]::ExceptHandler

Source: `infra/agentinfra/atomic.py:94`; AST `e239667fe236d7a3b0eab20b55449aec1736c67263e5db44d3649265a97e64d6`.

Rust module: `infra::agentinfra::atomic`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: PermissionError, exc. Outputs/bindings: last.
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[15].body[3].body[1].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_replace_with_bounded_retry::root.body[15].body[3].body[1].handlers[0].body[0]::Assign

Source: `infra/agentinfra/atomic.py:95`; AST `99a5cac4be16e7b8e66035d8b490db7915be888a23d22613580c86e1bd587db4`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: exc. Outputs/bindings: last.
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[3].body[1].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_replace_with_bounded_retry::root.body[15].body[4]::Assert

Source: `infra/agentinfra/atomic.py:96`; AST `06cd201c1e85bf53cfad9bb9551451b9930539c2a45010e38a5d4f4a98881b91`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: last. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Assert evaluation at root.body[15].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::_replace_with_bounded_retry::root.body[15].body[5]::Raise

Source: `infra/agentinfra/atomic.py:97`; AST `e0eb85e9a8b8054f67792c17139f2340f592e3f2014f085006b85305eb574745`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: last. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Raise evaluation at root.body[15].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16]::FunctionDef

Source: `infra/agentinfra/atomic.py:100`; AST `742480ef0c36722e0a061a82f87ec2ab869f19d847c21fcd3f0d7debe96853d4`.

Rust module: `infra::agentinfra::atomic`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: BaseException, FaultHook, Path, ValueError, _assert_confined, _call_fault, _directory_fsync, _replace_with_bounded_retry, bool, bytes, data, desired_mode, durability, fault, fd, int, mode, original_mode, os, path, preserve_mode, reject_symlinks, replaced, root, stat, str, stream, tempfile, tmp, tmp_name. Outputs/bindings: desired_mode, fd, original_mode, path, replaced, stream, tmp, tmp_name.
Calls/effect boundaries: Path, ValueError, _assert_confined, _call_fault, _directory_fsync, _replace_with_bounded_retry, os.chmod, os.close, os.fdopen, os.fsync, path.exists, path.parent.mkdir, path.stat, stat.S_IMODE, stream.fileno, stream.flush, stream.write, tempfile.mkstemp, tmp.unlink.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[0]::Expr

Source: `infra/agentinfra/atomic.py:111`; AST `46ce39b6a4a1bf1e9b7646027df19f317bcaa5469ec88caf4ffd086430a5a8ed`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[1]::Assign

Source: `infra/agentinfra/atomic.py:119`; AST `a6e457796281606eb892c15254e3e12d1f482a1a1ab80964ac184f36d274d875`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, path. Outputs/bindings: path.
Calls/effect boundaries: Path.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[1].value::Call

Source: `infra/agentinfra/atomic.py:119`; AST `c4b629495a6e643da3774e82f742688d4a24128b1ff8b4448236e96c64f51421`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, path. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[2]::If

Source: `infra/agentinfra/atomic.py:120`; AST `b419baeb5e06375837ec2d995fd010a6d084b9d7ab22a67e98668bd9effe9e22`.

Rust module: `infra::agentinfra::atomic`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ValueError, durability. Outputs/bindings: (none).
Calls/effect boundaries: ValueError.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered If evaluation at root.body[16].body[2]; no call, error or mutation may be omitted. Condition: durability not in {'required', 'best-effort'}
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[2].body[0]::Raise

Source: `infra/agentinfra/atomic.py:121`; AST `31b44842b8bb02cf12e0858f72826f431c05b7675a89500671a0d191e9903576`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ValueError. Outputs/bindings: (none).
Calls/effect boundaries: ValueError.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Raise evaluation at root.body[16].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[2].body[0].exc::Call

Source: `infra/agentinfra/atomic.py:121`; AST `aea48545e7e75dcd73d2775329fe27c2c1e1f48164dbf3a698b9d7a065488ebe`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ValueError. Outputs/bindings: (none).
Calls/effect boundaries: ValueError.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[3]::Expr

Source: `infra/agentinfra/atomic.py:122`; AST `24896f1a9a04cc21515521f380749bd6711c3c5c69defe8453ac1784034a70f4`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _assert_confined, path, reject_symlinks, root. Outputs/bindings: (none).
Calls/effect boundaries: _assert_confined.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[3].value::Call

Source: `infra/agentinfra/atomic.py:122`; AST `34994b6e67c3a5c237e521e0767046445b626528802ffa2ca00a395b7b75639c`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _assert_confined, path, reject_symlinks, root. Outputs/bindings: (none).
Calls/effect boundaries: _assert_confined.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[4]::Expr

Source: `infra/agentinfra/atomic.py:123`; AST `ee4624f1df91400daa13a3f4fa8ccf0654522660a49483e139d870f1d98cac38`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.parent.mkdir.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[4].value::Call

Source: `infra/agentinfra/atomic.py:123`; AST `f32fa3bf8bd728879b5ee78564c0e339658253e810165c3df033c0892f416875`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.parent.mkdir.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[5]::Expr

Source: `infra/agentinfra/atomic.py:124`; AST `24896f1a9a04cc21515521f380749bd6711c3c5c69defe8453ac1784034a70f4`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _assert_confined, path, reject_symlinks, root. Outputs/bindings: (none).
Calls/effect boundaries: _assert_confined.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[5].value::Call

Source: `infra/agentinfra/atomic.py:124`; AST `34994b6e67c3a5c237e521e0767046445b626528802ffa2ca00a395b7b75639c`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _assert_confined, path, reject_symlinks, root. Outputs/bindings: (none).
Calls/effect boundaries: _assert_confined.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[6]::Assign

Source: `infra/agentinfra/atomic.py:125`; AST `ec06751214477e33a0759c739e30277d3a37121265e95586516a8275ddb662b4`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: original_mode.
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[7]::If

Source: `infra/agentinfra/atomic.py:126`; AST `a3d0cde1e25d696d475ee4c858fa919e29726afef392996f8d00a75b379575a3`.

Rust module: `infra::agentinfra::atomic`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: path, preserve_mode, stat. Outputs/bindings: original_mode.
Calls/effect boundaries: path.exists, path.stat, stat.S_IMODE.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered If evaluation at root.body[16].body[7]; no call, error or mutation may be omitted. Condition: path.exists() and preserve_mode
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[7].test.values[0]::Call

Source: `infra/agentinfra/atomic.py:126`; AST `2cac3ec82b344023c57b4bbfcae282698ef12842cbda26a14724eacbefb97016`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.exists.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].test.values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[7].body[0]::Assign

Source: `infra/agentinfra/atomic.py:127`; AST `9cf3a07d55d244306af7b93cee958d7edba6ecea6659d4d4349cc2998bacd0d3`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path, stat. Outputs/bindings: original_mode.
Calls/effect boundaries: path.stat, stat.S_IMODE.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[7].body[0].value::Call

Source: `infra/agentinfra/atomic.py:127`; AST `5000b3727d4a08bc08940fc09e3a239c8cae85b8ce1b1e370944035830d61bda`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, stat. Outputs/bindings: (none).
Calls/effect boundaries: path.stat, stat.S_IMODE.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[7].body[0].value.args[0].value::Call

Source: `infra/agentinfra/atomic.py:127`; AST `d0f2660d5c576e75c41493128e9ef73fd43d1401a0dd272c961864f7164b7698`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.stat.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[0].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[8]::Assign

Source: `infra/agentinfra/atomic.py:128`; AST `8948b891e7d06d0541fc7ee0acbc01c924dc7a95ebaf6913e6f426f81a5259cd`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: mode, original_mode. Outputs/bindings: desired_mode.
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[9]::Expr

Source: `infra/agentinfra/atomic.py:129`; AST `9130db38bccfea91bc196ffb99b9a640125c16556909686c0bdd46a17781f1fc`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _call_fault, fault, path. Outputs/bindings: (none).
Calls/effect boundaries: _call_fault.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[9].value::Call

Source: `infra/agentinfra/atomic.py:129`; AST `64f8728489088ac1a8d9e0ad9a04b36bb5aad48f617dd5e9597274c4a614e188`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _call_fault, fault, path. Outputs/bindings: (none).
Calls/effect boundaries: _call_fault.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[10]::Assign

Source: `infra/agentinfra/atomic.py:130`; AST `68dbfd83f3f6f1c4d4920df29120ff24eb1fbffa060ffda582ccb5778023ad22`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path, tempfile. Outputs/bindings: fd, tmp_name.
Calls/effect boundaries: tempfile.mkstemp.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[10].value::Call

Source: `infra/agentinfra/atomic.py:130`; AST `bd63f987db9fdfb79a23e66e838a6cc27c413ab5a93bf50fd5191e3520fdcdf1`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.mkstemp.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[11]::Assign

Source: `infra/agentinfra/atomic.py:131`; AST `9a855231d31abe96320ee313b16abd77d3edd91d5926e62fed49ca34207923ea`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, tmp_name. Outputs/bindings: tmp.
Calls/effect boundaries: Path.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[11].value::Call

Source: `infra/agentinfra/atomic.py:131`; AST `4608e77e2dbea7780ef095500b0306224d49256e71f8212cf6788ec460ca14cb`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, tmp_name. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[12]::Assign

Source: `infra/agentinfra/atomic.py:132`; AST `cd17a82baccc8ed424a1b228c5134b0bd5415ee42a4a5967504e1ea1eb87c79f`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: replaced.
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13]::Try

Source: `infra/agentinfra/atomic.py:133`; AST `52666b559d822566dc2fc80e7b2f21f1200952a4fc52d6790d55b1cba00e5c07`.

Rust module: `infra::agentinfra::atomic`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: BaseException, _call_fault, _directory_fsync, _replace_with_bounded_retry, data, desired_mode, durability, fault, fd, os, path, replaced, stream, tmp. Outputs/bindings: fd, replaced, stream.
Calls/effect boundaries: _call_fault, _directory_fsync, _replace_with_bounded_retry, os.chmod, os.close, os.fdopen, os.fsync, stream.fileno, stream.flush, stream.write, tmp.unlink.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Try evaluation at root.body[16].body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].body[0]::Expr

Source: `infra/agentinfra/atomic.py:134`; AST `b40d0a89db5c3c78c0a19b98f0cb8a85b46c836a3ec0949c0c44892da12ab897`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: desired_mode, os, tmp. Outputs/bindings: (none).
Calls/effect boundaries: os.chmod.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].body[0].value::Call

Source: `infra/agentinfra/atomic.py:134`; AST `f0031ba8cc602491b691891db08250e1118d893277262865cce61b7c831388a5`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: desired_mode, os, tmp. Outputs/bindings: (none).
Calls/effect boundaries: os.chmod.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[13].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].body[1]::Expr

Source: `infra/agentinfra/atomic.py:135`; AST `3e404ad48cf1a33c262df82662cb697cf023507b2f2d15aed31912fadfaa8704`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _call_fault, fault, path. Outputs/bindings: (none).
Calls/effect boundaries: _call_fault.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[13].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].body[1].value::Call

Source: `infra/agentinfra/atomic.py:135`; AST `0da5c68b330b0afb2bffcfb769951d2dfef9c879478e47aab0646882e1a88cf4`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _call_fault, fault, path. Outputs/bindings: (none).
Calls/effect boundaries: _call_fault.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[13].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].body[2]::With

Source: `infra/agentinfra/atomic.py:136`; AST `7f92a911596a1b8c0a2f5109655deb7b48234c6884a65b1cde6c0f86d973309c`.

Rust module: `infra::agentinfra::atomic`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: _call_fault, data, fault, fd, os, path, stream. Outputs/bindings: fd, stream.
Calls/effect boundaries: _call_fault, os.fdopen, os.fsync, stream.fileno, stream.flush, stream.write.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered With evaluation at root.body[16].body[13].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].body[2].items[0].context_expr::Call

Source: `infra/agentinfra/atomic.py:136`; AST `58f2083f99f9d565afcbde03da3923bbe8eeeda611fed024de1825d26447d890`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fd, os. Outputs/bindings: (none).
Calls/effect boundaries: os.fdopen.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[13].body[2].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].body[2].body[0]::Assign

Source: `infra/agentinfra/atomic.py:137`; AST `919142994985c96cedcfa59e82d8125ed5e72efbf1b04d4680c16bb3417c35f9`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: fd.
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[13].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].body[2].body[1]::Expr

Source: `infra/agentinfra/atomic.py:138`; AST `7df58b0a179fc266b559edcf7625b4f664e9a6cd7a7e21d1f61e4ceb9272473c`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: data, stream. Outputs/bindings: (none).
Calls/effect boundaries: stream.write.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[13].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].body[2].body[1].value::Call

Source: `infra/agentinfra/atomic.py:138`; AST `9085f467734f1adf8d5092c3aaed185a7d0e1af466a43f6bf79dbd06b6fd9a6f`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data, stream. Outputs/bindings: (none).
Calls/effect boundaries: stream.write.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[13].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].body[2].body[2]::Expr

Source: `infra/agentinfra/atomic.py:139`; AST `95c6470424940b8c49192ce7c87518b4b98341e35105afae0d30cd9460c532df`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _call_fault, fault, path. Outputs/bindings: (none).
Calls/effect boundaries: _call_fault.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[13].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].body[2].body[2].value::Call

Source: `infra/agentinfra/atomic.py:139`; AST `54e761eed6a768e9ffc907c906718f98b28d0dc1794b7927dc99bfbc1e63cebd`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _call_fault, fault, path. Outputs/bindings: (none).
Calls/effect boundaries: _call_fault.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[13].body[2].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].body[2].body[3]::Expr

Source: `infra/agentinfra/atomic.py:140`; AST `30712519db7cf7c545c522e94f0bbceb17159cd53838ebe3acb16ebc578916dd`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: stream. Outputs/bindings: (none).
Calls/effect boundaries: stream.flush.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[13].body[2].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].body[2].body[3].value::Call

Source: `infra/agentinfra/atomic.py:140`; AST `dc9183626915285572f9f5f11a4c11f0386db10bee4db107d63c2469769b0631`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: stream. Outputs/bindings: (none).
Calls/effect boundaries: stream.flush.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[13].body[2].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].body[2].body[4]::Expr

Source: `infra/agentinfra/atomic.py:141`; AST `eaf888e23cc61c107ec0d54a10f219382583f810784d2b5380deae2c363a1206`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: os, stream. Outputs/bindings: (none).
Calls/effect boundaries: os.fsync, stream.fileno.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[13].body[2].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].body[2].body[4].value::Call

Source: `infra/agentinfra/atomic.py:141`; AST `29e1a002fb3ed92242523219b50a26133c0e15643b5dfd72168bc1eb4f1aed09`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os, stream. Outputs/bindings: (none).
Calls/effect boundaries: os.fsync, stream.fileno.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[13].body[2].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].body[2].body[4].value.args[0]::Call

Source: `infra/agentinfra/atomic.py:141`; AST `27f47889b85ed2bb90d146b9008836c66d42f49c92f140cae1596cf4efe4d050`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: stream. Outputs/bindings: (none).
Calls/effect boundaries: stream.fileno.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[13].body[2].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].body[3]::Expr

Source: `infra/agentinfra/atomic.py:142`; AST `0d788e274d4a8beb7c123159fa21d0619d9a45577233a5e3517e19e0e3efeead`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _call_fault, fault, path. Outputs/bindings: (none).
Calls/effect boundaries: _call_fault.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[13].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].body[3].value::Call

Source: `infra/agentinfra/atomic.py:142`; AST `7232dd9546b9ee3967bffff6e443f46ada5fb6761e7ea7a8c13fcb9d6a1274b8`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _call_fault, fault, path. Outputs/bindings: (none).
Calls/effect boundaries: _call_fault.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[13].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].body[4]::Expr

Source: `infra/agentinfra/atomic.py:143`; AST `240299edefa623600b268f1ddf7a3c687e20802a174e3bbb19ea8c1ab8988626`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _call_fault, fault, path. Outputs/bindings: (none).
Calls/effect boundaries: _call_fault.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[13].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].body[4].value::Call

Source: `infra/agentinfra/atomic.py:143`; AST `c12d84323d3ecc43c915b388cd514d1342add6f8b3ecc68bae06acee515baabf`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _call_fault, fault, path. Outputs/bindings: (none).
Calls/effect boundaries: _call_fault.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[13].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].body[5]::Expr

Source: `infra/agentinfra/atomic.py:144`; AST `ce4d64b1494bb85e2312814a4ec40a7a237cf0d8ecff4d060f913661d10765c1`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _replace_with_bounded_retry, path, tmp. Outputs/bindings: (none).
Calls/effect boundaries: _replace_with_bounded_retry.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[13].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].body[5].value::Call

Source: `infra/agentinfra/atomic.py:144`; AST `ac9cab11249d050e1c96347e83070f68e087f69487bcfb61c632f90136dca92d`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _replace_with_bounded_retry, path, tmp. Outputs/bindings: (none).
Calls/effect boundaries: _replace_with_bounded_retry.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[13].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].body[6]::Assign

Source: `infra/agentinfra/atomic.py:145`; AST `418d443f19633a6b34f4b9c00423074991ae786f3404d56a44d02b441474eaab`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: replaced.
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[13].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].body[7]::Expr

Source: `infra/agentinfra/atomic.py:146`; AST `b714f7ebe1ecf499f8babf811dd45c89d6b122faa7e6e839c3da0208fc4a8f00`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _call_fault, fault, path. Outputs/bindings: (none).
Calls/effect boundaries: _call_fault.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[13].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].body[7].value::Call

Source: `infra/agentinfra/atomic.py:146`; AST `a27d20c1b5c150a844c2d188019aff9841bdf674b87732eb62083dabd684cab7`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _call_fault, fault, path. Outputs/bindings: (none).
Calls/effect boundaries: _call_fault.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[13].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].body[8]::Expr

Source: `infra/agentinfra/atomic.py:147`; AST `46324bba1d4e7ddc3b882e7e05e3c70b8cbcafaffad51982004d667bef3dee07`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _directory_fsync, durability, path. Outputs/bindings: (none).
Calls/effect boundaries: _directory_fsync.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[13].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].body[8].value::Call

Source: `infra/agentinfra/atomic.py:147`; AST `4330ad9de36af91c2bc293298f49acd2abe036086cc5072a9422a27d700c3d6c`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _directory_fsync, durability, path. Outputs/bindings: (none).
Calls/effect boundaries: _directory_fsync.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[13].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].body[9]::Expr

Source: `infra/agentinfra/atomic.py:148`; AST `b983b93cd841b76547b2baed9f47a2ada6d42d4e71d3b92c95d74623b90f259c`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _call_fault, fault, path. Outputs/bindings: (none).
Calls/effect boundaries: _call_fault.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[13].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].body[9].value::Call

Source: `infra/agentinfra/atomic.py:148`; AST `b437eeefa9e4ccaddafe866ea664d714304c0cfd212a961d1701081cd62dc639`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _call_fault, fault, path. Outputs/bindings: (none).
Calls/effect boundaries: _call_fault.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[13].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].handlers[0]::ExceptHandler

Source: `infra/agentinfra/atomic.py:149`; AST `9dfb065f1c7f2c016adb09ec5cb8ebf3465ccd3c3aab8e4aa8b149e7a5ef83ec`.

Rust module: `infra::agentinfra::atomic`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: BaseException, fd, os, replaced, tmp. Outputs/bindings: (none).
Calls/effect boundaries: os.close, tmp.unlink.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[16].body[13].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].handlers[0].body[0]::If

Source: `infra/agentinfra/atomic.py:150`; AST `4b1ea62073bbc354a94af9033d7c85cf2e8f5843fe937b90dd03a7eea5911650`.

Rust module: `infra::agentinfra::atomic`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: fd, os. Outputs/bindings: (none).
Calls/effect boundaries: os.close.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered If evaluation at root.body[16].body[13].handlers[0].body[0]; no call, error or mutation may be omitted. Condition: fd >= 0
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].handlers[0].body[0].body[0]::Expr

Source: `infra/agentinfra/atomic.py:151`; AST `e3651c239428eac3c5a211e0813f2890d1a9be94a2f9822a2a262c2f1b0dc3de`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fd, os. Outputs/bindings: (none).
Calls/effect boundaries: os.close.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[13].handlers[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].handlers[0].body[0].body[0].value::Call

Source: `infra/agentinfra/atomic.py:151`; AST `5e53ed07e4ca5a07b4ea1627e0c8c20d53193bf9a8eca3acdc75bafd1d79af7f`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fd, os. Outputs/bindings: (none).
Calls/effect boundaries: os.close.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[13].handlers[0].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].handlers[0].body[1]::If

Source: `infra/agentinfra/atomic.py:152`; AST `da91d938a4757bee2d1aa91d8ad743c707e7a1e39ec4723e5076a3aac012e5bd`.

Rust module: `infra::agentinfra::atomic`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: replaced, tmp. Outputs/bindings: (none).
Calls/effect boundaries: tmp.unlink.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered If evaluation at root.body[16].body[13].handlers[0].body[1]; no call, error or mutation may be omitted. Condition: not replaced
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].handlers[0].body[1].body[0]::Expr

Source: `infra/agentinfra/atomic.py:153`; AST `a305b4ffa35a44867b3511e37b57e7f24d7942a5df6391b13c3724680b857b01`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: tmp. Outputs/bindings: (none).
Calls/effect boundaries: tmp.unlink.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[13].handlers[0].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].handlers[0].body[1].body[0].value::Call

Source: `infra/agentinfra/atomic.py:153`; AST `03a1c391f3345298cecf9ae128c5d1f27003cbf88d4b88d37ff033caac589ade`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tmp. Outputs/bindings: (none).
Calls/effect boundaries: tmp.unlink.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[13].handlers[0].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].handlers[0].body[2]::Raise

Source: `infra/agentinfra/atomic.py:154`; AST `ba28128c14dfbd0a9062c0dbab42ad6c52ecf0767df6b67576deb1dbbfdd038d`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Raise evaluation at root.body[16].body[13].handlers[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].finalbody[0]::If

Source: `infra/agentinfra/atomic.py:156`; AST `da91d938a4757bee2d1aa91d8ad743c707e7a1e39ec4723e5076a3aac012e5bd`.

Rust module: `infra::agentinfra::atomic`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: replaced, tmp. Outputs/bindings: (none).
Calls/effect boundaries: tmp.unlink.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered If evaluation at root.body[16].body[13].finalbody[0]; no call, error or mutation may be omitted. Condition: not replaced
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].finalbody[0].body[0]::Expr

Source: `infra/agentinfra/atomic.py:157`; AST `a305b4ffa35a44867b3511e37b57e7f24d7942a5df6391b13c3724680b857b01`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: tmp. Outputs/bindings: (none).
Calls/effect boundaries: tmp.unlink.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[13].finalbody[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_bytes::root.body[16].body[13].finalbody[0].body[0].value::Call

Source: `infra/agentinfra/atomic.py:157`; AST `03a1c391f3345298cecf9ae128c5d1f27003cbf88d4b88d37ff033caac589ade`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tmp. Outputs/bindings: (none).
Calls/effect boundaries: tmp.unlink.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[13].finalbody[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_text::root.body[17]::FunctionDef

Source: `infra/agentinfra/atomic.py:160`; AST `6a4d3ebe06edf6d72617c1dc335da6ec6e36a9ea6684a52e70e678a06aff32e4`.

Rust module: `infra::agentinfra::atomic`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, atomic_write_bytes, kwargs, path, str, text. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_bytes, text.encode.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_text::root.body[17].body[0]::Expr

Source: `infra/agentinfra/atomic.py:161`; AST `f83daeb398c91d61ab7f6344312713f24965a1928184cb325892d0a32d95f406`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_bytes, kwargs, path, text. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_bytes, text.encode.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_text::root.body[17].body[0].value::Call

Source: `infra/agentinfra/atomic.py:161`; AST `ce2f46d702bdc3b041c785475ec0014c32c9216cf2736b2e3c73f0f054698445`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_bytes, kwargs, path, text. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_bytes, text.encode.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_text::root.body[17].body[0].value.args[1]::Call

Source: `infra/agentinfra/atomic.py:161`; AST `bdbbd175b981b6e91fabbd52e252227c4146368ae5c0d182873ad91289c3786e`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: text. Outputs/bindings: (none).
Calls/effect boundaries: text.encode.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_json::root.body[18]::FunctionDef

Source: `infra/agentinfra/atomic.py:164`; AST `1c05699d5452a3b13068ac4318933665bdc37495165cbb8d3535b7a516b77351`.

Rust module: `infra::agentinfra::atomic`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, atomic_write_text, json, kwargs, obj, path. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_text, json.dumps.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[18]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_json::root.body[18].body[0]::Expr

Source: `infra/agentinfra/atomic.py:165`; AST `e53fdfdcceda993cbf700e25a532e188cdcfd67ab95ae7ea727bb02825981653`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_text, json, kwargs, obj, path. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_text, json.dumps.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_json::root.body[18].body[0].value::Call

Source: `infra/agentinfra/atomic.py:165`; AST `9cf485e226901a5b03623ece9f2ff373d1fc36f7ad74addf598fe86f79a6b897`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_text, json, kwargs, obj, path. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_text, json.dumps.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::atomic_write_json::root.body[18].body[0].value.args[1].left::Call

Source: `infra/agentinfra/atomic.py:165`; AST `30f162e1060bb20da7fd5aa792b514218135bf5dc34bf10fd2fae1977c1440f4`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, obj. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].value.args[1].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::durable_unlink::root.body[19]::FunctionDef

Source: `infra/agentinfra/atomic.py:168`; AST `8b63df1ee89da2d78557b75adea6e666ef01428a84fc0d23e85b56d73eb70912`.

Rust module: `infra::agentinfra::atomic`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileNotFoundError, Path, ValueError, _assert_confined, _directory_fsync, bool, durability, missing_ok, path, reject_symlinks, root, str. Outputs/bindings: path.
Calls/effect boundaries: Path, ValueError, _assert_confined, _directory_fsync, path.unlink.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[19]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::durable_unlink::root.body[19].body[0]::If

Source: `infra/agentinfra/atomic.py:176`; AST `b419baeb5e06375837ec2d995fd010a6d084b9d7ab22a67e98668bd9effe9e22`.

Rust module: `infra::agentinfra::atomic`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ValueError, durability. Outputs/bindings: (none).
Calls/effect boundaries: ValueError.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered If evaluation at root.body[19].body[0]; no call, error or mutation may be omitted. Condition: durability not in {'required', 'best-effort'}
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::durable_unlink::root.body[19].body[0].body[0]::Raise

Source: `infra/agentinfra/atomic.py:177`; AST `31b44842b8bb02cf12e0858f72826f431c05b7675a89500671a0d191e9903576`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ValueError. Outputs/bindings: (none).
Calls/effect boundaries: ValueError.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Raise evaluation at root.body[19].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::durable_unlink::root.body[19].body[0].body[0].exc::Call

Source: `infra/agentinfra/atomic.py:177`; AST `aea48545e7e75dcd73d2775329fe27c2c1e1f48164dbf3a698b9d7a065488ebe`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ValueError. Outputs/bindings: (none).
Calls/effect boundaries: ValueError.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::durable_unlink::root.body[19].body[1]::Assign

Source: `infra/agentinfra/atomic.py:178`; AST `a6e457796281606eb892c15254e3e12d1f482a1a1ab80964ac184f36d274d875`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, path. Outputs/bindings: path.
Calls/effect boundaries: Path.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::durable_unlink::root.body[19].body[1].value::Call

Source: `infra/agentinfra/atomic.py:178`; AST `c4b629495a6e643da3774e82f742688d4a24128b1ff8b4448236e96c64f51421`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, path. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::durable_unlink::root.body[19].body[2]::Expr

Source: `infra/agentinfra/atomic.py:179`; AST `24896f1a9a04cc21515521f380749bd6711c3c5c69defe8453ac1784034a70f4`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _assert_confined, path, reject_symlinks, root. Outputs/bindings: (none).
Calls/effect boundaries: _assert_confined.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::durable_unlink::root.body[19].body[2].value::Call

Source: `infra/agentinfra/atomic.py:179`; AST `34994b6e67c3a5c237e521e0767046445b626528802ffa2ca00a395b7b75639c`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _assert_confined, path, reject_symlinks, root. Outputs/bindings: (none).
Calls/effect boundaries: _assert_confined.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::durable_unlink::root.body[19].body[3]::Try

Source: `infra/agentinfra/atomic.py:180`; AST `5de366740ae520b0d38795ed6e73dcda79e4c3e1f6c223b62ccfabd40dd09188`.

Rust module: `infra::agentinfra::atomic`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: FileNotFoundError, missing_ok, path. Outputs/bindings: (none).
Calls/effect boundaries: path.unlink.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Try evaluation at root.body[19].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::durable_unlink::root.body[19].body[3].body[0]::Expr

Source: `infra/agentinfra/atomic.py:181`; AST `0f67381b298c0efd9d1f9e5b89a1a457af5d02f254ac1476f2c35c24aae27969`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.unlink.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::durable_unlink::root.body[19].body[3].body[0].value::Call

Source: `infra/agentinfra/atomic.py:181`; AST `d1be48384f6b878b78c26c20d263b4aac4c6efea3788dd6d0a68da3ce5902484`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.unlink.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::durable_unlink::root.body[19].body[3].handlers[0]::ExceptHandler

Source: `infra/agentinfra/atomic.py:182`; AST `87492e62e50e91066d8c3d8e914defa5dde5c5c7b36b6e639d8b07964ef4759a`.

Rust module: `infra::agentinfra::atomic`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: FileNotFoundError, missing_ok. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[19].body[3].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::durable_unlink::root.body[19].body[3].handlers[0].body[0]::If

Source: `infra/agentinfra/atomic.py:183`; AST `b33c300807012aa034e92e6edcfb22c7acf1911a5ff28a48aa42632a20da496d`.

Rust module: `infra::agentinfra::atomic`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: missing_ok. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered If evaluation at root.body[19].body[3].handlers[0].body[0]; no call, error or mutation may be omitted. Condition: not missing_ok
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::durable_unlink::root.body[19].body[3].handlers[0].body[0].body[0]::Raise

Source: `infra/agentinfra/atomic.py:184`; AST `ba28128c14dfbd0a9062c0dbab42ad6c52ecf0767df6b67576deb1dbbfdd038d`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Raise evaluation at root.body[19].body[3].handlers[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::durable_unlink::root.body[19].body[3].handlers[0].body[1]::Return

Source: `infra/agentinfra/atomic.py:185`; AST `d3ec646650be52e3f5b5700447f19313b1bab9ed1bd27c2483960d5d0bcaf584`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Return evaluation at root.body[19].body[3].handlers[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::durable_unlink::root.body[19].body[4]::Expr

Source: `infra/agentinfra/atomic.py:186`; AST `46324bba1d4e7ddc3b882e7e05e3c70b8cbcafaffad51982004d667bef3dee07`.

Rust module: `infra::agentinfra::atomic`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _directory_fsync, durability, path. Outputs/bindings: (none).
Calls/effect boundaries: _directory_fsync.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/atomic.py::module::durable_unlink::root.body[19].body[4].value::Call

Source: `infra/agentinfra/atomic.py:186`; AST `4330ad9de36af91c2bc293298f49acd2abe036086cc5072a9422a27d700c3d6c`.

Rust module: `infra::agentinfra::atomic`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _directory_fsync, durability, path. Outputs/bindings: (none).
Calls/effect boundaries: _directory_fsync.
Dependencies: __future__, governance, json, os, pathlib, security, stat, tempfile, time, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
