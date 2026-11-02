# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 383. Inventory digest: `63d9b4ce678f83477859a5a2a6594f2f075d7513ff6c173c52897d613717dab1`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/locks.py::module::root::Module

Source: `infra/agentinfra/locks.py:1`; AST `f4da9f659b8762ec1331aff4cebe1a726081b7b1a285c653bb1567f8628bafd6`.

Rust module: `infra::agentinfra::locks`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: Exception, FileExistsError, FileNotFoundError, IndexError, LockError, OSError, PROCESS_QUERY_LIMITED_INFORMATION, Path, PermissionError, ProcessLookupError, RuntimeError, ValueError, _now, _pid_alive, _process_identity, alive, any, bool, checks, creation, ctypes, current, data, dataclass, datetime, deadline, delay, dict, exc, exit_time, expected, expected_task_id, fd, field, float, handle, identity, info, int, isinstance, json, kernel, key, last_contention, last_error, lease_id, max, min, nonce, os, owner_nonce, parent_id, payload, pid, raw, reason, required, role, self, set, socket, stat_path, str, stream, tail, task_id, time, timeout, timezone, user, uuid, value. Outputs/bindings: PROCESS_QUERY_LIMITED_INFORMATION, _owner, alive, checks, creation, current, data, deadline, delay, exit_time, expected, fd, handle, info, kernel, key, last_contention, last_error, path, payload, purpose, raw, required, stat_path, stream, tail, user, value.
Calls/effect boundaries: (json.dumps(payload, sort_keys=True) + '\n').encode, (json.dumps({key: value for key, value in payload.items() if key not in {'exists', 'age_seconds'}}, sort_keys=True) + '\n').encode, LockError, Path, ValueError, _now, _pid_alive, _process_identity, any, checks.items, ctypes.byref, ctypes.windll.kernel32.CloseHandle, ctypes.windll.kernel32.GetLastError, ctypes.windll.kernel32.GetProcessTimes, ctypes.windll.kernel32.OpenProcess, ctypes.windll.kernel32.SetLastError, ctypes.wintypes.FILETIME, data.get, datetime.now, datetime.now(timezone.utc).isoformat, dict, field, float, info.get, int, isinstance, json.dump, json.dumps, json.loads, max, min, os.fdopen, os.fsync, os.getpid, os.kill, os.open, payload.get, payload.items, reason.strip, self._owner.get, self._try_create, self.inspect, self.path.parent.mkdir, self.path.read_text, self.path.stat, self.path.unlink, set, socket.gethostname, stat_path.read_text, stat_path.read_text(encoding='utf-8').rsplit, stat_path.read_text(encoding='utf-8').rsplit(')', 1)[1].split, str, stream.fileno, stream.flush, stream.write, time.monotonic, time.sleep, time.time, uuid.uuid4.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::root.body[0]::ImportFrom

Source: `infra/agentinfra/locks.py:1`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::root.body[1]::ImportFrom

Source: `infra/agentinfra/locks.py:3`; AST `5a46818000a4ba65186172bb0cb9a4b5dbc848a8a97f892692ffc6df7d8c6953`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::root.body[2]::ImportFrom

Source: `infra/agentinfra/locks.py:4`; AST `85598e37ba96d6e396880fbaf8f1a487d6502e6df91ce2ca25c05c876437624e`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::root.body[3]::Import

Source: `infra/agentinfra/locks.py:5`; AST `669c8db7bfb9b4e64a7aa5f9239cbd229a5c460f228936e83d225f5ab2176b82`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::root.body[4]::Import

Source: `infra/agentinfra/locks.py:6`; AST `af79723a2fd651a13b42afa080047e330560d43086896ca3ca7155f31b096dc9`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Import evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::root.body[5]::Import

Source: `infra/agentinfra/locks.py:7`; AST `211ee42757705c7e350e70e36b762987a737f5e9c268f2a343e2dbfcb8fbea75`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Import evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::root.body[6]::Import

Source: `infra/agentinfra/locks.py:8`; AST `ac3a74d6dd975a8e8fe4b7f85fce794793a9355595b850e3926964913948d386`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Import evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::root.body[7]::Import

Source: `infra/agentinfra/locks.py:9`; AST `9df267ed6eef4f61eaaffaebdf9ac9fe93bcf6d1aab9647b1fd045430624c91e`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Import evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::root.body[8]::Import

Source: `infra/agentinfra/locks.py:10`; AST `ff05bad0fd9a7212d3cd85fd2726055168be21bc8f6e0d93b29965794b0675d4`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Import evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::root.body[9]::Import

Source: `infra/agentinfra/locks.py:11`; AST `db14cae1a81ee06a1930fa9f46771b454957916d2bbbc048661adf0613fd70de`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Import evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::root.body[10]::ImportFrom

Source: `infra/agentinfra/locks.py:12`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::root.body[11]::ImportFrom

Source: `infra/agentinfra/locks.py:14`; AST `1b8b71be5203ae66cf696ad7ae023750f023f11fd20fe2501f8e1d56817881e3`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LockError::root.body[12]::ClassDef

Source: `infra/agentinfra/locks.py:17`; AST `c6866caef6728c275612c9dbe73edbe288c654cde98c2668b6ea9120ed685c54`.

Rust module: `infra::agentinfra::locks`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: RuntimeError. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered ClassDef evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LockError::root.body[12].body[0]::Pass

Source: `infra/agentinfra/locks.py:18`; AST `f8e211bd496e62be79e8542ba1d0a7cebbf2a6143ae07b375ae14ce00a91b69c`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Pass evaluation at root.body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_now::root.body[13]::FunctionDef

Source: `infra/agentinfra/locks.py:21`; AST `2002d96b29ea73dbaa36fb15a8de921b2b207655e9f6844445bc2640cc932d35`.

Rust module: `infra::agentinfra::locks`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: datetime, str, timezone. Outputs/bindings: (none).
Calls/effect boundaries: datetime.now, datetime.now(timezone.utc).isoformat.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_now::root.body[13].body[0]::Return

Source: `infra/agentinfra/locks.py:22`; AST `04d97f7b2f56105a8dee137484e2a607e200f29f786ca622301e010f18cb21c8`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: datetime, timezone. Outputs/bindings: (none).
Calls/effect boundaries: datetime.now, datetime.now(timezone.utc).isoformat.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Return evaluation at root.body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_now::root.body[13].body[0].value::Call

Source: `infra/agentinfra/locks.py:22`; AST `1b110a252c57d72f572683a982afb6160b9f4ceeec701cae738dc9a58366722d`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: datetime, timezone. Outputs/bindings: (none).
Calls/effect boundaries: datetime.now, datetime.now(timezone.utc).isoformat.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_now::root.body[13].body[0].value.func.value::Call

Source: `infra/agentinfra/locks.py:22`; AST `7d005ec5c408397d72b2a5196d97d2fa96db0d64d31cc38e5bd68f36bf7badb9`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: datetime, timezone. Outputs/bindings: (none).
Calls/effect boundaries: datetime.now.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14]::FunctionDef

Source: `infra/agentinfra/locks.py:25`; AST `17424fbe9048260eaa982920dd238a2fd0e66ccbb74d55073403b66264b83773`.

Rust module: `infra::agentinfra::locks`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: IndexError, OSError, PROCESS_QUERY_LIMITED_INFORMATION, Path, creation, ctypes, exit_time, handle, int, kernel, os, pid, stat_path, str, tail, user, value. Outputs/bindings: PROCESS_QUERY_LIMITED_INFORMATION, creation, exit_time, handle, kernel, stat_path, tail, user, value.
Calls/effect boundaries: Path, ctypes.byref, ctypes.windll.kernel32.CloseHandle, ctypes.windll.kernel32.GetProcessTimes, ctypes.windll.kernel32.OpenProcess, ctypes.wintypes.FILETIME, stat_path.read_text, stat_path.read_text(encoding='utf-8').rsplit, stat_path.read_text(encoding='utf-8').rsplit(')', 1)[1].split.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[0]::Expr

Source: `infra/agentinfra/locks.py:26`; AST `55e0ae4ebeb9b6cc37196bad650f22f6e4893736c379977bac13a35f5ded429a`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[1]::If

Source: `infra/agentinfra/locks.py:27`; AST `96a8ba321e4afe0cd70179959f3835831579a253bf1595a83abf5171415beaf2`.

Rust module: `infra::agentinfra::locks`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: pid. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered If evaluation at root.body[14].body[1]; no call, error or mutation may be omitted. Condition: pid <= 0
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[1].body[0]::Return

Source: `infra/agentinfra/locks.py:28`; AST `353401809590fce03527be76d16055befec3bf00b4443d2e1a26c5300e3da6a4`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Return evaluation at root.body[14].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[2]::If

Source: `infra/agentinfra/locks.py:29`; AST `16d7d30959b14fdfb7bcf7bb12b6fc054f2f131a6800a2ddb5cd468478940c4c`.

Rust module: `infra::agentinfra::locks`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: PROCESS_QUERY_LIMITED_INFORMATION, creation, ctypes, exit_time, handle, kernel, os, pid, user, value. Outputs/bindings: PROCESS_QUERY_LIMITED_INFORMATION, creation, exit_time, handle, kernel, user, value.
Calls/effect boundaries: ctypes.byref, ctypes.windll.kernel32.CloseHandle, ctypes.windll.kernel32.GetProcessTimes, ctypes.windll.kernel32.OpenProcess, ctypes.wintypes.FILETIME.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered If evaluation at root.body[14].body[2]; no call, error or mutation may be omitted. Condition: os.name == 'nt'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[2].body[0]::Assign

Source: `infra/agentinfra/locks.py:30`; AST `3371f8572b714685be1fcb884e0df458e8fb5616c85df32944c376b30a605eb6`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: PROCESS_QUERY_LIMITED_INFORMATION.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[2].body[1]::Assign

Source: `infra/agentinfra/locks.py:31`; AST `7f9cd3e7357e568a6406f1e4ea74fd1c94a32a622891cdbced5c87076daadf62`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: PROCESS_QUERY_LIMITED_INFORMATION, ctypes, pid. Outputs/bindings: handle.
Calls/effect boundaries: ctypes.windll.kernel32.OpenProcess.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[2].body[1].value::Call

Source: `infra/agentinfra/locks.py:31`; AST `359e5c7f7b7999f09fd70b2dc5cb1900fad2c9f8acca88d4a55f4693967c2b16`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: PROCESS_QUERY_LIMITED_INFORMATION, ctypes, pid. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.windll.kernel32.OpenProcess.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[2].body[2]::If

Source: `infra/agentinfra/locks.py:32`; AST `b44aaea75b1bd2126f4fc8436f4f2ce5ecdf83afb0eb8112371a12209898a3db`.

Rust module: `infra::agentinfra::locks`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: handle. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered If evaluation at root.body[14].body[2].body[2]; no call, error or mutation may be omitted. Condition: not handle
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[2].body[2].body[0]::Return

Source: `infra/agentinfra/locks.py:33`; AST `353401809590fce03527be76d16055befec3bf00b4443d2e1a26c5300e3da6a4`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Return evaluation at root.body[14].body[2].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[2].body[3]::Try

Source: `infra/agentinfra/locks.py:34`; AST `d7f929f4545a13662f2f8452f766b4267d1b21706087f7e11265dd692f16385f`.

Rust module: `infra::agentinfra::locks`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: creation, ctypes, exit_time, handle, kernel, user, value. Outputs/bindings: creation, exit_time, kernel, user, value.
Calls/effect boundaries: ctypes.byref, ctypes.windll.kernel32.CloseHandle, ctypes.windll.kernel32.GetProcessTimes, ctypes.wintypes.FILETIME.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Try evaluation at root.body[14].body[2].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[2].body[3].body[0]::Assign

Source: `infra/agentinfra/locks.py:35`; AST `18b2f8216bf9f257e73b4fdf69b37001aa4e52487f9dfdc8ddb3e13da169b225`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ctypes. Outputs/bindings: creation.
Calls/effect boundaries: ctypes.wintypes.FILETIME.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[2].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[2].body[3].body[0].value::Call

Source: `infra/agentinfra/locks.py:35`; AST `a64d8972272f70c6bc935731712cbb5d6be7b4c749d839b2b569fbf0bf130cf1`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ctypes. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.wintypes.FILETIME.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[2].body[3].body[1]::Assign

Source: `infra/agentinfra/locks.py:36`; AST `5566095c16bb36b16d6898b1668999f5de4e43daeeb587b415a60f6f20cdf91c`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ctypes. Outputs/bindings: exit_time.
Calls/effect boundaries: ctypes.wintypes.FILETIME.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[2].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[2].body[3].body[1].value::Call

Source: `infra/agentinfra/locks.py:36`; AST `a64d8972272f70c6bc935731712cbb5d6be7b4c749d839b2b569fbf0bf130cf1`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ctypes. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.wintypes.FILETIME.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[2].body[3].body[2]::Assign

Source: `infra/agentinfra/locks.py:37`; AST `de06f3b1abed31e9a2b1dc796b0ddf4b80b45f3a5d84c984244649087ac7a990`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ctypes. Outputs/bindings: kernel.
Calls/effect boundaries: ctypes.wintypes.FILETIME.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[2].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[2].body[3].body[2].value::Call

Source: `infra/agentinfra/locks.py:37`; AST `a64d8972272f70c6bc935731712cbb5d6be7b4c749d839b2b569fbf0bf130cf1`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ctypes. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.wintypes.FILETIME.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[2].body[3].body[3]::Assign

Source: `infra/agentinfra/locks.py:38`; AST `4bc86f638f13d15bf1e47ddb4cac796e7197b082a6aa66eee8319cf38063b1ec`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ctypes. Outputs/bindings: user.
Calls/effect boundaries: ctypes.wintypes.FILETIME.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[2].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[2].body[3].body[3].value::Call

Source: `infra/agentinfra/locks.py:38`; AST `a64d8972272f70c6bc935731712cbb5d6be7b4c749d839b2b569fbf0bf130cf1`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ctypes. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.wintypes.FILETIME.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].body[3].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[2].body[3].body[4]::If

Source: `infra/agentinfra/locks.py:39`; AST `c11badbd8d38b4f68ea672db4d55641852ead91a9fe063bfa2468b84f9a507db`.

Rust module: `infra::agentinfra::locks`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: creation, ctypes, exit_time, handle, kernel, user. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.byref, ctypes.windll.kernel32.GetProcessTimes.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered If evaluation at root.body[14].body[2].body[3].body[4]; no call, error or mutation may be omitted. Condition: not ctypes.windll.kernel32.GetProcessTimes(handle, ctypes.byref(creation), ctypes.byref(exit_time), ctypes.byref(kernel), ctypes.byref(user))
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[2].body[3].body[4].test.operand::Call

Source: `infra/agentinfra/locks.py:39`; AST `617f90fcdbae2224bdc4fca00341f1eae4a4a8486b5f28e5d2ca87df7a82f9eb`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: creation, ctypes, exit_time, handle, kernel, user. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.byref, ctypes.windll.kernel32.GetProcessTimes.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].body[3].body[4].test.operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[2].body[3].body[4].test.operand.args[1]::Call

Source: `infra/agentinfra/locks.py:40`; AST `f058abf8c1f3a5174e6cc592f8ab280868e074bef860b4355c6acdf06cbb4d1b`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: creation, ctypes. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.byref.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].body[3].body[4].test.operand.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[2].body[3].body[4].test.operand.args[2]::Call

