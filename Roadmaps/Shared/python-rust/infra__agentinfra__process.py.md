# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 315. Inventory digest: `83307f2d5999ec44d34fd599c5d91fb57a306a739ba42ca7db6dd42528da9b4c`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/process.py::module::root::Module

Source: `infra/agentinfra/process.py:1`; AST `a3114b2f91ba5ea1a070c6d36a2ab5f664d5c698213d5e8ea6e60ee38d506b57`.

Rust module: `infra::agentinfra::process`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: BaseException, Callable, ContextVar, Iterable, Mapping, Path, ProcessLookupError, ProcessResult, RuntimeError, ValueError, _Capture, _IO_COUNTERS, _JOBOBJECT_BASIC_LIMIT_INFORMATION, _JOBOBJECT_EXTENDED_LIMIT_INFORMATION, _assign_kill_job, _close_job, _kill_tree, _process_observer, _recipe_group, all, archive, argv, bool, bytearray, bytes, callback, capture_limit, child_env, chunk, command, contextmanager, ctypes, cwd, dataclass, datetime, defaults, env, exc, fd, finished, flags, float, group, hashlib, info, inherited_group, int, isinstance, isolated_directory, isolated_home, item, job, kernel, key, len, limit, logs, minimal_subprocess_env, observer, os, output, output_directory, proc, redact_text, result, run_process, self, signal, started, started_wall, stderr_capture, stderr_path, stderr_thread, stdout_capture, stdout_path, stdout_thread, str, stream, subprocess, tempfile, threading, time, timed_out, timeout, timezone, token, tuple, uuid, value. Outputs/bindings: _fields_, _process_observer, _recipe_group, argv, child_env, chunk, command, cwd, defaults, duration_seconds, fd, finished, finished_at, flags, info, inherited_group, isolated_directory, isolated_home, item, job, kernel, key, logs, observer, output, proc, result, returncode, started, started_at, started_wall, stderr, stderr_bytes, stderr_capture, stderr_path, stderr_sha256, stderr_thread, stderr_truncated, stdout, stdout_bytes, stdout_capture, stdout_path, stdout_sha256, stdout_thread, stdout_truncated, timed_out, token, value.
Calls/effect boundaries: ContextVar, Path, Path(child_env[key]).mkdir, ProcessResult, RuntimeError, ValueError, _Capture, _JOBOBJECT_EXTENDED_LIMIT_INFORMATION, _assign_kill_job, _close_job, _kill_tree, _process_observer.get, _process_observer.reset, _process_observer.set, _recipe_group.get, _recipe_group.reset, _recipe_group.set, all, bytearray, bytes, bytes(self.buffer).decode, child_env.setdefault, ctypes.byref, ctypes.sizeof, ctypes.windll.kernel32.CloseHandle, ctypes.windll.kernel32.TerminateJobObject, ctypes.wintypes.HANDLE, cwd.resolve, dataclass, datetime.now, datetime.now(timezone.utc).isoformat, defaults.items, float, hashlib.sha256, int, isinstance, kernel.AssignProcessToJobObject, kernel.CloseHandle, kernel.CreateJobObjectW, kernel.SetInformationJobObject, len, minimal_subprocess_env, observer, os.fdopen, os.getpgrp, os.getpid, os.getsid, os.killpg, os.open, output.close, output.write, output_directory.mkdir, proc.kill, proc.poll, proc.stderr.close, proc.stdout.close, proc.wait, redact_text, run_process, self.buffer.extend, self.digest.update, stderr_capture.digest.hexdigest, stderr_capture.text, stderr_path.resolve, stderr_thread.is_alive, stderr_thread.join, stderr_thread.start, stdout_capture.digest.hexdigest, stdout_capture.text, stdout_path.resolve, stdout_thread.is_alive, stdout_thread.join, stdout_thread.start, str, stream.read, subprocess.Popen, subprocess.run, tempfile.TemporaryDirectory, threading.Thread, time.monotonic, tuple, uuid.uuid4.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::root.body[0]::ImportFrom

Source: `infra/agentinfra/process.py:1`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::root.body[1]::ImportFrom

Source: `infra/agentinfra/process.py:3`; AST `321ed2ed3afceb74be547c9905ed4c676e453b1a68fe7cb2d3e214caeac2624d`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::root.body[2]::ImportFrom

Source: `infra/agentinfra/process.py:4`; AST `a510406c1fa6f159ec004f4ead0d836747696bf4154e0a5daee8abdfbd9829f0`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::root.body[3]::ImportFrom

Source: `infra/agentinfra/process.py:5`; AST `6588e8300f9de11fc19a7338e73f5cba5e5264abe31bdc98aaca6ec078376a63`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::root.body[4]::ImportFrom

Source: `infra/agentinfra/process.py:6`; AST `85598e37ba96d6e396880fbaf8f1a487d6502e6df91ce2ca25c05c876437624e`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::root.body[5]::Import

Source: `infra/agentinfra/process.py:7`; AST `092cb77ae0770f1627b29bf41b2732722fbcc3a0e1d77a79674801800a2721d1`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Import evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::root.body[6]::Import

Source: `infra/agentinfra/process.py:8`; AST `669c8db7bfb9b4e64a7aa5f9239cbd229a5c460f228936e83d225f5ab2176b82`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Import evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::root.body[7]::Import

Source: `infra/agentinfra/process.py:9`; AST `af79723a2fd651a13b42afa080047e330560d43086896ca3ca7155f31b096dc9`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Import evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::root.body[8]::Import

Source: `infra/agentinfra/process.py:10`; AST `ac3a74d6dd975a8e8fe4b7f85fce794793a9355595b850e3926964913948d386`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Import evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::root.body[9]::Import

Source: `infra/agentinfra/process.py:11`; AST `3cf2982d679537eedcb8aba5fc8ee366c6a4d23113e31f436f7107ab2cbcf537`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Import evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::root.body[10]::Import

Source: `infra/agentinfra/process.py:12`; AST `9d97d469cf8d66465563e1e22c6dab3b6107819aba2d9956c7080016c1ab9c1b`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Import evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::root.body[11]::Import

Source: `infra/agentinfra/process.py:13`; AST `81dafa7a7cf16b83e7a7cafd7a6702e15f4b4d576a43463dc14beb05d48e72d0`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Import evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::root.body[12]::Import

Source: `infra/agentinfra/process.py:14`; AST `80f21c52b46d18d972ae93db225486a900db10799e9bdba98d07dbcc819ff502`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Import evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::root.body[13]::Import

Source: `infra/agentinfra/process.py:15`; AST `ff05bad0fd9a7212d3cd85fd2726055168be21bc8f6e0d93b29965794b0675d4`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Import evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::root.body[14]::Import

Source: `infra/agentinfra/process.py:16`; AST `db14cae1a81ee06a1930fa9f46771b454957916d2bbbc048661adf0613fd70de`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Import evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::root.body[15]::ImportFrom

Source: `infra/agentinfra/process.py:17`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::root.body[16]::ImportFrom

Source: `infra/agentinfra/process.py:18`; AST `89385005d52c520f1564e4742f6a7f8aba51da0390e1ad6658e70eb4b6a5be91`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[16]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::root.body[17]::ImportFrom

Source: `infra/agentinfra/process.py:20`; AST `5a851b3e4ab28d1c33118b888257b405dd62da088e073a2cdfa94405fb50ed5d`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered ImportFrom evaluation at root.body[17]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::root.body[18]::Assign

Source: `infra/agentinfra/process.py:23`; AST `1300d954dcb85e77d5f2a6aa5c2327f6cdefcda99432f91d98b2dae1768e1766`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ContextVar. Outputs/bindings: _process_observer.
Calls/effect boundaries: ContextVar.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[18]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::root.body[18].value::Call

Source: `infra/agentinfra/process.py:23`; AST `d4274fe4f9e9242bf529e145d2c47fabf3002cc62e31a5321c1c6622f7f03412`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContextVar. Outputs/bindings: (none).
Calls/effect boundaries: ContextVar.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[18].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::root.body[19]::Assign

Source: `infra/agentinfra/process.py:24`; AST `f6f1dc0956fd5514472463236a4cefbfb900265760c104c95858afe1a0f309ef`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ContextVar. Outputs/bindings: _recipe_group.
Calls/effect boundaries: ContextVar.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[19]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::root.body[19].value::Call

Source: `infra/agentinfra/process.py:24`; AST `71730a0d9cd7dbe999e01c11da280aaf10147ebc8f8d22881df978ae2a16793d`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContextVar. Outputs/bindings: (none).
Calls/effect boundaries: ContextVar.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[19].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::observe_process::root.body[20]::FunctionDef

Source: `infra/agentinfra/process.py:28`; AST `6fd718422474704798e01739370bf87833e46dd6e4f9214aa025346176e822f6`.

Rust module: `infra::agentinfra::process`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Callable, _process_observer, callback, contextmanager, subprocess, token. Outputs/bindings: token.
Calls/effect boundaries: _process_observer.reset, _process_observer.set.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[20]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::observe_process::root.body[20].body[0]::Expr

Source: `infra/agentinfra/process.py:29`; AST `6796eb48664a9824825e845d2df7b3f0cf5236412c4b778eea0cb2c74d7e351b`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::observe_process::root.body[20].body[1]::Assign

Source: `infra/agentinfra/process.py:30`; AST `0f254af66c1ec564079d426f4071786e8eb78e72132d3daf484ca7ab60855892`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _process_observer, callback. Outputs/bindings: token.
Calls/effect boundaries: _process_observer.set.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[20].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::observe_process::root.body[20].body[1].value::Call

Source: `infra/agentinfra/process.py:30`; AST `b37c40c76a3c055a0f87275cf0540139ccf09e6f5227bc6804b441b9c6b97b45`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _process_observer, callback. Outputs/bindings: (none).
Calls/effect boundaries: _process_observer.set.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[20].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::observe_process::root.body[20].body[2]::Try

Source: `infra/agentinfra/process.py:31`; AST `5eabf99859234ddee12d9633a7ea77e2f7233c327048747c5b11a8c526ddaa24`.

Rust module: `infra::agentinfra::process`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: _process_observer, token. Outputs/bindings: (none).
Calls/effect boundaries: _process_observer.reset.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Try evaluation at root.body[20].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::observe_process::root.body[20].body[2].body[0]::Expr

Source: `infra/agentinfra/process.py:32`; AST `4ef85b91bd2f837cbb619428370c77b4e8f23faa1461fa93120d8bde06a4c480`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::observe_process::root.body[20].body[2].finalbody[0]::Expr

