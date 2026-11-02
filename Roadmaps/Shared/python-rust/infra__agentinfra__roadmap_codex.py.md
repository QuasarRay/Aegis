# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 202. Inventory digest: `76f000c8e8ebe888afe766f874c97a25973639e5467e3ff4aea0b6488c7d1ad7`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/roadmap_codex.py::module::root::Module

Source: `infra/agentinfra/roadmap_codex.py:1`; AST `4e73780e5b844bdf1c79fc3caa499fe4c2826a56b619d5417c7caf57c65aa75a`.

Rust module: `infra::agentinfra::roadmap_codex`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: BaseException, BrokenPipeError, CodexReader, CodexRpcError, ContractError, Path, TimeoutError, __version__, bool, canonical, chunk, client, compiled, contract_hash, cursor, deadline, dict, digest, error, executable, experimental, float, goal, ident, len, line, list, loads, m, max, message, method, milestone_ids, models, objective, observation, os, params, plan, range, ready, redact_text, require, result, select, self, set, shutil, str, subprocess, super, thread_id, time, timeout, version. Outputs/bindings: ALLOWED, _, chunk, client, cursor, deadline, goal, ident, line, m, message, models, ready, result, version.
Calls/effect boundaries: CodexReader, CodexRpcError, Path, Path(client.executable).read_bytes, TimeoutError, bool, canonical, client.call, digest, error.get, goal.get, len, line.decode, loads, m.get, max, message.get, models.extend, observation.get, os.read, plan.get, range, redact_text, require, result.get, select.select, self.__exit__, self.buffer.split, self.call, self.events.append, self.proc.kill, self.proc.stdin.close, self.proc.stdin.write, self.proc.stdout.close, self.proc.stdout.fileno, self.proc.terminate, self.proc.wait, set, shutil.which, str, subprocess.Popen, subprocess.run, subprocess.run([client.executable, '--version'], capture_output=True, text=True, timeout=10, check=True).stdout.strip, super, super().__init__, time.monotonic.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::root.body[0]::Expr

Source: `infra/agentinfra/roadmap_codex.py:1`; AST `072a162445acb060ad7c13469d801dac9691501253785580e7db87e9818ca44b`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::root.body[1]::ImportFrom

Source: `infra/agentinfra/roadmap_codex.py:6`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::root.body[2]::Import

Source: `infra/agentinfra/roadmap_codex.py:8`; AST `ac3a74d6dd975a8e8fe4b7f85fce794793a9355595b850e3926964913948d386`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::root.body[3]::Import

Source: `infra/agentinfra/roadmap_codex.py:9`; AST `f2f0fc3b60ddb100d265ce3555ff9c527572adf843116ddfb0cc1d738e9145e5`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::root.body[4]::Import

Source: `infra/agentinfra/roadmap_codex.py:10`; AST `b461ae95c16c1e73a466fdd306ad6da693ead3a324e5d33627958cc4a2f47e36`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Import evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::root.body[5]::Import

Source: `infra/agentinfra/roadmap_codex.py:11`; AST `9d97d469cf8d66465563e1e22c6dab3b6107819aba2d9956c7080016c1ab9c1b`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Import evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::root.body[6]::Import

Source: `infra/agentinfra/roadmap_codex.py:12`; AST `ff05bad0fd9a7212d3cd85fd2726055168be21bc8f6e0d93b29965794b0675d4`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Import evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::root.body[7]::ImportFrom

Source: `infra/agentinfra/roadmap_codex.py:13`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered ImportFrom evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::root.body[8]::ImportFrom

Source: `infra/agentinfra/roadmap_codex.py:15`; AST `03fdf65de39a4ca87683f0a0b904a242f99647cfec13e60ca8817bd5c61ca033`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered ImportFrom evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::root.body[9]::ImportFrom

Source: `infra/agentinfra/roadmap_codex.py:16`; AST `ab57d23e5809665f97cd65c61085e30d7ffc9928a0253eabde156a3ccc3ae6d8`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered ImportFrom evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexRpcError::root.body[10]::ClassDef

Source: `infra/agentinfra/roadmap_codex.py:19`; AST `5173eed8b5570bfa5f5a46b215c8c1cc4a34f6580264959c0d86998cd777b3f8`.

Rust module: `infra::agentinfra::roadmap_codex`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: ContractError, dict, error, method, redact_text, self, str, super. Outputs/bindings: (none).
Calls/effect boundaries: error.get, redact_text, str, super, super().__init__.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered ClassDef evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexRpcError::root.body[10].body[0]::Expr

Source: `infra/agentinfra/roadmap_codex.py:20`; AST `ae8dd7f2bc7e224a03f2e200468a6c0e41cc35a0e2ea7c766506255686276419`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexRpcError::__init__::root.body[10].body[1]::FunctionDef

Source: `infra/agentinfra/roadmap_codex.py:21`; AST `a2c323bd18a5ff74bbf864f3be745683dc7d402c609c3d1edcffe67e703afe7a`.

Rust module: `infra::agentinfra::roadmap_codex`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: dict, error, method, redact_text, self, str, super. Outputs/bindings: (none).
Calls/effect boundaries: error.get, redact_text, str, super, super().__init__.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexRpcError::__init__::root.body[10].body[1].body[0]::Assign

Source: `infra/agentinfra/roadmap_codex.py:22`; AST `d9a1ad04cc0faf221cdbfbfb5e06b2211f659fd8c5292fac8ccbf77fda287877`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: method, self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexRpcError::__init__::root.body[10].body[1].body[1]::Assign

Source: `infra/agentinfra/roadmap_codex.py:23`; AST `7ba6a709d299b01509307c010b241e9eac15ca61122a367d5b917ca1424790bd`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: error, self. Outputs/bindings: (none).
Calls/effect boundaries: error.get.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexRpcError::__init__::root.body[10].body[1].body[1].value::Call

Source: `infra/agentinfra/roadmap_codex.py:23`; AST `37c4ea7d5f2a18692447631a100120e1ed4c50cea5b4c976bab8a9aad1f75a4c`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: error. Outputs/bindings: (none).
Calls/effect boundaries: error.get.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexRpcError::__init__::root.body[10].body[1].body[2]::Assign

Source: `infra/agentinfra/roadmap_codex.py:24`; AST `e89ef96fe86fe8b86b5cebb623dd31f26fcd0488df7be56d7c3070f0f8d80f1e`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: error, redact_text, self, str. Outputs/bindings: (none).
Calls/effect boundaries: error.get, redact_text, str.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexRpcError::__init__::root.body[10].body[1].body[2].value.value::Call

Source: `infra/agentinfra/roadmap_codex.py:24`; AST `9804ce4922fda323daf67641cf1999a63847c98b3a81398b867a29b53cdc841b`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: error, redact_text, str. Outputs/bindings: (none).
Calls/effect boundaries: error.get, redact_text, str.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[2].value.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexRpcError::__init__::root.body[10].body[1].body[2].value.value.args[0]::Call

Source: `infra/agentinfra/roadmap_codex.py:24`; AST `eea5b352ca7da5570b7e178e2230ebaf744e5a479960ed6b123c21e461a57b0f`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: error, str. Outputs/bindings: (none).
Calls/effect boundaries: error.get, str.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[2].value.value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexRpcError::__init__::root.body[10].body[1].body[2].value.value.args[0].args[0]::Call

Source: `infra/agentinfra/roadmap_codex.py:24`; AST `2e33ea9326a8b430b8f082da0b5b817f6e2eacb1e0d60581bab7c54e92a3bb3c`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: error. Outputs/bindings: (none).
Calls/effect boundaries: error.get.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[2].value.value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexRpcError::__init__::root.body[10].body[1].body[3]::Expr

Source: `infra/agentinfra/roadmap_codex.py:25`; AST `c9a24926136114d9dd5f19c6a9daed64e1f317f2d163955daf7ee049b12887b6`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, super. Outputs/bindings: (none).
Calls/effect boundaries: super, super().__init__.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexRpcError::__init__::root.body[10].body[1].body[3].value::Call

Source: `infra/agentinfra/roadmap_codex.py:25`; AST `4c76c425f36ae95d70bfb2d04de3dca6a51b1649705b60079e8c1209cfd1515a`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, super. Outputs/bindings: (none).
Calls/effect boundaries: super, super().__init__.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexRpcError::__init__::root.body[10].body[1].body[3].value.func.value::Call

Source: `infra/agentinfra/roadmap_codex.py:25`; AST `29352a716af572cde18824794ed45cef0d41381b7241b8175f75da4aa39943e3`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: super. Outputs/bindings: (none).
Calls/effect boundaries: super.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[3].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::root.body[11]::ClassDef