Source: `infra/agentinfra/locks.py:40`; AST `89ae556e81ce6e7fc2c867a2d14c1d838dfeb6a802ebbe99a3b0f15524aec2f1`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ctypes, exit_time. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.byref.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].body[3].body[4].test.operand.args[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[2].body[3].body[4].test.operand.args[3]::Call

Source: `infra/agentinfra/locks.py:40`; AST `bac73cd899e3a3a935a1cdb758f3d3f14abe703c851e14f3d05dc62562436be8`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ctypes, kernel. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.byref.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].body[3].body[4].test.operand.args[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[2].body[3].body[4].test.operand.args[4]::Call

Source: `infra/agentinfra/locks.py:40`; AST `d48196b95eafc41adcb57b10a7745acd3ca5faf9dbf8b1d88ee797705c113020`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ctypes, user. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.byref.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].body[3].body[4].test.operand.args[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[2].body[3].body[4].body[0]::Return

Source: `infra/agentinfra/locks.py:42`; AST `353401809590fce03527be76d16055befec3bf00b4443d2e1a26c5300e3da6a4`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Return evaluation at root.body[14].body[2].body[3].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[2].body[3].body[5]::Assign

Source: `infra/agentinfra/locks.py:43`; AST `c57789b3b8b43266140ca615141d044c0b0cb73a481d3d3686c73fd808ae4188`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: creation. Outputs/bindings: value.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[2].body[3].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[2].body[3].body[6]::Return

Source: `infra/agentinfra/locks.py:44`; AST `bb7896deb8ee2be7a63fa13a0253fa3f5f4a9b7e7bcbff8bf2894676cd903347`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: value. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Return evaluation at root.body[14].body[2].body[3].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[2].body[3].finalbody[0]::Expr

Source: `infra/agentinfra/locks.py:46`; AST `e37f91a3d5a8d641de97c75718ce49503d95baab8e70182946f706757d03c593`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ctypes, handle. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.windll.kernel32.CloseHandle.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[2].body[3].finalbody[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[2].body[3].finalbody[0].value::Call

Source: `infra/agentinfra/locks.py:46`; AST `1bf2740d0e9303b5e6c79003fced2a8c3f8a975effee10eab4375456932d9e76`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ctypes, handle. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.windll.kernel32.CloseHandle.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].body[3].finalbody[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[3]::Assign

Source: `infra/agentinfra/locks.py:47`; AST `a56f93f854d7e7ae40cffef6feb723b773d0d50c4b3c1eaa79fec9a551e9013f`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, pid. Outputs/bindings: stat_path.
Calls/effect boundaries: Path.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[3].value::Call

Source: `infra/agentinfra/locks.py:47`; AST `279a33e7e99f80dcb74a62eabec3a0c2d3b25f659ae86c3b6573fb4a6fa49c55`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, pid. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[14].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[4]::Try

Source: `infra/agentinfra/locks.py:48`; AST `7f8442db30b46dea5539e5065559c2768c4951879f5dcaf37b76aeb7cfc93774`.

Rust module: `infra::agentinfra::locks`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: IndexError, OSError, stat_path, tail. Outputs/bindings: tail.
Calls/effect boundaries: stat_path.read_text, stat_path.read_text(encoding='utf-8').rsplit, stat_path.read_text(encoding='utf-8').rsplit(')', 1)[1].split.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Try evaluation at root.body[14].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[4].body[0]::Assign

Source: `infra/agentinfra/locks.py:50`; AST `e8030d78d15b6a41f1df3825eecabd3c096920fd850fa1b8f5fd1185f3ab8f79`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: stat_path. Outputs/bindings: tail.
Calls/effect boundaries: stat_path.read_text, stat_path.read_text(encoding='utf-8').rsplit, stat_path.read_text(encoding='utf-8').rsplit(')', 1)[1].split.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[4].body[0].value::Call

Source: `infra/agentinfra/locks.py:50`; AST `67b447906c6581f9428316e52faf38e549c697683713f6bd8e0e5ee2406fe8e0`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: stat_path. Outputs/bindings: (none).
Calls/effect boundaries: stat_path.read_text, stat_path.read_text(encoding='utf-8').rsplit, stat_path.read_text(encoding='utf-8').rsplit(')', 1)[1].split.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[14].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[4].body[0].value.func.value.value::Call

Source: `infra/agentinfra/locks.py:50`; AST `1a3530c32625b9b15f29975ec17d0746cd1e1a63dc2a89cda3cf3e9240760718`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: stat_path. Outputs/bindings: (none).
Calls/effect boundaries: stat_path.read_text, stat_path.read_text(encoding='utf-8').rsplit.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[14].body[4].body[0].value.func.value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[4].body[0].value.func.value.value.func.value::Call

Source: `infra/agentinfra/locks.py:50`; AST `8a36422eb25d6f5c2feae1ada40e0a239259586c11ab277dc83c1b62071f5781`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: stat_path. Outputs/bindings: (none).
Calls/effect boundaries: stat_path.read_text.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[14].body[4].body[0].value.func.value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[4].body[1]::Return

Source: `infra/agentinfra/locks.py:51`; AST `40b655d6ba69f9a03e1f7cf4b8654d0a01235ff54edbcb8d84af5628ceb36e0b`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: tail. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Return evaluation at root.body[14].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[4].handlers[0]::ExceptHandler

Source: `infra/agentinfra/locks.py:52`; AST `e23b18bcf9a70233e684ad1bffbacfcff58a2fcf2714ac57e26d3a781cd95186`.

Rust module: `infra::agentinfra::locks`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: IndexError, OSError. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[14].body[4].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_process_identity::root.body[14].body[4].handlers[0].body[0]::Return

Source: `infra/agentinfra/locks.py:53`; AST `353401809590fce03527be76d16055befec3bf00b4443d2e1a26c5300e3da6a4`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Return evaluation at root.body[14].body[4].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_pid_alive::root.body[15]::FunctionDef

Source: `infra/agentinfra/locks.py:56`; AST `af29ebae650823cbbc9cddf638d434d7f9f608d2cfbd8dc722a178d9348fdfab`.

Rust module: `infra::agentinfra::locks`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: PROCESS_QUERY_LIMITED_INFORMATION, PermissionError, ProcessLookupError, _process_identity, alive, bool, ctypes, current, handle, identity, int, os, pid, str. Outputs/bindings: PROCESS_QUERY_LIMITED_INFORMATION, alive, current, handle.
Calls/effect boundaries: _process_identity, ctypes.windll.kernel32.CloseHandle, ctypes.windll.kernel32.GetLastError, ctypes.windll.kernel32.OpenProcess, ctypes.windll.kernel32.SetLastError, os.kill.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_pid_alive::root.body[15].body[0]::If

Source: `infra/agentinfra/locks.py:57`; AST `a716ffc5cf07404b4c41e046ef07579ab450bc486f7927ca29c03136f1b8be55`.

Rust module: `infra::agentinfra::locks`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: pid. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered If evaluation at root.body[15].body[0]; no call, error or mutation may be omitted. Condition: pid <= 0
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_pid_alive::root.body[15].body[0].body[0]::Return

Source: `infra/agentinfra/locks.py:58`; AST `dd863ea504e8543d2fb185a820aa7e2cf2d0ceddec9c835185a3510fc2ab463d`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Return evaluation at root.body[15].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_pid_alive::root.body[15].body[1]::If

Source: `infra/agentinfra/locks.py:59`; AST `dc58d522d22e606116840cb758c94e0c7df954af2188bae84cd7bd308f392740`.

Rust module: `infra::agentinfra::locks`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: PROCESS_QUERY_LIMITED_INFORMATION, PermissionError, ProcessLookupError, ctypes, handle, os, pid. Outputs/bindings: PROCESS_QUERY_LIMITED_INFORMATION, alive, handle.
Calls/effect boundaries: ctypes.windll.kernel32.CloseHandle, ctypes.windll.kernel32.GetLastError, ctypes.windll.kernel32.OpenProcess, ctypes.windll.kernel32.SetLastError, os.kill.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered If evaluation at root.body[15].body[1]; no call, error or mutation may be omitted. Condition: os.name == 'nt'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_pid_alive::root.body[15].body[1].body[0]::Assign

Source: `infra/agentinfra/locks.py:60`; AST `3371f8572b714685be1fcb884e0df458e8fb5616c85df32944c376b30a605eb6`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: PROCESS_QUERY_LIMITED_INFORMATION.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_pid_alive::root.body[15].body[1].body[1]::Expr

Source: `infra/agentinfra/locks.py:61`; AST `732bce46c0296dacc953a58b0ed6e6485e9e51f7c73049ca51f6fac4a1077df6`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ctypes. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.windll.kernel32.SetLastError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_pid_alive::root.body[15].body[1].body[1].value::Call

Source: `infra/agentinfra/locks.py:61`; AST `cd7f0212dc051ebb8d5b295f01f9c70dcd525f3eba7da479044af1c74b2e853d`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ctypes. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.windll.kernel32.SetLastError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_pid_alive::root.body[15].body[1].body[2]::Assign

Source: `infra/agentinfra/locks.py:62`; AST `7f9cd3e7357e568a6406f1e4ea74fd1c94a32a622891cdbced5c87076daadf62`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: PROCESS_QUERY_LIMITED_INFORMATION, ctypes, pid. Outputs/bindings: handle.
Calls/effect boundaries: ctypes.windll.kernel32.OpenProcess.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_pid_alive::root.body[15].body[1].body[2].value::Call

Source: `infra/agentinfra/locks.py:62`; AST `359e5c7f7b7999f09fd70b2dc5cb1900fad2c9f8acca88d4a55f4693967c2b16`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: PROCESS_QUERY_LIMITED_INFORMATION, ctypes, pid. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.windll.kernel32.OpenProcess.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_pid_alive::root.body[15].body[1].body[3]::If

Source: `infra/agentinfra/locks.py:63`; AST `ac0e854894cd9844e87eacf2da95a47daa1a8086e61f17800371b26fc02c1316`.

Rust module: `infra::agentinfra::locks`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ctypes, handle. Outputs/bindings: alive.
Calls/effect boundaries: ctypes.windll.kernel32.CloseHandle, ctypes.windll.kernel32.GetLastError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered If evaluation at root.body[15].body[1].body[3]; no call, error or mutation may be omitted. Condition: handle
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_pid_alive::root.body[15].body[1].body[3].body[0]::Expr

Source: `infra/agentinfra/locks.py:64`; AST `e37f91a3d5a8d641de97c75718ce49503d95baab8e70182946f706757d03c593`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ctypes, handle. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.windll.kernel32.CloseHandle.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[1].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_pid_alive::root.body[15].body[1].body[3].body[0].value::Call

Source: `infra/agentinfra/locks.py:64`; AST `1bf2740d0e9303b5e6c79003fced2a8c3f8a975effee10eab4375456932d9e76`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ctypes, handle. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.windll.kernel32.CloseHandle.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_pid_alive::root.body[15].body[1].body[3].body[1]::Assign

Source: `infra/agentinfra/locks.py:65`; AST `d1f216023f0742efdaa6a96c54c9f676135c6a3900d6d39df1d6bb4cc35eb699`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: alive.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[1].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_pid_alive::root.body[15].body[1].body[3].orelse[0]::Assign

Source: `infra/agentinfra/locks.py:67`; AST `83ae7343915fa9e17db4d4470aea16aff727b1e785a780f54da8161a9b58f5aa`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ctypes. Outputs/bindings: alive.
Calls/effect boundaries: ctypes.windll.kernel32.GetLastError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[1].body[3].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_pid_alive::root.body[15].body[1].body[3].orelse[0].value.left::Call

Source: `infra/agentinfra/locks.py:67`; AST `aae5ed1516da6ab1c21edf2a2b4500e0701bebef60a35e9604a240607ab819e6`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ctypes. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.windll.kernel32.GetLastError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].body[3].orelse[0].value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_pid_alive::root.body[15].body[1].orelse[0]::Try

Source: `infra/agentinfra/locks.py:69`; AST `3f0d205b08f28fdb08effde8cf648efe3a15fc72a7dafb29f6abb33a96659f67`.

Rust module: `infra::agentinfra::locks`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: PermissionError, ProcessLookupError, os, pid. Outputs/bindings: alive.
Calls/effect boundaries: os.kill.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Try evaluation at root.body[15].body[1].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_pid_alive::root.body[15].body[1].orelse[0].body[0]::Expr

Source: `infra/agentinfra/locks.py:70`; AST `8186080ce4d13e190a0d894984cfeea49d492478b034f3378dbc19c28e514ded`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: os, pid. Outputs/bindings: (none).
Calls/effect boundaries: os.kill.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[1].orelse[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_pid_alive::root.body[15].body[1].orelse[0].body[0].value::Call

Source: `infra/agentinfra/locks.py:70`; AST `905cf14b05212f6414eb5fc28135b3d6c4c082a2485f56f3c2892cf256373757`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os, pid. Outputs/bindings: (none).
Calls/effect boundaries: os.kill.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].orelse[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_pid_alive::root.body[15].body[1].orelse[0].body[1]::Assign

Source: `infra/agentinfra/locks.py:71`; AST `d1f216023f0742efdaa6a96c54c9f676135c6a3900d6d39df1d6bb4cc35eb699`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: alive.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[1].orelse[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_pid_alive::root.body[15].body[1].orelse[0].handlers[0]::ExceptHandler

Source: `infra/agentinfra/locks.py:72`; AST `b3e3a9fa38b30a8487fe09fa6e64bd37948da772925c49a81b949cf577b59518`.

Rust module: `infra::agentinfra::locks`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: ProcessLookupError. Outputs/bindings: alive.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[15].body[1].orelse[0].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_pid_alive::root.body[15].body[1].orelse[0].handlers[0].body[0]::Assign

Source: `infra/agentinfra/locks.py:73`; AST `d37913d9ad7612e26c659f7dbaefe431038353010d2e238580f0706d645a8f6c`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: alive.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[1].orelse[0].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_pid_alive::root.body[15].body[1].orelse[0].handlers[1]::ExceptHandler

Source: `infra/agentinfra/locks.py:74`; AST `8916397403f74a0d610f490c666d5967ec126b79fecc736c59333d68effd072a`.

Rust module: `infra::agentinfra::locks`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: PermissionError. Outputs/bindings: alive.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[15].body[1].orelse[0].handlers[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_pid_alive::root.body[15].body[1].orelse[0].handlers[1].body[0]::Assign

Source: `infra/agentinfra/locks.py:75`; AST `d1f216023f0742efdaa6a96c54c9f676135c6a3900d6d39df1d6bb4cc35eb699`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: alive.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[1].orelse[0].handlers[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_pid_alive::root.body[15].body[2]::If

Source: `infra/agentinfra/locks.py:76`; AST `31b1d647121ef982e70f4b175e27a61ca8348d76538dd3f47873cc6e03f24fe4`.

Rust module: `infra::agentinfra::locks`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: _process_identity, alive, current, identity, pid. Outputs/bindings: current.
Calls/effect boundaries: _process_identity.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered If evaluation at root.body[15].body[2]; no call, error or mutation may be omitted. Condition: alive and identity is not None
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_pid_alive::root.body[15].body[2].body[0]::Assign

Source: `infra/agentinfra/locks.py:77`; AST `efbf435e201ea28c516bf77fca5ecaa9ed467a5196ab1bc5aa766b29226a0593`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _process_identity, pid. Outputs/bindings: current.
Calls/effect boundaries: _process_identity.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_pid_alive::root.body[15].body[2].body[0].value::Call

Source: `infra/agentinfra/locks.py:77`; AST `97ab2fa3d8871bfad69f9576517a3740e9cb2b5f09b34899b3b395aa0a4b4478`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _process_identity, pid. Outputs/bindings: (none).
Calls/effect boundaries: _process_identity.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[15].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_pid_alive::root.body[15].body[2].body[1]::Return

Source: `infra/agentinfra/locks.py:78`; AST `39a985aba8baa27ddfac71a6ac840b5e95a13425ee7ce6781e3bbf0938493c4d`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current, identity. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Return evaluation at root.body[15].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::_pid_alive::root.body[15].body[3]::Return

Source: `infra/agentinfra/locks.py:79`; AST `0588df2e1c64cb274c19dfe208ef7b3e79ef710f1c2af26d09327c02859f7841`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: alive. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Return evaluation at root.body[15].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::root.body[16]::ClassDef

Source: `infra/agentinfra/locks.py:83`; AST `fb0f3fb219d2348a76b8f179a3798dc0b06333ca4c7d68d1fd346ee4e4c5e56f`.

Rust module: `infra::agentinfra::locks`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: Exception, FileExistsError, FileNotFoundError, LockError, OSError, Path, PermissionError, ValueError, _now, _pid_alive, _process_identity, data, dataclass, deadline, delay, dict, exc, expected, fd, field, float, info, int, isinstance, json, last_contention, last_error, max, min, nonce, os, payload, self, socket, str, stream, time, timeout, uuid. Outputs/bindings: _owner, data, deadline, delay, expected, fd, info, last_contention, last_error, path, payload, purpose, stream.
Calls/effect boundaries: LockError, ValueError, _now, _pid_alive, _process_identity, data.get, dict, field, float, info.get, int, isinstance, json.dump, json.loads, max, min, os.fdopen, os.fsync, os.getpid, os.open, self._owner.get, self._try_create, self.inspect, self.path.parent.mkdir, self.path.read_text, self.path.stat, self.path.unlink, socket.gethostname, str, stream.fileno, stream.flush, stream.write, time.monotonic, time.sleep, time.time, uuid.uuid4.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered ClassDef evaluation at root.body[16]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::root.body[16].body[0]::Expr

Source: `infra/agentinfra/locks.py:84`; AST `0d9083eddf725692f7c3e32acd20e410461b26eb45da7e5cff01ea0ff2763cad`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::root.body[16].body[1]::AnnAssign

Source: `infra/agentinfra/locks.py:86`; AST `d3875b770eedb512c54cfa40a07917c19082ab47a2d6364a83103c2dc978d73b`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[16].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::root.body[16].body[2]::AnnAssign

Source: `infra/agentinfra/locks.py:87`; AST `22868c1e1ff59a4fe25d940b976b1ddf29bba3fbf10c4924a2e7219235c8117b`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: str. Outputs/bindings: purpose.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[16].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::root.body[16].body[3]::AnnAssign

Source: `infra/agentinfra/locks.py:88`; AST `19674646bd1a6bea582eb9bfc741548814923ee5d37e74943d804dc272624cd6`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, field. Outputs/bindings: _owner.
Calls/effect boundaries: field.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[16].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::root.body[16].body[3].value::Call

Source: `infra/agentinfra/locks.py:88`; AST `141959d2885db00c0d217c183acd3a24885a08161988352f9d5a4e1934cc5af3`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: field. Outputs/bindings: (none).
Calls/effect boundaries: field.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::_try_create::root.body[16].body[4]::FunctionDef

Source: `infra/agentinfra/locks.py:90`; AST `b3d04ceecb93df8b5adac25f92966c3bca6da0ab59a2097836309504c6ba7a75`.

Rust module: `infra::agentinfra::locks`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: dict, fd, json, os, payload, self, stream. Outputs/bindings: fd, stream.
Calls/effect boundaries: json.dump, os.fdopen, os.fsync, os.open, stream.fileno, stream.flush, stream.write.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::_try_create::root.body[16].body[4].body[0]::Assign

Source: `infra/agentinfra/locks.py:91`; AST `623a1cb9352b380120722b40d66cf9efc077cc8ac0fa5738dd0a7c78221dc34e`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: os, self. Outputs/bindings: fd.
Calls/effect boundaries: os.open.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::_try_create::root.body[16].body[4].body[0].value::Call

Source: `infra/agentinfra/locks.py:91`; AST `e002517ffd4d512df5d8859d522f0a3cfac8004a51c8e5e4bbe1fcdc6b4ab81d`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os, self. Outputs/bindings: (none).
Calls/effect boundaries: os.open.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::_try_create::root.body[16].body[4].body[1]::With

Source: `infra/agentinfra/locks.py:92`; AST `7015c32e5d85f91cf445ef4368aaff986633235fc5cd654a6bdfd581d2365d76`.

Rust module: `infra::agentinfra::locks`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: fd, json, os, payload, stream. Outputs/bindings: stream.
Calls/effect boundaries: json.dump, os.fdopen, os.fsync, stream.fileno, stream.flush, stream.write.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered With evaluation at root.body[16].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::_try_create::root.body[16].body[4].body[1].items[0].context_expr::Call

Source: `infra/agentinfra/locks.py:92`; AST `dd27ea5a73b3841c5b03e3a04eed4882b93cdd071c8ce9d209290b98c1239a29`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fd, os. Outputs/bindings: (none).
Calls/effect boundaries: os.fdopen.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[4].body[1].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::_try_create::root.body[16].body[4].body[1].body[0]::Expr

Source: `infra/agentinfra/locks.py:93`; AST `de11f8fa05523b327139ea35c06d0750719a0c36820d0f9cb009051c4764b8a2`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, payload, stream. Outputs/bindings: (none).
Calls/effect boundaries: json.dump.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[4].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::_try_create::root.body[16].body[4].body[1].body[0].value::Call

Source: `infra/agentinfra/locks.py:93`; AST `3d0ec13bd1d82d17a70973d78974616097918242ca33eee7947019a9ed300fae`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, payload, stream. Outputs/bindings: (none).
Calls/effect boundaries: json.dump.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[4].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::_try_create::root.body[16].body[4].body[1].body[1]::Expr

Source: `infra/agentinfra/locks.py:94`; AST `37e37f2cf1f8b084ed9ca8f7e61f0a66e5b349691a69159785879ef6ce29c2f9`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: stream. Outputs/bindings: (none).
Calls/effect boundaries: stream.write.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[4].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::_try_create::root.body[16].body[4].body[1].body[1].value::Call

Source: `infra/agentinfra/locks.py:94`; AST `3a23591d76cdf19c95d26ff8395a86806987319e69cccf3f31115b4e5f5d5180`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: stream. Outputs/bindings: (none).
Calls/effect boundaries: stream.write.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[4].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::_try_create::root.body[16].body[4].body[1].body[2]::Expr

Source: `infra/agentinfra/locks.py:95`; AST `30712519db7cf7c545c522e94f0bbceb17159cd53838ebe3acb16ebc578916dd`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: stream. Outputs/bindings: (none).
Calls/effect boundaries: stream.flush.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[4].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::_try_create::root.body[16].body[4].body[1].body[2].value::Call

Source: `infra/agentinfra/locks.py:95`; AST `dc9183626915285572f9f5f11a4c11f0386db10bee4db107d63c2469769b0631`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: stream. Outputs/bindings: (none).
Calls/effect boundaries: stream.flush.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[4].body[1].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::_try_create::root.body[16].body[4].body[1].body[3]::Expr

Source: `infra/agentinfra/locks.py:96`; AST `eaf888e23cc61c107ec0d54a10f219382583f810784d2b5380deae2c363a1206`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: os, stream. Outputs/bindings: (none).
Calls/effect boundaries: os.fsync, stream.fileno.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[4].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::_try_create::root.body[16].body[4].body[1].body[3].value::Call

Source: `infra/agentinfra/locks.py:96`; AST `29e1a002fb3ed92242523219b50a26133c0e15643b5dfd72168bc1eb4f1aed09`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os, stream. Outputs/bindings: (none).
Calls/effect boundaries: os.fsync, stream.fileno.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[4].body[1].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::_try_create::root.body[16].body[4].body[1].body[3].value.args[0]::Call

Source: `infra/agentinfra/locks.py:96`; AST `27f47889b85ed2bb90d146b9008836c66d42f49c92f140cae1596cf4efe4d050`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: stream. Outputs/bindings: (none).
Calls/effect boundaries: stream.fileno.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[4].body[1].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5]::FunctionDef

Source: `infra/agentinfra/locks.py:98`; AST `1fc05198890a81c8cfeaff0e908c5d32044341174535394776f9d9859556ca69`.

Rust module: `infra::agentinfra::locks`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileExistsError, FileNotFoundError, LockError, PermissionError, ValueError, _now, _process_identity, deadline, dict, exc, float, info, last_contention, max, min, os, payload, self, socket, time, timeout, uuid. Outputs/bindings: deadline, info, last_contention, payload.
Calls/effect boundaries: LockError, ValueError, _now, _process_identity, dict, float, info.get, max, min, os.getpid, self._try_create, self.inspect, self.path.parent.mkdir, self.path.unlink, socket.gethostname, time.monotonic, time.sleep, uuid.uuid4.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[0]::If

Source: `infra/agentinfra/locks.py:99`; AST `dc5519276638164dc2d81fbfaeed0f64657f8b74cfc2b2d582edfde7b4480539`.

Rust module: `infra::agentinfra::locks`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: LockError, self. Outputs/bindings: (none).
Calls/effect boundaries: LockError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered If evaluation at root.body[16].body[5].body[0]; no call, error or mutation may be omitted. Condition: self._owner is not None
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[0].body[0]::Raise

Source: `infra/agentinfra/locks.py:100`; AST `51bf908cc6e5e9ae608d97ac15004f74ff0766e7af0cea262c3597f6f914d8ac`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: LockError. Outputs/bindings: (none).
Calls/effect boundaries: LockError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[16].body[5].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[0].body[0].exc::Call

Source: `infra/agentinfra/locks.py:100`; AST `029802bdd574376642692778854932d73d271d4e4e1e4d4fe8df7792b8d1650a`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: LockError. Outputs/bindings: (none).
Calls/effect boundaries: LockError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].body[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[1]::If

Source: `infra/agentinfra/locks.py:101`; AST `01e83f5a65a3bd7d884f8e0b409f0c0e0f20da7d1a0bf49d3c02db42720829e8`.

Rust module: `infra::agentinfra::locks`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ValueError, float, timeout. Outputs/bindings: (none).
Calls/effect boundaries: ValueError, float.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered If evaluation at root.body[16].body[5].body[1]; no call, error or mutation may be omitted. Condition: timeout < 0 or timeout != timeout or timeout == float('inf')
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[1].test.values[2].comparators[0]::Call

Source: `infra/agentinfra/locks.py:101`; AST `5351252e8d825a36374a8c9dcb78a6daead302dce402af2a4c74c8d17167f46a`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: float. Outputs/bindings: (none).
Calls/effect boundaries: float.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].body[1].test.values[2].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[1].body[0]::Raise

Source: `infra/agentinfra/locks.py:102`; AST `9ec81f3a654cfadef44dcda2e39b4f930fca513c8dccd8c4b2edad97f6a0b402`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ValueError. Outputs/bindings: (none).
Calls/effect boundaries: ValueError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[16].body[5].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[1].body[0].exc::Call

Source: `infra/agentinfra/locks.py:102`; AST `564e842888a54e8dd1d1d2d561d18e86ccc298ffb52309ff11f72a0f3ac19583`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ValueError. Outputs/bindings: (none).
Calls/effect boundaries: ValueError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].body[1].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[2]::Expr

Source: `infra/agentinfra/locks.py:103`; AST `0d74d9688ae835d21ca73b92559370108c358f58471257ab965a3e0953c45c11`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.parent.mkdir.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[2].value::Call

Source: `infra/agentinfra/locks.py:103`; AST `02b3b5924f8cfb1ea300dcb615b348adaef01080a21462fa884d7a5bf5539cb2`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.parent.mkdir.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[3]::Assign

Source: `infra/agentinfra/locks.py:104`; AST `44dadd88bdd8fd65065dc2f92c11d4516fb978744a8e0120cf3e4f3d16b4eeec`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _now, _process_identity, os, self, socket, uuid. Outputs/bindings: payload.
Calls/effect boundaries: _now, _process_identity, os.getpid, socket.gethostname, uuid.uuid4.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[5].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[3].value.values[1].value::Call

Source: `infra/agentinfra/locks.py:106`; AST `87eafda000cba758be33f767d487f36fa6a34917ff4cfe4cbd289edd7d07163b`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: uuid. Outputs/bindings: (none).
Calls/effect boundaries: uuid.uuid4.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].body[3].value.values[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[3].value.values[2]::Call

Source: `infra/agentinfra/locks.py:107`; AST `ba1923643b161051a18bf7ae7386addd84146f4ab481f99d56712bc1ce97df2c`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os. Outputs/bindings: (none).
Calls/effect boundaries: os.getpid.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].body[3].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[3].value.values[3]::Call

Source: `infra/agentinfra/locks.py:108`; AST `2aef08e15d3cfc5066148b99b3fad757eb10c1fc0ece67ab3e79ebacee362383`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _process_identity, os. Outputs/bindings: (none).
Calls/effect boundaries: _process_identity, os.getpid.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].body[3].value.values[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[3].value.values[3].args[0]::Call

Source: `infra/agentinfra/locks.py:108`; AST `ba1923643b161051a18bf7ae7386addd84146f4ab481f99d56712bc1ce97df2c`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os. Outputs/bindings: (none).
Calls/effect boundaries: os.getpid.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].body[3].value.values[3].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[3].value.values[4]::Call