Source: `infra/agentinfra/process.py:34`; AST `cdf41bb2dbe2fc01bf3653abfad2dfcd94436e251dbcaafaa3f271e9a0885a93`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _process_observer, token. Outputs/bindings: (none).
Calls/effect boundaries: _process_observer.reset.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[2].finalbody[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::observe_process::root.body[20].body[2].finalbody[0].value::Call

Source: `infra/agentinfra/process.py:34`; AST `5be18551dfdee442ca99eeaf642c5870696b44bdc8cd6a02430105bcef78eb6b`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _process_observer, token. Outputs/bindings: (none).
Calls/effect boundaries: _process_observer.reset.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[20].body[2].finalbody[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::root.body[21]::If

Source: `infra/agentinfra/process.py:37`; AST `ae68a12e8e034836c1e3d1dfb379d277e5c39dc781ce9fa68a8a6bb72fba768d`.

Rust module: `infra::agentinfra::process`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: _IO_COUNTERS, _JOBOBJECT_BASIC_LIMIT_INFORMATION, ctypes, os. Outputs/bindings: _fields_.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[21]; no call, error or mutation may be omitted. Condition: os.name == 'nt'
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_IO_COUNTERS::root.body[21].body[0]::ClassDef

Source: `infra/agentinfra/process.py:38`; AST `ddd6e607ba1af39c949bbc4a27b2da2bd7a766f35a2da7429395715ab21fc470`.

Rust module: `infra::agentinfra::process`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: ctypes. Outputs/bindings: _fields_.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered ClassDef evaluation at root.body[21].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_IO_COUNTERS::root.body[21].body[0].body[0]::Assign

Source: `infra/agentinfra/process.py:39`; AST `b75ef57640aeda99876d1bd3db69970399c83bc7bf03700ee30fa6af4ef43004`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ctypes. Outputs/bindings: _fields_.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_JOBOBJECT_BASIC_LIMIT_INFORMATION::root.body[21].body[1]::ClassDef

Source: `infra/agentinfra/process.py:49`; AST `43d420daac916d6db00af260f42c62efb9aa560cfa206fe656d0584d743f594e`.

Rust module: `infra::agentinfra::process`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: ctypes. Outputs/bindings: _fields_.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered ClassDef evaluation at root.body[21].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_JOBOBJECT_BASIC_LIMIT_INFORMATION::root.body[21].body[1].body[0]::Assign

Source: `infra/agentinfra/process.py:50`; AST `b1887ff83d8500d63a54843139e6c0451d7b1e5325aec67b14eaf78c93653265`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ctypes. Outputs/bindings: _fields_.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_JOBOBJECT_EXTENDED_LIMIT_INFORMATION::root.body[21].body[2]::ClassDef

Source: `infra/agentinfra/process.py:63`; AST `59f7c0e514a720c825a6fd185a0b32a7a91e5ea8b900ea206c042b0f752407ba`.

Rust module: `infra::agentinfra::process`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: _IO_COUNTERS, _JOBOBJECT_BASIC_LIMIT_INFORMATION, ctypes. Outputs/bindings: _fields_.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered ClassDef evaluation at root.body[21].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_JOBOBJECT_EXTENDED_LIMIT_INFORMATION::root.body[21].body[2].body[0]::Assign

Source: `infra/agentinfra/process.py:64`; AST `c04f6beb765618bf9d7b891eb54f1d32ad55cd16d1daa3015189dcb9ec873742`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _IO_COUNTERS, _JOBOBJECT_BASIC_LIMIT_INFORMATION, ctypes. Outputs/bindings: _fields_.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_assign_kill_job::root.body[22]::FunctionDef

Source: `infra/agentinfra/process.py:74`; AST `95fd65850c0fb9f11a7e8d149d3deefb0d55f5aadd64e5f374edf966af287bee`.

Rust module: `infra::agentinfra::process`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: _JOBOBJECT_EXTENDED_LIMIT_INFORMATION, ctypes, info, int, job, kernel, os, proc, subprocess. Outputs/bindings: info, job, kernel.
Calls/effect boundaries: _JOBOBJECT_EXTENDED_LIMIT_INFORMATION, ctypes.byref, ctypes.sizeof, ctypes.wintypes.HANDLE, int, kernel.AssignProcessToJobObject, kernel.CloseHandle, kernel.CreateJobObjectW, kernel.SetInformationJobObject.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[22]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_assign_kill_job::root.body[22].body[0]::If

Source: `infra/agentinfra/process.py:75`; AST `28eaacd9cae3a35bd5fd3913c6b29d041fc2057278bb9ac70c27c212bae2b946`.

Rust module: `infra::agentinfra::process`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: os. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[22].body[0]; no call, error or mutation may be omitted. Condition: os.name != 'nt'
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_assign_kill_job::root.body[22].body[0].body[0]::Return

Source: `infra/agentinfra/process.py:76`; AST `353401809590fce03527be76d16055befec3bf00b4443d2e1a26c5300e3da6a4`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Return evaluation at root.body[22].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_assign_kill_job::root.body[22].body[1]::Assign

Source: `infra/agentinfra/process.py:77`; AST `8cd62392235fda4c5625bf9e98ef66cce97090b52dd6a40428e778ebc004e624`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ctypes. Outputs/bindings: kernel.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_assign_kill_job::root.body[22].body[2]::Assign

Source: `infra/agentinfra/process.py:78`; AST `f080eeaf19d8b3e7805087cf9f2c70542684adb29b4e6045e4e7ef522adb3a85`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ctypes, kernel. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_assign_kill_job::root.body[22].body[3]::Assign

Source: `infra/agentinfra/process.py:79`; AST `2f8cdcf2feed12ab5aa3c102c51e4ba1b80440cfb01f869bb6292b94c07439cb`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ctypes, kernel. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_assign_kill_job::root.body[22].body[4]::Assign

Source: `infra/agentinfra/process.py:80`; AST `88ef88372687ee848d897c4ed45874ee1ca7ca442147c17adeb9f03c622a3b6d`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ctypes, kernel. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_assign_kill_job::root.body[22].body[5]::Assign

Source: `infra/agentinfra/process.py:81`; AST `c352a3fccda90940f01eef66e82a993ec5cf6bc97dd1d3bee76ef3e17522255e`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ctypes, kernel. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_assign_kill_job::root.body[22].body[6]::Assign

Source: `infra/agentinfra/process.py:82`; AST `b3cca4c6d302ee48092dc3536ff7049e573d581f8ef3efd3393cc13d2b7cd7b5`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ctypes, kernel. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_assign_kill_job::root.body[22].body[7]::Assign

Source: `infra/agentinfra/process.py:83`; AST `c0a50be5c7ca786835bb3f8917fb72b2920a3707eb2285298853a92e3196a7b1`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ctypes, kernel. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_assign_kill_job::root.body[22].body[8]::Assign

Source: `infra/agentinfra/process.py:84`; AST `d31e0d993ae295a4fe75acd28e619b7bb11ac250dda7ee705185847ef21f2014`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: kernel. Outputs/bindings: job.
Calls/effect boundaries: kernel.CreateJobObjectW.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_assign_kill_job::root.body[22].body[8].value::Call

Source: `infra/agentinfra/process.py:84`; AST `26b0919a9014541662ce29f972eec5b445988fc685231d8dfd3a03df76648a79`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: kernel. Outputs/bindings: (none).
Calls/effect boundaries: kernel.CreateJobObjectW.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[22].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_assign_kill_job::root.body[22].body[9]::If

Source: `infra/agentinfra/process.py:85`; AST `20d7f505f3f052bf5b73bc7333b889dae1a3b4c4ef2cfffa50921a4e244cb5ad`.

Rust module: `infra::agentinfra::process`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: job. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[22].body[9]; no call, error or mutation may be omitted. Condition: not job
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_assign_kill_job::root.body[22].body[9].body[0]::Return

Source: `infra/agentinfra/process.py:86`; AST `353401809590fce03527be76d16055befec3bf00b4443d2e1a26c5300e3da6a4`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Return evaluation at root.body[22].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_assign_kill_job::root.body[22].body[10]::Assign

Source: `infra/agentinfra/process.py:87`; AST `2c90e67a3b6652d1f8d8000ea150bf538acd18da953dae2cb3c1a38e4b66d9e1`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _JOBOBJECT_EXTENDED_LIMIT_INFORMATION. Outputs/bindings: info.
Calls/effect boundaries: _JOBOBJECT_EXTENDED_LIMIT_INFORMATION.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_assign_kill_job::root.body[22].body[10].value::Call

Source: `infra/agentinfra/process.py:87`; AST `73e46a8041b278cb57c32fba46a677bcb25078f84928008730fbc8247ea15bbf`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _JOBOBJECT_EXTENDED_LIMIT_INFORMATION. Outputs/bindings: (none).
Calls/effect boundaries: _JOBOBJECT_EXTENDED_LIMIT_INFORMATION.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[22].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_assign_kill_job::root.body[22].body[11]::Assign

Source: `infra/agentinfra/process.py:88`; AST `ef6d5def17db3bf7b5d3946eaedc25552c819d5958c9ba454e0ce5c3302a3f7e`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: info. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_assign_kill_job::root.body[22].body[12]::If

Source: `infra/agentinfra/process.py:89`; AST `def56cca921a677a7a8f89bec5bbc27eff92a7932a6dfe9651f4f0f932955758`.

Rust module: `infra::agentinfra::process`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ctypes, info, job, kernel. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.byref, ctypes.sizeof, kernel.CloseHandle, kernel.SetInformationJobObject.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[22].body[12]; no call, error or mutation may be omitted. Condition: not kernel.SetInformationJobObject(job, 9, ctypes.byref(info), ctypes.sizeof(info))
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_assign_kill_job::root.body[22].body[12].test.operand::Call

Source: `infra/agentinfra/process.py:89`; AST `54210b9e6b8cda9797ef612823856638d852f90b5a865ca668dec9e4fd0bb82f`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ctypes, info, job, kernel. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.byref, ctypes.sizeof, kernel.SetInformationJobObject.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[22].body[12].test.operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_assign_kill_job::root.body[22].body[12].test.operand.args[2]::Call

Source: `infra/agentinfra/process.py:89`; AST `964fd03c67747d0da2b91b063e8636fa777907abb3e3b252ae75fcaa8ed0bd66`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ctypes, info. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.byref.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[22].body[12].test.operand.args[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_assign_kill_job::root.body[22].body[12].test.operand.args[3]::Call

Source: `infra/agentinfra/process.py:89`; AST `046877915f5debad8bda7fcb78cf9ef976dde35a67a61cf5ddd543ed5d8f7d6b`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ctypes, info. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.sizeof.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[22].body[12].test.operand.args[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_assign_kill_job::root.body[22].body[12].body[0]::Expr

Source: `infra/agentinfra/process.py:90`; AST `83e9f455339fdf5879591bda7d7739026b9d8894d6f58a53cc50b5d1784f3a33`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: job, kernel. Outputs/bindings: (none).
Calls/effect boundaries: kernel.CloseHandle.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[22].body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_assign_kill_job::root.body[22].body[12].body[0].value::Call

Source: `infra/agentinfra/process.py:90`; AST `9ccbbfe3facd122cce8e3795ecbf747c6c816bef341f3c0190d5cac1a89c9c0c`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: job, kernel. Outputs/bindings: (none).
Calls/effect boundaries: kernel.CloseHandle.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[22].body[12].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_assign_kill_job::root.body[22].body[12].body[1]::Return

Source: `infra/agentinfra/process.py:91`; AST `353401809590fce03527be76d16055befec3bf00b4443d2e1a26c5300e3da6a4`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Return evaluation at root.body[22].body[12].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_assign_kill_job::root.body[22].body[13]::If

Source: `infra/agentinfra/process.py:92`; AST `72936d90d322abf7a97ddf140857a386416ab35d055aa5500238522e33085b88`.

Rust module: `infra::agentinfra::process`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ctypes, int, job, kernel, proc. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.wintypes.HANDLE, int, kernel.AssignProcessToJobObject, kernel.CloseHandle.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[22].body[13]; no call, error or mutation may be omitted. Condition: not kernel.AssignProcessToJobObject(job, ctypes.wintypes.HANDLE(int(proc._handle)))
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_assign_kill_job::root.body[22].body[13].test.operand::Call

Source: `infra/agentinfra/process.py:92`; AST `45fca638e13e1f73e0dc058a5087a5941f3f8e0961ca3d7421c52d737fc794dd`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ctypes, int, job, kernel, proc. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.wintypes.HANDLE, int, kernel.AssignProcessToJobObject.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[22].body[13].test.operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_assign_kill_job::root.body[22].body[13].test.operand.args[1]::Call

Source: `infra/agentinfra/process.py:92`; AST `d72310aace5c02979dd5c0167ac8992d927aee23b5c08f10d25a6c3d719078ee`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ctypes, int, proc. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.wintypes.HANDLE, int.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[22].body[13].test.operand.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_assign_kill_job::root.body[22].body[13].test.operand.args[1].args[0]::Call

Source: `infra/agentinfra/process.py:92`; AST `eae5af0c9cc4a39519ac0bcbd29691306131668b8d67e85634a939dcb6cc2d20`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: int, proc. Outputs/bindings: (none).
Calls/effect boundaries: int.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[22].body[13].test.operand.args[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_assign_kill_job::root.body[22].body[13].body[0]::Expr

Source: `infra/agentinfra/process.py:93`; AST `83e9f455339fdf5879591bda7d7739026b9d8894d6f58a53cc50b5d1784f3a33`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: job, kernel. Outputs/bindings: (none).
Calls/effect boundaries: kernel.CloseHandle.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[22].body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_assign_kill_job::root.body[22].body[13].body[0].value::Call

Source: `infra/agentinfra/process.py:93`; AST `9ccbbfe3facd122cce8e3795ecbf747c6c816bef341f3c0190d5cac1a89c9c0c`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: job, kernel. Outputs/bindings: (none).
Calls/effect boundaries: kernel.CloseHandle.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[22].body[13].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_assign_kill_job::root.body[22].body[13].body[1]::Return

Source: `infra/agentinfra/process.py:94`; AST `353401809590fce03527be76d16055befec3bf00b4443d2e1a26c5300e3da6a4`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Return evaluation at root.body[22].body[13].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_assign_kill_job::root.body[22].body[14]::Return

Source: `infra/agentinfra/process.py:95`; AST `a134282c6d30676380017ec3f8be924435d931b551b7a142a2b01ecb8033a1bb`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: job. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Return evaluation at root.body[22].body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_close_job::root.body[23]::FunctionDef

Source: `infra/agentinfra/process.py:98`; AST `34f9f58cde628265d7b0d320dec3e10e217b45aabae08dac23eaeb2e14351731`.

Rust module: `infra::agentinfra::process`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ctypes, job, os. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.windll.kernel32.CloseHandle.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[23]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_close_job::root.body[23].body[0]::If

Source: `infra/agentinfra/process.py:99`; AST `bab817a3a72bc7c89090867ff09c8f03c14de9a72b47500e7421638c7a0091d6`.

Rust module: `infra::agentinfra::process`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ctypes, job, os. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.windll.kernel32.CloseHandle.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[23].body[0]; no call, error or mutation may be omitted. Condition: job is not None and os.name == 'nt'
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_close_job::root.body[23].body[0].body[0]::Expr

Source: `infra/agentinfra/process.py:100`; AST `5c5868abe2e3c5dae8b6fc4dca89cfbbcb030a8e71f76c83a14aa624956be945`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ctypes, job. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.windll.kernel32.CloseHandle.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_close_job::root.body[23].body[0].body[0].value::Call

Source: `infra/agentinfra/process.py:100`; AST `65dd344b1954265a8d1f540a0e59c10d7bf4c1ea43e335b3070310114379eabc`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ctypes, job. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.windll.kernel32.CloseHandle.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[23].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::ProcessResult::root.body[24]::ClassDef

Source: `infra/agentinfra/process.py:104`; AST `955f3089164d7d09df9c5a83d5a09bfa223798e73dafca7c42bca91f3e3e628e`.

Rust module: `infra::agentinfra::process`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: bool, dataclass, float, int, str, tuple. Outputs/bindings: argv, cwd, duration_seconds, finished_at, returncode, started_at, stderr, stderr_bytes, stderr_path, stderr_sha256, stderr_truncated, stdout, stdout_bytes, stdout_path, stdout_sha256, stdout_truncated, timed_out.
Calls/effect boundaries: dataclass.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered ClassDef evaluation at root.body[24]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::ProcessResult::root.body[24].body[0]::AnnAssign

Source: `infra/agentinfra/process.py:105`; AST `d7f42150394ad059443bfa51462b2ed4a07e5fe75c8384f523f3324250dc0baf`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: str, tuple. Outputs/bindings: argv.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[24].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::ProcessResult::root.body[24].body[1]::AnnAssign

Source: `infra/agentinfra/process.py:106`; AST `48c22a884ff96cb02d48e55e28def60bb2deb3f41fa10c1f3cdcee06622b4aac`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: str. Outputs/bindings: cwd.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[24].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::ProcessResult::root.body[24].body[2]::AnnAssign

Source: `infra/agentinfra/process.py:107`; AST `f9e8a79db4f311bff810bda9cfa7747bc6f3736033b3a5b231153631f7f51548`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: int. Outputs/bindings: returncode.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[24].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::ProcessResult::root.body[24].body[3]::AnnAssign

Source: `infra/agentinfra/process.py:108`; AST `d5b7c6ccae9f88eab71b60956122c7f081240d20ac594f37a821295c62580eed`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: str. Outputs/bindings: stdout.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[24].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::ProcessResult::root.body[24].body[4]::AnnAssign

Source: `infra/agentinfra/process.py:109`; AST `3ed69d17e9f80d7f95543317f9aeb7431011c02b60b5ee18d068709b86258362`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: str. Outputs/bindings: stderr.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[24].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::ProcessResult::root.body[24].body[5]::AnnAssign

Source: `infra/agentinfra/process.py:110`; AST `57f9069d9147b8139d38658387648baf43f96f60336b4eda2c2c6378208ecdbe`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: str. Outputs/bindings: stdout_sha256.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[24].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::ProcessResult::root.body[24].body[6]::AnnAssign

Source: `infra/agentinfra/process.py:111`; AST `7332c211830cb44f4efa62a77fb6a75679f03de8e1d287d89f2a75660a5684fa`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: str. Outputs/bindings: stderr_sha256.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[24].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::ProcessResult::root.body[24].body[7]::AnnAssign

Source: `infra/agentinfra/process.py:112`; AST `11ad121e8714e17ffbf710b997e02c4aec4e37009c6bd52f7e63a8c5d37d1e8c`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: int. Outputs/bindings: stdout_bytes.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[24].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::ProcessResult::root.body[24].body[8]::AnnAssign

Source: `infra/agentinfra/process.py:113`; AST `d8d23e3a7a603e0e292916f263f4c43f4525d3c25864822bad82cacca0278a47`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: int. Outputs/bindings: stderr_bytes.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[24].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::ProcessResult::root.body[24].body[9]::AnnAssign

Source: `infra/agentinfra/process.py:114`; AST `a159574c3b40f066a5b9354fff5942d8cbc9357e591e24ea3a3fefc3744649a8`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool. Outputs/bindings: stdout_truncated.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[24].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::ProcessResult::root.body[24].body[10]::AnnAssign

Source: `infra/agentinfra/process.py:115`; AST `14298284b94df54346dc13b09e8a61d0f399a9fe7ba014702d71eadca4bb389a`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool. Outputs/bindings: stderr_truncated.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[24].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::ProcessResult::root.body[24].body[11]::AnnAssign

Source: `infra/agentinfra/process.py:116`; AST `7a4ab72f9566b9f7c6c2f4fbd2e488910abdb86a6b27afacd38cff97918d9103`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool. Outputs/bindings: timed_out.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[24].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::ProcessResult::root.body[24].body[12]::AnnAssign

Source: `infra/agentinfra/process.py:117`; AST `18ead2122660455c1ec0dc277dbb03bce6fb8a2392f3f6154fd421ae5ecc6f41`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: str. Outputs/bindings: started_at.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[24].body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::ProcessResult::root.body[24].body[13]::AnnAssign

Source: `infra/agentinfra/process.py:118`; AST `6806364f2fb3c49d3f701dcd684aa01981037c188332c0c92c9bcbf1c860cede`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: str. Outputs/bindings: finished_at.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[24].body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::ProcessResult::root.body[24].body[14]::AnnAssign

Source: `infra/agentinfra/process.py:119`; AST `198ad42d2003ef67e58ae88c355f4689e2a65728244defc6e3beb8336acef19c`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: float. Outputs/bindings: duration_seconds.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[24].body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::ProcessResult::root.body[24].body[15]::AnnAssign

Source: `infra/agentinfra/process.py:120`; AST `f2b9050ffecba32daa2fc4bcb0e895a56c62eab59685652e0c9cb7e6bd2637e8`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: str. Outputs/bindings: stdout_path.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[24].body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::ProcessResult::root.body[24].body[16]::AnnAssign

Source: `infra/agentinfra/process.py:121`; AST `d2873a17b20b0410997ad459587375b6a1e8dbea72c8e16335da8af8bfd87c72`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: str. Outputs/bindings: stderr_path.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered AnnAssign evaluation at root.body[24].body[16]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::ProcessResult::root.body[24].decorator_list[0]::Call

Source: `infra/agentinfra/process.py:103`; AST `fc70015bf40dfb1bdf9c74c7ec3567232b79ad9aa1cd1edc6c02254994330803`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dataclass. Outputs/bindings: (none).
Calls/effect boundaries: dataclass.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[24].decorator_list[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::root.body[25]::ClassDef

Source: `infra/agentinfra/process.py:124`; AST `366edf0a0b3357d118279a4a81e8131ede21f3c3ac2e7ad73b9db198556d8869`.

Rust module: `infra::agentinfra::process`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: BaseException, Path, archive, bytearray, bytes, chunk, exc, fd, hashlib, int, len, limit, os, output, redact_text, self, str, stream. Outputs/bindings: chunk, fd, output.
Calls/effect boundaries: bytearray, bytes, bytes(self.buffer).decode, hashlib.sha256, len, os.fdopen, os.open, output.close, output.write, redact_text, self.buffer.extend, self.digest.update, stream.read.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered ClassDef evaluation at root.body[25]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::__init__::root.body[25].body[0]::FunctionDef

Source: `infra/agentinfra/process.py:125`; AST `13b6662feacd6d1ccc6175879e36dc267badee1b64b5589125b7dae68c5f0a23`.

Rust module: `infra::agentinfra::process`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, archive, bytearray, hashlib, int, limit, self. Outputs/bindings: (none).
Calls/effect boundaries: bytearray, hashlib.sha256.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[25].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::__init__::root.body[25].body[0].body[0]::Assign

Source: `infra/agentinfra/process.py:126`; AST `4e35b5a6d80f8d15dec7ff992d79a55e06dfe267914c361c99ee8a780ec8fb34`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: limit, self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[25].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::__init__::root.body[25].body[0].body[1]::Assign

Source: `infra/agentinfra/process.py:127`; AST `b2aed248cf293d1fc61c8786379e1038d57fb88894efbf011c33f4157c1e388a`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bytearray, self. Outputs/bindings: (none).
Calls/effect boundaries: bytearray.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[25].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::__init__::root.body[25].body[0].body[1].value::Call

Source: `infra/agentinfra/process.py:127`; AST `98999811768fc053899af0ed0545b7d6724b86b55a8a65335970386fa307ed0f`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bytearray. Outputs/bindings: (none).
Calls/effect boundaries: bytearray.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[25].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::__init__::root.body[25].body[0].body[2]::Assign

Source: `infra/agentinfra/process.py:128`; AST `92824b6431fc5c102a5af690f837258513ff8c4560620fd17748ad939d49ad01`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: hashlib, self. Outputs/bindings: (none).
Calls/effect boundaries: hashlib.sha256.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[25].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::__init__::root.body[25].body[0].body[2].value::Call

Source: `infra/agentinfra/process.py:128`; AST `46ef61fb8c7d09a7bf845569bbc8968c05c256379ed5433a5aca1ba6d226695f`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: hashlib. Outputs/bindings: (none).
Calls/effect boundaries: hashlib.sha256.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[25].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::__init__::root.body[25].body[0].body[3]::Assign

Source: `infra/agentinfra/process.py:129`; AST `6bcc7c27a63769ac4ef187bd9869ed9c291079532140db2fdde991aa7b446f0a`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[25].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::__init__::root.body[25].body[0].body[4]::Assign

Source: `infra/agentinfra/process.py:130`; AST `71ba7a8861699b55288fbf351b3a8f040fb84576402d5cb56f4ae06236cab954`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: archive, self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[25].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::__init__::root.body[25].body[0].body[5]::Assign

Source: `infra/agentinfra/process.py:131`; AST `e0d90a8559f695fe1533d987bcc2dde935a1e65f6a4a8b201132f3d441834714`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[25].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::consume::root.body[25].body[1]::FunctionDef

Source: `infra/agentinfra/process.py:133`; AST `0cd9ce2e112031db076858ae1d1a3150ccef778829f6749a1bf4c70a77f46ac9`.

Rust module: `infra::agentinfra::process`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: BaseException, chunk, exc, fd, len, os, output, self, stream. Outputs/bindings: chunk, fd, output.
Calls/effect boundaries: len, os.fdopen, os.open, output.close, output.write, self.buffer.extend, self.digest.update, stream.read.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[25].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::consume::root.body[25].body[1].body[0]::Assign

Source: `infra/agentinfra/process.py:134`; AST `d5bdc75f700b66a3a8c8bda1c2fb59298937458f3ba742a6aa7fe76132ff2eb0`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: output.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[25].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::consume::root.body[25].body[1].body[1]::Try

Source: `infra/agentinfra/process.py:135`; AST `45ac995174665c48128939a14797f865c98a7c4ceb9c3a8abc0f644d8fb0ea55`.

Rust module: `infra::agentinfra::process`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: BaseException, chunk, exc, fd, len, os, output, self, stream. Outputs/bindings: chunk, fd, output.
Calls/effect boundaries: len, os.fdopen, os.open, output.close, output.write, self.buffer.extend, self.digest.update, stream.read.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Try evaluation at root.body[25].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::consume::root.body[25].body[1].body[1].body[0]::If

Source: `infra/agentinfra/process.py:136`; AST `235289813e4ed9758508b7a60dbc505331ed828b74bd4511bc380d174c1afaf0`.

Rust module: `infra::agentinfra::process`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: fd, os, self. Outputs/bindings: fd, output.
Calls/effect boundaries: os.fdopen, os.open.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[25].body[1].body[1].body[0]; no call, error or mutation may be omitted. Condition: self.archive is not None
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::consume::root.body[25].body[1].body[1].body[0].body[0]::Assign

Source: `infra/agentinfra/process.py:137`; AST `b053ede8bcb4edf5aafaa780ac770327e75641fa6f18ee936d0a4b332b769512`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: os, self. Outputs/bindings: fd.
Calls/effect boundaries: os.open.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[25].body[1].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::consume::root.body[25].body[1].body[1].body[0].body[0].value::Call

Source: `infra/agentinfra/process.py:137`; AST `c3f296137989cb6bc4cef847cddb501a59d9f24e93b5a1c796b60f237a02c70f`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os, self. Outputs/bindings: (none).
Calls/effect boundaries: os.open.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[25].body[1].body[1].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::consume::root.body[25].body[1].body[1].body[0].body[1]::Assign

Source: `infra/agentinfra/process.py:138`; AST `26ea461b27e9e2cb71a73dd637adf880f7cd3931eab3c0174885d5927d8ca3d7`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fd, os. Outputs/bindings: output.
Calls/effect boundaries: os.fdopen.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[25].body[1].body[1].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::consume::root.body[25].body[1].body[1].body[0].body[1].value::Call

Source: `infra/agentinfra/process.py:138`; AST `58f2083f99f9d565afcbde03da3923bbe8eeeda611fed024de1825d26447d890`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fd, os. Outputs/bindings: (none).
Calls/effect boundaries: os.fdopen.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[25].body[1].body[1].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::consume::root.body[25].body[1].body[1].body[1]::While

Source: `infra/agentinfra/process.py:139`; AST `bdf86d38dcb0f0ac4ef43d23c3038c5ed09bf1ba6f8d27eefa309716465fa2ac`.

Rust module: `infra::agentinfra::process`. while with explicit truth conversion and a normal-exhaustion flag for loop else

Inputs: chunk, len, output, self, stream. Outputs/bindings: chunk.
Calls/effect boundaries: len, output.write, self.buffer.extend, self.digest.update, stream.read.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered While evaluation at root.body[25].body[1].body[1].body[1]; no call, error or mutation may be omitted. Condition: True
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::consume::root.body[25].body[1].body[1].body[1].body[0]::Assign

Source: `infra/agentinfra/process.py:140`; AST `45d2266e7d04683c67a067a5960e8a6eeeeb0b64606bedf446cba58f0ff24325`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: stream. Outputs/bindings: chunk.
Calls/effect boundaries: stream.read.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[25].body[1].body[1].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::consume::root.body[25].body[1].body[1].body[1].body[0].value::Call

Source: `infra/agentinfra/process.py:140`; AST `ebb136574e34869afe211ad6c971af18ea31f9d36c5b5ec80456246c4811ea61`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: stream. Outputs/bindings: (none).
Calls/effect boundaries: stream.read.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[25].body[1].body[1].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::consume::root.body[25].body[1].body[1].body[1].body[1]::If

Source: `infra/agentinfra/process.py:141`; AST `32c9c51af1806fa5afbd127a4250133e5df01ed9c2bc1c1f592dee21a5ad93d3`.

Rust module: `infra::agentinfra::process`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: chunk. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[25].body[1].body[1].body[1].body[1]; no call, error or mutation may be omitted. Condition: not chunk
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::consume::root.body[25].body[1].body[1].body[1].body[1].body[0]::Return

Source: `infra/agentinfra/process.py:142`; AST `d3ec646650be52e3f5b5700447f19313b1bab9ed1bd27c2483960d5d0bcaf584`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Return evaluation at root.body[25].body[1].body[1].body[1].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::consume::root.body[25].body[1].body[1].body[1].body[2]::Expr

Source: `infra/agentinfra/process.py:143`; AST `ebcdf119bb7f9c570ce12ebf2975f17e818f452070f7bbcec7a4128a7d429dae`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: chunk, self. Outputs/bindings: (none).
Calls/effect boundaries: self.digest.update.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[25].body[1].body[1].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::consume::root.body[25].body[1].body[1].body[1].body[2].value::Call

Source: `infra/agentinfra/process.py:143`; AST `e239dc425dc8c367066396daec97264cb7e9b6ff0ac15a2ad9a2807196e033b6`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: chunk, self. Outputs/bindings: (none).
Calls/effect boundaries: self.digest.update.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[25].body[1].body[1].body[1].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::consume::root.body[25].body[1].body[1].body[1].body[3]::AugAssign

Source: `infra/agentinfra/process.py:144`; AST `fb432ab65c4296b8778121f640785f14b1797be7f42e442c155f6f9c09f99536`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: chunk, len, self. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered AugAssign evaluation at root.body[25].body[1].body[1].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::consume::root.body[25].body[1].body[1].body[1].body[3].value::Call

Source: `infra/agentinfra/process.py:144`; AST `6f99d4ecb2708ba92e74d7c76fd9b2c1d7b1aa91d619b54799b549e649104fc3`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: chunk, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[25].body[1].body[1].body[1].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::consume::root.body[25].body[1].body[1].body[1].body[4]::If

Source: `infra/agentinfra/process.py:145`; AST `c4f60fc6f8da39662e079ef9098a8af22ff333a2a787c9a5227e6ba53c03c9e9`.

Rust module: `infra::agentinfra::process`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: chunk, output. Outputs/bindings: (none).
Calls/effect boundaries: output.write.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[25].body[1].body[1].body[1].body[4]; no call, error or mutation may be omitted. Condition: output is not None
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::consume::root.body[25].body[1].body[1].body[1].body[4].body[0]::Expr

Source: `infra/agentinfra/process.py:146`; AST `9c802f4657e8e7d7607ed61235070098592ebe3b89265147793dd56aa51c617c`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: chunk, output. Outputs/bindings: (none).
Calls/effect boundaries: output.write.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[25].body[1].body[1].body[1].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::consume::root.body[25].body[1].body[1].body[1].body[4].body[0].value::Call

Source: `infra/agentinfra/process.py:146`; AST `190360950a5fd203e4c19531c04f75f94bc12254565043396c7251615d294d97`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: chunk, output. Outputs/bindings: (none).
Calls/effect boundaries: output.write.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[25].body[1].body[1].body[1].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::consume::root.body[25].body[1].body[1].body[1].body[5]::If

Source: `infra/agentinfra/process.py:147`; AST `9c8457564d727115aa5e31e527ddff6bc785e927ac6491721b90b8ed2706ac47`.

Rust module: `infra::agentinfra::process`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: chunk, len, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.buffer.extend.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[25].body[1].body[1].body[1].body[5]; no call, error or mutation may be omitted. Condition: len(self.buffer) < self.limit
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::consume::root.body[25].body[1].body[1].body[1].body[5].test.left::Call

Source: `infra/agentinfra/process.py:147`; AST `348733d7439f589c925a5bf296bf67ef3de5bd227c94342df760f920f2a2c25b`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, self. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[25].body[1].body[1].body[1].body[5].test.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::consume::root.body[25].body[1].body[1].body[1].body[5].body[0]::Expr

Source: `infra/agentinfra/process.py:148`; AST `09a13ed1d61a842bd33f03de3821ce4fef6afd0ace0b6c4b39c4f80465aebd91`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: chunk, len, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.buffer.extend.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[25].body[1].body[1].body[1].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::consume::root.body[25].body[1].body[1].body[1].body[5].body[0].value::Call

Source: `infra/agentinfra/process.py:148`; AST `7752ca84ee02dd623f9281a5ad217b7b9966319bcfd0a453395186ebd0ab0284`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: chunk, len, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.buffer.extend.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[25].body[1].body[1].body[1].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::consume::root.body[25].body[1].body[1].body[1].body[5].body[0].value.args[0].slice.upper.right::Call

Source: `infra/agentinfra/process.py:148`; AST `348733d7439f589c925a5bf296bf67ef3de5bd227c94342df760f920f2a2c25b`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, self. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[25].body[1].body[1].body[1].body[5].body[0].value.args[0].slice.upper.right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::consume::root.body[25].body[1].body[1].handlers[0]::ExceptHandler

Source: `infra/agentinfra/process.py:149`; AST `0400707f208f0356f4249c515e3cdecc18d9b5d6d43f4aece600ecbe51e888ac`.

Rust module: `infra::agentinfra::process`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: BaseException, exc, self, stream. Outputs/bindings: (none).
Calls/effect boundaries: stream.read.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[25].body[1].body[1].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::consume::root.body[25].body[1].body[1].handlers[0].body[0]::Assign

Source: `infra/agentinfra/process.py:150`; AST `370644e2c8f5e9c5dfa9a39110abc26ac5a447198cdd95914af6a0af90d5409f`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: exc, self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[25].body[1].body[1].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::consume::root.body[25].body[1].body[1].handlers[0].body[1]::While

Source: `infra/agentinfra/process.py:153`; AST `4d58691b6ad2e0716cf8397ba03dcd18900b4bce9330dd4060b0272b13fe0dd6`.

Rust module: `infra::agentinfra::process`. while with explicit truth conversion and a normal-exhaustion flag for loop else

Inputs: stream. Outputs/bindings: (none).
Calls/effect boundaries: stream.read.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered While evaluation at root.body[25].body[1].body[1].handlers[0].body[1]; no call, error or mutation may be omitted. Condition: stream.read(65536)
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::consume::root.body[25].body[1].body[1].handlers[0].body[1].test::Call

Source: `infra/agentinfra/process.py:153`; AST `ebb136574e34869afe211ad6c971af18ea31f9d36c5b5ec80456246c4811ea61`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: stream. Outputs/bindings: (none).
Calls/effect boundaries: stream.read.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[25].body[1].body[1].handlers[0].body[1].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::consume::root.body[25].body[1].body[1].handlers[0].body[1].body[0]::Pass

Source: `infra/agentinfra/process.py:154`; AST `f8e211bd496e62be79e8542ba1d0a7cebbf2a6143ae07b375ae14ce00a91b69c`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Pass evaluation at root.body[25].body[1].body[1].handlers[0].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::consume::root.body[25].body[1].body[1].finalbody[0]::If

Source: `infra/agentinfra/process.py:156`; AST `ba35d346ebcf3fbd1952007e10b0942475641af594312990049402831e48b1a7`.

Rust module: `infra::agentinfra::process`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: BaseException, exc, output, self. Outputs/bindings: (none).
Calls/effect boundaries: output.close.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[25].body[1].body[1].finalbody[0]; no call, error or mutation may be omitted. Condition: output is not None
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::consume::root.body[25].body[1].body[1].finalbody[0].body[0]::Try

Source: `infra/agentinfra/process.py:157`; AST `0a9caf7ec93753bb80328796fb55d22b3578b8e01b49d703e7b81df7c5dcfb90`.

Rust module: `infra::agentinfra::process`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: BaseException, exc, output, self. Outputs/bindings: (none).
Calls/effect boundaries: output.close.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Try evaluation at root.body[25].body[1].body[1].finalbody[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::consume::root.body[25].body[1].body[1].finalbody[0].body[0].body[0]::Expr

Source: `infra/agentinfra/process.py:158`; AST `ae8e215e797117cf906df8207ec8d37e18b879c1227d69c6c856b5321cb63d8d`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: output. Outputs/bindings: (none).
Calls/effect boundaries: output.close.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[25].body[1].body[1].finalbody[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::consume::root.body[25].body[1].body[1].finalbody[0].body[0].body[0].value::Call

Source: `infra/agentinfra/process.py:158`; AST `42e777468315917010db353c3c027ae30ef506815893bb326a0241059687ee43`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: output. Outputs/bindings: (none).
Calls/effect boundaries: output.close.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[25].body[1].body[1].finalbody[0].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::consume::root.body[25].body[1].body[1].finalbody[0].body[0].handlers[0]::ExceptHandler

Source: `infra/agentinfra/process.py:159`; AST `ecd6bf6ed77e68c265a62fdae16a8991a3ef8d560ffc8778744b8b16e571bceb`.

Rust module: `infra::agentinfra::process`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: BaseException, exc, self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[25].body[1].body[1].finalbody[0].body[0].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::consume::root.body[25].body[1].body[1].finalbody[0].body[0].handlers[0].body[0]::Assign

Source: `infra/agentinfra/process.py:160`; AST `370644e2c8f5e9c5dfa9a39110abc26ac5a447198cdd95914af6a0af90d5409f`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: exc, self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[25].body[1].body[1].finalbody[0].body[0].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::text::root.body[25].body[2]::FunctionDef

Source: `infra/agentinfra/process.py:162`; AST `3fd7ba4691c33fbdc5ba35782db23fa9e0a5a52658c8aab0972f719271246ac0`.

Rust module: `infra::agentinfra::process`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: bytes, redact_text, self, str. Outputs/bindings: (none).
Calls/effect boundaries: bytes, bytes(self.buffer).decode, redact_text.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[25].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::text::root.body[25].body[2].body[0]::Return

Source: `infra/agentinfra/process.py:163`; AST `6a1200bdfab236a79f4f0fc4ebc91049440c14039fab7c84f2eb9fd6dd2ee164`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bytes, redact_text, self. Outputs/bindings: (none).
Calls/effect boundaries: bytes, bytes(self.buffer).decode, redact_text.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Return evaluation at root.body[25].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::text::root.body[25].body[2].body[0].value::Call

Source: `infra/agentinfra/process.py:163`; AST `f64238db90c43d85c28f900a52135e6c178e4eafc0482df663ba6801f15fbc6b`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bytes, redact_text, self. Outputs/bindings: (none).
Calls/effect boundaries: bytes, bytes(self.buffer).decode, redact_text.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[25].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::text::root.body[25].body[2].body[0].value.args[0]::Call

Source: `infra/agentinfra/process.py:163`; AST `dfe26980d0e1320c7494653186aa99733ac0e9b95279efc5f7ae05a51fbd517c`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bytes, self. Outputs/bindings: (none).
Calls/effect boundaries: bytes, bytes(self.buffer).decode.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[25].body[2].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_Capture::text::root.body[25].body[2].body[0].value.args[0].func.value::Call

Source: `infra/agentinfra/process.py:163`; AST `b51ec1f828aa9953dbd779e69757dda7db76f4da9bf661f58aed0adc39c4b0f7`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bytes, self. Outputs/bindings: (none).
Calls/effect boundaries: bytes.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[25].body[2].body[0].value.args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_kill_tree::root.body[26]::FunctionDef

Source: `infra/agentinfra/process.py:166`; AST `fc45976e43ebcfa5fd5c6f5c4459d2ed03070701b06f14419138cefb742d51e2`.

Rust module: `infra::agentinfra::process`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ProcessLookupError, ctypes, group, int, job, minimal_subprocess_env, os, proc, signal, str, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.windll.kernel32.TerminateJobObject, minimal_subprocess_env, os.killpg, proc.kill, proc.poll, str, subprocess.run.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[26]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_kill_tree::root.body[26].body[0]::If

Source: `infra/agentinfra/process.py:167`; AST `f946c1b2526a0b21d9909cbf45b642969a6f0331061b33b5f7ef7482964cf2ed`.

Rust module: `infra::agentinfra::process`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ctypes, job, os, proc. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.windll.kernel32.TerminateJobObject, proc.poll.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[26].body[0]; no call, error or mutation may be omitted. Condition: proc.poll() is not None
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_kill_tree::root.body[26].body[0].test.left::Call

Source: `infra/agentinfra/process.py:167`; AST `3bcd0731b1917f0df78e7aa7360f1c4af6df6ddc962e6ef2be6ee95ff127b762`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: proc. Outputs/bindings: (none).
Calls/effect boundaries: proc.poll.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[0].test.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_kill_tree::root.body[26].body[0].body[0]::If

Source: `infra/agentinfra/process.py:168`; AST `de21aebad7f12c5d976702646fe0462899c1b54fda946a02bacc08f34659fda3`.

Rust module: `infra::agentinfra::process`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ctypes, job, os. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.windll.kernel32.TerminateJobObject.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[26].body[0].body[0]; no call, error or mutation may be omitted. Condition: job is not None and os.name == 'nt'
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_kill_tree::root.body[26].body[0].body[0].body[0]::Expr

Source: `infra/agentinfra/process.py:169`; AST `a6dccdaaf212c52af68be3c6af3e1472e1db9e6b6223c7e1e4fc18328cc21419`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ctypes, job. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.windll.kernel32.TerminateJobObject.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[26].body[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_kill_tree::root.body[26].body[0].body[0].body[0].value::Call

Source: `infra/agentinfra/process.py:169`; AST `2523921b9b1d625ff14df40441eb5845422480a7c9d11bd8108e73330c33d2f7`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ctypes, job. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.windll.kernel32.TerminateJobObject.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[0].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_kill_tree::root.body[26].body[0].body[1]::Return

Source: `infra/agentinfra/process.py:170`; AST `d3ec646650be52e3f5b5700447f19313b1bab9ed1bd27c2483960d5d0bcaf584`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Return evaluation at root.body[26].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_kill_tree::root.body[26].body[1]::If

Source: `infra/agentinfra/process.py:171`; AST `9238246c7cacf4893302fe1fd9e757e09bcb34bab4ba3854c85dc73a61cad2df`.

Rust module: `infra::agentinfra::process`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ProcessLookupError, ctypes, group, job, minimal_subprocess_env, os, proc, signal, str, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.windll.kernel32.TerminateJobObject, minimal_subprocess_env, os.killpg, proc.kill, proc.poll, str, subprocess.run.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[26].body[1]; no call, error or mutation may be omitted. Condition: os.name == 'nt'
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_kill_tree::root.body[26].body[1].body[0]::If

Source: `infra/agentinfra/process.py:172`; AST `2f2bb392846fe5b4c2e881d8f767989ed9a1bc613aa9d9ac79e6f4631b935b06`.

Rust module: `infra::agentinfra::process`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ctypes, job. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.windll.kernel32.TerminateJobObject.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[26].body[1].body[0]; no call, error or mutation may be omitted. Condition: job is not None and ctypes.windll.kernel32.TerminateJobObject(job, 1)
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_kill_tree::root.body[26].body[1].body[0].test.values[1]::Call

Source: `infra/agentinfra/process.py:172`; AST `2523921b9b1d625ff14df40441eb5845422480a7c9d11bd8108e73330c33d2f7`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ctypes, job. Outputs/bindings: (none).
Calls/effect boundaries: ctypes.windll.kernel32.TerminateJobObject.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[1].body[0].test.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_kill_tree::root.body[26].body[1].body[0].body[0]::Return

Source: `infra/agentinfra/process.py:173`; AST `d3ec646650be52e3f5b5700447f19313b1bab9ed1bd27c2483960d5d0bcaf584`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Return evaluation at root.body[26].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_kill_tree::root.body[26].body[1].body[1]::Expr

Source: `infra/agentinfra/process.py:174`; AST `7f2970aca7200806c026c5c8a51df15b0e06c0c7866bdb707bb3d4aefd03b267`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: minimal_subprocess_env, proc, str, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: minimal_subprocess_env, str, subprocess.run.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[26].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_kill_tree::root.body[26].body[1].body[1].value::Call

Source: `infra/agentinfra/process.py:174`; AST `bbb9e051e10880048cef1fbe43a141fcdfdf8da51b7a4c8cb7396ecf0f18080d`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: minimal_subprocess_env, proc, str, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: minimal_subprocess_env, str, subprocess.run.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_kill_tree::root.body[26].body[1].body[1].value.args[0].elts[2]::Call

Source: `infra/agentinfra/process.py:175`; AST `59414530e209390ed6d959ba29b76d6dc832830241bd0d7022229ff85ac9fbc8`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: proc, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[1].body[1].value.args[0].elts[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_kill_tree::root.body[26].body[1].body[1].value.keywords[3].value::Call

Source: `infra/agentinfra/process.py:179`; AST `9e9061036bd9e328e720270b436538e3d5500df22e91a0d49a0d1cd8cd8d5695`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: minimal_subprocess_env. Outputs/bindings: (none).
Calls/effect boundaries: minimal_subprocess_env.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[1].body[1].value.keywords[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_kill_tree::root.body[26].body[1].body[2]::If

Source: `infra/agentinfra/process.py:181`; AST `f8aa149856e7cc814f4f08ef852a8b0c6e78b952c2405d15cee44f185c344cc0`.

Rust module: `infra::agentinfra::process`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: proc. Outputs/bindings: (none).
Calls/effect boundaries: proc.kill, proc.poll.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[26].body[1].body[2]; no call, error or mutation may be omitted. Condition: proc.poll() is None
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_kill_tree::root.body[26].body[1].body[2].test.left::Call

Source: `infra/agentinfra/process.py:181`; AST `3bcd0731b1917f0df78e7aa7360f1c4af6df6ddc962e6ef2be6ee95ff127b762`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: proc. Outputs/bindings: (none).
Calls/effect boundaries: proc.poll.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[1].body[2].test.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_kill_tree::root.body[26].body[1].body[2].body[0]::Expr

Source: `infra/agentinfra/process.py:182`; AST `840e72d69dcda4859aaf7b38dcedd1f9c5dbefc935ed16fc7315b52656470117`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: proc. Outputs/bindings: (none).
Calls/effect boundaries: proc.kill.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[26].body[1].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_kill_tree::root.body[26].body[1].body[2].body[0].value::Call

Source: `infra/agentinfra/process.py:182`; AST `8ed086cdf10a0ea14b67ccf17979da5b24c8363d8bc20f02ecb2a947e6050076`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: proc. Outputs/bindings: (none).
Calls/effect boundaries: proc.kill.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[1].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_kill_tree::root.body[26].body[1].orelse[0]::Try

Source: `infra/agentinfra/process.py:184`; AST `081878037a22f5a787d652c2f2184c7b2476fe233b8d3c25b9768aee1d113f3b`.

Rust module: `infra::agentinfra::process`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: ProcessLookupError, group, os, proc, signal. Outputs/bindings: (none).
Calls/effect boundaries: os.killpg.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Try evaluation at root.body[26].body[1].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_kill_tree::root.body[26].body[1].orelse[0].body[0]::Expr

Source: `infra/agentinfra/process.py:185`; AST `1b9efc16d0ae98ca8ecf355046a800d6fa7fbe2435edd1d69b8a2834129b7489`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: group, os, proc, signal. Outputs/bindings: (none).
Calls/effect boundaries: os.killpg.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[26].body[1].orelse[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_kill_tree::root.body[26].body[1].orelse[0].body[0].value::Call

Source: `infra/agentinfra/process.py:185`; AST `854aca09f56d2000abaa30ee3f8ec50254e60dd8732756a2d92c2a4d526b4ee0`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: group, os, proc, signal. Outputs/bindings: (none).
Calls/effect boundaries: os.killpg.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[26].body[1].orelse[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_kill_tree::root.body[26].body[1].orelse[0].handlers[0]::ExceptHandler

Source: `infra/agentinfra/process.py:186`; AST `979fb164c2b97ab534410ca0015d7d3405c2af35a180925d2390cb6b61011463`.

Rust module: `infra::agentinfra::process`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: ProcessLookupError. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[26].body[1].orelse[0].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::_kill_tree::root.body[26].body[1].orelse[0].handlers[0].body[0]::Pass

Source: `infra/agentinfra/process.py:187`; AST `f8e211bd496e62be79e8542ba1d0a7cebbf2a6143ae07b375ae14ce00a91b69c`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Pass evaluation at root.body[26].body[1].orelse[0].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_recipe_stage::root.body[27]::FunctionDef

Source: `infra/agentinfra/process.py:190`; AST `0b2afaf3a7479be00cfc83c4681a619d07f81d0551d6cc92df577659c9621238`.

Rust module: `infra::agentinfra::process`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Iterable, Mapping, Path, ProcessResult, ValueError, _recipe_group, argv, capture_limit, cwd, env, float, int, logs, os, run_process, str, timeout, token, uuid. Outputs/bindings: logs, token.
Calls/effect boundaries: ValueError, _recipe_group.reset, _recipe_group.set, os.getpgrp, os.getpid, os.getsid, run_process, uuid.uuid4.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[27]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_recipe_stage::root.body[27].body[0]::Expr

Source: `infra/agentinfra/process.py:198`; AST `eaea93fba95ab9c729344a114c15911f7fb53141ed0a263b32e95608270bdd8b`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[27].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_recipe_stage::root.body[27].body[1]::If

Source: `infra/agentinfra/process.py:204`; AST `753b09c6ea4bfe3cf75156d111ab0e9123c0831e574cafbc54bd7aeede92e3f3`.

Rust module: `infra::agentinfra::process`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ValueError, os. Outputs/bindings: (none).
Calls/effect boundaries: ValueError, os.getpid, os.getsid.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[27].body[1]; no call, error or mutation may be omitted. Condition: os.name != 'posix' or os.getsid(0) != os.getpid()
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_recipe_stage::root.body[27].body[1].test.values[1].left::Call

Source: `infra/agentinfra/process.py:204`; AST `c8e647e030eeb1e927e412b2caa33070a17ad44c1c67818ad4f20f0049f485ba`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os. Outputs/bindings: (none).
Calls/effect boundaries: os.getsid.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[27].body[1].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_recipe_stage::root.body[27].body[1].test.values[1].comparators[0]::Call

Source: `infra/agentinfra/process.py:204`; AST `ba1923643b161051a18bf7ae7386addd84146f4ab481f99d56712bc1ce97df2c`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os. Outputs/bindings: (none).
Calls/effect boundaries: os.getpid.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[27].body[1].test.values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_recipe_stage::root.body[27].body[1].body[0]::Raise

Source: `infra/agentinfra/process.py:205`; AST `8f941d3a2784b26a40a93d2dea04f2868fe821debeb378710ce27fb6498b8ea6`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ValueError. Outputs/bindings: (none).
Calls/effect boundaries: ValueError.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[27].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_recipe_stage::root.body[27].body[1].body[0].exc::Call

Source: `infra/agentinfra/process.py:205`; AST `b5f25fe17665344e6a8b111d77db169da134bb744b37ce5cb5d8a871774257e4`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ValueError. Outputs/bindings: (none).
Calls/effect boundaries: ValueError.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[27].body[1].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_recipe_stage::root.body[27].body[2]::Assign

Source: `infra/agentinfra/process.py:206`; AST `2cb31e24359069e6d48f279577f3872a44496aadb2b11b9425485ebf50f4ffa6`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _recipe_group, os. Outputs/bindings: token.
Calls/effect boundaries: _recipe_group.set, os.getpgrp.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[27].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_recipe_stage::root.body[27].body[2].value::Call

Source: `infra/agentinfra/process.py:206`; AST `66f270dfdc3834e1054ead0f79eb8d80f4bf00a1fda0970471060ceba1ba47c8`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _recipe_group, os. Outputs/bindings: (none).
Calls/effect boundaries: _recipe_group.set, os.getpgrp.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[27].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_recipe_stage::root.body[27].body[2].value.args[0]::Call

Source: `infra/agentinfra/process.py:206`; AST `b7282502e336f925e346653cf46be8b1d34f183317b09c626803580c84b724ab`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os. Outputs/bindings: (none).
Calls/effect boundaries: os.getpgrp.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[27].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_recipe_stage::root.body[27].body[3]::Try

Source: `infra/agentinfra/process.py:207`; AST `b93f92bfab96a4b2f71ef698bbd8648acf6ab6c95f646158311c5968935f4d6d`.

Rust module: `infra::agentinfra::process`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: _recipe_group, argv, capture_limit, cwd, env, logs, run_process, timeout, token, uuid. Outputs/bindings: logs.
Calls/effect boundaries: _recipe_group.reset, run_process, uuid.uuid4.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Try evaluation at root.body[27].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_recipe_stage::root.body[27].body[3].body[0]::Assign

Source: `infra/agentinfra/process.py:208`; AST `fbfafcb6b4d7c684333c6eb2a132fe209ebb966f28b88bde52f60fb72b633c80`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cwd, timeout, uuid. Outputs/bindings: logs.
Calls/effect boundaries: uuid.uuid4.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[27].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_recipe_stage::root.body[27].body[3].body[0].value.body.right.value::Call

Source: `infra/agentinfra/process.py:208`; AST `87eafda000cba758be33f767d487f36fa6a34917ff4cfe4cbd289edd7d07163b`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: uuid. Outputs/bindings: (none).
Calls/effect boundaries: uuid.uuid4.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[27].body[3].body[0].value.body.right.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_recipe_stage::root.body[27].body[3].body[1]::Return

Source: `infra/agentinfra/process.py:209`; AST `fd67fa7201f8be3304724d65c53c11f1b981a06ceff3516b6f865700d32c838c`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: argv, capture_limit, cwd, env, logs, run_process, timeout. Outputs/bindings: (none).
Calls/effect boundaries: run_process.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Return evaluation at root.body[27].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_recipe_stage::root.body[27].body[3].body[1].value::Call

Source: `infra/agentinfra/process.py:209`; AST `bab16c6fbafe540516ec0f206bfea17e81006792e79d69ae397794349eb3e0ba`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: argv, capture_limit, cwd, env, logs, run_process, timeout. Outputs/bindings: (none).
Calls/effect boundaries: run_process.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[27].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_recipe_stage::root.body[27].body[3].finalbody[0]::Expr

Source: `infra/agentinfra/process.py:212`; AST `163ed72f6fbfdeec4dbf3744039aa314a42635f0a4c016de21e45bb8408176d0`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _recipe_group, token. Outputs/bindings: (none).
Calls/effect boundaries: _recipe_group.reset.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[27].body[3].finalbody[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_recipe_stage::root.body[27].body[3].finalbody[0].value::Call

Source: `infra/agentinfra/process.py:212`; AST `c607bc0f771d35851089ae1dcb53be523b92b4b68bdd5709d680d33ffe92f995`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _recipe_group, token. Outputs/bindings: (none).
Calls/effect boundaries: _recipe_group.reset.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[27].body[3].finalbody[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28]::FunctionDef

Source: `infra/agentinfra/process.py:215`; AST `df4d75a42f41070c9b4119f6aba5b40f650b4e335fa2215777af1a17b2450a3f`.

Rust module: `infra::agentinfra::process`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: BaseException, Iterable, Mapping, Path, ProcessResult, RuntimeError, ValueError, _Capture, _assign_kill_job, _close_job, _kill_tree, _process_observer, _recipe_group, all, argv, capture_limit, child_env, command, cwd, datetime, defaults, env, finished, flags, float, inherited_group, int, isinstance, isolated_directory, isolated_home, item, job, key, len, minimal_subprocess_env, observer, os, output_directory, proc, result, started, started_wall, stderr_capture, stderr_path, stderr_thread, stdout_capture, stdout_path, stdout_thread, str, subprocess, tempfile, threading, time, timed_out, timeout, timezone, tuple, value. Outputs/bindings: child_env, command, defaults, finished, flags, inherited_group, isolated_directory, isolated_home, item, job, key, observer, proc, result, started, started_wall, stderr_capture, stderr_path, stderr_thread, stdout_capture, stdout_path, stdout_thread, timed_out, value.
Calls/effect boundaries: Path, Path(child_env[key]).mkdir, ProcessResult, RuntimeError, ValueError, _Capture, _assign_kill_job, _close_job, _kill_tree, _process_observer.get, _recipe_group.get, all, child_env.setdefault, cwd.resolve, datetime.now, datetime.now(timezone.utc).isoformat, defaults.items, float, int, isinstance, len, minimal_subprocess_env, observer, output_directory.mkdir, proc.stderr.close, proc.stdout.close, proc.wait, stderr_capture.digest.hexdigest, stderr_capture.text, stderr_path.resolve, stderr_thread.is_alive, stderr_thread.join, stderr_thread.start, stdout_capture.digest.hexdigest, stdout_capture.text, stdout_path.resolve, stdout_thread.is_alive, stdout_thread.join, stdout_thread.start, str, subprocess.Popen, tempfile.TemporaryDirectory, threading.Thread, time.monotonic, tuple.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered FunctionDef evaluation at root.body[28]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[0]::Assign

Source: `infra/agentinfra/process.py:228`; AST `f9a59b2a150996bf0874a3a3ef87891d3045808675919b497967f0ce732880f1`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _recipe_group. Outputs/bindings: inherited_group.
Calls/effect boundaries: _recipe_group.get.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[28].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[0].value::Call

Source: `infra/agentinfra/process.py:228`; AST `498173db67a373f48f0bf77bac93a0dc2b60b8c40b81d426a77c9b9bdabf5667`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _recipe_group. Outputs/bindings: (none).
Calls/effect boundaries: _recipe_group.get.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[1]::Assign

Source: `infra/agentinfra/process.py:229`; AST `a6401804f1fafdb7ee70f6b908e155d0ce6215585043d6d597b9fda680849a3e`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: argv, tuple. Outputs/bindings: command.
Calls/effect boundaries: tuple.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[28].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[1].value::Call

Source: `infra/agentinfra/process.py:229`; AST `6caa7f248d9150e4b08b91615eafec18b004e62c4ed91fba8aa3998614ba833d`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: argv, tuple. Outputs/bindings: (none).
Calls/effect boundaries: tuple.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[2]::If

Source: `infra/agentinfra/process.py:230`; AST `546f74e39db6ad3751b2da7ac890ab80f5f27bdbab5bf460c9673dc96845cf43`.

Rust module: `infra::agentinfra::process`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ValueError, all, command, isinstance, item, str. Outputs/bindings: item.
Calls/effect boundaries: ValueError, all, isinstance.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[28].body[2]; no call, error or mutation may be omitted. Condition: not command or not all((isinstance(item, str) and item for item in command))
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[2].test.values[1].operand::Call

Source: `infra/agentinfra/process.py:230`; AST `a5a4c80f62c0900ba749a879eb99570d53e2d6f1d94173a2be79d4d76ecf0616`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, command, isinstance, item, str. Outputs/bindings: item.
Calls/effect boundaries: all, isinstance.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[2].test.values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[2].test.values[1].operand.args[0]::GeneratorExp

Source: `infra/agentinfra/process.py:230`; AST `ba993707c37dfd46922118f309383534b88949fb02cfc1f6cf0ae2aa917d46a5`.

Rust module: `infra::agentinfra::process`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: command, isinstance, item, str. Outputs/bindings: item.
Calls/effect boundaries: isinstance.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[28].body[2].test.values[1].operand.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[2].test.values[1].operand.args[0].elt.values[0]::Call

Source: `infra/agentinfra/process.py:230`; AST `f4f66d21edf6502e42eb466f8ae56934935ef82237f1d15da20d98a4721529b0`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, item, str. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[2].test.values[1].operand.args[0].elt.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[2].body[0]::Raise

Source: `infra/agentinfra/process.py:231`; AST `13bd085c89e72efcda0bb546204ac7b24a648b18fd19d87b644df4eba5451e71`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ValueError. Outputs/bindings: (none).
Calls/effect boundaries: ValueError.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[28].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[2].body[0].exc::Call

Source: `infra/agentinfra/process.py:231`; AST `924cfcda385fbe83287046681088ad39646c272eb1754821ee882e1d8155dc5e`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ValueError. Outputs/bindings: (none).
Calls/effect boundaries: ValueError.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[2].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[3]::If

Source: `infra/agentinfra/process.py:232`; AST `5eb9d5df887881c56438a502432782ee461b2e49477b2ecf23e04c9773d4cec2`.

Rust module: `infra::agentinfra::process`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ValueError, float, timeout. Outputs/bindings: (none).
Calls/effect boundaries: ValueError, float.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[28].body[3]; no call, error or mutation may be omitted. Condition: timeout is not None and (timeout <= 0 or timeout != timeout or timeout == float('inf'))
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[3].test.values[1].values[2].comparators[0]::Call

Source: `infra/agentinfra/process.py:232`; AST `5351252e8d825a36374a8c9dcb78a6daead302dce402af2a4c74c8d17167f46a`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: float. Outputs/bindings: (none).
Calls/effect boundaries: float.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[3].test.values[1].values[2].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[3].body[0]::Raise

Source: `infra/agentinfra/process.py:233`; AST `02f278d0e41b82b66762d557a68215c8919786e93526100635534e0c0c5f199d`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ValueError. Outputs/bindings: (none).
Calls/effect boundaries: ValueError.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[28].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[3].body[0].exc::Call

Source: `infra/agentinfra/process.py:233`; AST `c41a8e1c36bf5caed745982df5a7af563fd9e7f84422d9871db219a4730673df`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ValueError. Outputs/bindings: (none).
Calls/effect boundaries: ValueError.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[3].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[4]::If

Source: `infra/agentinfra/process.py:234`; AST `2c21ee6527eb43c45eecaa023b077134c05994ad18f998fe1fec24f8484b2f35`.

Rust module: `infra::agentinfra::process`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ValueError, capture_limit. Outputs/bindings: (none).
Calls/effect boundaries: ValueError.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[28].body[4]; no call, error or mutation may be omitted. Condition: capture_limit < 1024
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[4].body[0]::Raise

Source: `infra/agentinfra/process.py:235`; AST `cf6f803012426bc12b979ddc8a6c88a8b673e02361a328aa484971cc3e5a8201`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ValueError. Outputs/bindings: (none).
Calls/effect boundaries: ValueError.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[28].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[4].body[0].exc::Call

Source: `infra/agentinfra/process.py:235`; AST `2be7ef1a1cd6ae7728ca2d71aa7ce52e08acea7f8bba0d40fb329d1e54045a40`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ValueError. Outputs/bindings: (none).
Calls/effect boundaries: ValueError.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[4].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[5]::If

Source: `infra/agentinfra/process.py:236`; AST `342f54dedc7d173edaef88e9d55590adf547fb2f1ad8f870116f8cc29a8d5414`.

Rust module: `infra::agentinfra::process`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: output_directory. Outputs/bindings: (none).
Calls/effect boundaries: output_directory.mkdir.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[28].body[5]; no call, error or mutation may be omitted. Condition: output_directory is not None
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[5].body[0]::Expr

Source: `infra/agentinfra/process.py:237`; AST `94b79ed6ed2e6cc9f06acf21fa788126d9929a1acb160a69ec35653e984eccfc`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: output_directory. Outputs/bindings: (none).
Calls/effect boundaries: output_directory.mkdir.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[28].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[5].body[0].value::Call

Source: `infra/agentinfra/process.py:237`; AST `69425baaba4123efa24a0294e409882aa395b70781048f786036b04c2801f107`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: output_directory. Outputs/bindings: (none).
Calls/effect boundaries: output_directory.mkdir.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[6]::Assign

Source: `infra/agentinfra/process.py:238`; AST `5163984b2ec72e97e43542a0ddea850df6bf8228f65e026ef40c981cbf689ea0`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: output_directory. Outputs/bindings: stdout_path.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[28].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[7]::Assign

Source: `infra/agentinfra/process.py:239`; AST `8269e26362ddb838fcfe8c3f81732066bb174a526f65af25ca5db60a443dd946`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: output_directory. Outputs/bindings: stderr_path.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[28].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[8]::Assign

Source: `infra/agentinfra/process.py:240`; AST `e80ae23b5e14433d4838c60460ae14cf306d57e8a2da9e183464ad34f8a6db18`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: datetime, timezone. Outputs/bindings: started_wall.
Calls/effect boundaries: datetime.now, datetime.now(timezone.utc).isoformat.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[28].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[8].value::Call

Source: `infra/agentinfra/process.py:240`; AST `1b110a252c57d72f572683a982afb6160b9f4ceeec701cae738dc9a58366722d`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: datetime, timezone. Outputs/bindings: (none).
Calls/effect boundaries: datetime.now, datetime.now(timezone.utc).isoformat.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[8].value.func.value::Call

Source: `infra/agentinfra/process.py:240`; AST `7d005ec5c408397d72b2a5196d97d2fa96db0d64d31cc38e5bd68f36bf7badb9`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: datetime, timezone. Outputs/bindings: (none).
Calls/effect boundaries: datetime.now.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[8].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[9]::Assign

Source: `infra/agentinfra/process.py:241`; AST `ffb01939a1744166f8e8b1b6999b1f72c7d696dab355b4b68f83c3a867bfd6b0`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: time. Outputs/bindings: started.
Calls/effect boundaries: time.monotonic.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[28].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[9].value::Call

Source: `infra/agentinfra/process.py:241`; AST `1518ec519851d0a5084168b533bc641ad5d2ce5a406bada9f9d7d919d82e5b92`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: time. Outputs/bindings: (none).
Calls/effect boundaries: time.monotonic.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[10]::Assign

Source: `infra/agentinfra/process.py:242`; AST `856b409688fc13106d36435ae5897c244df41d39464ec2ff3d9dbf644c5329bc`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: os, subprocess. Outputs/bindings: flags.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[28].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11]::With

Source: `infra/agentinfra/process.py:243`; AST `25f9ef5c46620d28d5dab435cfde21d82c4d968582ecfaf5d73853f602ffa4f5`.

Rust module: `infra::agentinfra::process`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: BaseException, Path, ProcessResult, RuntimeError, _Capture, _assign_kill_job, _close_job, _kill_tree, _process_observer, capture_limit, child_env, command, cwd, datetime, defaults, env, finished, flags, inherited_group, int, isolated_directory, isolated_home, job, key, len, minimal_subprocess_env, observer, os, proc, started, started_wall, stderr_capture, stderr_path, stderr_thread, stdout_capture, stdout_path, stdout_thread, str, subprocess, tempfile, threading, time, timed_out, timeout, timezone, value. Outputs/bindings: child_env, defaults, finished, isolated_directory, isolated_home, job, key, observer, proc, result, stderr_capture, stderr_thread, stdout_capture, stdout_thread, timed_out, value.
Calls/effect boundaries: Path, Path(child_env[key]).mkdir, ProcessResult, RuntimeError, _Capture, _assign_kill_job, _close_job, _kill_tree, _process_observer.get, child_env.setdefault, cwd.resolve, datetime.now, datetime.now(timezone.utc).isoformat, defaults.items, int, len, minimal_subprocess_env, observer, proc.stderr.close, proc.stdout.close, proc.wait, stderr_capture.digest.hexdigest, stderr_capture.text, stderr_path.resolve, stderr_thread.is_alive, stderr_thread.join, stderr_thread.start, stdout_capture.digest.hexdigest, stdout_capture.text, stdout_path.resolve, stdout_thread.is_alive, stdout_thread.join, stdout_thread.start, str, subprocess.Popen, tempfile.TemporaryDirectory, threading.Thread, time.monotonic.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered With evaluation at root.body[28].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].items[0].context_expr::Call

Source: `infra/agentinfra/process.py:243`; AST `b9e7b31a04a27d51bb87884551f408bd07e3965242bac7285432a7d9f8ca4925`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[0]::Assign

Source: `infra/agentinfra/process.py:244`; AST `327e560e470cef8a9f2f1e4a191db00c41248246b387daefd2553b109f49b87f`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, isolated_directory. Outputs/bindings: isolated_home.
Calls/effect boundaries: Path.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[28].body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[0].value::Call

Source: `infra/agentinfra/process.py:244`; AST `b2f6a130bd554af520a1024bc9060f48197985be49d88e3291a57fe9cc6ef056`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, isolated_directory. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[1]::Assign

Source: `infra/agentinfra/process.py:245`; AST `b163c671b159629e94c7f34d00549f0594c4684ae96dc186b2f7b0750e06ee18`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: env, minimal_subprocess_env. Outputs/bindings: child_env.
Calls/effect boundaries: minimal_subprocess_env.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[28].body[11].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[1].value::Call

Source: `infra/agentinfra/process.py:245`; AST `6cea2c1d25d7f4e901f1960a0bd12e8e9f094adeeac7ff6dae50c656f448eacd`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: env, minimal_subprocess_env. Outputs/bindings: (none).
Calls/effect boundaries: minimal_subprocess_env.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[2]::Assign

Source: `infra/agentinfra/process.py:246`; AST `f330563ba893b0b537d4bdd5b85ab6d9c1626ff3551a5cb1f163e152bb23e6fa`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: isolated_home, len, str. Outputs/bindings: defaults.
Calls/effect boundaries: len, str.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[28].body[11].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[2].value.values[0]::Call

Source: `infra/agentinfra/process.py:247`; AST `31e88f68effb0abf10d639fd9ff1a980d4e5b6ab4a44abcdab3c2b6a6f476a62`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isolated_home, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[2].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[2].value.values[1]::Call

Source: `infra/agentinfra/process.py:248`; AST `31e88f68effb0abf10d639fd9ff1a980d4e5b6ab4a44abcdab3c2b6a6f476a62`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isolated_home, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[2].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[2].value.values[3].body.value::Call

Source: `infra/agentinfra/process.py:250`; AST `31e88f68effb0abf10d639fd9ff1a980d4e5b6ab4a44abcdab3c2b6a6f476a62`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isolated_home, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[2].value.values[3].body.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[2].value.values[3].body.slice.lower::Call

Source: `infra/agentinfra/process.py:250`; AST `5a6125775c465b0213023e0f0e92b5dda13d40bece8122188aa83ab7dee3865b`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isolated_home, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[2].value.values[3].body.slice.lower; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[2].value.values[3].orelse::Call

Source: `infra/agentinfra/process.py:250`; AST `31e88f68effb0abf10d639fd9ff1a980d4e5b6ab4a44abcdab3c2b6a6f476a62`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isolated_home, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[2].value.values[3].orelse; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[2].value.values[4]::Call

Source: `infra/agentinfra/process.py:251`; AST `bb08b7a84b460cdd81fbf29e4bed45af8c47346af349fee7366ec3d81408ebd7`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isolated_home, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[2].value.values[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[2].value.values[5]::Call

Source: `infra/agentinfra/process.py:252`; AST `48c27ca34ee117805f64941d636c0f2b9922d03d1436f580a1536842efffb2f0`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isolated_home, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[2].value.values[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[2].value.values[6]::Call

Source: `infra/agentinfra/process.py:253`; AST `fbbe5b943d3b4df9a7c7be0b27b21b71aecc26489f20d6f41476adefc99e2f0a`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isolated_home, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[2].value.values[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[2].value.values[7]::Call

Source: `infra/agentinfra/process.py:254`; AST `7bd95a363d95548dee33a3e8c1c416d61ca9fb0612e9ee93caca276cded28d1b`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isolated_home, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[2].value.values[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[2].value.values[8]::Call

Source: `infra/agentinfra/process.py:255`; AST `b5cbe7ec6e9ed90e032523922c1c9069cba3c0746c82036de7746603cd3c9750`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isolated_home, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[2].value.values[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[3]::For

Source: `infra/agentinfra/process.py:257`; AST `0a1c2bb78969f3bd00d87c6413461b7db9c1ed21a28980938faedd407f13a113`.

Rust module: `infra::agentinfra::process`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: child_env, defaults, key, value. Outputs/bindings: key, value.
Calls/effect boundaries: child_env.setdefault, defaults.items.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered For evaluation at root.body[28].body[11].body[3]; no call, error or mutation may be omitted. Iteration: (key, value) in defaults.items()
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[3].iter::Call

Source: `infra/agentinfra/process.py:257`; AST `5c8355624206d4d5daf58f43da914e545e81b9b8c39e1183daa78e071d87dc7c`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: defaults. Outputs/bindings: (none).
Calls/effect boundaries: defaults.items.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[3].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[3].body[0]::Expr

Source: `infra/agentinfra/process.py:258`; AST `8411fb60f26b86002b2bfb38fdf74b4f50f0f90a7941b0784954361018e35f26`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: child_env, key, value. Outputs/bindings: (none).
Calls/effect boundaries: child_env.setdefault.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[28].body[11].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[3].body[0].value::Call

Source: `infra/agentinfra/process.py:258`; AST `8fa1062d21a64818b3f01dadbc81d45bdab2e076905984bc5841400a38319963`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: child_env, key, value. Outputs/bindings: (none).
Calls/effect boundaries: child_env.setdefault.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[4]::For

Source: `infra/agentinfra/process.py:259`; AST `b5fa7ef69efbf356ed7308d7711456568baef301e0da389481450f172b6f468b`.

Rust module: `infra::agentinfra::process`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: Path, child_env, key. Outputs/bindings: key.
Calls/effect boundaries: Path, Path(child_env[key]).mkdir.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered For evaluation at root.body[28].body[11].body[4]; no call, error or mutation may be omitted. Iteration: key in ('APPDATA', 'LOCALAPPDATA', 'XDG_CACHE_HOME', 'XONSH_DATA_DIR', 'XONSH_CACHE_DIR')
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[4].body[0]::Expr

Source: `infra/agentinfra/process.py:266`; AST `7c88bdf0135e2d9dd72ae06c01e2e0fdd55bd4e27946cc47e3eb97c02ca087b5`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, child_env, key. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(child_env[key]).mkdir.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[28].body[11].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[4].body[0].value::Call

Source: `infra/agentinfra/process.py:266`; AST `c919ee334503e764ba6d6c2f80514a09d89f3ff88e8ed10ef40612a8f7eb857f`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, child_env, key. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(child_env[key]).mkdir.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[4].body[0].value.func.value::Call

Source: `infra/agentinfra/process.py:266`; AST `c74094e45327cc6703a67f996a1ed20fb1a7332f22270e8b0ccf0c6474019e75`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, child_env, key. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[4].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[5]::Assign

Source: `infra/agentinfra/process.py:267`; AST `2e2ebeabcf7257d9e7c1bba57b2a235a0413a21a26e18fd15dff25e7f8baaa9e`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: child_env, command, cwd, flags, inherited_group, os, subprocess. Outputs/bindings: proc.
Calls/effect boundaries: subprocess.Popen.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[28].body[11].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[5].value::Call

Source: `infra/agentinfra/process.py:267`; AST `8fa7212c66284d8ec3b84d0b237b678c480a3eb420f37b28074a0aa9fd881a91`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: child_env, command, cwd, flags, inherited_group, os, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: subprocess.Popen.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[6]::Assign

Source: `infra/agentinfra/process.py:278`; AST `d77dcd3d044c9c0f92be290a73dcb4640c6353b631986380a767a56b7205e3a1`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _assign_kill_job, proc. Outputs/bindings: job.
Calls/effect boundaries: _assign_kill_job.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[28].body[11].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[6].value::Call

Source: `infra/agentinfra/process.py:278`; AST `14c5cbf058b1b0e4efe3f2b2034e27ce1239ca377813f47b2d4bf4671f0372ef`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _assign_kill_job, proc. Outputs/bindings: (none).
Calls/effect boundaries: _assign_kill_job.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[7]::Assign

Source: `infra/agentinfra/process.py:279`; AST `a23fe022603f0cc1e1033a5428a845c1940c4b1597821cf173a7e149e8ef8cbb`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _Capture, capture_limit, stdout_path. Outputs/bindings: stdout_capture.
Calls/effect boundaries: _Capture.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[28].body[11].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[7].value::Call

Source: `infra/agentinfra/process.py:279`; AST `1c1736ebe89a38baee758cf912c0b29cd0305287375fc54b66b8bbcd37ea6e8d`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _Capture, capture_limit, stdout_path. Outputs/bindings: (none).
Calls/effect boundaries: _Capture.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[8]::Assign

Source: `infra/agentinfra/process.py:280`; AST `1fe17f9c28c00d339655f34527cd97cd8571dd05f70a639850504ce28bc09bda`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _Capture, capture_limit, stderr_path. Outputs/bindings: stderr_capture.
Calls/effect boundaries: _Capture.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[28].body[11].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[8].value::Call

Source: `infra/agentinfra/process.py:280`; AST `b2a1615b04d7e7a91e38cf89ec92b3be015dc510702881afa47917da5a377749`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _Capture, capture_limit, stderr_path. Outputs/bindings: (none).
Calls/effect boundaries: _Capture.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[9]::Assign

Source: `infra/agentinfra/process.py:281`; AST `0d93d43bd3c606464e699b2515b664749c8dfc582c72317cba82bcee9971aa53`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: proc, stdout_capture, threading. Outputs/bindings: stdout_thread.
Calls/effect boundaries: threading.Thread.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[28].body[11].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[9].value::Call

Source: `infra/agentinfra/process.py:281`; AST `11be4d5e3b49cb5c75cc2ad34a89b2179874acaf736c6d560b033e52bed5fe5e`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: proc, stdout_capture, threading. Outputs/bindings: (none).
Calls/effect boundaries: threading.Thread.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[10]::Assign

Source: `infra/agentinfra/process.py:282`; AST `c182c6400304db1e4acfb78cc47e1aaaec6cd64d05c6893d7ab3bb29aa3e776c`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: proc, stderr_capture, threading. Outputs/bindings: stderr_thread.
Calls/effect boundaries: threading.Thread.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[28].body[11].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[10].value::Call

Source: `infra/agentinfra/process.py:282`; AST `4352e4ef1697d610d69f2deebe8c728795f4f2a1ae6c65853421b91f5622ef6c`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: proc, stderr_capture, threading. Outputs/bindings: (none).
Calls/effect boundaries: threading.Thread.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[11]::Expr

Source: `infra/agentinfra/process.py:283`; AST `bbdad6ce421a6451786f10be56b08de0fb82cc3c1021103c0430c8ad4795a32b`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: stdout_thread. Outputs/bindings: (none).
Calls/effect boundaries: stdout_thread.start.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[28].body[11].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[11].value::Call

Source: `infra/agentinfra/process.py:283`; AST `c8ba5fb7ba927fe9d664b0f6985bc5aafcccbe2cd845fd97a86e979dac2b54fa`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: stdout_thread. Outputs/bindings: (none).
Calls/effect boundaries: stdout_thread.start.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[12]::Expr

Source: `infra/agentinfra/process.py:284`; AST `3da0ee4385f017e2756630fac09db88868ecd8f0125ff0cc722feecf6b5be141`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: stderr_thread. Outputs/bindings: (none).
Calls/effect boundaries: stderr_thread.start.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[28].body[11].body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[12].value::Call

Source: `infra/agentinfra/process.py:284`; AST `00bd72d4411f93dfd6d79b75cc3c5983a5517155fe0b12aad1971f13e9937c19`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: stderr_thread. Outputs/bindings: (none).
Calls/effect boundaries: stderr_thread.start.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[13]::Assign

Source: `infra/agentinfra/process.py:285`; AST `d83728042a9718e033779a0587464b9a2215aaa8b0a4defd795488624f23ce82`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: timed_out.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[28].body[11].body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14]::Try

Source: `infra/agentinfra/process.py:286`; AST `5051680abd28dba07fb71389574568f927fde1d1bb18ef86b8e3a01418df8edb`.

Rust module: `infra::agentinfra::process`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: BaseException, RuntimeError, _close_job, _kill_tree, _process_observer, inherited_group, job, observer, proc, stderr_thread, stdout_thread, subprocess, timeout. Outputs/bindings: job, observer, timed_out.
Calls/effect boundaries: RuntimeError, _close_job, _kill_tree, _process_observer.get, observer, proc.stderr.close, proc.stdout.close, proc.wait, stderr_thread.is_alive, stderr_thread.join, stdout_thread.is_alive, stdout_thread.join.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Try evaluation at root.body[28].body[11].body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].body[0]::Assign

Source: `infra/agentinfra/process.py:287`; AST `3f5d6098b3c964221c7e767d1b334d0332469bbfb6d0ca732c0d0d709fe15753`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _process_observer. Outputs/bindings: observer.
Calls/effect boundaries: _process_observer.get.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[28].body[11].body[14].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].body[0].value::Call

Source: `infra/agentinfra/process.py:287`; AST `071600788f4bed9ec0a4f36eff1084d0f879581f444ef7c02eb0b21863610779`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _process_observer. Outputs/bindings: (none).
Calls/effect boundaries: _process_observer.get.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[14].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].body[1]::If

Source: `infra/agentinfra/process.py:288`; AST `08499033c8e0b6a055b6c8dac1ffe8ebc3c560ba471d63f595d27c8529a99146`.

Rust module: `infra::agentinfra::process`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: observer, proc. Outputs/bindings: (none).
Calls/effect boundaries: observer.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[28].body[11].body[14].body[1]; no call, error or mutation may be omitted. Condition: observer is not None
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].body[1].body[0]::Expr

Source: `infra/agentinfra/process.py:289`; AST `bb0992d579ca854458c90fac2e38246a97ab7da5930a7a038b3345581c229359`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observer, proc. Outputs/bindings: (none).
Calls/effect boundaries: observer.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[28].body[11].body[14].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].body[1].body[0].value::Call

Source: `infra/agentinfra/process.py:289`; AST `bd1894cdff511037afd5edd922d3ec317268339234f90016770bc37c5de4a960`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observer, proc. Outputs/bindings: (none).
Calls/effect boundaries: observer.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[14].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].body[2]::Expr

Source: `infra/agentinfra/process.py:290`; AST `190002f3d1d8b2381d8179ac97aa6dbd4958d6338d3a05f604ed00946d56f8a2`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: proc, timeout. Outputs/bindings: (none).
Calls/effect boundaries: proc.wait.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[28].body[11].body[14].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].body[2].value::Call

Source: `infra/agentinfra/process.py:290`; AST `4b71b80539a60955cc15393e38757e135ed9a3327e0eb47c15970672a8b764e6`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: proc, timeout. Outputs/bindings: (none).
Calls/effect boundaries: proc.wait.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[14].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].handlers[0]::ExceptHandler

Source: `infra/agentinfra/process.py:291`; AST `096a5c6a2e4583bf91793398b4c75572d27043a1edc15acdc08962dc60d4c829`.

Rust module: `infra::agentinfra::process`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: _kill_tree, inherited_group, job, proc, subprocess. Outputs/bindings: timed_out.
Calls/effect boundaries: _kill_tree, proc.wait.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[28].body[11].body[14].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].handlers[0].body[0]::Assign

Source: `infra/agentinfra/process.py:292`; AST `4a26802e42ddce6a979f0a8a3afbf2000b33003f9a1991e037b0472056e05bfd`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: timed_out.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[28].body[11].body[14].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].handlers[0].body[1]::Expr

Source: `infra/agentinfra/process.py:293`; AST `817366d54f32565eea75aba2a64f26f2b7a91212b30ea4213d6638fc99cff7e2`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _kill_tree, inherited_group, job, proc. Outputs/bindings: (none).
Calls/effect boundaries: _kill_tree.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[28].body[11].body[14].handlers[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].handlers[0].body[1].value::Call

Source: `infra/agentinfra/process.py:293`; AST `10d9c940d7a92db3e6dc72322e3d7e72bfbf7c7b9010383ec6d3473943f0e155`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _kill_tree, inherited_group, job, proc. Outputs/bindings: (none).
Calls/effect boundaries: _kill_tree.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[14].handlers[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].handlers[0].body[2]::Expr

Source: `infra/agentinfra/process.py:294`; AST `db4f33c8110184801470e9f61c5b3ba700e3d2358ab6bbcd7baac7307480ea3b`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: proc. Outputs/bindings: (none).
Calls/effect boundaries: proc.wait.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[28].body[11].body[14].handlers[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].handlers[0].body[2].value::Call

Source: `infra/agentinfra/process.py:294`; AST `c40a4c817bf2fc8db53fe84a8c2221e473cf88a7d6239478b15c1167190e5af1`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: proc. Outputs/bindings: (none).
Calls/effect boundaries: proc.wait.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[14].handlers[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].handlers[1]::ExceptHandler

Source: `infra/agentinfra/process.py:295`; AST `e7b134b3f77bca8c516a0bffb92621baadefa360cfa687818ada660f24c303c8`.

Rust module: `infra::agentinfra::process`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: BaseException, _kill_tree, inherited_group, job, proc. Outputs/bindings: (none).
Calls/effect boundaries: _kill_tree, proc.wait.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[28].body[11].body[14].handlers[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].handlers[1].body[0]::Expr

Source: `infra/agentinfra/process.py:296`; AST `817366d54f32565eea75aba2a64f26f2b7a91212b30ea4213d6638fc99cff7e2`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _kill_tree, inherited_group, job, proc. Outputs/bindings: (none).
Calls/effect boundaries: _kill_tree.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[28].body[11].body[14].handlers[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].handlers[1].body[0].value::Call

Source: `infra/agentinfra/process.py:296`; AST `10d9c940d7a92db3e6dc72322e3d7e72bfbf7c7b9010383ec6d3473943f0e155`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _kill_tree, inherited_group, job, proc. Outputs/bindings: (none).
Calls/effect boundaries: _kill_tree.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[14].handlers[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].handlers[1].body[1]::Expr

Source: `infra/agentinfra/process.py:297`; AST `db4f33c8110184801470e9f61c5b3ba700e3d2358ab6bbcd7baac7307480ea3b`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: proc. Outputs/bindings: (none).
Calls/effect boundaries: proc.wait.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[28].body[11].body[14].handlers[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].handlers[1].body[1].value::Call

Source: `infra/agentinfra/process.py:297`; AST `c40a4c817bf2fc8db53fe84a8c2221e473cf88a7d6239478b15c1167190e5af1`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: proc. Outputs/bindings: (none).
Calls/effect boundaries: proc.wait.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[14].handlers[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].handlers[1].body[2]::Raise

Source: `infra/agentinfra/process.py:298`; AST `ba28128c14dfbd0a9062c0dbab42ad6c52ecf0767df6b67576deb1dbbfdd038d`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[28].body[11].body[14].handlers[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].finalbody[0]::Expr

Source: `infra/agentinfra/process.py:302`; AST `a432349d312f1a7a993c20dc8df132b5641707b38d8b89c06f15f701388d8813`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _close_job, job. Outputs/bindings: (none).
Calls/effect boundaries: _close_job.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[28].body[11].body[14].finalbody[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].finalbody[0].value::Call

Source: `infra/agentinfra/process.py:302`; AST `ed2fdb90c7d14be4a4757523ce8bf86199557a7a3e03b7f574d2dbbf977df9e5`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _close_job, job. Outputs/bindings: (none).
Calls/effect boundaries: _close_job.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[14].finalbody[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].finalbody[1]::Assign

Source: `infra/agentinfra/process.py:303`; AST `4a33da1c87482bec6a386cd2c9168c9a850b9e08f4f40c5cdcf0371150b548bc`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: job.
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[28].body[11].body[14].finalbody[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].finalbody[2]::Expr

Source: `infra/agentinfra/process.py:304`; AST `e4ed61132fb3da70b73f993a16613b6747ba94e74d57c1cc5c824eb4329d479f`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: stdout_thread. Outputs/bindings: (none).
Calls/effect boundaries: stdout_thread.join.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[28].body[11].body[14].finalbody[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].finalbody[2].value::Call

Source: `infra/agentinfra/process.py:304`; AST `04e32b2e73491b0b30c538ad352dc4583e19558de7eb6ac3e56c9e38e0c560d4`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: stdout_thread. Outputs/bindings: (none).
Calls/effect boundaries: stdout_thread.join.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[14].finalbody[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].finalbody[3]::Expr

Source: `infra/agentinfra/process.py:305`; AST `caa223db906435141183d93d7154c6e4f12750b426ab6f675901b84c1d71bc64`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: stderr_thread. Outputs/bindings: (none).
Calls/effect boundaries: stderr_thread.join.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[28].body[11].body[14].finalbody[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].finalbody[3].value::Call

Source: `infra/agentinfra/process.py:305`; AST `a5a5b41c8e25823ec59ccfb10cb0f2344ded7633bfcaf3e283989074faf97051`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: stderr_thread. Outputs/bindings: (none).
Calls/effect boundaries: stderr_thread.join.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[14].finalbody[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].finalbody[4]::If

Source: `infra/agentinfra/process.py:306`; AST `05d3ad757169f6c26733c1a08f2216275bdd69d37c9d51852f74be01a94edb94`.

Rust module: `infra::agentinfra::process`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: RuntimeError, _kill_tree, inherited_group, job, proc, stderr_thread, stdout_thread. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError, _kill_tree, stderr_thread.is_alive, stdout_thread.is_alive.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[28].body[11].body[14].finalbody[4]; no call, error or mutation may be omitted. Condition: stdout_thread.is_alive() or stderr_thread.is_alive()
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].finalbody[4].test.values[0]::Call

Source: `infra/agentinfra/process.py:306`; AST `b553e26bbe45307e55915042492494cd744fc3965e9cb29629ca807fb56771b7`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: stdout_thread. Outputs/bindings: (none).
Calls/effect boundaries: stdout_thread.is_alive.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[14].finalbody[4].test.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].finalbody[4].test.values[1]::Call

Source: `infra/agentinfra/process.py:306`; AST `f5ca4ae55ebcdfddaff9b7bed1681c90fd5cc0658a3f43b2832c8c46fc84ea8b`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: stderr_thread. Outputs/bindings: (none).
Calls/effect boundaries: stderr_thread.is_alive.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[14].finalbody[4].test.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].finalbody[4].body[0]::Expr

Source: `infra/agentinfra/process.py:307`; AST `817366d54f32565eea75aba2a64f26f2b7a91212b30ea4213d6638fc99cff7e2`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _kill_tree, inherited_group, job, proc. Outputs/bindings: (none).
Calls/effect boundaries: _kill_tree.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[28].body[11].body[14].finalbody[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].finalbody[4].body[0].value::Call

Source: `infra/agentinfra/process.py:307`; AST `10d9c940d7a92db3e6dc72322e3d7e72bfbf7c7b9010383ec6d3473943f0e155`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _kill_tree, inherited_group, job, proc. Outputs/bindings: (none).
Calls/effect boundaries: _kill_tree.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[14].finalbody[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].finalbody[4].body[1]::Raise

Source: `infra/agentinfra/process.py:308`; AST `b6d8f3afdf01b565aa06c80262a06ac4769152426195206d9a8f1afe36c18e28`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: RuntimeError. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[28].body[11].body[14].finalbody[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].finalbody[4].body[1].exc::Call

Source: `infra/agentinfra/process.py:308`; AST `00baa8b32ed90d971024fd910e8987e6f82b009e3be14a74058371c6cf1b4eca`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: RuntimeError. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[14].finalbody[4].body[1].exc; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].finalbody[5]::Expr

Source: `infra/agentinfra/process.py:309`; AST `884b5612f3378f01b766123d9ce2e4d11dc4e2f72c0792fa07d254e9b6f8a96a`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: proc. Outputs/bindings: (none).
Calls/effect boundaries: proc.stdout.close.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[28].body[11].body[14].finalbody[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].finalbody[5].value::Call

Source: `infra/agentinfra/process.py:309`; AST `8effe89b2a9081e9e208e0dfdfb4d4900d058264a8de8a42efaf51b41b31124f`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: proc. Outputs/bindings: (none).
Calls/effect boundaries: proc.stdout.close.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[14].finalbody[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].finalbody[6]::Expr

Source: `infra/agentinfra/process.py:310`; AST `dcb5d7f68a980788efcff076de2084215eb4cd348fc9faa0df745eb487b90f59`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: proc. Outputs/bindings: (none).
Calls/effect boundaries: proc.stderr.close.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Expr evaluation at root.body[28].body[11].body[14].finalbody[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[14].finalbody[6].value::Call

Source: `infra/agentinfra/process.py:310`; AST `1cc76edec6d85862d875d5ca71a098daf51102d6a9c87ea586c7b5cb30ae5dfa`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: proc. Outputs/bindings: (none).
Calls/effect boundaries: proc.stderr.close.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[14].finalbody[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[15]::If

Source: `infra/agentinfra/process.py:311`; AST `67a218aa134734efd730c2d2ee2ac2469776873f9cf6aa3992f89629c96d28d7`.

Rust module: `infra::agentinfra::process`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: RuntimeError, stderr_capture, stdout_capture. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered If evaluation at root.body[28].body[11].body[15]; no call, error or mutation may be omitted. Condition: stdout_capture.error or stderr_capture.error
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[15].body[0]::Raise

Source: `infra/agentinfra/process.py:312`; AST `df6ddff313a25ff3b1a48b0dff72443b6537daf0fe562411dae3ac40e59cda8f`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: RuntimeError, stderr_capture, stdout_capture. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Raise evaluation at root.body[28].body[11].body[15].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[15].body[0].exc::Call

Source: `infra/agentinfra/process.py:312`; AST `98907ff667d73fe4a94eee876b9b664988b376b6faf28808f628627d364cca97`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: RuntimeError. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[15].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[16]::Assign

Source: `infra/agentinfra/process.py:313`; AST `81ccdcbf14b62e365def039a8e6f071346484172f99496a4a2fdd99bd0f1c3bd`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: time. Outputs/bindings: finished.
Calls/effect boundaries: time.monotonic.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[28].body[11].body[16]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[16].value::Call

Source: `infra/agentinfra/process.py:313`; AST `1518ec519851d0a5084168b533bc641ad5d2ce5a406bada9f9d7d919d82e5b92`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: time. Outputs/bindings: (none).
Calls/effect boundaries: time.monotonic.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[16].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[17]::Assign

Source: `infra/agentinfra/process.py:314`; AST `ee33f7fac1a5c5c44e330e21fa449520189778e6f51e2db43ccba028afdb3b5a`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ProcessResult, capture_limit, command, cwd, datetime, finished, int, proc, started, started_wall, stderr_capture, stderr_path, stdout_capture, stdout_path, str, timed_out, timezone. Outputs/bindings: result.
Calls/effect boundaries: ProcessResult, cwd.resolve, datetime.now, datetime.now(timezone.utc).isoformat, int, stderr_capture.digest.hexdigest, stderr_capture.text, stderr_path.resolve, stdout_capture.digest.hexdigest, stdout_capture.text, stdout_path.resolve, str.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Assign evaluation at root.body[28].body[11].body[17]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[17].value::Call

Source: `infra/agentinfra/process.py:314`; AST `c7bd8892cc2f8e666f6956857b870ce0d73b53bb6323c1ce77afaaef45b1824d`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ProcessResult, capture_limit, command, cwd, datetime, finished, int, proc, started, started_wall, stderr_capture, stderr_path, stdout_capture, stdout_path, str, timed_out, timezone. Outputs/bindings: (none).
Calls/effect boundaries: ProcessResult, cwd.resolve, datetime.now, datetime.now(timezone.utc).isoformat, int, stderr_capture.digest.hexdigest, stderr_capture.text, stderr_path.resolve, stdout_capture.digest.hexdigest, stdout_capture.text, stdout_path.resolve, str.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[17].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[17].value.keywords[1].value::Call

Source: `infra/agentinfra/process.py:316`; AST `9dbe6739b3f4af19122c7d4ce38c7b9c7a64474d22e47abc6e04c21cb85c9a1f`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cwd, str. Outputs/bindings: (none).
Calls/effect boundaries: cwd.resolve, str.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[17].value.keywords[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[17].value.keywords[1].value.args[0]::Call

Source: `infra/agentinfra/process.py:316`; AST `0474fc4d9848c20ff517f61571bfd44f3e1da964918f17e79a44ca1da83041ce`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cwd. Outputs/bindings: (none).
Calls/effect boundaries: cwd.resolve.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[17].value.keywords[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[17].value.keywords[2].value::Call

Source: `infra/agentinfra/process.py:317`; AST `345f35de68092a06e63f458b169e584f29ad6abf791b466015c531ae96251ccf`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: int, proc. Outputs/bindings: (none).
Calls/effect boundaries: int.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[17].value.keywords[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[17].value.keywords[3].value::Call

Source: `infra/agentinfra/process.py:318`; AST `c9fe5add9b6c30ccd0934bfb2dd1746295e516ba67db98bcc0cd05957faa154e`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: stdout_capture. Outputs/bindings: (none).
Calls/effect boundaries: stdout_capture.text.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[17].value.keywords[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[17].value.keywords[4].value::Call

Source: `infra/agentinfra/process.py:319`; AST `1203d64d4d07e28d03e4d060b4c91310fbabaafe38d944dee94b3b50faeb82c0`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: stderr_capture. Outputs/bindings: (none).
Calls/effect boundaries: stderr_capture.text.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[17].value.keywords[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[17].value.keywords[5].value::Call

Source: `infra/agentinfra/process.py:320`; AST `82367ed9d13f94d6ee9a989f01647a607819ab782a373fb457b8221dfb053a6d`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: stdout_capture. Outputs/bindings: (none).
Calls/effect boundaries: stdout_capture.digest.hexdigest.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[17].value.keywords[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[17].value.keywords[6].value::Call

Source: `infra/agentinfra/process.py:321`; AST `a01c594ad839b6040300265325323689a9ad3f4fce2577579772d849bb220759`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: stderr_capture. Outputs/bindings: (none).
Calls/effect boundaries: stderr_capture.digest.hexdigest.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[17].value.keywords[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[17].value.keywords[13].value::Call

Source: `infra/agentinfra/process.py:328`; AST `1b110a252c57d72f572683a982afb6160b9f4ceeec701cae738dc9a58366722d`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: datetime, timezone. Outputs/bindings: (none).
Calls/effect boundaries: datetime.now, datetime.now(timezone.utc).isoformat.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[17].value.keywords[13].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[17].value.keywords[13].value.func.value::Call

Source: `infra/agentinfra/process.py:328`; AST `7d005ec5c408397d72b2a5196d97d2fa96db0d64d31cc38e5bd68f36bf7badb9`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: datetime, timezone. Outputs/bindings: (none).
Calls/effect boundaries: datetime.now.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[17].value.keywords[13].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[17].value.keywords[15].value.body::Call

Source: `infra/agentinfra/process.py:330`; AST `7ddd8a05d35ba636ad8bfdbc48df57f057fa20fa374de9c00c5d6663b04b15bb`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: stdout_path, str. Outputs/bindings: (none).
Calls/effect boundaries: stdout_path.resolve, str.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[17].value.keywords[15].value.body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[17].value.keywords[15].value.body.args[0]::Call

Source: `infra/agentinfra/process.py:330`; AST `fba274420af44f7c044b555692d0326b6d81e6b815f31272aaea70c7a8df777e`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: stdout_path. Outputs/bindings: (none).
Calls/effect boundaries: stdout_path.resolve.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[17].value.keywords[15].value.body.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[17].value.keywords[16].value.body::Call

Source: `infra/agentinfra/process.py:331`; AST `fe6bdfabf499813acae8526066116765876f47b043d3ccb382181e626d4bed5b`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: stderr_path, str. Outputs/bindings: (none).
Calls/effect boundaries: stderr_path.resolve, str.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[17].value.keywords[16].value.body; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[11].body[17].value.keywords[16].value.body.args[0]::Call

Source: `infra/agentinfra/process.py:331`; AST `72a016ad67e8e7d5f6e8eb82fa80fba8446ba61042725f0cf732200d6f16d75b`.

Rust module: `infra::agentinfra::process`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: stderr_path. Outputs/bindings: (none).
Calls/effect boundaries: stderr_path.resolve.
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Call evaluation at root.body[28].body[11].body[17].value.keywords[16].value.body.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/process.py::module::run_process::root.body[28].body[12]::Return

Source: `infra/agentinfra/process.py:333`; AST `7b1d642d8354b03513d85ddd38bf4e4911c5b147b5b68f50fd12c2072903af3e`.

Rust module: `infra::agentinfra::process`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, contextlib, contextvars, ctypes, ctypes.wintypes, dataclasses, datetime, hashlib, os, pathlib, security, signal, subprocess, tempfile, threading, time, typing, uuid.

Invariants: Preserve ordered Return evaluation at root.body[28].body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::sync plus OS file locks; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