Source: `infra/agentinfra/roadmap_codex.py:28`; AST `f088d01795de38a2de230a82967bffd0893426ec332e041d08b098c7c2973830`.

Rust module: `infra::agentinfra::roadmap_codex`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: BaseException, BrokenPipeError, CodexRpcError, TimeoutError, __version__, bool, canonical, chunk, deadline, dict, executable, experimental, float, ident, len, line, loads, max, message, method, os, params, ready, require, select, self, shutil, str, subprocess, time, timeout. Outputs/bindings: ALLOWED, _, chunk, deadline, ident, line, message, ready.
Calls/effect boundaries: CodexRpcError, TimeoutError, bool, canonical, len, line.decode, loads, max, message.get, os.read, require, select.select, self.__exit__, self.buffer.split, self.call, self.events.append, self.proc.kill, self.proc.stdin.close, self.proc.stdin.write, self.proc.stdout.close, self.proc.stdout.fileno, self.proc.terminate, self.proc.wait, shutil.which, subprocess.Popen, time.monotonic.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered ClassDef evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::root.body[11].body[0]::Assign

Source: `infra/agentinfra/roadmap_codex.py:29`; AST `6e7a58c5686adfd280702409858bdbe941f73d10311563440dcdb04a6ba705a6`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: ALLOWED.
Calls/effect boundaries: (none).
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__init__::root.body[11].body[1]::FunctionDef

Source: `infra/agentinfra/roadmap_codex.py:32`; AST `ea69625299941c79a24c50478228bde0e4568fde5e89bcc667fed74bf52d8e7f`.

Rust module: `infra::agentinfra::roadmap_codex`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: bool, executable, experimental, float, require, self, shutil, str, timeout. Outputs/bindings: (none).
Calls/effect boundaries: bool, require, shutil.which.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__init__::root.body[11].body[1].body[0]::Expr

Source: `infra/agentinfra/roadmap_codex.py:33`; AST `643b9cd1002850f4d6c84314360b8258b9375d25869ee747b455841566b92038`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, timeout. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__init__::root.body[11].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_codex.py:33`; AST `7d3bb737b6f4484a0bfb02de08fed36fde385dda9f0677dc8ab4ac3dff849e48`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, timeout. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__init__::root.body[11].body[1].body[1]::Assign

Source: `infra/agentinfra/roadmap_codex.py:34`; AST `7925a6ea0d2f23034210268dbb9159ca17d62dd7f6160c6cc45d5a907ca73492`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: executable, self, shutil. Outputs/bindings: (none).
Calls/effect boundaries: shutil.which.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__init__::root.body[11].body[1].body[1].value::Call

Source: `infra/agentinfra/roadmap_codex.py:34`; AST `c868638663e88b9320c22817083604371f3cfee8bf3bd49a61d54c93e0e340aa`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: executable, shutil. Outputs/bindings: (none).
Calls/effect boundaries: shutil.which.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__init__::root.body[11].body[1].body[2]::Expr

Source: `infra/agentinfra/roadmap_codex.py:35`; AST `e6a9bf6f2d1d4c9db9fcef2b39310a75654d285e9f0de5c7b9891804d71db258`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, require, self. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__init__::root.body[11].body[1].body[2].value::Call

Source: `infra/agentinfra/roadmap_codex.py:35`; AST `44acab31651101bf8baf3371484a5dd184b938dbd455ada120e269f0a2e7f0c9`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, require, self. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[1].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__init__::root.body[11].body[1].body[2].value.args[0]::Call

Source: `infra/agentinfra/roadmap_codex.py:35`; AST `220ae84f1702ed89af7863d18d6f69bffab5f78b5e9263ef6782dfb1eb32e6c0`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, self. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[1].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__init__::root.body[11].body[1].body[3]::Assign

Source: `infra/agentinfra/roadmap_codex.py:36`; AST `761652d45252302e952be1bc487540206af3f0cd0b4254b818e7e06ef1f21f4c`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, timeout. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__init__::root.body[11].body[1].body[4]::Assign

Source: `infra/agentinfra/roadmap_codex.py:37`; AST `58f91f491ca5c0d66440c029f2f5e2f69db94f3b811e310daab77e2d27a51bc6`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: experimental, self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[1].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__init__::root.body[11].body[1].body[5]::Assign

Source: `infra/agentinfra/roadmap_codex.py:38`; AST `02e8ddf2ad427a9745ce616fb1275fa0f486a92d19a5788c4f6063066f0f5f58`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[1].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__init__::root.body[11].body[1].body[6]::Assign

Source: `infra/agentinfra/roadmap_codex.py:39`; AST `d3704947693be5c60e909f85f804260e74c3256705c23b16467cab0702a8dc6d`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[1].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__init__::root.body[11].body[1].body[7]::Assign

Source: `infra/agentinfra/roadmap_codex.py:40`; AST `1e4ab0539eb3a1bc9f2f58350394640a7f6c3463d7be61a4455df918ef007a5d`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[1].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__init__::root.body[11].body[1].body[8]::Assign

Source: `infra/agentinfra/roadmap_codex.py:41`; AST `2548f2abb5fefa34b31e77f8389a34f4ae9222b7dde5f54106172666ee96e89c`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[1].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__init__::root.body[11].body[1].body[9]::Assign

Source: `infra/agentinfra/roadmap_codex.py:42`; AST `3daef3f0909c68fe1a0ba832a2a5c300f05bb1c066876c80b4257b904d5e0eee`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[1].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__enter__::root.body[11].body[2]::FunctionDef

Source: `infra/agentinfra/roadmap_codex.py:44`; AST `d646cc192f2646cbc3c868fc16f981f81bc44533ae988acaf6de24456eec4687`.

Rust module: `infra::agentinfra::roadmap_codex`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: BaseException, __version__, canonical, self, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: canonical, self.__exit__, self.call, self.proc.stdin.write, subprocess.Popen.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__enter__::root.body[11].body[2].body[0]::Assign

Source: `infra/agentinfra/roadmap_codex.py:45`; AST `ae41ee9f739881afa5189da83a1bf445e847379029656cff2469e9210731c186`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: subprocess.Popen.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__enter__::root.body[11].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_codex.py:45`; AST `a46e0a911439f5dd40fc86f761f2cfa77c240843b35484d358f6f2db5f680e9b`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: subprocess.Popen.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__enter__::root.body[11].body[2].body[1]::Try

Source: `infra/agentinfra/roadmap_codex.py:48`; AST `9f6c013e777f1bed55b560c1a4b84015a215303076ed5aedcc8725c1ec2c4503`.

Rust module: `infra::agentinfra::roadmap_codex`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: BaseException, __version__, canonical, self. Outputs/bindings: (none).
Calls/effect boundaries: canonical, self.__exit__, self.call, self.proc.stdin.write.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Try evaluation at root.body[11].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__enter__::root.body[11].body[2].body[1].body[0]::ImportFrom

Source: `infra/agentinfra/roadmap_codex.py:49`; AST `22c4a3f8037e3ffaeae5fa6d6e32729988a4ba88a5462816be5e1aaaab3dfbe1`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered ImportFrom evaluation at root.body[11].body[2].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__enter__::root.body[11].body[2].body[1].body[1]::Assign

Source: `infra/agentinfra/roadmap_codex.py:50`; AST `0f0ff37a239cca5aa5d6591e1b90a4015dbaa50e28e768844537fc715dcbcbfa`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: __version__, self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[2].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__enter__::root.body[11].body[2].body[1].body[1].value::Call

Source: `infra/agentinfra/roadmap_codex.py:50`; AST `52f4ab746b17921f1f14c228e063a51b0117cd68cdb781bae3ab34cfe54e2d7c`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: __version__, self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__enter__::root.body[11].body[2].body[1].body[2]::Expr

Source: `infra/agentinfra/roadmap_codex.py:52`; AST `872ca994cd07d4b8c9e0c915c58c607fe96d21b9433bb38338a27961457059f3`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: canonical, self. Outputs/bindings: (none).
Calls/effect boundaries: canonical, self.proc.stdin.write.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[2].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__enter__::root.body[11].body[2].body[1].body[2].value::Call