Source: `infra/agentinfra/locks.py:109`; AST `4263cfe4ff762fbfb73db5540d6d421a621a7fb22318759bc79d367d143d5895`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: socket. Outputs/bindings: (none).
Calls/effect boundaries: socket.gethostname.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].body[3].value.values[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[3].value.values[5]::Call

Source: `infra/agentinfra/locks.py:110`; AST `a45c2ac57befcf1212794e7c42a7aad7870de2198eba961b8d2f47b37f928f0f`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _now. Outputs/bindings: (none).
Calls/effect boundaries: _now.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].body[3].value.values[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[4]::Assign

Source: `infra/agentinfra/locks.py:113`; AST `ad997073dee2dfc4b88a201afc9f77f4860e0a0b5a4123ea83e57cde59633ebf`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: time, timeout. Outputs/bindings: deadline.
Calls/effect boundaries: time.monotonic.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[5].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[4].value.left::Call

Source: `infra/agentinfra/locks.py:113`; AST `1518ec519851d0a5084168b533bc641ad5d2ce5a406bada9f9d7d919d82e5b92`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: time. Outputs/bindings: (none).
Calls/effect boundaries: time.monotonic.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].body[4].value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[5]::AnnAssign

Source: `infra/agentinfra/locks.py:114`; AST `765e60bd651f4490380eb9646cbc36e0ccba9c7e6f85ade3dfb98ee8a3454435`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: PermissionError. Outputs/bindings: last_contention.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[16].body[5].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[6]::While

Source: `infra/agentinfra/locks.py:115`; AST `ee9090376849747f8a348431807d613292dc2f746456e59b51cea5fad22865c5`.

Rust module: `infra::agentinfra::locks`. while with explicit truth conversion and a normal-exhaustion flag for loop else

Inputs: FileExistsError, FileNotFoundError, LockError, PermissionError, deadline, dict, exc, info, last_contention, max, min, os, payload, self, time. Outputs/bindings: info, last_contention.
Calls/effect boundaries: LockError, dict, info.get, max, min, self._try_create, self.inspect, self.path.unlink, time.monotonic, time.sleep.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered While evaluation at root.body[16].body[5].body[6]; no call, error or mutation may be omitted. Condition: True
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[6].body[0]::Try

Source: `infra/agentinfra/locks.py:116`; AST `4feada89d63008c9460e6a0b8bc60adf52380ff50b9efd17e9d69bbf2ae8ad6f`.

Rust module: `infra::agentinfra::locks`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: FileExistsError, PermissionError, dict, exc, os, payload, self. Outputs/bindings: last_contention.
Calls/effect boundaries: dict, self._try_create.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Try evaluation at root.body[16].body[5].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[6].body[0].body[0]::Expr

Source: `infra/agentinfra/locks.py:117`; AST `115428b88ba518a5709b67fb9ff8986af8b89a8b692bd1c71f80904ba737f38a`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: payload, self. Outputs/bindings: (none).
Calls/effect boundaries: self._try_create.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[5].body[6].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[6].body[0].body[0].value::Call

Source: `infra/agentinfra/locks.py:117`; AST `030ac7d915e32f3925487274a1cd341d4050837ffe3386b7b9f36d1ec7100767`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: payload, self. Outputs/bindings: (none).
Calls/effect boundaries: self._try_create.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].body[6].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[6].body[0].body[1]::Assign

Source: `infra/agentinfra/locks.py:118`; AST `a1e35e9e7ac3fed2b2af861f6569ecfc9c2b8543522a8c457c2e3e948d40e4fc`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: payload, self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[5].body[6].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[6].body[0].body[2]::Return

Source: `infra/agentinfra/locks.py:119`; AST `77cd9819c1315f07eca341632a290f08cc602fe73c3eaec45ff09ef8508b51e6`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, payload. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Return evaluation at root.body[16].body[5].body[6].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[6].body[0].body[2].value::Call

Source: `infra/agentinfra/locks.py:119`; AST `95308c2763daf8ae258704fecf825b5f5c555658fbf5609e9e26b1309439c314`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, payload. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].body[6].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[6].body[0].handlers[0]::ExceptHandler

Source: `infra/agentinfra/locks.py:120`; AST `85f553c8ae6062f4e008afd0833d5a5bfec196f16e212366b1db7c3bde1c2f18`.

Rust module: `infra::agentinfra::locks`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: FileExistsError. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[16].body[5].body[6].body[0].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[6].body[0].handlers[0].body[0]::Pass

Source: `infra/agentinfra/locks.py:121`; AST `f8e211bd496e62be79e8542ba1d0a7cebbf2a6143ae07b375ae14ce00a91b69c`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Pass evaluation at root.body[16].body[5].body[6].body[0].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[6].body[0].handlers[1]::ExceptHandler

Source: `infra/agentinfra/locks.py:122`; AST `54a667224569b32d7f880df1d3ce4a2c9c5b8d948b3cba8fd030fd24d1151715`.

Rust module: `infra::agentinfra::locks`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: PermissionError, exc, os. Outputs/bindings: last_contention.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[16].body[5].body[6].body[0].handlers[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[6].body[0].handlers[1].body[0]::If

Source: `infra/agentinfra/locks.py:128`; AST `9e2d51ebeca437aac1b9d31dcc5ac82eb1f9636a7250a5ba838d411d0300752f`.

Rust module: `infra::agentinfra::locks`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: os. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered If evaluation at root.body[16].body[5].body[6].body[0].handlers[1].body[0]; no call, error or mutation may be omitted. Condition: os.name != 'nt'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[6].body[0].handlers[1].body[0].body[0]::Raise

Source: `infra/agentinfra/locks.py:129`; AST `ba28128c14dfbd0a9062c0dbab42ad6c52ecf0767df6b67576deb1dbbfdd038d`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[16].body[5].body[6].body[0].handlers[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[6].body[0].handlers[1].body[1]::Assign

Source: `infra/agentinfra/locks.py:130`; AST `c946ae42be0f26bd46aaf8b6fe0af561a061b871f67fcdccac7ff936daaa323f`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: exc. Outputs/bindings: last_contention.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[5].body[6].body[0].handlers[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[6].body[1]::Assign

Source: `infra/agentinfra/locks.py:131`; AST `1d59754ac091a6ee214aac9371cc173038673f91ac8a94e0c454082eb7ad1079`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: info.
Calls/effect boundaries: self.inspect.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[5].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[6].body[1].value::Call

Source: `infra/agentinfra/locks.py:131`; AST `2fbbe4645de7d7ecd0402e1fe2e444a18e99da2860dfdefba2385664d7001ac1`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.inspect.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].body[6].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[6].body[2]::If

Source: `infra/agentinfra/locks.py:132`; AST `5ee883141898f6b8c5eb1684a1bee79faab208c1f6c5b774b4966156aa7150a2`.

Rust module: `infra::agentinfra::locks`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: FileNotFoundError, info, self. Outputs/bindings: (none).
Calls/effect boundaries: info.get, self.path.unlink.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered If evaluation at root.body[16].body[5].body[6].body[2]; no call, error or mutation may be omitted. Condition: info.get('exists') and info.get('same_host') and (info.get('pid_alive_here') is False)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[6].body[2].test.values[0]::Call

Source: `infra/agentinfra/locks.py:132`; AST `e8931dad20df8ee78b06dedbbd189250617a028b70ff4355bd472db9215d4624`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: info. Outputs/bindings: (none).
Calls/effect boundaries: info.get.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].body[6].body[2].test.values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[6].body[2].test.values[1]::Call

Source: `infra/agentinfra/locks.py:132`; AST `0b6d9612b0e3175463a20136a4cde4e1aa3c3d00b49fe9ea6a6957f73ca66ca9`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: info. Outputs/bindings: (none).
Calls/effect boundaries: info.get.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].body[6].body[2].test.values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[6].body[2].test.values[2].left::Call