Source: `infra/agentinfra/roadmap_codex.py:52`; AST `0d20d865cdfcee1ba7b4eb9ce639db79d22a4a042f8775ca50b07e6d9e16ba81`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, self. Outputs/bindings: (none).
Calls/effect boundaries: canonical, self.proc.stdin.write.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[1].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__enter__::root.body[11].body[2].body[1].body[2].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_codex.py:52`; AST `895079025b9aa930ecc0bf8a24e298e470b31cd6cb017a503e5b56125303ae02`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical. Outputs/bindings: (none).
Calls/effect boundaries: canonical.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[1].body[2].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__enter__::root.body[11].body[2].body[1].handlers[0]::ExceptHandler

Source: `infra/agentinfra/roadmap_codex.py:53`; AST `26a446e7af88138c8acad86efce51bef8d3c73f163f58e13fb9d924d9a62dfa2`.

Rust module: `infra::agentinfra::roadmap_codex`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: BaseException, self. Outputs/bindings: (none).
Calls/effect boundaries: self.__exit__.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[11].body[2].body[1].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__enter__::root.body[11].body[2].body[1].handlers[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_codex.py:54`; AST `2d7c75b86a80f445f05bef6e4182c73654dc02cf3c7ade3ad0e30c19adc87bf3`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.__exit__.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[2].body[1].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__enter__::root.body[11].body[2].body[1].handlers[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_codex.py:54`; AST `32b2c53a81d4d595ae7989dca821cee4c71590d20bc98baf85e3147a4bc57246`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.__exit__.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[1].handlers[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__enter__::root.body[11].body[2].body[1].handlers[0].body[1]::Raise

Source: `infra/agentinfra/roadmap_codex.py:55`; AST `ba28128c14dfbd0a9062c0dbab42ad6c52ecf0767df6b67576deb1dbbfdd038d`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Raise evaluation at root.body[11].body[2].body[1].handlers[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__enter__::root.body[11].body[2].body[2]::Return

Source: `infra/agentinfra/roadmap_codex.py:56`; AST `6a68aee6f7ab1ee550cd0313a4445fc0789479dfc91ef51f64fa79554e46702d`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Return evaluation at root.body[11].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3]::FunctionDef

Source: `infra/agentinfra/roadmap_codex.py:58`; AST `6c64a38c3ec33b34aa11f3087e895164f02509162309179f321baeff9d97a172`.

Rust module: `infra::agentinfra::roadmap_codex`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: CodexRpcError, TimeoutError, bool, canonical, chunk, deadline, dict, ident, len, line, loads, max, message, method, os, params, ready, require, select, self, str, time. Outputs/bindings: _, chunk, deadline, ident, line, message, ready.
Calls/effect boundaries: CodexRpcError, TimeoutError, bool, canonical, len, line.decode, loads, max, message.get, os.read, require, select.select, self.buffer.split, self.events.append, self.proc.stdin.write, self.proc.stdout.fileno, time.monotonic.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[0]::Expr

Source: `infra/agentinfra/roadmap_codex.py:59`; AST `2e243d7196679c2886a80077cca5a7b924bca0cde2e657dc1f347b07ae2de34d`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: method, require, self. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_codex.py:59`; AST `1e1644c7fdc852327072f5764fd196c5a3d7187aad5435e60b539fe4382cfbf4`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: method, require, self. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[1]::Expr

Source: `infra/agentinfra/roadmap_codex.py:60`; AST `231ed4ac4db0b9e1ba690ea3cdb0df2a8b91324803d544010ca04bd1b528495d`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, self. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[1].value::Call

Source: `infra/agentinfra/roadmap_codex.py:60`; AST `201c6b5a8740d0fc1d6def04f4c118fb6cc0f16af0d23c6f7f323ceda204e865`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, self. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[2]::AugAssign

Source: `infra/agentinfra/roadmap_codex.py:61`; AST `629a3af669f8b8493933f150706eb595ad99d130881a82bbccd82cc5f862de07`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered AugAssign evaluation at root.body[11].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[3]::Assign

Source: `infra/agentinfra/roadmap_codex.py:62`; AST `2cdd40793bc9add014529145dd76ddd6f768149bf46c00656a380059e1e480bb`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: ident.
Calls/effect boundaries: (none).
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[4]::Expr

Source: `infra/agentinfra/roadmap_codex.py:63`; AST `c5ed5cd7242b3e2ecf442e76b336ba40ac7517df5884f0fa93e98b624bb34297`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: canonical, ident, method, params, self. Outputs/bindings: (none).
Calls/effect boundaries: canonical, self.proc.stdin.write.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[3].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[4].value::Call

Source: `infra/agentinfra/roadmap_codex.py:63`; AST `d6ca590dd424c5eb2a20eae21fb540b492afea342033948813a3870d713883b2`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, ident, method, params, self. Outputs/bindings: (none).
Calls/effect boundaries: canonical, self.proc.stdin.write.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[4].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_codex.py:63`; AST `58876d4c13d5ec9a40580fa8713e53e98fb63cd97221d73b2c6d64476cfb85d7`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, ident, method, params. Outputs/bindings: (none).
Calls/effect boundaries: canonical.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[4].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[5]::Assign

Source: `infra/agentinfra/roadmap_codex.py:64`; AST `7e325045a856fe7dba1d7a726704ce10497be0722e548a02d7b8d4d6772b26a1`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, time. Outputs/bindings: deadline.
Calls/effect boundaries: time.monotonic.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[3].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[5].value.left::Call

Source: `infra/agentinfra/roadmap_codex.py:64`; AST `1518ec519851d0a5084168b533bc641ad5d2ce5a406bada9f9d7d919d82e5b92`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: time. Outputs/bindings: (none).
Calls/effect boundaries: time.monotonic.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[5].value.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[6]::While

Source: `infra/agentinfra/roadmap_codex.py:65`; AST `5c5000d704364131a41908fa58e22c59e029f0b1860a4f7691b6d33baca54354`.

Rust module: `infra::agentinfra::roadmap_codex`. while with explicit truth conversion and a normal-exhaustion flag for loop else

Inputs: CodexRpcError, bool, chunk, deadline, ident, len, line, loads, max, message, method, os, ready, require, select, self, time. Outputs/bindings: _, chunk, line, message, ready.
Calls/effect boundaries: CodexRpcError, bool, len, line.decode, loads, max, message.get, os.read, require, select.select, self.buffer.split, self.events.append, self.proc.stdout.fileno, time.monotonic.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered While evaluation at root.body[11].body[3].body[6]; no call, error or mutation may be omitted. Condition: time.monotonic() < deadline
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[6].test.left::Call

Source: `infra/agentinfra/roadmap_codex.py:65`; AST `1518ec519851d0a5084168b533bc641ad5d2ce5a406bada9f9d7d919d82e5b92`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: time. Outputs/bindings: (none).
Calls/effect boundaries: time.monotonic.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[6].test.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[6].body[0]::If

Source: `infra/agentinfra/roadmap_codex.py:66`; AST `b2bfcd7de099cdef7394062b04cc7b77459c6dc3521e5193353ecb096ec10477`.

Rust module: `infra::agentinfra::roadmap_codex`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: CodexRpcError, ident, len, line, loads, message, method, require, self. Outputs/bindings: line, message.
Calls/effect boundaries: CodexRpcError, len, line.decode, loads, message.get, require, self.buffer.split, self.events.append.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered If evaluation at root.body[11].body[3].body[6].body[0]; no call, error or mutation may be omitted. Condition: b'\n' in self.buffer
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[6].body[0].body[0]::Assign

Source: `infra/agentinfra/roadmap_codex.py:67`; AST `0feeea3db81014b94c86a2059b8c3e047bf00a1962fa7c5360b21bf87b40c66a`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: line.
Calls/effect boundaries: self.buffer.split.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[3].body[6].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[6].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_codex.py:67`; AST `2cd73eedadaef2b1bd3e4580569dd2d328491cb55efb3b57fdd5bfe1000af747`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.buffer.split.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[6].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[6].body[0].body[1]::Assign

Source: `infra/agentinfra/roadmap_codex.py:68`; AST `c660ea34f96770abad3d8373468d9d695cdc4c9a55052fff215d7fa3991a98c3`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: line, loads. Outputs/bindings: message.
Calls/effect boundaries: line.decode, loads.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[3].body[6].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[6].body[0].body[1].value::Call

Source: `infra/agentinfra/roadmap_codex.py:68`; AST `a9e8a6e1a298a4fedc7ca10ad28dff2de27a768bb7f35a481734c0146f939992`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: line, loads. Outputs/bindings: (none).
Calls/effect boundaries: line.decode, loads.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[6].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[6].body[0].body[1].value.args[0]::Call

Source: `infra/agentinfra/roadmap_codex.py:68`; AST `8aa36d6ace1b029236c0003a34736d7d507717605fd7685e6c05d9cd85f1ee01`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: line. Outputs/bindings: (none).
Calls/effect boundaries: line.decode.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[6].body[0].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[6].body[0].body[2]::If

Source: `infra/agentinfra/roadmap_codex.py:69`; AST `054ec328f05a2dddc9bc6fb31b406aca1e03b0c6661ba8c4019c1227ff4c5aab`.

Rust module: `infra::agentinfra::roadmap_codex`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: CodexRpcError, ident, message, method. Outputs/bindings: (none).
Calls/effect boundaries: CodexRpcError, message.get.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered If evaluation at root.body[11].body[3].body[6].body[0].body[2]; no call, error or mutation may be omitted. Condition: message.get('id') == ident
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[6].body[0].body[2].test.left::Call

Source: `infra/agentinfra/roadmap_codex.py:69`; AST `e62fddc6d8ebc7354a426317f70b0bc4fe643dabe6391018527a49ebaa367fbf`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: message. Outputs/bindings: (none).
Calls/effect boundaries: message.get.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[6].body[0].body[2].test.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[6].body[0].body[2].body[0]::If

Source: `infra/agentinfra/roadmap_codex.py:70`; AST `715d8bce6f101528fc6167f5ea57261edd210ddafddd3d739792e13b8117627c`.

Rust module: `infra::agentinfra::roadmap_codex`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: CodexRpcError, message, method. Outputs/bindings: (none).
Calls/effect boundaries: CodexRpcError.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered If evaluation at root.body[11].body[3].body[6].body[0].body[2].body[0]; no call, error or mutation may be omitted. Condition: 'error' in message
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[6].body[0].body[2].body[0].body[0]::Raise

Source: `infra/agentinfra/roadmap_codex.py:71`; AST `7f1250cc4937220a07b3273ff6c6e0d9a33008c25827df23ecfaac9b7d41b7ad`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: CodexRpcError, message, method. Outputs/bindings: (none).
Calls/effect boundaries: CodexRpcError.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Raise evaluation at root.body[11].body[3].body[6].body[0].body[2].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[6].body[0].body[2].body[0].body[0].exc::Call

Source: `infra/agentinfra/roadmap_codex.py:71`; AST `6be6886e853fbab221b43607d16ebfb0d7b732b178e00d058755f2801efdce29`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: CodexRpcError, message, method. Outputs/bindings: (none).
Calls/effect boundaries: CodexRpcError.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[6].body[0].body[2].body[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[6].body[0].body[2].body[1]::Return

Source: `infra/agentinfra/roadmap_codex.py:72`; AST `298cbb2f6b42ddb3d343a3b0eaf483567ece41b22c9a4f361fbec46492ad4615`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: message. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Return evaluation at root.body[11].body[3].body[6].body[0].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[6].body[0].body[3]::Expr

Source: `infra/agentinfra/roadmap_codex.py:73`; AST `804db0f609fd9ca87523a1cab331898628c9af77e7987c835e98a97b006add27`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: message, self. Outputs/bindings: (none).
Calls/effect boundaries: self.events.append.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[3].body[6].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[6].body[0].body[3].value::Call

Source: `infra/agentinfra/roadmap_codex.py:73`; AST `e89a5184f013a1bf18f39085fcf88e0133cc3a5b42ab5d71c60864156f5c0a0f`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: message, self. Outputs/bindings: (none).
Calls/effect boundaries: self.events.append.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[6].body[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[6].body[0].body[4]::Expr

Source: `infra/agentinfra/roadmap_codex.py:74`; AST `996cbb30f1c23c22b063a797029b0bde8a7909d19310281385f00196f47df11b`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, require, self. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[3].body[6].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[6].body[0].body[4].value::Call

Source: `infra/agentinfra/roadmap_codex.py:74`; AST `da132fbb38cf16854365c32096827ba173fcaed71d99216f426c640244c947be`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, require, self. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[6].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[6].body[0].body[4].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_codex.py:74`; AST `5b7644463a3dbc36bdcc70baf05a3fe3d5a1b363a2036242a0a3acb00fcb04ca`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, self. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[6].body[0].body[4].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[6].body[0].body[5]::Continue

Source: `infra/agentinfra/roadmap_codex.py:75`; AST `3d1e0aaa463df3eefc9bd5be83f453adcd9621b2dc7f387c3eaff3ab42e91059`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Continue evaluation at root.body[11].body[3].body[6].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[6].body[1]::Assign

Source: `infra/agentinfra/roadmap_codex.py:76`; AST `cf7c3973566997ac6f1441e008747841c2ee227f92602710f6aecd5e99831064`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: deadline, max, select, self, time. Outputs/bindings: _, ready.
Calls/effect boundaries: max, select.select, time.monotonic.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[3].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[6].body[1].value::Call

Source: `infra/agentinfra/roadmap_codex.py:76`; AST `5dc993e682698d1dd215b2179fa5f73186dd6496b92905e0a993f186952f21c4`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: deadline, max, select, self, time. Outputs/bindings: (none).
Calls/effect boundaries: max, select.select, time.monotonic.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[6].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[6].body[1].value.args[3]::Call

Source: `infra/agentinfra/roadmap_codex.py:76`; AST `5dba788b04314b9baa244b2cb0e916332435c15a4f852e72aa7760807312c35b`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: deadline, max, time. Outputs/bindings: (none).
Calls/effect boundaries: max, time.monotonic.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[6].body[1].value.args[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[6].body[1].value.args[3].args[1].right::Call

Source: `infra/agentinfra/roadmap_codex.py:76`; AST `1518ec519851d0a5084168b533bc641ad5d2ce5a406bada9f9d7d919d82e5b92`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: time. Outputs/bindings: (none).
Calls/effect boundaries: time.monotonic.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[6].body[1].value.args[3].args[1].right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[6].body[2]::If

Source: `infra/agentinfra/roadmap_codex.py:77`; AST `f3f48f6d2315698fd0416f57387b8fa90aad845ecf1a652a946f2d7a39b68598`.

Rust module: `infra::agentinfra::roadmap_codex`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: bool, chunk, len, os, ready, require, self. Outputs/bindings: chunk.
Calls/effect boundaries: bool, len, os.read, require, self.proc.stdout.fileno.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered If evaluation at root.body[11].body[3].body[6].body[2]; no call, error or mutation may be omitted. Condition: ready
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[6].body[2].body[0]::Assign

Source: `infra/agentinfra/roadmap_codex.py:78`; AST `1b7e7a58c3b0e4e168bff1dd03302c1ae57b3c0c1eeec89a951610b6de8d7a24`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: os, self. Outputs/bindings: chunk.
Calls/effect boundaries: os.read, self.proc.stdout.fileno.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[3].body[6].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[6].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_codex.py:78`; AST `9074ec966d0f99557d996f6f3caf7fe3f697b6f173f42103d6247d238cd7f446`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os, self. Outputs/bindings: (none).
Calls/effect boundaries: os.read, self.proc.stdout.fileno.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[6].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[6].body[2].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_codex.py:78`; AST `edbe9415d3d12a157f1eab364864abebb7cd299716f9ec95be539dd79e3f1e39`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.proc.stdout.fileno.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[6].body[2].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[6].body[2].body[1]::Expr

Source: `infra/agentinfra/roadmap_codex.py:79`; AST `17f90865e1fb1c4a649ae1bba060cb7e52f6afa289adf0f71bc564fc8d8f8843`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, chunk, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[3].body[6].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[6].body[2].body[1].value::Call

Source: `infra/agentinfra/roadmap_codex.py:79`; AST `caf88cec42a095fdc33bc5b28fbdac2d00569faa044089d1cb90060fb95d883d`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, chunk, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[6].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[6].body[2].body[1].value.args[0]::Call

Source: `infra/agentinfra/roadmap_codex.py:79`; AST `6f25ed122a0a8c6ca06e750da3f7c19bcfa11b091ac491b5a6d48d9ec6e2bc24`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, chunk. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[6].body[2].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[6].body[2].body[2]::AugAssign

Source: `infra/agentinfra/roadmap_codex.py:80`; AST `6507b3626898e6da05bf78af295a8322e6f7a527f231e756e19fb74a1d25bfd5`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: chunk, self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered AugAssign evaluation at root.body[11].body[3].body[6].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[6].body[2].body[3]::Expr

Source: `infra/agentinfra/roadmap_codex.py:81`; AST `3c328b9fecdc442d1d98cf850889061e730a0cb63638295c01f20ca7d9a1dd26`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, require, self. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[3].body[6].body[2].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[6].body[2].body[3].value::Call

Source: `infra/agentinfra/roadmap_codex.py:81`; AST `53ec15dada7967025eb18d3005d44618b3db862ee12e1e05d7008c39baba1ee5`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, require, self. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[6].body[2].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[6].body[2].body[3].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_codex.py:81`; AST `348733d7439f589c925a5bf296bf67ef3de5bd227c94342df760f920f2a2c25b`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, self. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[6].body[2].body[3].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[7]::Raise

Source: `infra/agentinfra/roadmap_codex.py:82`; AST `7a6a85e96a4ee42d81111229334b779e5ab65804787d03884405540e140144ca`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: TimeoutError, method, self. Outputs/bindings: (none).
Calls/effect boundaries: TimeoutError.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Raise evaluation at root.body[11].body[3].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::call::root.body[11].body[3].body[7].exc::Call

Source: `infra/agentinfra/roadmap_codex.py:82`; AST `7f9fe3e58f5d4c169029bd44be7f3771cd6c784c194b116599e02d18df80c202`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: TimeoutError, method, self. Outputs/bindings: (none).
Calls/effect boundaries: TimeoutError.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].body[7].exc; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__exit__::root.body[11].body[4]::FunctionDef

Source: `infra/agentinfra/roadmap_codex.py:84`; AST `651caeead6094411ff6fb3187a85ac7f5e4062c8943d39e58d2cb96b307d2d10`.

Rust module: `infra::agentinfra::roadmap_codex`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: BrokenPipeError, self, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: self.proc.kill, self.proc.stdin.close, self.proc.stdout.close, self.proc.terminate, self.proc.wait.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__exit__::root.body[11].body[4].body[0]::If

Source: `infra/agentinfra/roadmap_codex.py:85`; AST `de871585a8a839db89fbc79f4574d25dc4a272df21c5035cb639077789668e99`.

Rust module: `infra::agentinfra::roadmap_codex`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: BrokenPipeError, self, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: self.proc.kill, self.proc.stdin.close, self.proc.stdout.close, self.proc.terminate, self.proc.wait.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered If evaluation at root.body[11].body[4].body[0]; no call, error or mutation may be omitted. Condition: self.proc
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__exit__::root.body[11].body[4].body[0].body[0]::Try

Source: `infra/agentinfra/roadmap_codex.py:86`; AST `626586c33ab2b69b2517059b460403398542d0457f88b2f825bf77cefe2e86a5`.

Rust module: `infra::agentinfra::roadmap_codex`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: BrokenPipeError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.proc.stdin.close.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Try evaluation at root.body[11].body[4].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__exit__::root.body[11].body[4].body[0].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_codex.py:87`; AST `0b46661e042243dbfae68051c81694aa747669682de59301089f9dc606cff87a`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.proc.stdin.close.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[4].body[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__exit__::root.body[11].body[4].body[0].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_codex.py:87`; AST `51fd35ff5f26b9683c0bc183dde5d999464f44c2ed312ec6e61642102d72985b`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.proc.stdin.close.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[0].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__exit__::root.body[11].body[4].body[0].body[0].handlers[0]::ExceptHandler

Source: `infra/agentinfra/roadmap_codex.py:88`; AST `3f502bcdcc5e0d20fc69c40e0553bb3740a8f79a1ae7285e10fc179684b59288`.

Rust module: `infra::agentinfra::roadmap_codex`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: BrokenPipeError. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[11].body[4].body[0].body[0].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__exit__::root.body[11].body[4].body[0].body[0].handlers[0].body[0]::Pass

Source: `infra/agentinfra/roadmap_codex.py:89`; AST `f8e211bd496e62be79e8542ba1d0a7cebbf2a6143ae07b375ae14ce00a91b69c`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Pass evaluation at root.body[11].body[4].body[0].body[0].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__exit__::root.body[11].body[4].body[0].body[1]::Try

Source: `infra/agentinfra/roadmap_codex.py:90`; AST `d660763edda7159bc8d7611ca3ce92254142c7f0b2bf53d4b47d0325f1bb7100`.

Rust module: `infra::agentinfra::roadmap_codex`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: self, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: self.proc.kill, self.proc.terminate, self.proc.wait.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Try evaluation at root.body[11].body[4].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__exit__::root.body[11].body[4].body[0].body[1].body[0]::Expr

Source: `infra/agentinfra/roadmap_codex.py:91`; AST `fc45fca27d5ab93e81794aee11a663629728c392bb3e659d90a9fefb0c5b66dc`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.proc.wait.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[4].body[0].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__exit__::root.body[11].body[4].body[0].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_codex.py:91`; AST `19d3720df269c2729057e04098a5bb753ecf224cd0e7f4ab69a11054c3e17e03`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.proc.wait.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[0].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__exit__::root.body[11].body[4].body[0].body[1].handlers[0]::ExceptHandler

Source: `infra/agentinfra/roadmap_codex.py:92`; AST `d65018f49b772a832594d40a5c99e8ca77ea89d27833f63e146dee630e2bd0ea`.

Rust module: `infra::agentinfra::roadmap_codex`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: self, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: self.proc.kill, self.proc.terminate, self.proc.wait.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[11].body[4].body[0].body[1].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__exit__::root.body[11].body[4].body[0].body[1].handlers[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_codex.py:93`; AST `af480be8ed0b0202927da7618a2b43d6cb0efc66ecbc574677ec6b1d6b0d4a6a`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.proc.terminate.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[4].body[0].body[1].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__exit__::root.body[11].body[4].body[0].body[1].handlers[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_codex.py:93`; AST `0a7f36fde051b7dac7c3565e9499e076ab060792f3a06e045792f4bd8a7746a1`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.proc.terminate.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[0].body[1].handlers[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__exit__::root.body[11].body[4].body[0].body[1].handlers[0].body[1]::Try

Source: `infra/agentinfra/roadmap_codex.py:94`; AST `b987549099ca3a79314e19a5a431618f11311f291330068a4298d0cb99eb159c`.

Rust module: `infra::agentinfra::roadmap_codex`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: self, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: self.proc.kill, self.proc.wait.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Try evaluation at root.body[11].body[4].body[0].body[1].handlers[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__exit__::root.body[11].body[4].body[0].body[1].handlers[0].body[1].body[0]::Expr

Source: `infra/agentinfra/roadmap_codex.py:95`; AST `52a93995b73681b02aa7aef8b49f1a9484e4f2238371860390d66c5d23e5c745`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.proc.wait.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[4].body[0].body[1].handlers[0].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__exit__::root.body[11].body[4].body[0].body[1].handlers[0].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_codex.py:95`; AST `f5648504e9ad631d7c5e418e4464b76dd6fca06aba3041cad0288f42cf9da8e2`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.proc.wait.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[0].body[1].handlers[0].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__exit__::root.body[11].body[4].body[0].body[1].handlers[0].body[1].handlers[0]::ExceptHandler

Source: `infra/agentinfra/roadmap_codex.py:96`; AST `97478ead449332cc101e61de4018cf303e5fb128f9f844f1976b794748c0da78`.

Rust module: `infra::agentinfra::roadmap_codex`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: self, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: self.proc.kill, self.proc.wait.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[11].body[4].body[0].body[1].handlers[0].body[1].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__exit__::root.body[11].body[4].body[0].body[1].handlers[0].body[1].handlers[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_codex.py:97`; AST `9a3ef3c7280d599bebe62e4579ab45c7c119c844986d37bf9f58e38c3297f118`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.proc.kill.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[4].body[0].body[1].handlers[0].body[1].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__exit__::root.body[11].body[4].body[0].body[1].handlers[0].body[1].handlers[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_codex.py:97`; AST `1f8b9a9ea165e76c4d697da73333442885ac6ce610db4909705d4912c8210981`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.proc.kill.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[0].body[1].handlers[0].body[1].handlers[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__exit__::root.body[11].body[4].body[0].body[1].handlers[0].body[1].handlers[0].body[1]::Expr

Source: `infra/agentinfra/roadmap_codex.py:98`; AST `52a93995b73681b02aa7aef8b49f1a9484e4f2238371860390d66c5d23e5c745`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.proc.wait.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[4].body[0].body[1].handlers[0].body[1].handlers[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__exit__::root.body[11].body[4].body[0].body[1].handlers[0].body[1].handlers[0].body[1].value::Call

Source: `infra/agentinfra/roadmap_codex.py:98`; AST `f5648504e9ad631d7c5e418e4464b76dd6fca06aba3041cad0288f42cf9da8e2`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.proc.wait.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[0].body[1].handlers[0].body[1].handlers[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__exit__::root.body[11].body[4].body[0].body[2]::Expr

Source: `infra/agentinfra/roadmap_codex.py:99`; AST `dba3b7a1e1a61b34d359bed2b854859181637472271d35f2fa9e6cda546347cb`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.proc.stdout.close.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Expr evaluation at root.body[11].body[4].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::CodexReader::__exit__::root.body[11].body[4].body[0].body[2].value::Call

Source: `infra/agentinfra/roadmap_codex.py:99`; AST `3d0780ae69e36e15f538d1f466b9cd329385edcc351c2c84fe1db404425f6a12`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.proc.stdout.close.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::capabilities::root.body[12]::FunctionDef

Source: `infra/agentinfra/roadmap_codex.py:102`; AST `7b366ffe394184ea0ccfa2d727458cdf4ddaae83eb84a65cca816db0491be6f0`.

Rust module: `infra::agentinfra::roadmap_codex`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: CodexReader, Path, client, cursor, dict, digest, m, models, range, require, result, subprocess, version. Outputs/bindings: _, client, cursor, m, models, result, version.
Calls/effect boundaries: CodexReader, Path, Path(client.executable).read_bytes, client.call, digest, m.get, models.extend, range, require, result.get, subprocess.run, subprocess.run([client.executable, '--version'], capture_output=True, text=True, timeout=10, check=True).stdout.strip.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::capabilities::root.body[12].body[0]::With

Source: `infra/agentinfra/roadmap_codex.py:103`; AST `1fde29c411675b63af9ecabd9dba3be45d6751b763c1161332c6138f177631ac`.

Rust module: `infra::agentinfra::roadmap_codex`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: CodexReader, Path, client, cursor, digest, m, models, range, require, result, subprocess, version. Outputs/bindings: _, client, cursor, m, models, result, version.
Calls/effect boundaries: CodexReader, Path, Path(client.executable).read_bytes, client.call, digest, m.get, models.extend, range, require, result.get, subprocess.run, subprocess.run([client.executable, '--version'], capture_output=True, text=True, timeout=10, check=True).stdout.strip.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered With evaluation at root.body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::capabilities::root.body[12].body[0].items[0].context_expr::Call

Source: `infra/agentinfra/roadmap_codex.py:103`; AST `6f1ebb990e6b2be2fe44bbe7550ddec34020ad3eb8ab8d5184d17d47544c899f`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: CodexReader. Outputs/bindings: (none).
Calls/effect boundaries: CodexReader.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::capabilities::root.body[12].body[0].body[0]::Assign

Source: `infra/agentinfra/roadmap_codex.py:104`; AST `c3e7e7c7e232bc9516397f515b78671dbf9f3c49363117285e818f812bde91fe`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: client, subprocess. Outputs/bindings: version.
Calls/effect boundaries: subprocess.run, subprocess.run([client.executable, '--version'], capture_output=True, text=True, timeout=10, check=True).stdout.strip.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::capabilities::root.body[12].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_codex.py:104`; AST `4fc5ce3bf27d385d3b5d00d589b2bee9de4c16b6425aa57178bcee5e1f3129f4`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: client, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: subprocess.run, subprocess.run([client.executable, '--version'], capture_output=True, text=True, timeout=10, check=True).stdout.strip.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::capabilities::root.body[12].body[0].body[0].value.func.value.value::Call

Source: `infra/agentinfra/roadmap_codex.py:104`; AST `8f9deb425fcd72eba3315c2fb5b44479b8ecba0690c8d482865d34790534b9e1`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: client, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: subprocess.run.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[0].value.func.value.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::capabilities::root.body[12].body[0].body[1]::Assign

Source: `infra/agentinfra/roadmap_codex.py:105`; AST `34da1b02b0a41204634eeba47d80a99986eafa868df9987c23c80339beae159d`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: cursor, models.
Calls/effect boundaries: (none).
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::capabilities::root.body[12].body[0].body[2]::For

Source: `infra/agentinfra/roadmap_codex.py:106`; AST `c88d7f80eaf349b066b61bc2bb64300c348dc1a04dbe78698b8cb793ef61bae0`.

Rust module: `infra::agentinfra::roadmap_codex`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: client, cursor, m, models, range, result. Outputs/bindings: _, cursor, m, result.
Calls/effect boundaries: client.call, m.get, models.extend, range, result.get.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered For evaluation at root.body[12].body[0].body[2]; no call, error or mutation may be omitted. Iteration: _ in range(20)
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::capabilities::root.body[12].body[0].body[2].iter::Call

Source: `infra/agentinfra/roadmap_codex.py:106`; AST `7ea593e32d743fff8ff8883c01f6e6e8389baa46992ca6bfd00a1fa327a334b0`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: range. Outputs/bindings: (none).
Calls/effect boundaries: range.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[2].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::capabilities::root.body[12].body[0].body[2].body[0]::Assign

Source: `infra/agentinfra/roadmap_codex.py:107`; AST `25328813f20470d464941538f09e2ec54db13c4ebb49670e03da74428f9ab5ec`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: client, cursor. Outputs/bindings: result.
Calls/effect boundaries: client.call.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::capabilities::root.body[12].body[0].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_codex.py:107`; AST `af47cef75d0208f35ce17f8aeb612fb4737d46e44b4079ec5b6c3f4c6ba1f525`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: client, cursor. Outputs/bindings: (none).
Calls/effect boundaries: client.call.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::capabilities::root.body[12].body[0].body[2].body[1]::Expr

Source: `infra/agentinfra/roadmap_codex.py:108`; AST `788f1f8ad62596c6d3e90b635aa18e7a12feeb8e08616fac2bf4310c6c042139`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: m, models, result. Outputs/bindings: m.
Calls/effect boundaries: m.get, models.extend, result.get.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::capabilities::root.body[12].body[0].body[2].body[1].value::Call

Source: `infra/agentinfra/roadmap_codex.py:108`; AST `37f8ac22fcfe5be5234bb916ac7ecfdec755b2aa163150ab309213ac187d2543`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: m, models, result. Outputs/bindings: m.
Calls/effect boundaries: m.get, models.extend, result.get.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::capabilities::root.body[12].body[0].body[2].body[1].value.args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_codex.py:108`; AST `68e6c87c4aff6c74fb703b7c6c4a578c18dddf2bb5dfa6ff2528123a926764d5`.

Rust module: `infra::agentinfra::roadmap_codex`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: m, result. Outputs/bindings: m.
Calls/effect boundaries: m.get, result.get.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[12].body[0].body[2].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::capabilities::root.body[12].body[0].body[2].body[1].value.args[0].elt.values[0]::Call

Source: `infra/agentinfra/roadmap_codex.py:108`; AST `36b8acc3df0650de3efbd2645bb03d09733208dddc9cb259c42b0d67d9970e13`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: m. Outputs/bindings: (none).
Calls/effect boundaries: m.get.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[2].body[1].value.args[0].elt.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::capabilities::root.body[12].body[0].body[2].body[1].value.args[0].elt.values[1]::Call

Source: `infra/agentinfra/roadmap_codex.py:108`; AST `d64cf9047e14f551d9235b27cec151a4e7dd886c88e95e2dc87b58c4b9b24f47`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: m. Outputs/bindings: (none).
Calls/effect boundaries: m.get.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[2].body[1].value.args[0].elt.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::capabilities::root.body[12].body[0].body[2].body[1].value.args[0].elt.values[2]::Call

Source: `infra/agentinfra/roadmap_codex.py:109`; AST `01e8b3336726c983deca64d4c48554215052a0697a6c59307ca9602bd46795a3`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: m. Outputs/bindings: (none).
Calls/effect boundaries: m.get.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[2].body[1].value.args[0].elt.values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::capabilities::root.body[12].body[0].body[2].body[1].value.args[0].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_codex.py:109`; AST `5e635d7e6c6cf95864db1399d5846b5a92aee677f3712f71b59738392bfeb3a1`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result. Outputs/bindings: (none).
Calls/effect boundaries: result.get.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[2].body[1].value.args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::capabilities::root.body[12].body[0].body[2].body[2]::Assign

Source: `infra/agentinfra/roadmap_codex.py:110`; AST `7598bb79d7e8bfe5228793a2788f94bccd99d686231104c1fed649ce7f0392c2`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result. Outputs/bindings: cursor.
Calls/effect boundaries: result.get.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::capabilities::root.body[12].body[0].body[2].body[2].value::Call

Source: `infra/agentinfra/roadmap_codex.py:110`; AST `63dfb9bafc31287489a48d2ac82b954ae503f18dde74935432966100a7780416`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result. Outputs/bindings: (none).
Calls/effect boundaries: result.get.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[2].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::capabilities::root.body[12].body[0].body[2].body[3]::If

Source: `infra/agentinfra/roadmap_codex.py:111`; AST `774574291b909078f0ca881df4472d121f1e589d7133611916bff40a47f3d8ff`.

Rust module: `infra::agentinfra::roadmap_codex`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: cursor. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered If evaluation at root.body[12].body[0].body[2].body[3]; no call, error or mutation may be omitted. Condition: not cursor
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::capabilities::root.body[12].body[0].body[2].body[3].body[0]::Break

Source: `infra/agentinfra/roadmap_codex.py:112`; AST `c0d25d96e6146e7b648417b86bf6bbfedd0a458099247cf2cd469124da4c9fec`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Break evaluation at root.body[12].body[0].body[2].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::capabilities::root.body[12].body[0].body[3]::Expr

Source: `infra/agentinfra/roadmap_codex.py:113`; AST `f099527ef3d6f2aacb17ca7349177cd2f7eb20e9cc59c95aa9dc906ec24fb42a`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cursor, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::capabilities::root.body[12].body[0].body[3].value::Call

Source: `infra/agentinfra/roadmap_codex.py:113`; AST `3165431ef30743c4ce76710aae108b367bcd8f9c1c9bd510556b9dc212ba6675`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cursor, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::capabilities::root.body[12].body[0].body[4]::Return

Source: `infra/agentinfra/roadmap_codex.py:114`; AST `58a6fc3beec6f47fb63a59cd7902849fd5b31ee3076048cfc506003e9aef488b`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, client, digest, models, version. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(client.executable).read_bytes, digest.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Return evaluation at root.body[12].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::capabilities::root.body[12].body[0].body[4].value.values[3]::Call

Source: `infra/agentinfra/roadmap_codex.py:115`; AST `0ad8a3ab6a13f1648ff746560ab6ace8cc1701de0d607511e0cf0cf4f96d77b0`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, client, digest. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(client.executable).read_bytes, digest.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[4].value.values[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::capabilities::root.body[12].body[0].body[4].value.values[3].args[0]::Call

Source: `infra/agentinfra/roadmap_codex.py:115`; AST `a5716cbca75c2e8d15ba9b23f04415592adaad3e27233003c711aaeb0963164e`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, client. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(client.executable).read_bytes.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[4].value.values[3].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::capabilities::root.body[12].body[0].body[4].value.values[3].args[0].func.value::Call

Source: `infra/agentinfra/roadmap_codex.py:115`; AST `8e918ec44e1a14e1691757c17663cddf52724a8e2388abc0fcc63a1b6a46b287`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, client. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[4].value.values[3].args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_goal::root.body[13]::FunctionDef

Source: `infra/agentinfra/roadmap_codex.py:121`; AST `fa04069f7afbe57e595ad88b9c60328f31834c641d79e0c4a82003d0ebc9d557`.

Rust module: `infra::agentinfra::roadmap_codex`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: bool, contract_hash, dict, digest, goal, len, objective, observation, require, str, thread_id. Outputs/bindings: goal.
Calls/effect boundaries: bool, digest, goal.get, len, observation.get, require.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_goal::root.body[13].body[0]::Assign

Source: `infra/agentinfra/roadmap_codex.py:122`; AST `44ec338b1fc0ae25e82c1692835ae39d295cb793540462325f3218e34d71e41b`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observation. Outputs/bindings: goal.
Calls/effect boundaries: observation.get.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_goal::root.body[13].body[0].value::Call

Source: `infra/agentinfra/roadmap_codex.py:122`; AST `44c4d6760e76396bd173ab189b72f0489598d1e77c26e46cbc5796c1768b2a9f`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observation. Outputs/bindings: (none).
Calls/effect boundaries: observation.get.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_goal::root.body[13].body[1]::Expr

Source: `infra/agentinfra/roadmap_codex.py:123`; AST `96dcc42f50a7f0a3550055b9b938a22336444f732a8890867aa61912ff4b63ee`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: goal, require, thread_id. Outputs/bindings: (none).
Calls/effect boundaries: goal.get, require.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_goal::root.body[13].body[1].value::Call

Source: `infra/agentinfra/roadmap_codex.py:123`; AST `aca2b8524efd91f9814895cf1b7ca4c5df2723ebe597e5d976d46fd9868b0867`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: goal, require, thread_id. Outputs/bindings: (none).
Calls/effect boundaries: goal.get, require.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_goal::root.body[13].body[1].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_codex.py:123`; AST `8882eb7d5b9f4dc8d2105e4953998c448940325a4f4149b97780ded2830a8ee0`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: goal. Outputs/bindings: (none).
Calls/effect boundaries: goal.get.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_goal::root.body[13].body[1].value.args[0].left.args[1]::Call

Source: `infra/agentinfra/roadmap_codex.py:123`; AST `12a3aafb86d4ac1fabfccdf44687ff589a7892691f5c30c1ec9f07c0e05a13a9`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: goal. Outputs/bindings: (none).
Calls/effect boundaries: goal.get.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].value.args[0].left.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_goal::root.body[13].body[2]::Expr

Source: `infra/agentinfra/roadmap_codex.py:124`; AST `8fa5fd0de7195986baea44bc341a00397beb48c10bc48134ca365381fb84ee16`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, goal, objective, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, goal.get, require.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_goal::root.body[13].body[2].value::Call

Source: `infra/agentinfra/roadmap_codex.py:124`; AST `a7e536b91b3b2be3433ba328fb7e793bf6e81d25e39a34f41829f2162a141c1e`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, goal, objective, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, goal.get, require.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_goal::root.body[13].body[2].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_codex.py:124`; AST `f63919515d3be4b4c9952f900298cbf76eac49214dedb5f1b96049934fdc731c`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: goal. Outputs/bindings: (none).
Calls/effect boundaries: goal.get.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_goal::root.body[13].body[2].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_codex.py:124`; AST `34ef5fd140328e98e8827e7d96ded7ee6166ef01a8005f24ed45fcfe47586207`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, objective. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_goal::root.body[13].body[3]::Expr

Source: `infra/agentinfra/roadmap_codex.py:125`; AST `b3123408a389bf3577bcd2b94fbe09e45826189a9f8a30c2b15b1619e21e4c49`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: goal, require. Outputs/bindings: (none).
Calls/effect boundaries: goal.get, require.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_goal::root.body[13].body[3].value::Call

Source: `infra/agentinfra/roadmap_codex.py:125`; AST `e74ca86d864d2aac6e339f44c896302c50ca14de3635fd7515dfa4a2449c4b21`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: goal, require. Outputs/bindings: (none).
Calls/effect boundaries: goal.get, require.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_goal::root.body[13].body[3].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_codex.py:125`; AST `337340fc2dab2135d3885d03c2bb3040fb953c98284ab395c2e6270568db0732`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: goal. Outputs/bindings: (none).
Calls/effect boundaries: goal.get.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_goal::root.body[13].body[4]::Expr

Source: `infra/agentinfra/roadmap_codex.py:126`; AST `f81f1c15bbbd681cf4ab3690e827d1d249db2e47dfe94030ebaf0fcb9941764e`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: contract_hash, len, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_goal::root.body[13].body[4].value::Call

Source: `infra/agentinfra/roadmap_codex.py:126`; AST `e4939091c3d822c237430945b6c703957a6b237df6a1266b33e5c308eaca2495`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: contract_hash, len, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_goal::root.body[13].body[4].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_codex.py:126`; AST `3e0c5979857efa3e9114b3d7eb83eb0afeec724c96331e3d2f166a285a6c2021`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: contract_hash, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_goal::root.body[13].body[5]::Return

Source: `infra/agentinfra/roadmap_codex.py:127`; AST `53d100147a11a74db2f73c16ed42e38bc8dfe9dfd638e801935fee03ac5d8443`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: contract_hash, digest, goal, objective, observation, thread_id. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Return evaluation at root.body[13].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_goal::root.body[13].body[5].value.values[5]::Call

Source: `infra/agentinfra/roadmap_codex.py:129`; AST `1af2dcd5f19d85a8db08951a0b972298a6efa0e6a519bf5bdfb56892001b494c`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, observation. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].value.values[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_plan::root.body[14]::FunctionDef

Source: `infra/agentinfra/roadmap_codex.py:132`; AST `52efed4564e80c151abc2d7052a2920bb00481827953a3f6641ee8ec8c58af59`.

Rust module: `infra::agentinfra::roadmap_codex`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: bool, compiled, dict, digest, len, list, milestone_ids, plan, require, set, str. Outputs/bindings: (none).
Calls/effect boundaries: bool, digest, len, plan.get, require, set.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_plan::root.body[14].body[0]::Expr

Source: `infra/agentinfra/roadmap_codex.py:133`; AST `f06ad80928ad3efb26b9c83eb8f0ea5b2fcf47efa4352d00260b132eb09045da`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, plan, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, plan.get, require.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_plan::root.body[14].body[0].value::Call

Source: `infra/agentinfra/roadmap_codex.py:133`; AST `74d46b0ed79ef8ba95b9543d6ec8fda0293f0621640d7846934d720bd262c5bd`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, plan, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, plan.get, require.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_plan::root.body[14].body[0].value.args[0].values[0]::Call

Source: `infra/agentinfra/roadmap_codex.py:133`; AST `542d5b7f02045b89dc6731cab57fdf26ba3905fe14c6d86b859a8d03f539bcd4`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, plan. Outputs/bindings: (none).
Calls/effect boundaries: bool, plan.get.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_plan::root.body[14].body[0].value.args[0].values[0].args[0]::Call

Source: `infra/agentinfra/roadmap_codex.py:133`; AST `e6679008911d05510f5cfe1977749dc2d67546ef2c48b72ee77fe8f328544a00`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: plan. Outputs/bindings: (none).
Calls/effect boundaries: plan.get.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].value.args[0].values[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_plan::root.body[14].body[0].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_codex.py:133`; AST `76c112159d6ecae24714fea738e62902afa44c71e3b703408dc9ffa631f78856`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: plan. Outputs/bindings: (none).
Calls/effect boundaries: plan.get.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_plan::root.body[14].body[0].value.args[0].values[2]::Call

Source: `infra/agentinfra/roadmap_codex.py:133`; AST `fe72bc72629c465e22e889e96581ecb4414417d8b975b7dd99daeab0152defa4`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, plan. Outputs/bindings: (none).
Calls/effect boundaries: bool, plan.get.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].value.args[0].values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_plan::root.body[14].body[0].value.args[0].values[2].args[0]::Call

Source: `infra/agentinfra/roadmap_codex.py:133`; AST `8fc62e1cb5906b94a17e914095912a999b8e5f33ddbc58889c95e3051026eb0f`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: plan. Outputs/bindings: (none).
Calls/effect boundaries: plan.get.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].value.args[0].values[2].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_plan::root.body[14].body[1]::Expr

Source: `infra/agentinfra/roadmap_codex.py:134`; AST `9a8054276922567d2b5c4d6d1d889c53c0e721aa70cf96c29daf171825868d03`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, milestone_ids, require, set. Outputs/bindings: (none).
Calls/effect boundaries: len, require, set.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_plan::root.body[14].body[1].value::Call

Source: `infra/agentinfra/roadmap_codex.py:134`; AST `d905875edd693aa33e0063be4ece7bea88b81e0428b614940a74678182b01aaa`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, milestone_ids, require, set. Outputs/bindings: (none).
Calls/effect boundaries: len, require, set.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_plan::root.body[14].body[1].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_codex.py:134`; AST `1328e0082446e29942957f8577f9548ab8e0a1f3c403422c0a4647ff237cd71d`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, milestone_ids, set. Outputs/bindings: (none).
Calls/effect boundaries: len, set.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_plan::root.body[14].body[1].value.args[0].values[1].left.args[0]::Call

Source: `infra/agentinfra/roadmap_codex.py:134`; AST `f8b8563ad4ace738368549a786f8757f341aeef3e77b5a7ff9445313c959684e`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: milestone_ids, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].value.args[0].values[1].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_plan::root.body[14].body[1].value.args[0].values[1].comparators[0]::Call

Source: `infra/agentinfra/roadmap_codex.py:134`; AST `27d8c15bbc60a8173bcc7a8ea97037e65365e4a4d3e36ca6a1ea15ee159079e7`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, milestone_ids. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].value.args[0].values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_plan::root.body[14].body[2]::Expr

Source: `infra/agentinfra/roadmap_codex.py:135`; AST `c90bb0c6df9ba2ef285f20f88b9421d6f3fc929053cef2edfedd63ee213484de`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, milestone_ids, require, set. Outputs/bindings: (none).
Calls/effect boundaries: require, set.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_plan::root.body[14].body[2].value::Call

Source: `infra/agentinfra/roadmap_codex.py:135`; AST `5550e7a8dffd7284b182a3d58a115c084a2786fa6b0852ca7ea51513ed78b7d5`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, milestone_ids, require, set. Outputs/bindings: (none).
Calls/effect boundaries: require, set.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_plan::root.body[14].body[2].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_codex.py:135`; AST `f8b8563ad4ace738368549a786f8757f341aeef3e77b5a7ff9445313c959684e`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: milestone_ids, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_plan::root.body[14].body[2].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_codex.py:135`; AST `85761b3dcf55321f5048e494de4853b6ce7118dad1510f0bc72170bda4c392d0`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_plan::root.body[14].body[3]::Return

Source: `infra/agentinfra/roadmap_codex.py:136`; AST `67ef3b32fbd18d10b6103e7aa4dfb02033d3de538328de8ecf41cb6d6ff9bdd4`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, digest, milestone_ids, plan. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Return evaluation at root.body[14].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::bind_plan::root.body[14].body[3].value.values[1]::Call

Source: `infra/agentinfra/roadmap_codex.py:136`; AST `5892eba9f51cb7f20a26a3b4ecbdfe97ed50e126ce98f5413712c4077e457581`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, plan. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[14].body[3].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::read_native_goal::root.body[15]::FunctionDef

Source: `infra/agentinfra/roadmap_codex.py:141`; AST `e3d3f7f7339895e6779222962f38cf0b87e488ebe1e78d484d945f4eeff440da`.

Rust module: `infra::agentinfra::roadmap_codex`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: CodexReader, bool, client, dict, require, str, thread_id. Outputs/bindings: client.
Calls/effect boundaries: CodexReader, bool, client.call, require.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::read_native_goal::root.body[15].body[0]::Expr

Source: `infra/agentinfra/roadmap_codex.py:142`; AST `49d3db8522a590b8152a7e8f0a7ba40066727899e655b67297612100a968a4d2`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, require, thread_id. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::read_native_goal::root.body[15].body[0].value::Call

Source: `infra/agentinfra/roadmap_codex.py:142`; AST `9b9ff617908a6c28d1660433ff223d2ab5f4b43daaff39e48bf005087f733160`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, require, thread_id. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::read_native_goal::root.body[15].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_codex.py:142`; AST `cd37e63e8c7eb3c36062f0fbd5dd0ea6964ef29927b2cb95206c3f8060580755`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, thread_id. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::read_native_goal::root.body[15].body[1]::With

Source: `infra/agentinfra/roadmap_codex.py:143`; AST `4802203fbecac822b30dbaa5cd996bc7f69c7203c7b312ac6e8661d667354cc0`.

Rust module: `infra::agentinfra::roadmap_codex`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: CodexReader, client, thread_id. Outputs/bindings: client.
Calls/effect boundaries: CodexReader, client.call.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered With evaluation at root.body[15].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::read_native_goal::root.body[15].body[1].items[0].context_expr::Call

Source: `infra/agentinfra/roadmap_codex.py:143`; AST `5474868276eac54ee388fbec780e85b338d421cad5310223341f527dadf813f2`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: CodexReader. Outputs/bindings: (none).
Calls/effect boundaries: CodexReader.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::read_native_goal::root.body[15].body[1].body[0]::Return

Source: `infra/agentinfra/roadmap_codex.py:144`; AST `5fca0cd98b9c9e38e95457b4c57f8e68acbd078e6d62d6ba26605279453e7e38`.

Rust module: `infra::agentinfra::roadmap_codex`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: client, thread_id. Outputs/bindings: (none).
Calls/effect boundaries: client.call.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Return evaluation at root.body[15].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_codex.py::module::read_native_goal::root.body[15].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_codex.py:144`; AST `163eed9079a55768391169665ad058366f2d2f6478e72551b210d6dec2d2fd4a`.

Rust module: `infra::agentinfra::roadmap_codex`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: client, thread_id. Outputs/bindings: (none).
Calls/effect boundaries: client.call.
Dependencies: , __future__, os, pathlib, roadmap_records, security, select, shutil, subprocess, time.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