Source: `infra/agentinfra/locks.py:132`; AST `dbdeec6c43f7db76c06d146aac8ce5f48ab622c30a12e2643ff2f5eb00684404`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: info. Outputs/bindings: (none).
Calls/effect boundaries: info.get.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].body[6].body[2].test.values[2].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[6].body[2].body[0]::Try

Source: `infra/agentinfra/locks.py:133`; AST `6a5b2cd9be2a4ebc03ac3b06f442efb453979d69a662dfc8a8db524b563ff879`.

Rust module: `infra::agentinfra::locks`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: FileNotFoundError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.unlink.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Try evaluation at root.body[16].body[5].body[6].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[6].body[2].body[0].body[0]::Expr

Source: `infra/agentinfra/locks.py:134`; AST `2eaaf0646f30797a74f5ad962af1b2c2d1159db247bb9e6a1ee6721b6520377e`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.unlink.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[5].body[6].body[2].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[6].body[2].body[0].body[0].value::Call

Source: `infra/agentinfra/locks.py:134`; AST `43f225d591630075cea5936de3ed0a36454310cb59f02d58caec2c978b9bb6ea`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.unlink.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].body[6].body[2].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[6].body[2].body[0].handlers[0]::ExceptHandler

Source: `infra/agentinfra/locks.py:135`; AST `c7e1d4b13630c3bb5f289bcb8e939f9b54e9bdd3291b7d197e789650db8f0aa6`.

Rust module: `infra::agentinfra::locks`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: FileNotFoundError. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[16].body[5].body[6].body[2].body[0].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[6].body[2].body[0].handlers[0].body[0]::Pass

Source: `infra/agentinfra/locks.py:136`; AST `f8e211bd496e62be79e8542ba1d0a7cebbf2a6143ae07b375ae14ce00a91b69c`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Pass evaluation at root.body[16].body[5].body[6].body[2].body[0].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[6].body[2].body[1]::Continue

Source: `infra/agentinfra/locks.py:137`; AST `3d1e0aaa463df3eefc9bd5be83f453adcd9621b2dc7f387c3eaff3ab42e91059`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Continue evaluation at root.body[16].body[5].body[6].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[6].body[3]::If

Source: `infra/agentinfra/locks.py:138`; AST `eb4de33eee4c4a44ce51907f003dd4329ebfff52a92ebff8c7dc5110ebf078a4`.

Rust module: `infra::agentinfra::locks`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: LockError, deadline, info, last_contention, self, time. Outputs/bindings: (none).
Calls/effect boundaries: LockError, time.monotonic.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered If evaluation at root.body[16].body[5].body[6].body[3]; no call, error or mutation may be omitted. Condition: time.monotonic() >= deadline
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[6].body[3].test.left::Call

Source: `infra/agentinfra/locks.py:138`; AST `1518ec519851d0a5084168b533bc641ad5d2ce5a406bada9f9d7d919d82e5b92`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: time. Outputs/bindings: (none).
Calls/effect boundaries: time.monotonic.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].body[6].body[3].test.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[6].body[3].body[0]::Raise

Source: `infra/agentinfra/locks.py:139`; AST `1cbce50b133afb27b7812479ab4fcc883effc2bb3a12bfe4b27071172155adb3`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: LockError, info, last_contention, self. Outputs/bindings: (none).
Calls/effect boundaries: LockError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[16].body[5].body[6].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[6].body[3].body[0].exc::Call

Source: `infra/agentinfra/locks.py:139`; AST `d1b4edbae84adc522ff63da119b07b7b25a529b74463abe28b09fc770c41fd81`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: LockError, info, self. Outputs/bindings: (none).
Calls/effect boundaries: LockError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].body[6].body[3].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[6].body[4]::Expr

Source: `infra/agentinfra/locks.py:140`; AST `8463423063f8f3e3d646ac634c5ee81a91c4003490f2e7ed6cf3258800c35af9`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: deadline, max, min, time. Outputs/bindings: (none).
Calls/effect boundaries: max, min, time.monotonic, time.sleep.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[5].body[6].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[6].body[4].value::Call

Source: `infra/agentinfra/locks.py:140`; AST `dd34c8e4bbbad432ae08878441dfe2eadf28a1a1b3bae0966b94ff0cff9f6039`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: deadline, max, min, time. Outputs/bindings: (none).
Calls/effect boundaries: max, min, time.monotonic, time.sleep.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].body[6].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[6].body[4].value.args[0]::Call

Source: `infra/agentinfra/locks.py:140`; AST `eb36e72513e39b85a7039e7bd1eea12a475b0837d2c57d4915644aa2e1b0c1cc`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: deadline, max, min, time. Outputs/bindings: (none).
Calls/effect boundaries: max, min, time.monotonic.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].body[6].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[6].body[4].value.args[0].args[1]::Call

Source: `infra/agentinfra/locks.py:140`; AST `6424d866722f77ffe3b6a7e01e594ade49ac1e30864b05989a7fb6d6100949bf`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: deadline, max, time. Outputs/bindings: (none).
Calls/effect boundaries: max, time.monotonic.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].body[6].body[4].value.args[0].args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::acquire::root.body[16].body[5].body[6].body[4].value.args[0].args[1].args[1].right::Call

Source: `infra/agentinfra/locks.py:140`; AST `1518ec519851d0a5084168b533bc641ad5d2ce5a406bada9f9d7d919d82e5b92`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: time. Outputs/bindings: (none).
Calls/effect boundaries: time.monotonic.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].body[6].body[4].value.args[0].args[1].args[1].right; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6]::FunctionDef

Source: `infra/agentinfra/locks.py:142`; AST `9a2c1cf6df61976c9bcb3e0f16924a775477fed4fca6b595c3a9219c9cbf99dd`.

Rust module: `infra::agentinfra::locks`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Exception, FileNotFoundError, OSError, PermissionError, _pid_alive, data, delay, dict, exc, int, isinstance, json, last_error, max, self, socket, str, time. Outputs/bindings: data, delay, last_error.
Calls/effect boundaries: _pid_alive, data.get, int, isinstance, json.loads, max, self.path.read_text, self.path.stat, socket.gethostname, str, time.sleep, time.time.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[0]::Assign

Source: `infra/agentinfra/locks.py:143`; AST `c5039daca53505ecea0eef9b371a19d7f47f71bcc5eafecb2c3e23902b54eb4f`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: last_error.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[1]::For

Source: `infra/agentinfra/locks.py:144`; AST `c214b9b18e80399603513da78405ff2667e694cef3a3e20c5528acbf28f0b5b5`.

Rust module: `infra::agentinfra::locks`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: Exception, FileNotFoundError, PermissionError, delay, exc, json, last_error, self, str, time. Outputs/bindings: data, delay, last_error.
Calls/effect boundaries: json.loads, self.path.read_text, str, time.sleep.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered For evaluation at root.body[16].body[6].body[1]; no call, error or mutation may be omitted. Iteration: delay in (0.0, 0.002, 0.01, 0.03)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[1].body[0]::If

Source: `infra/agentinfra/locks.py:145`; AST `ffd0ebf7abdb267ef583b1a6577a01ad8579277e2e4a0dc2d4223611de05258e`.

Rust module: `infra::agentinfra::locks`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: delay, time. Outputs/bindings: (none).
Calls/effect boundaries: time.sleep.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered If evaluation at root.body[16].body[6].body[1].body[0]; no call, error or mutation may be omitted. Condition: delay
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[1].body[0].body[0]::Expr

Source: `infra/agentinfra/locks.py:146`; AST `63460f424effbf8b7431cba8d93b061f273993505e5342b990dd6ee91178a9d9`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: delay, time. Outputs/bindings: (none).
Calls/effect boundaries: time.sleep.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[6].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[1].body[0].body[0].value::Call

Source: `infra/agentinfra/locks.py:146`; AST `77933c8d2024856a54243855e5a5ced8ff5fce6afbb828d52c8100a292a2cdf3`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: delay, time. Outputs/bindings: (none).
Calls/effect boundaries: time.sleep.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].body[1].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[1].body[1]::Try

Source: `infra/agentinfra/locks.py:147`; AST `2e321dac8a1a3f4ed1d6c2c0f03902d8cf6306d00ed19ffc98004a8280517edb`.

Rust module: `infra::agentinfra::locks`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: Exception, FileNotFoundError, PermissionError, exc, json, self, str. Outputs/bindings: data, last_error.
Calls/effect boundaries: json.loads, self.path.read_text, str.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Try evaluation at root.body[16].body[6].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[1].body[1].body[0]::Assign

Source: `infra/agentinfra/locks.py:148`; AST `537866d8a69dce44662a10218817fcecfb6a1dafbf579a9f1fa675bb6453b84a`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, self. Outputs/bindings: data.
Calls/effect boundaries: json.loads, self.path.read_text.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[6].body[1].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[1].body[1].body[0].value::Call

Source: `infra/agentinfra/locks.py:148`; AST `0821249bc5d520456a58c8bd759d33bc2795100268ab823b399b37e6440024f2`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, self. Outputs/bindings: (none).
Calls/effect boundaries: json.loads, self.path.read_text.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].body[1].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[1].body[1].body[0].value.args[0]::Call

Source: `infra/agentinfra/locks.py:148`; AST `f9fe252e092d67f80149821fa317f11a8793887293ededd32e981c87c392711c`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.read_text.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].body[1].body[1].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[1].body[1].body[1]::Break

Source: `infra/agentinfra/locks.py:149`; AST `c0d25d96e6146e7b648417b86bf6bbfedd0a458099247cf2cd469124da4c9fec`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Break evaluation at root.body[16].body[6].body[1].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[1].body[1].handlers[0]::ExceptHandler

Source: `infra/agentinfra/locks.py:150`; AST `fa7ad1a3c52dd00b6e0686de362062e0eac9fe38a80e0e214992ccaf9f65746b`.

Rust module: `infra::agentinfra::locks`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: FileNotFoundError. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[16].body[6].body[1].body[1].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[1].body[1].handlers[0].body[0]::Return

Source: `infra/agentinfra/locks.py:151`; AST `eab80d6e76c04ede53120941fe0ce12178b01b5fe238c1f31f365b64aab5dd11`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Return evaluation at root.body[16].body[6].body[1].body[1].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[1].body[1].handlers[1]::ExceptHandler

Source: `infra/agentinfra/locks.py:152`; AST `8c89db6ec6a39b28b7e1d05517ad562a914833f3ed6e5f8a498921bfdc6de3ef`.

Rust module: `infra::agentinfra::locks`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: PermissionError, exc. Outputs/bindings: last_error.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[16].body[6].body[1].body[1].handlers[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[1].body[1].handlers[1].body[0]::Assign

Source: `infra/agentinfra/locks.py:153`; AST `30f88c0a10ae6e7341ebad4d2c46ef4986c5e3ad095562ee388e9d491eeaf1f2`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: exc. Outputs/bindings: last_error.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[6].body[1].body[1].handlers[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[1].body[1].handlers[2]::ExceptHandler

Source: `infra/agentinfra/locks.py:154`; AST `e3c862d9bc93f22584ed47fc6aba2fe5ed63c088eb80dfde4dffd25a06efde56`.

Rust module: `infra::agentinfra::locks`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: Exception, exc, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[16].body[6].body[1].body[1].handlers[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[1].body[1].handlers[2].body[0]::Return

Source: `infra/agentinfra/locks.py:155`; AST `bfdc47d031d7b3d86b4f4f2ea684540e8241094d9cd47458b17ee8d7c3aaa42e`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: exc, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Return evaluation at root.body[16].body[6].body[1].body[1].handlers[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[1].body[1].handlers[2].body[0].value.values[2]::Call

Source: `infra/agentinfra/locks.py:155`; AST `ed91e0e2c4feb43ad37ba7941b4ee3c7dcc36d3eb80d4a170990c028aa16f027`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exc, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].body[1].body[1].handlers[2].body[0].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[1].orelse[0]::Return

Source: `infra/agentinfra/locks.py:157`; AST `53a93ad9d11966ab640cd903db176c248a30c20888de0f757c8634e88d43e191`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: last_error, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Return evaluation at root.body[16].body[6].body[1].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[1].orelse[0].value.values[2]::Call

Source: `infra/agentinfra/locks.py:157`; AST `114e8bb9f32a305200f0e717e72ecba3c1dcd9fbca2eeee8ee3acc9f5cac07f8`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: last_error, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].body[1].orelse[0].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[2]::If

Source: `infra/agentinfra/locks.py:158`; AST `1703361284d303f6f8fb518ae4ecaeabc6f6fe9a27116a76ea2dbfad192693c4`.

Rust module: `infra::agentinfra::locks`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: data, dict, isinstance. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered If evaluation at root.body[16].body[6].body[2]; no call, error or mutation may be omitted. Condition: not isinstance(data, dict)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[2].test.operand::Call

Source: `infra/agentinfra/locks.py:158`; AST `5f3dfa3b23b16e077ee85aed20c0cc9933e4cb3a08ae821ef38b1086b65c69f5`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data, dict, isinstance. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].body[2].test.operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[2].body[0]::Return

Source: `infra/agentinfra/locks.py:159`; AST `b4eb57056b0fab37cfa69330fbcab3e7dd84ce1f403d5c4044820a0e968229e0`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Return evaluation at root.body[16].body[6].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[3]::If

Source: `infra/agentinfra/locks.py:160`; AST `4f8c261c2c6d678e24f570906b97e49371f87b62266f25bb18363af52ce4c670`.

Rust module: `infra::agentinfra::locks`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: data, dict, isinstance, str. Outputs/bindings: (none).
Calls/effect boundaries: data.get, isinstance.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered If evaluation at root.body[16].body[6].body[3]; no call, error or mutation may be omitted. Condition: not isinstance(data, dict) or not isinstance(data.get('nonce'), str)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[3].test.values[0].operand::Call

Source: `infra/agentinfra/locks.py:160`; AST `5f3dfa3b23b16e077ee85aed20c0cc9933e4cb3a08ae821ef38b1086b65c69f5`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data, dict, isinstance. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].body[3].test.values[0].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[3].test.values[1].operand::Call

Source: `infra/agentinfra/locks.py:160`; AST `716e8c621bc7fafbb095e361b096a13f9c97f74308c4bb2fda7bef845e4afe71`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data, isinstance, str. Outputs/bindings: (none).
Calls/effect boundaries: data.get, isinstance.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].body[3].test.values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[3].test.values[1].operand.args[0]::Call

Source: `infra/agentinfra/locks.py:160`; AST `902e959f8dacbbc42a7513971215f94ba292bfe5527b5ecd0027858e1fc76d4b`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data. Outputs/bindings: (none).
Calls/effect boundaries: data.get.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].body[3].test.values[1].operand.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[3].body[0]::Return

Source: `infra/agentinfra/locks.py:161`; AST `f76d19d69991239703896e0c064e8823f5f1b2dee618653c5696a7e3705128c1`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Return evaluation at root.body[16].body[6].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[4]::Assign

Source: `infra/agentinfra/locks.py:162`; AST `f4187c8948196d02d6822cd20ce2b44831cbe2d30b5b00ebe4ace3d9e8f2d5ab`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: data. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[6].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[5]::Assign

Source: `infra/agentinfra/locks.py:163`; AST `592f021ded9d0dbff2d8bb1203269c4bc11816e4764678dcc9431840b35a21c3`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: data, socket. Outputs/bindings: (none).
Calls/effect boundaries: data.get, socket.gethostname.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[6].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[5].value.left::Call

Source: `infra/agentinfra/locks.py:163`; AST `cafdbdb15995b6effa251935f6a9f5e1ce9a8848056b759440b1e40ab6cd8d48`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data. Outputs/bindings: (none).
Calls/effect boundaries: data.get.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].body[5].value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[5].value.comparators[0]::Call

Source: `infra/agentinfra/locks.py:163`; AST `4263cfe4ff762fbfb73db5540d6d421a621a7fb22318759bc79d367d143d5895`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: socket. Outputs/bindings: (none).
Calls/effect boundaries: socket.gethostname.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].body[5].value.comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[6]::Assign

Source: `infra/agentinfra/locks.py:164`; AST `1f26c48810781b986baa53a00b073619a0633fe9272d8d3e77e44e55f91fa4e8`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _pid_alive, data, int. Outputs/bindings: (none).
Calls/effect boundaries: _pid_alive, data.get, int.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[6].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[6].value.body::Call

Source: `infra/agentinfra/locks.py:165`; AST `3ded3eff5149e11eca7365d15f90f1ccf768d31f838e5ee742677c06bbb8e0d5`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _pid_alive, data, int. Outputs/bindings: (none).
Calls/effect boundaries: _pid_alive, data.get, int.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].body[6].value.body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[6].value.body.args[0]::Call

Source: `infra/agentinfra/locks.py:165`; AST `013313b879e5bd873188e69f288738094c35404d4da742e887254676a2762e78`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data, int. Outputs/bindings: (none).
Calls/effect boundaries: data.get, int.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].body[6].value.body.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[6].value.body.args[0].args[0]::Call

Source: `infra/agentinfra/locks.py:165`; AST `ddd9f56a3d390c9d3d03c2c77610c7865326859f5341902cbcb423abd2abc8de`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data. Outputs/bindings: (none).
Calls/effect boundaries: data.get.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].body[6].value.body.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[6].value.body.args[1]::Call

Source: `infra/agentinfra/locks.py:165`; AST `32d593f811c92796e0efdbf08bbc106ab62b7e085739d88d5bc70eff9a71ba3f`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data. Outputs/bindings: (none).
Calls/effect boundaries: data.get.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].body[6].value.body.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[7]::Try

Source: `infra/agentinfra/locks.py:167`; AST `fb0c62cc9aea1ee56697962ed8e2e22aebe45cdc5debc4fe728bd85590ce68e9`.

Rust module: `infra::agentinfra::locks`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: OSError, data, max, self, time. Outputs/bindings: (none).
Calls/effect boundaries: max, self.path.stat, time.time.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Try evaluation at root.body[16].body[6].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[7].body[0]::Assign

Source: `infra/agentinfra/locks.py:168`; AST `f803e4b043a3ceb0d17790d72e4c5d141fab611179a1e389045afcfd97e9e087`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: data, max, self, time. Outputs/bindings: (none).
Calls/effect boundaries: max, self.path.stat, time.time.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[6].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[7].body[0].value::Call

Source: `infra/agentinfra/locks.py:168`; AST `146540ddb068f0c4d4197575e63b4961eb6edb2394b48538d2a5b600a8b3e146`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: max, self, time. Outputs/bindings: (none).
Calls/effect boundaries: max, self.path.stat, time.time.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[7].body[0].value.args[1].left::Call

Source: `infra/agentinfra/locks.py:168`; AST `bd39b5d643e5010141bcdbc0472d642c43f78408efe5a8a37b77a851078be1be`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: time. Outputs/bindings: (none).
Calls/effect boundaries: time.time.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].body[7].body[0].value.args[1].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[7].body[0].value.args[1].right.value::Call

Source: `infra/agentinfra/locks.py:168`; AST `3fc580e6a650bd3d3a3d89c2b66b934681f907a52aa28d74e3f10ec2cca2751a`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.stat.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].body[7].body[0].value.args[1].right.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[7].handlers[0]::ExceptHandler

Source: `infra/agentinfra/locks.py:169`; AST `80a311151e65e1bafda4060311f4ae294880f8bbd36b9aaceda28890d927c5db`.

Rust module: `infra::agentinfra::locks`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: OSError, data. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[16].body[6].body[7].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[7].handlers[0].body[0]::Assign

Source: `infra/agentinfra/locks.py:170`; AST `ed32b4c902fb3a0237ce3e7c430f4e5fe29aa4d7daf452f2176bdb9501978f26`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: data. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[6].body[7].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::inspect::root.body[16].body[6].body[8]::Return

Source: `infra/agentinfra/locks.py:171`; AST `a12e64fa3a041e609d3a25dc46c10c675ec5ec937a53909e14dc1d95d37a3c33`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: data. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Return evaluation at root.body[16].body[6].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7]::FunctionDef

Source: `infra/agentinfra/locks.py:173`; AST `8f208f5958cc103d6b8f844d5163f3c27091bac2cea1e808de1a7a39912fd709`.

Rust module: `infra::agentinfra::locks`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: LockError, PermissionError, delay, exc, expected, info, int, last_error, nonce, os, self, str, time. Outputs/bindings: delay, expected, info, last_error.
Calls/effect boundaries: LockError, info.get, int, os.getpid, self._owner.get, self.inspect, self.path.unlink, time.sleep.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[0]::If

Source: `infra/agentinfra/locks.py:174`; AST `ee174f5d7e205b39b0e29488b4153e8a369a7108624f2cfabb85367456a14238`.

Rust module: `infra::agentinfra::locks`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: LockError, self. Outputs/bindings: (none).
Calls/effect boundaries: LockError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered If evaluation at root.body[16].body[7].body[0]; no call, error or mutation may be omitted. Condition: self._owner is None
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[0].body[0]::Raise

Source: `infra/agentinfra/locks.py:175`; AST `4d5c1978eb10b3eaf9763906c9aa28fab68c9ee5048742f6089865bb63614ec8`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: LockError. Outputs/bindings: (none).
Calls/effect boundaries: LockError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[16].body[7].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[0].body[0].exc::Call

Source: `infra/agentinfra/locks.py:175`; AST `a799d600e941bc8e1e2adcf3e0dc8c7bb003162852b6fd71cccf138d3ce1b225`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: LockError. Outputs/bindings: (none).
Calls/effect boundaries: LockError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[1]::Assign

Source: `infra/agentinfra/locks.py:176`; AST `1d59754ac091a6ee214aac9371cc173038673f91ac8a94e0c454082eb7ad1079`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: info.
Calls/effect boundaries: self.inspect.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[7].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[1].value::Call

Source: `infra/agentinfra/locks.py:176`; AST `2fbbe4645de7d7ecd0402e1fe2e444a18e99da2860dfdefba2385664d7001ac1`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.inspect.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[2]::If

Source: `infra/agentinfra/locks.py:177`; AST `75f2fa41024dad0e97d1cd31b2bdc380321d45170d6a3b23fdd64f46ae309af9`.

Rust module: `infra::agentinfra::locks`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: LockError, info, self. Outputs/bindings: (none).
Calls/effect boundaries: LockError, info.get.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered If evaluation at root.body[16].body[7].body[2]; no call, error or mutation may be omitted. Condition: not info.get('exists')
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[2].test.operand::Call

Source: `infra/agentinfra/locks.py:177`; AST `e8931dad20df8ee78b06dedbbd189250617a028b70ff4355bd472db9215d4624`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: info. Outputs/bindings: (none).
Calls/effect boundaries: info.get.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[2].test.operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[2].body[0]::Assign

Source: `infra/agentinfra/locks.py:178`; AST `fc4c24dde43de29cbbc33c973e661d9a2eba6bf7a17801c1afed32859d598810`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[7].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[2].body[1]::Raise

Source: `infra/agentinfra/locks.py:179`; AST `b783b5ce96d4a0cc47f65e64d50c7b212c8eee781e398588ae88aff977702603`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: LockError. Outputs/bindings: (none).
Calls/effect boundaries: LockError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[16].body[7].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[2].body[1].exc::Call

Source: `infra/agentinfra/locks.py:179`; AST `56fb45785454efae0eb0f2e07cccfcced2ab48635a6cb7b0d58d444ec5940f75`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: LockError. Outputs/bindings: (none).
Calls/effect boundaries: LockError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[2].body[1].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[3]::Assign

Source: `infra/agentinfra/locks.py:180`; AST `8e5f3f9de28a1336eb28196482b413d28e48b16030e6b0ec4f378a39e61def51`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: nonce, self. Outputs/bindings: expected.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[7].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[4]::If

Source: `infra/agentinfra/locks.py:181`; AST `e6d6383233532882d6a154b4ae7e7c13fb5b0d22b7a0fd4d9cbe83d7c1042ab6`.

Rust module: `infra::agentinfra::locks`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: LockError, expected, info, int, os, self. Outputs/bindings: (none).
Calls/effect boundaries: LockError, info.get, int, os.getpid, self._owner.get.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered If evaluation at root.body[16].body[7].body[4]; no call, error or mutation may be omitted. Condition: info.get('nonce') != expected or info.get('nonce') != self._owner.get('nonce') or info.get('host') != self._owner.get('host') or (int(info.get('pid', -1)) != os.getpid()) or (info.get('process_identity') != self._owner.get('process_identity'))
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[4].test.values[0].left::Call

Source: `infra/agentinfra/locks.py:182`; AST `44011854f920a1278e4502f259fba44b834a11871ff5455dcaab2735805b7b2b`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: info. Outputs/bindings: (none).
Calls/effect boundaries: info.get.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[4].test.values[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[4].test.values[1].left::Call

Source: `infra/agentinfra/locks.py:183`; AST `44011854f920a1278e4502f259fba44b834a11871ff5455dcaab2735805b7b2b`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: info. Outputs/bindings: (none).
Calls/effect boundaries: info.get.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[4].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[4].test.values[1].comparators[0]::Call

Source: `infra/agentinfra/locks.py:183`; AST `3b4a7e8081105f1e61b6872d3384f6dbdf17b96e297082b72b51965073203566`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self._owner.get.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[4].test.values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[4].test.values[2].left::Call

Source: `infra/agentinfra/locks.py:184`; AST `fd7da59784c8ddd9380cee82f7cf8fcfcb4b748d9b9197f4d8901dfb983f6031`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: info. Outputs/bindings: (none).
Calls/effect boundaries: info.get.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[4].test.values[2].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[4].test.values[2].comparators[0]::Call

Source: `infra/agentinfra/locks.py:184`; AST `bf968147efe35979a4a8e66736a0f0482da45886b8515b84b3dd4f954536b0b0`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self._owner.get.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[4].test.values[2].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[4].test.values[3].left::Call

Source: `infra/agentinfra/locks.py:185`; AST `cb0e0f718921e24b55e8dc129a5e14a2201728423997a963059139504549cb9c`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: info, int. Outputs/bindings: (none).
Calls/effect boundaries: info.get, int.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[4].test.values[3].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[4].test.values[3].left.args[0]::Call

Source: `infra/agentinfra/locks.py:185`; AST `a5104e597cfddaf22bc85aa8ad197eb6951d1f1ecfcacefb64739bc7273641c0`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: info. Outputs/bindings: (none).
Calls/effect boundaries: info.get.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[4].test.values[3].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[4].test.values[3].comparators[0]::Call

Source: `infra/agentinfra/locks.py:185`; AST `ba1923643b161051a18bf7ae7386addd84146f4ab481f99d56712bc1ce97df2c`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os. Outputs/bindings: (none).
Calls/effect boundaries: os.getpid.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[4].test.values[3].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[4].test.values[4].left::Call

Source: `infra/agentinfra/locks.py:186`; AST `8d84c3624e1e48220a87b7dd9b943b4f3c01770967924c8e5430d82a84ccdd8a`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: info. Outputs/bindings: (none).
Calls/effect boundaries: info.get.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[4].test.values[4].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[4].test.values[4].comparators[0]::Call

Source: `infra/agentinfra/locks.py:186`; AST `1802a3a7841437ae79a00f56a096814c96a2f1b0b1ee43c0d1256b24875d4c54`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self._owner.get.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[4].test.values[4].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[4].body[0]::Raise

Source: `infra/agentinfra/locks.py:188`; AST `2a63ec0255e489afbb2cdb4b1bcdf21a37e9ac0f02636eb3133bf84eccc8e778`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: LockError. Outputs/bindings: (none).
Calls/effect boundaries: LockError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[16].body[7].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[4].body[0].exc::Call

Source: `infra/agentinfra/locks.py:188`; AST `4ac87c9452b074a2ffc754e87061f063fc469dfa3a2e389447fb5d77be60bf60`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: LockError. Outputs/bindings: (none).
Calls/effect boundaries: LockError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[4].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[5]::Assign

Source: `infra/agentinfra/locks.py:189`; AST `c5039daca53505ecea0eef9b371a19d7f47f71bcc5eafecb2c3e23902b54eb4f`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: last_error.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[7].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[6]::For

Source: `infra/agentinfra/locks.py:190`; AST `7a56fc28c244c6f053a75572bcad9ac0f21e49556c9cdf1e29279dc1f9026221`.

Rust module: `infra::agentinfra::locks`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: LockError, PermissionError, delay, exc, last_error, self, time. Outputs/bindings: delay, last_error.
Calls/effect boundaries: LockError, self.path.unlink, time.sleep.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered For evaluation at root.body[16].body[7].body[6]; no call, error or mutation may be omitted. Iteration: delay in (0.0, 0.002, 0.01, 0.03, 0.08)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[6].body[0]::If

Source: `infra/agentinfra/locks.py:191`; AST `ffd0ebf7abdb267ef583b1a6577a01ad8579277e2e4a0dc2d4223611de05258e`.

Rust module: `infra::agentinfra::locks`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: delay, time. Outputs/bindings: (none).
Calls/effect boundaries: time.sleep.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered If evaluation at root.body[16].body[7].body[6].body[0]; no call, error or mutation may be omitted. Condition: delay
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[6].body[0].body[0]::Expr

Source: `infra/agentinfra/locks.py:192`; AST `63460f424effbf8b7431cba8d93b061f273993505e5342b990dd6ee91178a9d9`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: delay, time. Outputs/bindings: (none).
Calls/effect boundaries: time.sleep.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[7].body[6].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[6].body[0].body[0].value::Call

Source: `infra/agentinfra/locks.py:192`; AST `77933c8d2024856a54243855e5a5ced8ff5fce6afbb828d52c8100a292a2cdf3`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: delay, time. Outputs/bindings: (none).
Calls/effect boundaries: time.sleep.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[6].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[6].body[1]::Try

Source: `infra/agentinfra/locks.py:193`; AST `3966da9546478059413929ec0b54b6233b083a50896299af9f6d40d28710631e`.

Rust module: `infra::agentinfra::locks`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: PermissionError, exc, self. Outputs/bindings: last_error.
Calls/effect boundaries: self.path.unlink.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Try evaluation at root.body[16].body[7].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[6].body[1].body[0]::Expr

Source: `infra/agentinfra/locks.py:194`; AST `2eaaf0646f30797a74f5ad962af1b2c2d1159db247bb9e6a1ee6721b6520377e`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.unlink.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[7].body[6].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[6].body[1].body[0].value::Call

Source: `infra/agentinfra/locks.py:194`; AST `43f225d591630075cea5936de3ed0a36454310cb59f02d58caec2c978b9bb6ea`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.unlink.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[6].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[6].body[1].body[1]::Break

Source: `infra/agentinfra/locks.py:195`; AST `c0d25d96e6146e7b648417b86bf6bbfedd0a458099247cf2cd469124da4c9fec`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Break evaluation at root.body[16].body[7].body[6].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[6].body[1].handlers[0]::ExceptHandler

Source: `infra/agentinfra/locks.py:196`; AST `8c89db6ec6a39b28b7e1d05517ad562a914833f3ed6e5f8a498921bfdc6de3ef`.

Rust module: `infra::agentinfra::locks`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: PermissionError, exc. Outputs/bindings: last_error.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[16].body[7].body[6].body[1].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[6].body[1].handlers[0].body[0]::Assign

Source: `infra/agentinfra/locks.py:197`; AST `30f88c0a10ae6e7341ebad4d2c46ef4986c5e3ad095562ee388e9d491eeaf1f2`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: exc. Outputs/bindings: last_error.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[7].body[6].body[1].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[6].orelse[0]::Raise

Source: `infra/agentinfra/locks.py:199`; AST `a95e6e041e797b79af2d70b857efb46226b25fb91a9642a651743cc489b369cf`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: LockError, last_error. Outputs/bindings: (none).
Calls/effect boundaries: LockError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[16].body[7].body[6].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[6].orelse[0].exc::Call

Source: `infra/agentinfra/locks.py:199`; AST `c3c8f307514932ff6130dcb86796c1edb2f1d25967da79b61cc341b42c291993`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: LockError, last_error. Outputs/bindings: (none).
Calls/effect boundaries: LockError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[6].orelse[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::FileLock::release::root.body[16].body[7].body[7]::Assign

Source: `infra/agentinfra/locks.py:200`; AST `fc4c24dde43de29cbbc33c973e661d9a2eba6bf7a17801c1afed32859d598810`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[7].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::root.body[17]::ClassDef

Source: `infra/agentinfra/locks.py:204`; AST `ab4c755950081fd589e7978eee4a667a5abb57df344f83a890cde2b506ab243d`.

Rust module: `infra::agentinfra::locks`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: Exception, FileExistsError, FileNotFoundError, LockError, OSError, Path, _now, _process_identity, any, checks, data, dataclass, dict, exc, expected, expected_task_id, fd, info, isinstance, json, key, lease_id, max, os, owner_nonce, parent_id, payload, raw, reason, required, role, self, set, socket, str, stream, task_id, time, uuid, value. Outputs/bindings: checks, data, expected, fd, info, key, path, payload, purpose, raw, required, stream, value.
Calls/effect boundaries: (json.dumps(payload, sort_keys=True) + '\n').encode, (json.dumps({key: value for key, value in payload.items() if key not in {'exists', 'age_seconds'}}, sort_keys=True) + '\n').encode, LockError, _now, _process_identity, any, checks.items, data.get, info.get, isinstance, json.dumps, json.loads, max, os.fdopen, os.fsync, os.getpid, os.open, payload.get, payload.items, reason.strip, self.inspect, self.path.parent.mkdir, self.path.read_text, self.path.stat, self.path.unlink, set, socket.gethostname, str, stream.fileno, stream.flush, stream.write, time.time, uuid.uuid4.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered ClassDef evaluation at root.body[17]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::root.body[17].body[0]::Expr

Source: `infra/agentinfra/locks.py:205`; AST `14a81df997f64a48af0cc3f1ee1ff655ec57d2328c75c859e72eebaa5fb5fbf4`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::root.body[17].body[1]::AnnAssign

Source: `infra/agentinfra/locks.py:207`; AST `d3875b770eedb512c54cfa40a07917c19082ab47a2d6364a83103c2dc978d73b`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[17].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::root.body[17].body[2]::AnnAssign

Source: `infra/agentinfra/locks.py:208`; AST `22868c1e1ff59a4fe25d940b976b1ddf29bba3fbf10c4924a2e7219235c8117b`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: str. Outputs/bindings: purpose.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[17].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::acquire::root.body[17].body[3]::FunctionDef

Source: `infra/agentinfra/locks.py:210`; AST `d40770b4863fa9e1d51f514f245acf80248d45c9035a4a37e0c5eb553a7d7743`.

Rust module: `infra::agentinfra::locks`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileExistsError, LockError, _now, _process_identity, dict, exc, fd, json, os, parent_id, payload, raw, role, self, socket, str, stream, task_id, uuid. Outputs/bindings: fd, payload, raw, stream.
Calls/effect boundaries: (json.dumps(payload, sort_keys=True) + '\n').encode, LockError, _now, _process_identity, json.dumps, os.fdopen, os.fsync, os.getpid, os.open, self.inspect, self.path.parent.mkdir, socket.gethostname, stream.fileno, stream.flush, stream.write, uuid.uuid4.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::acquire::root.body[17].body[3].body[0]::Expr

Source: `infra/agentinfra/locks.py:211`; AST `0d74d9688ae835d21ca73b92559370108c358f58471257ab965a3e0953c45c11`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.parent.mkdir.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::acquire::root.body[17].body[3].body[0].value::Call

Source: `infra/agentinfra/locks.py:211`; AST `02b3b5924f8cfb1ea300dcb615b348adaef01080a21462fa884d7a5bf5539cb2`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.parent.mkdir.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::acquire::root.body[17].body[3].body[1]::Assign

Source: `infra/agentinfra/locks.py:212`; AST `d5d066d7222f9c4d9a1a71d91fc3c442eb15669a9798a38c40b842f11655b79f`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _now, _process_identity, os, parent_id, role, self, socket, task_id, uuid. Outputs/bindings: payload.
Calls/effect boundaries: _now, _process_identity, os.getpid, socket.gethostname, uuid.uuid4.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::acquire::root.body[17].body[3].body[1].value.values[1].right.value::Call

Source: `infra/agentinfra/locks.py:214`; AST `87eafda000cba758be33f767d487f36fa6a34917ff4cfe4cbd289edd7d07163b`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: uuid. Outputs/bindings: (none).
Calls/effect boundaries: uuid.uuid4.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[1].value.values[1].right.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::acquire::root.body[17].body[3].body[1].value.values[2].value::Call

Source: `infra/agentinfra/locks.py:215`; AST `87eafda000cba758be33f767d487f36fa6a34917ff4cfe4cbd289edd7d07163b`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: uuid. Outputs/bindings: (none).
Calls/effect boundaries: uuid.uuid4.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[1].value.values[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::acquire::root.body[17].body[3].body[1].value.values[6]::Call

Source: `infra/agentinfra/locks.py:219`; AST `ba1923643b161051a18bf7ae7386addd84146f4ab481f99d56712bc1ce97df2c`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os. Outputs/bindings: (none).
Calls/effect boundaries: os.getpid.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[1].value.values[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::acquire::root.body[17].body[3].body[1].value.values[7]::Call

Source: `infra/agentinfra/locks.py:220`; AST `2aef08e15d3cfc5066148b99b3fad757eb10c1fc0ece67ab3e79ebacee362383`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _process_identity, os. Outputs/bindings: (none).
Calls/effect boundaries: _process_identity, os.getpid.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[1].value.values[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::acquire::root.body[17].body[3].body[1].value.values[7].args[0]::Call

Source: `infra/agentinfra/locks.py:220`; AST `ba1923643b161051a18bf7ae7386addd84146f4ab481f99d56712bc1ce97df2c`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os. Outputs/bindings: (none).
Calls/effect boundaries: os.getpid.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[1].value.values[7].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::acquire::root.body[17].body[3].body[1].value.values[8]::Call

Source: `infra/agentinfra/locks.py:221`; AST `4263cfe4ff762fbfb73db5540d6d421a621a7fb22318759bc79d367d143d5895`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: socket. Outputs/bindings: (none).
Calls/effect boundaries: socket.gethostname.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[1].value.values[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::acquire::root.body[17].body[3].body[1].value.values[9]::Call

Source: `infra/agentinfra/locks.py:222`; AST `a45c2ac57befcf1212794e7c42a7aad7870de2198eba961b8d2f47b37f928f0f`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _now. Outputs/bindings: (none).
Calls/effect boundaries: _now.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[1].value.values[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::acquire::root.body[17].body[3].body[2]::Assign

Source: `infra/agentinfra/locks.py:225`; AST `0222f1b0242766c14615e6ac27a9254241cd20621a56f0e96808feb0a0e17da5`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, payload. Outputs/bindings: raw.
Calls/effect boundaries: (json.dumps(payload, sort_keys=True) + '\n').encode, json.dumps.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::acquire::root.body[17].body[3].body[2].value::Call

Source: `infra/agentinfra/locks.py:225`; AST `ff245e9e4d63900ad30b62e7b418d3df7c3829ce5123ed1ff8e53ff5d12bf77a`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, payload. Outputs/bindings: (none).
Calls/effect boundaries: (json.dumps(payload, sort_keys=True) + '\n').encode, json.dumps.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::acquire::root.body[17].body[3].body[2].value.func.value.left::Call

Source: `infra/agentinfra/locks.py:225`; AST `aff17a1663bd39b6c1bf78d744b9f1d24b7f90351cafcdc991b594986626181d`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, payload. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[2].value.func.value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::acquire::root.body[17].body[3].body[3]::Try

Source: `infra/agentinfra/locks.py:226`; AST `3eaeed95eebd8e91b59fa2a798e9daff764d4077cca1f3938d9e9c54d1d28c3f`.

Rust module: `infra::agentinfra::locks`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: FileExistsError, LockError, exc, os, self. Outputs/bindings: fd.
Calls/effect boundaries: LockError, os.open, self.inspect.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Try evaluation at root.body[17].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::acquire::root.body[17].body[3].body[3].body[0]::Assign

Source: `infra/agentinfra/locks.py:227`; AST `623a1cb9352b380120722b40d66cf9efc077cc8ac0fa5738dd0a7c78221dc34e`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: os, self. Outputs/bindings: fd.
Calls/effect boundaries: os.open.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[3].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::acquire::root.body[17].body[3].body[3].body[0].value::Call

Source: `infra/agentinfra/locks.py:227`; AST `e002517ffd4d512df5d8859d522f0a3cfac8004a51c8e5e4bbe1fcdc6b4ab81d`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os, self. Outputs/bindings: (none).
Calls/effect boundaries: os.open.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::acquire::root.body[17].body[3].body[3].handlers[0]::ExceptHandler

Source: `infra/agentinfra/locks.py:228`; AST `5561339337dc27f162f81b8778c7a80549a567881cfbea2df71494d5d89ad9dd`.

Rust module: `infra::agentinfra::locks`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: FileExistsError, LockError, exc, self. Outputs/bindings: (none).
Calls/effect boundaries: LockError, self.inspect.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[17].body[3].body[3].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::acquire::root.body[17].body[3].body[3].handlers[0].body[0]::Raise

Source: `infra/agentinfra/locks.py:229`; AST `3485466fc58932b76a7889460f76d9bb398436517db84bcba0b3052767a5ce5d`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: LockError, exc, self. Outputs/bindings: (none).
Calls/effect boundaries: LockError, self.inspect.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[17].body[3].body[3].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::acquire::root.body[17].body[3].body[3].handlers[0].body[0].exc::Call

Source: `infra/agentinfra/locks.py:229`; AST `dd4b6578be4a44888c0b176ce4fc4471c1d681ce1fed596f4399d399a21c050f`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: LockError, self. Outputs/bindings: (none).
Calls/effect boundaries: LockError, self.inspect.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[3].handlers[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::acquire::root.body[17].body[3].body[3].handlers[0].body[0].exc.args[0].values[1].value::Call

Source: `infra/agentinfra/locks.py:229`; AST `2fbbe4645de7d7ecd0402e1fe2e444a18e99da2860dfdefba2385664d7001ac1`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.inspect.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[3].handlers[0].body[0].exc.args[0].values[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::acquire::root.body[17].body[3].body[4]::With

Source: `infra/agentinfra/locks.py:230`; AST `2aa5cbbacea276348620fe8119f1cc26ec57d08cb943ef8db91b3fd9bbb9fea3`.

Rust module: `infra::agentinfra::locks`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: fd, os, raw, stream. Outputs/bindings: stream.
Calls/effect boundaries: os.fdopen, os.fsync, stream.fileno, stream.flush, stream.write.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered With evaluation at root.body[17].body[3].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::acquire::root.body[17].body[3].body[4].items[0].context_expr::Call

Source: `infra/agentinfra/locks.py:230`; AST `58f2083f99f9d565afcbde03da3923bbe8eeeda611fed024de1825d26447d890`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fd, os. Outputs/bindings: (none).
Calls/effect boundaries: os.fdopen.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[4].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::acquire::root.body[17].body[3].body[4].body[0]::Expr

Source: `infra/agentinfra/locks.py:231`; AST `2a461a89089704220a95c27a0ec8d02f54d50aaa26621a54224617c29cb3fe5d`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: raw, stream. Outputs/bindings: (none).
Calls/effect boundaries: stream.write.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[3].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::acquire::root.body[17].body[3].body[4].body[0].value::Call

Source: `infra/agentinfra/locks.py:231`; AST `ac7ded157cc95907fd946e597f00bd804c0e13e7202765033649fc9007fe2fea`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: raw, stream. Outputs/bindings: (none).
Calls/effect boundaries: stream.write.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::acquire::root.body[17].body[3].body[4].body[1]::Expr

Source: `infra/agentinfra/locks.py:232`; AST `30712519db7cf7c545c522e94f0bbceb17159cd53838ebe3acb16ebc578916dd`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: stream. Outputs/bindings: (none).
Calls/effect boundaries: stream.flush.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[3].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::acquire::root.body[17].body[3].body[4].body[1].value::Call

Source: `infra/agentinfra/locks.py:232`; AST `dc9183626915285572f9f5f11a4c11f0386db10bee4db107d63c2469769b0631`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: stream. Outputs/bindings: (none).
Calls/effect boundaries: stream.flush.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::acquire::root.body[17].body[3].body[4].body[2]::Expr

Source: `infra/agentinfra/locks.py:233`; AST `eaf888e23cc61c107ec0d54a10f219382583f810784d2b5380deae2c363a1206`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: os, stream. Outputs/bindings: (none).
Calls/effect boundaries: os.fsync, stream.fileno.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[3].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::acquire::root.body[17].body[3].body[4].body[2].value::Call

Source: `infra/agentinfra/locks.py:233`; AST `29e1a002fb3ed92242523219b50a26133c0e15643b5dfd72168bc1eb4f1aed09`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os, stream. Outputs/bindings: (none).
Calls/effect boundaries: os.fsync, stream.fileno.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[4].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::acquire::root.body[17].body[3].body[4].body[2].value.args[0]::Call

Source: `infra/agentinfra/locks.py:233`; AST `27f47889b85ed2bb90d146b9008836c66d42f49c92f140cae1596cf4efe4d050`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: stream. Outputs/bindings: (none).
Calls/effect boundaries: stream.fileno.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[4].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::acquire::root.body[17].body[3].body[5]::Return

Source: `infra/agentinfra/locks.py:234`; AST `31199a657685d9bde25418544954175dd3a5199003555910823f3b7f1b07142e`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: payload. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Return evaluation at root.body[17].body[3].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::inspect::root.body[17].body[4]::FunctionDef

Source: `infra/agentinfra/locks.py:236`; AST `7fbbb115e6cb34f65a4488b98742da4dc242511bf836952cf36aad39346c92da`.

Rust module: `infra::agentinfra::locks`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Exception, FileNotFoundError, OSError, any, data, dict, exc, isinstance, json, key, max, required, self, str, time. Outputs/bindings: data, key, required.
Calls/effect boundaries: any, data.get, isinstance, json.loads, max, self.path.read_text, self.path.stat, str, time.time.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::inspect::root.body[17].body[4].body[0]::Try

Source: `infra/agentinfra/locks.py:237`; AST `707d22a26f7c1593073d4788437dc5e5700291ccd9fa0a300d995ff2cafca515`.

Rust module: `infra::agentinfra::locks`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: Exception, FileNotFoundError, exc, json, self, str. Outputs/bindings: data.
Calls/effect boundaries: json.loads, self.path.read_text, str.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Try evaluation at root.body[17].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::inspect::root.body[17].body[4].body[0].body[0]::Assign

Source: `infra/agentinfra/locks.py:238`; AST `537866d8a69dce44662a10218817fcecfb6a1dafbf579a9f1fa675bb6453b84a`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, self. Outputs/bindings: data.
Calls/effect boundaries: json.loads, self.path.read_text.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[4].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::inspect::root.body[17].body[4].body[0].body[0].value::Call

Source: `infra/agentinfra/locks.py:238`; AST `0821249bc5d520456a58c8bd759d33bc2795100268ab823b399b37e6440024f2`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, self. Outputs/bindings: (none).
Calls/effect boundaries: json.loads, self.path.read_text.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::inspect::root.body[17].body[4].body[0].body[0].value.args[0]::Call

Source: `infra/agentinfra/locks.py:238`; AST `f9fe252e092d67f80149821fa317f11a8793887293ededd32e981c87c392711c`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.read_text.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[0].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::inspect::root.body[17].body[4].body[0].handlers[0]::ExceptHandler

Source: `infra/agentinfra/locks.py:239`; AST `fa7ad1a3c52dd00b6e0686de362062e0eac9fe38a80e0e214992ccaf9f65746b`.

Rust module: `infra::agentinfra::locks`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: FileNotFoundError. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[17].body[4].body[0].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::inspect::root.body[17].body[4].body[0].handlers[0].body[0]::Return

Source: `infra/agentinfra/locks.py:240`; AST `eab80d6e76c04ede53120941fe0ce12178b01b5fe238c1f31f365b64aab5dd11`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Return evaluation at root.body[17].body[4].body[0].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::inspect::root.body[17].body[4].body[0].handlers[1]::ExceptHandler

Source: `infra/agentinfra/locks.py:241`; AST `e3c862d9bc93f22584ed47fc6aba2fe5ed63c088eb80dfde4dffd25a06efde56`.

Rust module: `infra::agentinfra::locks`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: Exception, exc, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[17].body[4].body[0].handlers[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::inspect::root.body[17].body[4].body[0].handlers[1].body[0]::Return

Source: `infra/agentinfra/locks.py:242`; AST `bfdc47d031d7b3d86b4f4f2ea684540e8241094d9cd47458b17ee8d7c3aaa42e`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: exc, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Return evaluation at root.body[17].body[4].body[0].handlers[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::inspect::root.body[17].body[4].body[0].handlers[1].body[0].value.values[2]::Call

Source: `infra/agentinfra/locks.py:242`; AST `ed91e0e2c4feb43ad37ba7941b4ee3c7dcc36d3eb80d4a170990c028aa16f027`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exc, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[0].handlers[1].body[0].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::inspect::root.body[17].body[4].body[1]::Assign

Source: `infra/agentinfra/locks.py:243`; AST `334465c43291432dcd429ea45be5947d23ceca2e437df31df38fd4d21ccd0dca`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: required.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::inspect::root.body[17].body[4].body[2]::If

Source: `infra/agentinfra/locks.py:244`; AST `432054f0139d7a671ac95c4f4385e363ee49b2ce969a015a65a4c4b2edbeb431`.

Rust module: `infra::agentinfra::locks`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: any, data, dict, isinstance, key, required, str. Outputs/bindings: key.
Calls/effect boundaries: any, data.get, isinstance.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered If evaluation at root.body[17].body[4].body[2]; no call, error or mutation may be omitted. Condition: not isinstance(data, dict) or any((not isinstance(data.get(key), str) or not data[key] for key in required))
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::inspect::root.body[17].body[4].body[2].test.values[0].operand::Call

Source: `infra/agentinfra/locks.py:244`; AST `5f3dfa3b23b16e077ee85aed20c0cc9933e4cb3a08ae821ef38b1086b65c69f5`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data, dict, isinstance. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[2].test.values[0].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::inspect::root.body[17].body[4].body[2].test.values[1]::Call

Source: `infra/agentinfra/locks.py:244`; AST `476b0982395354910df4b4a03fa357b6f6cec0603aab48bfc8fde40bda3783a1`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, data, isinstance, key, required, str. Outputs/bindings: key.
Calls/effect boundaries: any, data.get, isinstance.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[2].test.values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::inspect::root.body[17].body[4].body[2].test.values[1].args[0]::GeneratorExp

Source: `infra/agentinfra/locks.py:244`; AST `0e725536e77d5f9165323d825aacb3b0703c085ee327a53daa11094115c735d5`.

Rust module: `infra::agentinfra::locks`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: data, isinstance, key, required, str. Outputs/bindings: key.
Calls/effect boundaries: data.get, isinstance.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[17].body[4].body[2].test.values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::inspect::root.body[17].body[4].body[2].test.values[1].args[0].elt.values[0].operand::Call

Source: `infra/agentinfra/locks.py:244`; AST `f31854683382c9dd46070d02a0ebaa19b4509108879187ef063872ea9314b485`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data, isinstance, key, str. Outputs/bindings: (none).
Calls/effect boundaries: data.get, isinstance.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[2].test.values[1].args[0].elt.values[0].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::inspect::root.body[17].body[4].body[2].test.values[1].args[0].elt.values[0].operand.args[0]::Call

Source: `infra/agentinfra/locks.py:244`; AST `f6d38af0eae1210b65e2d04ac103d854ee923c0c8bfdcc1fdad74ed2b12fd42d`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data, key. Outputs/bindings: (none).
Calls/effect boundaries: data.get.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[2].test.values[1].args[0].elt.values[0].operand.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::inspect::root.body[17].body[4].body[2].body[0]::Return

Source: `infra/agentinfra/locks.py:245`; AST `517c45e7b34b8c1db91ea8d2ffb3695f14a5b720ec53b4a6a64710c85c276bd8`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Return evaluation at root.body[17].body[4].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::inspect::root.body[17].body[4].body[3]::Assign

Source: `infra/agentinfra/locks.py:246`; AST `f4187c8948196d02d6822cd20ce2b44831cbe2d30b5b00ebe4ace3d9e8f2d5ab`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: data. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::inspect::root.body[17].body[4].body[4]::Try

Source: `infra/agentinfra/locks.py:247`; AST `fb0c62cc9aea1ee56697962ed8e2e22aebe45cdc5debc4fe728bd85590ce68e9`.

Rust module: `infra::agentinfra::locks`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: OSError, data, max, self, time. Outputs/bindings: (none).
Calls/effect boundaries: max, self.path.stat, time.time.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Try evaluation at root.body[17].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::inspect::root.body[17].body[4].body[4].body[0]::Assign

Source: `infra/agentinfra/locks.py:248`; AST `f803e4b043a3ceb0d17790d72e4c5d141fab611179a1e389045afcfd97e9e087`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: data, max, self, time. Outputs/bindings: (none).
Calls/effect boundaries: max, self.path.stat, time.time.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[4].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::inspect::root.body[17].body[4].body[4].body[0].value::Call

Source: `infra/agentinfra/locks.py:248`; AST `146540ddb068f0c4d4197575e63b4961eb6edb2394b48538d2a5b600a8b3e146`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: max, self, time. Outputs/bindings: (none).
Calls/effect boundaries: max, self.path.stat, time.time.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::inspect::root.body[17].body[4].body[4].body[0].value.args[1].left::Call

Source: `infra/agentinfra/locks.py:248`; AST `bd39b5d643e5010141bcdbc0472d642c43f78408efe5a8a37b77a851078be1be`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: time. Outputs/bindings: (none).
Calls/effect boundaries: time.time.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[4].body[0].value.args[1].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::inspect::root.body[17].body[4].body[4].body[0].value.args[1].right.value::Call

Source: `infra/agentinfra/locks.py:248`; AST `3fc580e6a650bd3d3a3d89c2b66b934681f907a52aa28d74e3f10ec2cca2751a`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.stat.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[4].body[0].value.args[1].right.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::inspect::root.body[17].body[4].body[4].handlers[0]::ExceptHandler

Source: `infra/agentinfra/locks.py:249`; AST `80a311151e65e1bafda4060311f4ae294880f8bbd36b9aaceda28890d927c5db`.

Rust module: `infra::agentinfra::locks`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: OSError, data. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[17].body[4].body[4].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::inspect::root.body[17].body[4].body[4].handlers[0].body[0]::Assign

Source: `infra/agentinfra/locks.py:250`; AST `ed32b4c902fb3a0237ce3e7c430f4e5fe29aa4d7daf452f2176bdb9501978f26`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: data. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[4].body[4].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::inspect::root.body[17].body[4].body[5]::Return

Source: `infra/agentinfra/locks.py:251`; AST `a12e64fa3a041e609d3a25dc46c10c675ec5ec937a53909e14dc1d95d37a3c33`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: data. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Return evaluation at root.body[17].body[4].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::release::root.body[17].body[5]::FunctionDef

Source: `infra/agentinfra/locks.py:253`; AST `b50e249023504920fef64edc42d2c5fdcf519293577302381a31eb86378986fd`.

Rust module: `infra::agentinfra::locks`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: LockError, checks, expected, info, key, lease_id, owner_nonce, role, self, str, task_id. Outputs/bindings: checks, expected, info, key.
Calls/effect boundaries: LockError, checks.items, info.get, self.inspect, self.path.unlink.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::release::root.body[17].body[5].body[0]::Assign

Source: `infra/agentinfra/locks.py:261`; AST `1d59754ac091a6ee214aac9371cc173038673f91ac8a94e0c454082eb7ad1079`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: info.
Calls/effect boundaries: self.inspect.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::release::root.body[17].body[5].body[0].value::Call

Source: `infra/agentinfra/locks.py:261`; AST `2fbbe4645de7d7ecd0402e1fe2e444a18e99da2860dfdefba2385664d7001ac1`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.inspect.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::release::root.body[17].body[5].body[1]::If

Source: `infra/agentinfra/locks.py:262`; AST `43ceb32cc1ce621c615b4ca7797b1b72b5eafe256aaefd77196df9372746ffcd`.

Rust module: `infra::agentinfra::locks`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: LockError, info. Outputs/bindings: (none).
Calls/effect boundaries: LockError, info.get.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered If evaluation at root.body[17].body[5].body[1]; no call, error or mutation may be omitted. Condition: not info.get('exists')
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::release::root.body[17].body[5].body[1].test.operand::Call

Source: `infra/agentinfra/locks.py:262`; AST `e8931dad20df8ee78b06dedbbd189250617a028b70ff4355bd472db9215d4624`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: info. Outputs/bindings: (none).
Calls/effect boundaries: info.get.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[5].body[1].test.operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::release::root.body[17].body[5].body[1].body[0]::Raise

Source: `infra/agentinfra/locks.py:263`; AST `4fb178e884d4b836945bfbd316c13c01ded8028e54e6e2ba5e2719735b20538e`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: LockError. Outputs/bindings: (none).
Calls/effect boundaries: LockError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[17].body[5].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::release::root.body[17].body[5].body[1].body[0].exc::Call

Source: `infra/agentinfra/locks.py:263`; AST `fa07083f5303b5b2a1e8ca0b2e3d545483358c453d2b19fbbaa36489c9fb0d89`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: LockError. Outputs/bindings: (none).
Calls/effect boundaries: LockError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[5].body[1].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::release::root.body[17].body[5].body[2]::If

Source: `infra/agentinfra/locks.py:264`; AST `13db25a89ccb585ef66b286ffcdd52f00b5abdc4bf4f89bd3fe7ddf379f6e890`.

Rust module: `infra::agentinfra::locks`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: LockError, info. Outputs/bindings: (none).
Calls/effect boundaries: LockError, info.get.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered If evaluation at root.body[17].body[5].body[2]; no call, error or mutation may be omitted. Condition: info.get('corrupt')
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::release::root.body[17].body[5].body[2].test::Call

Source: `infra/agentinfra/locks.py:264`; AST `ad9f69baa4bf52ed19b18f4668adb65edeebd40b2696a7322a44e5b095d99c30`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: info. Outputs/bindings: (none).
Calls/effect boundaries: info.get.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[5].body[2].test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::release::root.body[17].body[5].body[2].body[0]::Raise

Source: `infra/agentinfra/locks.py:265`; AST `c5cdc070954e5dd7d6d8e14c34c1a4c8f2e5c32c147e987fab2b7e271cbc50bd`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: LockError. Outputs/bindings: (none).
Calls/effect boundaries: LockError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[17].body[5].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::release::root.body[17].body[5].body[2].body[0].exc::Call

Source: `infra/agentinfra/locks.py:265`; AST `c6ae6701a02946af8e7676909f4ac1dfc7bc2999dc0d46626534b5b2b09983f7`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: LockError. Outputs/bindings: (none).
Calls/effect boundaries: LockError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[5].body[2].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::release::root.body[17].body[5].body[3]::Assign

Source: `infra/agentinfra/locks.py:266`; AST `95544bfd288d3a5c8e00f3c4aafaba855da17ebefafc4a8c7ba8190e1871cf5e`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lease_id, owner_nonce, role, task_id. Outputs/bindings: checks.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[5].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::release::root.body[17].body[5].body[4]::For

Source: `infra/agentinfra/locks.py:272`; AST `f57d2b8b697f52efe59af0a09b29f3e46225b335b4124fc76784d77b9fd7aa4b`.

Rust module: `infra::agentinfra::locks`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: LockError, checks, expected, info, key. Outputs/bindings: expected, key.
Calls/effect boundaries: LockError, checks.items, info.get.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered For evaluation at root.body[17].body[5].body[4]; no call, error or mutation may be omitted. Iteration: (key, expected) in checks.items()
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::release::root.body[17].body[5].body[4].iter::Call

Source: `infra/agentinfra/locks.py:272`; AST `02f070cbe9d4daa17248e8647aadbcd70881a1d43f154fdcf64dc48278fa881e`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: checks. Outputs/bindings: (none).
Calls/effect boundaries: checks.items.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[5].body[4].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::release::root.body[17].body[5].body[4].body[0]::If

Source: `infra/agentinfra/locks.py:273`; AST `5bdcda48b2d35c347f38d4c93838b877701471a87145c72b9a035aacf3783e4b`.

Rust module: `infra::agentinfra::locks`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: LockError, expected, info, key. Outputs/bindings: (none).
Calls/effect boundaries: LockError, info.get.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered If evaluation at root.body[17].body[5].body[4].body[0]; no call, error or mutation may be omitted. Condition: expected is not None and info.get(key) != expected
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::release::root.body[17].body[5].body[4].body[0].test.values[1].left::Call

Source: `infra/agentinfra/locks.py:273`; AST `c650cae76d7bba257a1c960a9ed5140c1d3187847ae1ef74c14bf78a28169a39`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: info, key. Outputs/bindings: (none).
Calls/effect boundaries: info.get.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[5].body[4].body[0].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::release::root.body[17].body[5].body[4].body[0].body[0]::Raise

Source: `infra/agentinfra/locks.py:274`; AST `1b90577f11d334a6657f46363126f06f16da7be4345ea0a6a28318ab0e1aeb0f`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: LockError, key. Outputs/bindings: (none).
Calls/effect boundaries: LockError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[17].body[5].body[4].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::release::root.body[17].body[5].body[4].body[0].body[0].exc::Call

Source: `infra/agentinfra/locks.py:274`; AST `0b53bd9a0677acdecb62455b2feaccca97aae82e5680a62d1f6dd4a49c8c68e0`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: LockError, key. Outputs/bindings: (none).
Calls/effect boundaries: LockError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[5].body[4].body[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::release::root.body[17].body[5].body[5]::Expr

Source: `infra/agentinfra/locks.py:275`; AST `2eaaf0646f30797a74f5ad962af1b2c2d1159db247bb9e6a1ee6721b6520377e`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.unlink.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[5].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::release::root.body[17].body[5].body[5].value::Call

Source: `infra/agentinfra/locks.py:275`; AST `43f225d591630075cea5936de3ed0a36454310cb59f02d58caec2c978b9bb6ea`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.unlink.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[5].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::force_clear::root.body[17].body[6]::FunctionDef

Source: `infra/agentinfra/locks.py:277`; AST `550a38acd3124d6cb9a50eab20b14ae324b9bd5f34b6436967fd10d406af58c0`.

Rust module: `infra::agentinfra::locks`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: LockError, dict, expected_task_id, info, reason, self, str. Outputs/bindings: info.
Calls/effect boundaries: LockError, info.get, reason.strip, self.inspect, self.path.unlink.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::force_clear::root.body[17].body[6].body[0]::If

Source: `infra/agentinfra/locks.py:278`; AST `ee1b32365110d37731dcfb53f96836a29df3f7d3a409d4f946d4b0e32c07333c`.

Rust module: `infra::agentinfra::locks`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: LockError, reason. Outputs/bindings: (none).
Calls/effect boundaries: LockError, reason.strip.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered If evaluation at root.body[17].body[6].body[0]; no call, error or mutation may be omitted. Condition: not reason.strip()
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::force_clear::root.body[17].body[6].body[0].test.operand::Call

Source: `infra/agentinfra/locks.py:278`; AST `ef6f35fc4ea4552c79415f7496891492d7a89447aea719304467be59ab3987dc`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: reason. Outputs/bindings: (none).
Calls/effect boundaries: reason.strip.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].body[0].test.operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::force_clear::root.body[17].body[6].body[0].body[0]::Raise

Source: `infra/agentinfra/locks.py:279`; AST `0a5e1f42a51223404ec2e7274234687f3e706274a8d9a9d8953c255b954ca3ec`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: LockError. Outputs/bindings: (none).
Calls/effect boundaries: LockError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[17].body[6].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::force_clear::root.body[17].body[6].body[0].body[0].exc::Call

Source: `infra/agentinfra/locks.py:279`; AST `39c84e6e51183cf641ff400bf5a0b51b9b83b839eb6aaccb846fd3a8bec46361`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: LockError. Outputs/bindings: (none).
Calls/effect boundaries: LockError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].body[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::force_clear::root.body[17].body[6].body[1]::Assign

Source: `infra/agentinfra/locks.py:280`; AST `1d59754ac091a6ee214aac9371cc173038673f91ac8a94e0c454082eb7ad1079`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: info.
Calls/effect boundaries: self.inspect.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::force_clear::root.body[17].body[6].body[1].value::Call

Source: `infra/agentinfra/locks.py:280`; AST `2fbbe4645de7d7ecd0402e1fe2e444a18e99da2860dfdefba2385664d7001ac1`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.inspect.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::force_clear::root.body[17].body[6].body[2]::If

Source: `infra/agentinfra/locks.py:281`; AST `8b937a5e6354788473877961ba8137282a3f85bd1fe880ebd4b6ddd1cd2c614e`.

Rust module: `infra::agentinfra::locks`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: info. Outputs/bindings: (none).
Calls/effect boundaries: info.get.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered If evaluation at root.body[17].body[6].body[2]; no call, error or mutation may be omitted. Condition: not info.get('exists')
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::force_clear::root.body[17].body[6].body[2].test.operand::Call

Source: `infra/agentinfra/locks.py:281`; AST `e8931dad20df8ee78b06dedbbd189250617a028b70ff4355bd472db9215d4624`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: info. Outputs/bindings: (none).
Calls/effect boundaries: info.get.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].body[2].test.operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::force_clear::root.body[17].body[6].body[2].body[0]::Return

Source: `infra/agentinfra/locks.py:282`; AST `a861adaef16964fecf1801cc58d4bf7bc461aeedab415da146c04d8d7225d3c8`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: info. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Return evaluation at root.body[17].body[6].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::force_clear::root.body[17].body[6].body[3]::If

Source: `infra/agentinfra/locks.py:283`; AST `cc158862d32ae81d3bc1201eb4a18abb143f53a3c3651e4b510f6fdbe2c590a8`.

Rust module: `infra::agentinfra::locks`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: LockError, info. Outputs/bindings: (none).
Calls/effect boundaries: LockError, info.get.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered If evaluation at root.body[17].body[6].body[3]; no call, error or mutation may be omitted. Condition: info.get('corrupt')
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::force_clear::root.body[17].body[6].body[3].test::Call

Source: `infra/agentinfra/locks.py:283`; AST `ad9f69baa4bf52ed19b18f4668adb65edeebd40b2696a7322a44e5b095d99c30`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: info. Outputs/bindings: (none).
Calls/effect boundaries: info.get.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].body[3].test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::force_clear::root.body[17].body[6].body[3].body[0]::Raise

Source: `infra/agentinfra/locks.py:284`; AST `d4e7d9b59eaa113cfa22d1bb75c6d5cecd1f09e05ef8f68e8563b14af5a37ba6`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: LockError. Outputs/bindings: (none).
Calls/effect boundaries: LockError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[17].body[6].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::force_clear::root.body[17].body[6].body[3].body[0].exc::Call

Source: `infra/agentinfra/locks.py:284`; AST `15e5e419d2dac0139f09bde27f91e28ff10ecc9c6a6c4e6bcb8dc9d59b9dfada`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: LockError. Outputs/bindings: (none).
Calls/effect boundaries: LockError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].body[3].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::force_clear::root.body[17].body[6].body[4]::If

Source: `infra/agentinfra/locks.py:285`; AST `a1d2d564cf8301f3bfe4c1731a79df218fd3a83ec8e89872dfef0d882b7365ea`.

Rust module: `infra::agentinfra::locks`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: LockError, expected_task_id, info. Outputs/bindings: (none).
Calls/effect boundaries: LockError, info.get.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered If evaluation at root.body[17].body[6].body[4]; no call, error or mutation may be omitted. Condition: expected_task_id is not None and info.get('task_id') != expected_task_id
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::force_clear::root.body[17].body[6].body[4].test.values[1].left::Call

Source: `infra/agentinfra/locks.py:285`; AST `679a11f13949e84cfc0422b47859c73b42af25509676fecbf15dae51e1ad4a18`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: info. Outputs/bindings: (none).
Calls/effect boundaries: info.get.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].body[4].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::force_clear::root.body[17].body[6].body[4].body[0]::Raise

Source: `infra/agentinfra/locks.py:286`; AST `53d5058e83e00ba6f39938ed2f563151a73ccb36b4f179c917c3fd4e97fab7a8`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: LockError. Outputs/bindings: (none).
Calls/effect boundaries: LockError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[17].body[6].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::force_clear::root.body[17].body[6].body[4].body[0].exc::Call

Source: `infra/agentinfra/locks.py:286`; AST `eab521c6db5917295323317c0c4e36c6dc15865fcfe89da63e319c13ac70e164`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: LockError. Outputs/bindings: (none).
Calls/effect boundaries: LockError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].body[4].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::force_clear::root.body[17].body[6].body[5]::Expr

Source: `infra/agentinfra/locks.py:287`; AST `2eaaf0646f30797a74f5ad962af1b2c2d1159db247bb9e6a1ee6721b6520377e`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.unlink.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[6].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::force_clear::root.body[17].body[6].body[5].value::Call

Source: `infra/agentinfra/locks.py:287`; AST `43f225d591630075cea5936de3ed0a36454310cb59f02d58caec2c978b9bb6ea`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.unlink.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::force_clear::root.body[17].body[6].body[6]::Return

Source: `infra/agentinfra/locks.py:288`; AST `a861adaef16964fecf1801cc58d4bf7bc461aeedab415da146c04d8d7225d3c8`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: info. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Return evaluation at root.body[17].body[6].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::restore::root.body[17].body[7]::FunctionDef

Source: `infra/agentinfra/locks.py:290`; AST `d2c20f950ebc1f6c6efdfaac19b7cf15a61c26341fce9e3f65e28c28efeeb171`.

Rust module: `infra::agentinfra::locks`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileExistsError, LockError, dict, exc, fd, isinstance, json, key, os, payload, raw, required, self, set, stream, value. Outputs/bindings: fd, key, raw, required, stream, value.
Calls/effect boundaries: (json.dumps({key: value for key, value in payload.items() if key not in {'exists', 'age_seconds'}}, sort_keys=True) + '\n').encode, LockError, isinstance, json.dumps, os.fdopen, os.fsync, os.open, payload.get, payload.items, self.path.parent.mkdir, set, stream.fileno, stream.flush, stream.write.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::restore::root.body[17].body[7].body[0]::Expr

Source: `infra/agentinfra/locks.py:291`; AST `fa66355f0c31ed9b5bed1259ac10346001e2e748ad790105b3ac0d64c91a6652`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::restore::root.body[17].body[7].body[1]::Assign

Source: `infra/agentinfra/locks.py:296`; AST `54883c65898f8683593e7060e0718275de06bf15d0d8adcdccf00f81e783736f`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: required.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[7].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::restore::root.body[17].body[7].body[2]::If

Source: `infra/agentinfra/locks.py:297`; AST `5d6d6a84e1f39ce94696173ef4ea0c33348fd066ee63403559580f818b698ae2`.

Rust module: `infra::agentinfra::locks`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: LockError, dict, isinstance, payload, required, set. Outputs/bindings: (none).
Calls/effect boundaries: LockError, isinstance, payload.get, set.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered If evaluation at root.body[17].body[7].body[2]; no call, error or mutation may be omitted. Condition: not isinstance(payload, dict) or payload.get('schema') != 2 or (not required <= set(payload))
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::restore::root.body[17].body[7].body[2].test.values[0].operand::Call

Source: `infra/agentinfra/locks.py:297`; AST `73cc006a0bc4955016bf69609a5e7cace6b92c6f2821c614c5464801fe674ef2`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, isinstance, payload. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[2].test.values[0].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::restore::root.body[17].body[7].body[2].test.values[1].left::Call

Source: `infra/agentinfra/locks.py:297`; AST `3467da07a54d9cde826fd53c6c9795cf91848557abe35d9e6707a6c5a6855286`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: payload. Outputs/bindings: (none).
Calls/effect boundaries: payload.get.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[2].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::restore::root.body[17].body[7].body[2].test.values[2].operand.comparators[0]::Call

Source: `infra/agentinfra/locks.py:297`; AST `e10c6f00551bd05d72a32f330bfb9969dba805f792ed5dd616982882448962e7`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: payload, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[2].test.values[2].operand.comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::restore::root.body[17].body[7].body[2].body[0]::Raise

Source: `infra/agentinfra/locks.py:298`; AST `1ce2ede0ba3ebadc1899386c23c77b0b5648832d41fc2da665eea5e6780864c0`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: LockError. Outputs/bindings: (none).
Calls/effect boundaries: LockError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[17].body[7].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::restore::root.body[17].body[7].body[2].body[0].exc::Call

Source: `infra/agentinfra/locks.py:298`; AST `02ed3c582e91d7b78cd3aa5e38058e01d4b305ff77ba57d4469d3989c0cba823`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: LockError. Outputs/bindings: (none).
Calls/effect boundaries: LockError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[2].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::restore::root.body[17].body[7].body[3]::If

Source: `infra/agentinfra/locks.py:299`; AST `610b0834020d7f67ab886da5e073424774d24486cb7444b3a66a89ff0ea3b9cb`.

Rust module: `infra::agentinfra::locks`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: LockError, payload, self. Outputs/bindings: (none).
Calls/effect boundaries: LockError, payload.get.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered If evaluation at root.body[17].body[7].body[3]; no call, error or mutation may be omitted. Condition: payload.get('purpose') != self.purpose
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::restore::root.body[17].body[7].body[3].test.left::Call

Source: `infra/agentinfra/locks.py:299`; AST `783078533901a47615cc8d3b33b7fc4ad6f83d8f4c3673e4965ec6b730f78e2b`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: payload. Outputs/bindings: (none).
Calls/effect boundaries: payload.get.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[3].test.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::restore::root.body[17].body[7].body[3].body[0]::Raise

Source: `infra/agentinfra/locks.py:300`; AST `f928695553a8fdb6460359c0cb6c59c0bf261918020a822f4fd4f77d112e4440`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: LockError. Outputs/bindings: (none).
Calls/effect boundaries: LockError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[17].body[7].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::restore::root.body[17].body[7].body[3].body[0].exc::Call

Source: `infra/agentinfra/locks.py:300`; AST `39131fc21165a7c5a01c92ce5776285ea641d82b6aa4f03ad02c82381bf33a95`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: LockError. Outputs/bindings: (none).
Calls/effect boundaries: LockError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[3].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::restore::root.body[17].body[7].body[4]::Expr

Source: `infra/agentinfra/locks.py:301`; AST `0d74d9688ae835d21ca73b92559370108c358f58471257ab965a3e0953c45c11`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.parent.mkdir.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[7].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::restore::root.body[17].body[7].body[4].value::Call

Source: `infra/agentinfra/locks.py:301`; AST `02b3b5924f8cfb1ea300dcb615b348adaef01080a21462fa884d7a5bf5539cb2`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.parent.mkdir.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::restore::root.body[17].body[7].body[5]::Assign

Source: `infra/agentinfra/locks.py:302`; AST `999869b77edb67e109d9daa5b64288b49c7c3ce9773ba954944842c87b56be3a`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, key, payload, value. Outputs/bindings: key, raw, value.
Calls/effect boundaries: (json.dumps({key: value for key, value in payload.items() if key not in {'exists', 'age_seconds'}}, sort_keys=True) + '\n').encode, json.dumps, payload.items.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[7].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::restore::root.body[17].body[7].body[5].value::Call

Source: `infra/agentinfra/locks.py:302`; AST `279311383c4df34931e731347b337870f41de2d06f09a719f59183c20163cd4e`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, key, payload, value. Outputs/bindings: key, value.
Calls/effect boundaries: (json.dumps({key: value for key, value in payload.items() if key not in {'exists', 'age_seconds'}}, sort_keys=True) + '\n').encode, json.dumps, payload.items.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::restore::root.body[17].body[7].body[5].value.func.value.left::Call

Source: `infra/agentinfra/locks.py:302`; AST `2b18ed7c5f7d0f5c6e435263b5e5a663c1223faf5d9d7888bfb926149123a47f`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, key, payload, value. Outputs/bindings: key, value.
Calls/effect boundaries: json.dumps, payload.items.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[5].value.func.value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::restore::root.body[17].body[7].body[5].value.func.value.left.args[0]::DictComp

Source: `infra/agentinfra/locks.py:302`; AST `7805ba82c342a1201c06a5224245e93612baad15efb92498d9c42fbb5c2dbf0a`.

Rust module: `infra::agentinfra::locks`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: key, payload, value. Outputs/bindings: key, value.
Calls/effect boundaries: payload.items.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered DictComp evaluation at root.body[17].body[7].body[5].value.func.value.left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::restore::root.body[17].body[7].body[5].value.func.value.left.args[0].generators[0].iter::Call

Source: `infra/agentinfra/locks.py:302`; AST `8d50802794fc04b6540ec47aa903b37ffec52d5fda0f09f9ccc31de12872f8a5`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: payload. Outputs/bindings: (none).
Calls/effect boundaries: payload.items.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[5].value.func.value.left.args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::restore::root.body[17].body[7].body[6]::Try

Source: `infra/agentinfra/locks.py:303`; AST `7384cb8f6f3c9b15e44a700a2d9c46217db08e544a52a0e6fe49c523bab57629`.

Rust module: `infra::agentinfra::locks`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: FileExistsError, LockError, exc, os, self. Outputs/bindings: fd.
Calls/effect boundaries: LockError, os.open.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Try evaluation at root.body[17].body[7].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::restore::root.body[17].body[7].body[6].body[0]::Assign

Source: `infra/agentinfra/locks.py:304`; AST `623a1cb9352b380120722b40d66cf9efc077cc8ac0fa5738dd0a7c78221dc34e`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: os, self. Outputs/bindings: fd.
Calls/effect boundaries: os.open.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[7].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::restore::root.body[17].body[7].body[6].body[0].value::Call

Source: `infra/agentinfra/locks.py:304`; AST `e002517ffd4d512df5d8859d522f0a3cfac8004a51c8e5e4bbe1fcdc6b4ab81d`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os, self. Outputs/bindings: (none).
Calls/effect boundaries: os.open.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::restore::root.body[17].body[7].body[6].handlers[0]::ExceptHandler

Source: `infra/agentinfra/locks.py:305`; AST `5bcfbf43a0e0bd2df7e82ade471b317a5f48faf49ea2057190e7bf3a443d2959`.

Rust module: `infra::agentinfra::locks`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: FileExistsError, LockError, exc. Outputs/bindings: (none).
Calls/effect boundaries: LockError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[17].body[7].body[6].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::restore::root.body[17].body[7].body[6].handlers[0].body[0]::Raise

Source: `infra/agentinfra/locks.py:306`; AST `8fe0da3f809f984975212d3560d6d5f5c418635d337af2c4e7ad910bcfcf8c23`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: LockError, exc. Outputs/bindings: (none).
Calls/effect boundaries: LockError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[17].body[7].body[6].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::restore::root.body[17].body[7].body[6].handlers[0].body[0].exc::Call

Source: `infra/agentinfra/locks.py:306`; AST `1cb97e241589f2874fcfad276611e50d933096f950449d69cf193e2192ef5158`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: LockError. Outputs/bindings: (none).
Calls/effect boundaries: LockError.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[6].handlers[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::restore::root.body[17].body[7].body[7]::With

Source: `infra/agentinfra/locks.py:307`; AST `2aa5cbbacea276348620fe8119f1cc26ec57d08cb943ef8db91b3fd9bbb9fea3`.

Rust module: `infra::agentinfra::locks`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: fd, os, raw, stream. Outputs/bindings: stream.
Calls/effect boundaries: os.fdopen, os.fsync, stream.fileno, stream.flush, stream.write.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered With evaluation at root.body[17].body[7].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::restore::root.body[17].body[7].body[7].items[0].context_expr::Call

Source: `infra/agentinfra/locks.py:307`; AST `58f2083f99f9d565afcbde03da3923bbe8eeeda611fed024de1825d26447d890`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fd, os. Outputs/bindings: (none).
Calls/effect boundaries: os.fdopen.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[7].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::restore::root.body[17].body[7].body[7].body[0]::Expr

Source: `infra/agentinfra/locks.py:308`; AST `2a461a89089704220a95c27a0ec8d02f54d50aaa26621a54224617c29cb3fe5d`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: raw, stream. Outputs/bindings: (none).
Calls/effect boundaries: stream.write.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[7].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::restore::root.body[17].body[7].body[7].body[0].value::Call

Source: `infra/agentinfra/locks.py:308`; AST `ac7ded157cc95907fd946e597f00bd804c0e13e7202765033649fc9007fe2fea`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: raw, stream. Outputs/bindings: (none).
Calls/effect boundaries: stream.write.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::restore::root.body[17].body[7].body[7].body[1]::Expr

Source: `infra/agentinfra/locks.py:309`; AST `30712519db7cf7c545c522e94f0bbceb17159cd53838ebe3acb16ebc578916dd`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: stream. Outputs/bindings: (none).
Calls/effect boundaries: stream.flush.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[7].body[7].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::restore::root.body[17].body[7].body[7].body[1].value::Call

Source: `infra/agentinfra/locks.py:309`; AST `dc9183626915285572f9f5f11a4c11f0386db10bee4db107d63c2469769b0631`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: stream. Outputs/bindings: (none).
Calls/effect boundaries: stream.flush.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[7].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::restore::root.body[17].body[7].body[7].body[2]::Expr

Source: `infra/agentinfra/locks.py:310`; AST `eaf888e23cc61c107ec0d54a10f219382583f810784d2b5380deae2c363a1206`.

Rust module: `infra::agentinfra::locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: os, stream. Outputs/bindings: (none).
Calls/effect boundaries: os.fsync, stream.fileno.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[7].body[7].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::restore::root.body[17].body[7].body[7].body[2].value::Call

Source: `infra/agentinfra/locks.py:310`; AST `29e1a002fb3ed92242523219b50a26133c0e15643b5dfd72168bc1eb4f1aed09`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os, stream. Outputs/bindings: (none).
Calls/effect boundaries: os.fsync, stream.fileno.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[7].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/locks.py::module::LeaseLock::restore::root.body[17].body[7].body[7].body[2].value.args[0]::Call

Source: `infra/agentinfra/locks.py:310`; AST `27f47889b85ed2bb90d146b9008836c66d42f49c92f140cae1596cf4efe4d050`.

Rust module: `infra::agentinfra::locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: stream. Outputs/bindings: (none).
Calls/effect boundaries: stream.fileno.
Dependencies: __future__, atomic, ctypes, ctypes.wintypes, dataclasses, datetime, json, os, pathlib, socket, time, uuid.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[7].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
