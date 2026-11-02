# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 332. Inventory digest: `65e69e099ff1f810d8cc7ad0ef19d76e0c54d0d61c083e41950962cce111495a`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/context_cache.py::module::root::Module

Source: `infra/agentinfra/context_cache.py:1`; AST `ec2b38b5e6f40d15d949daa17d5f22304a0ad5cd875e003f32e7fffc63748d17`.

Rust module: `infra::agentinfra::context_cache`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: Exception, FileLock, Iterable, Path, RuntimeError, SCHEMA, ValueError, _now, _parse, _source_key, _stat_identity, _validate, after, all, atomic_write_json, before, bool, bytes, cache_dir, chunk, commit_digest, commit_identity, conclusion, confined_path, confirm, current, current_digest, current_identity, current_stat, data, datetime, dep_path, dependencies, dependencies_fresh, dependency, dependency_path, dependency_records, dict, digest, entry, exc, failure_region, field, fingerprint, fingerprint_fresh, float, fresh, getattr, hashlib, identity, int, isinstance, iter, json, key, len, list, math, middle, old, path, provenance, range, raw, reason, redact_text, root, self, sha256_file, source, stat, str, stream, summary, timedelta, timezone, ttl_fresh, ttl_seconds, tuple, until, valid_until, value. Outputs/bindings: SCHEMA, _, after, before, chunk, commit_digest, commit_identity, confirm, current, current_digest, current_identity, current_stat, data, dep_path, dependencies_fresh, dependency, dependency_path, dependency_records, digest, entry, field, fingerprint_fresh, fresh, identity, key, middle, old, path, reason, stat, stream, summary, ttl_fresh, until, valid_until.
Calls/effect boundaries: (current + timedelta(seconds=ttl_seconds)).isoformat, FileLock, Path, RuntimeError, ValueError, _now, _now().isoformat, _parse, _source_key, _stat_identity, _validate, all, atomic_write_json, bool, cache_dir, confined_path, current.isoformat, data.get, data['sources'].get, data['sources'].items, datetime.fromisoformat, datetime.now, dep_path.exists, dependency.get, dependency_records.append, digest.hexdigest, digest.update, entry.get, fingerprint.strip, getattr, hashlib.sha256, hashlib.sha256(raw).hexdigest, hashlib.sha256(source.encode('utf-8')).hexdigest, hashlib.sha256(source.encode()).hexdigest, hashlib.sha256(str(path.readlink()).encode()).hexdigest, isinstance, iter, json.loads, len, math.isfinite, old.get, path.exists, path.is_symlink, path.open, path.readlink, path.stat, range, redact_text, root.resolve, self._confined, self._consistent_digest, self._save, self.load, self.load()['sources'].get, self.lock.acquire, self.lock.release, self.path.exists, self.path.read_text, sha256_file, source.encode, source.strip, str, str(path.readlink()).encode, stream.read, timedelta.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::root.body[0]::ImportFrom

Source: `infra/agentinfra/context_cache.py:1`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered ImportFrom evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::root.body[1]::ImportFrom

Source: `infra/agentinfra/context_cache.py:3`; AST `a8f4d002a63b56f5cb49084865867786cca358e591ed0da2248e071a8ec9c7b8`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::root.body[2]::Import

Source: `infra/agentinfra/context_cache.py:4`; AST `092cb77ae0770f1627b29bf41b2732722fbcc3a0e1d77a79674801800a2721d1`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::root.body[3]::Import

Source: `infra/agentinfra/context_cache.py:5`; AST `211ee42757705c7e350e70e36b762987a737f5e9c268f2a343e2dbfcb8fbea75`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::root.body[4]::Import

Source: `infra/agentinfra/context_cache.py:6`; AST `f329650e2c61a07a1bab85b32296a6d93760e313e108904819fa27d09cf3954d`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Import evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::root.body[5]::Import

Source: `infra/agentinfra/context_cache.py:7`; AST `ac3a74d6dd975a8e8fe4b7f85fce794793a9355595b850e3926964913948d386`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Import evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::root.body[6]::ImportFrom

Source: `infra/agentinfra/context_cache.py:8`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered ImportFrom evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::root.body[7]::ImportFrom

Source: `infra/agentinfra/context_cache.py:9`; AST `40df91c16312754769db381b92a50d223932b28beb76d17581061a55cc87ddee`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered ImportFrom evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::root.body[8]::ImportFrom

Source: `infra/agentinfra/context_cache.py:11`; AST `1b8b71be5203ae66cf696ad7ae023750f023f11fd20fe2501f8e1d56817881e3`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered ImportFrom evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::root.body[9]::ImportFrom

Source: `infra/agentinfra/context_cache.py:12`; AST `f49eec2be7586a81b0fa34570d7cbaa58bc5eeaa5e471a05fac611f36b0ee7bd`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered ImportFrom evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::root.body[10]::ImportFrom

Source: `infra/agentinfra/context_cache.py:13`; AST `83494d935e377857eb320dc3d46c08c874216b7c1ed349a268e7e9dc62f5c64d`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered ImportFrom evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::root.body[11]::ImportFrom

Source: `infra/agentinfra/context_cache.py:14`; AST `e26154642ecba27e2a0fe9239e284c9b28af3d1d19816e5186f4f832440317c9`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered ImportFrom evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::root.body[12]::Assign

Source: `infra/agentinfra/context_cache.py:17`; AST `34e25d46d26b74f7b92907b2ab0c3978b8bbe9c30f3cf60b936ae5282cd8ea89`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: SCHEMA.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::sha256_file::root.body[13]::FunctionDef

Source: `infra/agentinfra/context_cache.py:20`; AST `bbb5ff8f1fbb95e9ed4e7b5bc7d07827474ae54a08012dbd82a441281249b1c5`.

Rust module: `infra::agentinfra::context_cache`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, chunk, digest, hashlib, iter, path, str, stream. Outputs/bindings: chunk, digest, stream.
Calls/effect boundaries: digest.hexdigest, digest.update, hashlib.sha256, iter, path.open, stream.read.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::sha256_file::root.body[13].body[0]::Assign

Source: `infra/agentinfra/context_cache.py:21`; AST `fe6bd5c62ad2a41dddd85cb58b72442d3be980b0c84a8717f691d42321033fb8`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: hashlib. Outputs/bindings: digest.
Calls/effect boundaries: hashlib.sha256.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::sha256_file::root.body[13].body[0].value::Call

Source: `infra/agentinfra/context_cache.py:21`; AST `46ef61fb8c7d09a7bf845569bbc8968c05c256379ed5433a5aca1ba6d226695f`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: hashlib. Outputs/bindings: (none).
Calls/effect boundaries: hashlib.sha256.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::sha256_file::root.body[13].body[1]::With

Source: `infra/agentinfra/context_cache.py:22`; AST `22334ba2fb62b1bf9fd8759167ab7274a05c91d6996443f167f42caa35eea6a5`.

Rust module: `infra::agentinfra::context_cache`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: chunk, digest, iter, path, stream. Outputs/bindings: chunk, stream.
Calls/effect boundaries: digest.update, iter, path.open, stream.read.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered With evaluation at root.body[13].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::sha256_file::root.body[13].body[1].items[0].context_expr::Call

Source: `infra/agentinfra/context_cache.py:22`; AST `cf2984cb08c691f2c9c1f8bae5b41cfff4de4e7a17dbea14d92d2e0c1b1b6ab3`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.open.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::sha256_file::root.body[13].body[1].body[0]::For

Source: `infra/agentinfra/context_cache.py:23`; AST `f7746fd1e12c6e670a972db744e0dd8586ddd33e124393fe35685834e0575da6`.

Rust module: `infra::agentinfra::context_cache`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: chunk, digest, iter, stream. Outputs/bindings: chunk.
Calls/effect boundaries: digest.update, iter, stream.read.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered For evaluation at root.body[13].body[1].body[0]; no call, error or mutation may be omitted. Iteration: chunk in iter(lambda: stream.read(1024 * 1024), b'')
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::sha256_file::root.body[13].body[1].body[0].iter::Call

Source: `infra/agentinfra/context_cache.py:23`; AST `91d7b8f279e554d4ce648868d1d9996183e45cf2e9247774d8ab9f72b478f9c7`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: iter, stream. Outputs/bindings: (none).
Calls/effect boundaries: iter, stream.read.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::sha256_file::root.body[13].body[1].body[0].iter.args[0]::Lambda

Source: `infra/agentinfra/context_cache.py:23`; AST `6ceba3732bc666c70312ccf40a19d3aa1d4d5903340fb6ea4670fda2c5b9abf1`.

Rust module: `infra::agentinfra::context_cache`. closure with explicit captures; preserve Python late binding and argument defaults

Inputs: stream. Outputs/bindings: (none).
Calls/effect boundaries: stream.read.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Lambda evaluation at root.body[13].body[1].body[0].iter.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::sha256_file::root.body[13].body[1].body[0].iter.args[0].body::Call

Source: `infra/agentinfra/context_cache.py:23`; AST `c446f51bca41c2d8c80c760630a00eb81df572cee9a8f3ff5f38134d12c676f9`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: stream. Outputs/bindings: (none).
Calls/effect boundaries: stream.read.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].iter.args[0].body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::sha256_file::root.body[13].body[1].body[0].body[0]::Expr

Source: `infra/agentinfra/context_cache.py:24`; AST `88c7e083d23506f94b1617c15384f414663dbf96091e338b6eb06be061c3ead4`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: chunk, digest. Outputs/bindings: (none).
Calls/effect boundaries: digest.update.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::sha256_file::root.body[13].body[1].body[0].body[0].value::Call

Source: `infra/agentinfra/context_cache.py:24`; AST `907c147b4ab754c3dae552291780e6a6d2e5b536db067fcee603d9c423862c63`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: chunk, digest. Outputs/bindings: (none).
Calls/effect boundaries: digest.update.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::sha256_file::root.body[13].body[2]::Return

Source: `infra/agentinfra/context_cache.py:25`; AST `aa3da7efc023d445bac735413e5e5d7c2c33ca84064f55771ef78a21494fcd5c`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest. Outputs/bindings: (none).
Calls/effect boundaries: digest.hexdigest.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Return evaluation at root.body[13].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::sha256_file::root.body[13].body[2].value::Call

Source: `infra/agentinfra/context_cache.py:25`; AST `4c6a75079c9264af34821bef99907cdba4eee27bff05166ea6cb69802560cefc`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest. Outputs/bindings: (none).
Calls/effect boundaries: digest.hexdigest.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_now::root.body[14]::FunctionDef

Source: `infra/agentinfra/context_cache.py:28`; AST `2c9f3a6d918e370e4e79a067a5a75b2414a0d5af0cf5e406619ae919a20ee304`.

Rust module: `infra::agentinfra::context_cache`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: datetime, timezone. Outputs/bindings: (none).
Calls/effect boundaries: datetime.now.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_now::root.body[14].body[0]::Return

Source: `infra/agentinfra/context_cache.py:29`; AST `5ddf9889f8e2b8d4a382e472b4cfafc1ecdacde7df700463e3b7e3b8147db576`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: datetime, timezone. Outputs/bindings: (none).
Calls/effect boundaries: datetime.now.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Return evaluation at root.body[14].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_now::root.body[14].body[0].value::Call

Source: `infra/agentinfra/context_cache.py:29`; AST `7d005ec5c408397d72b2a5196d97d2fa96db0d64d31cc38e5bd68f36bf7badb9`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: datetime, timezone. Outputs/bindings: (none).
Calls/effect boundaries: datetime.now.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_parse::root.body[15]::FunctionDef

Source: `infra/agentinfra/context_cache.py:32`; AST `0fa57c65176f0603e5aca06569b03bb429994a3bd89d884c0147fbe8d675883f`.

Rust module: `infra::agentinfra::context_cache`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: datetime, value. Outputs/bindings: (none).
Calls/effect boundaries: datetime.fromisoformat.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_parse::root.body[15].body[0]::Return

Source: `infra/agentinfra/context_cache.py:33`; AST `cea5b248262ff0b8a78d4cf3e16b819c41cdaa545c42938caa478aefa90462c5`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: datetime, value. Outputs/bindings: (none).
Calls/effect boundaries: datetime.fromisoformat.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Return evaluation at root.body[15].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_parse::root.body[15].body[0].value.body::Call

Source: `infra/agentinfra/context_cache.py:33`; AST `a8ed96558562e4695dc6c2f0187ea76bcca85752cef13d3d87b4fd637fef2f4b`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: datetime, value. Outputs/bindings: (none).
Calls/effect boundaries: datetime.fromisoformat.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].value.body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_source_key::root.body[16]::FunctionDef

Source: `infra/agentinfra/context_cache.py:36`; AST `83cbaad188fdae45e42ca13cad4022db1f0a257a43918bfc4ca7d4b49a701bb2`.

Rust module: `infra::agentinfra::context_cache`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: hashlib, source, str. Outputs/bindings: (none).
Calls/effect boundaries: hashlib.sha256, hashlib.sha256(source.encode('utf-8')).hexdigest, source.encode.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_source_key::root.body[16].body[0]::Return

Source: `infra/agentinfra/context_cache.py:37`; AST `446a93841569874603b078c3dba23aa36e51a228eaa10da1223edd53d8836731`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: hashlib, source. Outputs/bindings: (none).
Calls/effect boundaries: hashlib.sha256, hashlib.sha256(source.encode('utf-8')).hexdigest, source.encode.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Return evaluation at root.body[16].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_source_key::root.body[16].body[0].value.right::Call

Source: `infra/agentinfra/context_cache.py:37`; AST `7d27b93b990afe022933ff7ae7e4d1a57ab98551c552838e15cfb6060c542808`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: hashlib, source. Outputs/bindings: (none).
Calls/effect boundaries: hashlib.sha256, hashlib.sha256(source.encode('utf-8')).hexdigest, source.encode.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].value.right; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_source_key::root.body[16].body[0].value.right.func.value::Call

Source: `infra/agentinfra/context_cache.py:37`; AST `1ff0b886591699859d371a805ac2760f23c0f99eda4ef73dde681a5d9f53a8f2`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: hashlib, source. Outputs/bindings: (none).
Calls/effect boundaries: hashlib.sha256, source.encode.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].value.right.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_source_key::root.body[16].body[0].value.right.func.value.args[0]::Call

Source: `infra/agentinfra/context_cache.py:37`; AST `61d63a135d9a74e117ddc1c4ab9eac4e60c406cecff95bc674b4b4da7e157b38`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: source. Outputs/bindings: (none).
Calls/effect boundaries: source.encode.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].value.right.func.value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_stat_identity::root.body[17]::FunctionDef

Source: `infra/agentinfra/context_cache.py:40`; AST `30132b1401fbf7bc126603fdeab0cd5466c5ec9559ee287f4685f0a0888f4d5b`.

Rust module: `infra::agentinfra::context_cache`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, dict, getattr, path, stat, str. Outputs/bindings: stat.
Calls/effect boundaries: getattr, path.is_symlink, path.readlink, path.stat, str.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_stat_identity::root.body[17].body[0]::Assign

Source: `infra/agentinfra/context_cache.py:41`; AST `5cf18abe522a75ec1abb69284fa5ad43945757b98db1848f7ba6c9af95a324d4`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: stat.
Calls/effect boundaries: path.stat.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_stat_identity::root.body[17].body[0].value::Call

Source: `infra/agentinfra/context_cache.py:41`; AST `d0f2660d5c576e75c41493128e9ef73fd43d1401a0dd272c961864f7164b7698`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.stat.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_stat_identity::root.body[17].body[1]::Return

Source: `infra/agentinfra/context_cache.py:42`; AST `9a25a3c6bb3433878bfa8e49a624cdaea4e3573e3e28a22b88e006f80efff6e2`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: getattr, path, stat, str. Outputs/bindings: (none).
Calls/effect boundaries: getattr, path.is_symlink, path.readlink, str.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Return evaluation at root.body[17].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_stat_identity::root.body[17].body[1].value.values[3]::Call

Source: `infra/agentinfra/context_cache.py:46`; AST `d2b93dd2535a5076038b5120c468e7c32ba3fab718872b9df0550bf948d525d1`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: getattr, stat. Outputs/bindings: (none).
Calls/effect boundaries: getattr.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].value.values[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_stat_identity::root.body[17].body[1].value.values[4]::Call

Source: `infra/agentinfra/context_cache.py:47`; AST `98bf23b99d573800eced037df190f8e1ac0c9669cef22b55ec80dc7dbc971eea`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: getattr, stat. Outputs/bindings: (none).
Calls/effect boundaries: getattr.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].value.values[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_stat_identity::root.body[17].body[1].value.values[5].test::Call

Source: `infra/agentinfra/context_cache.py:48`; AST `59b1c604985dcd3e66bb0b7ae49c367ee9372b6c297d22636b1ad06e54b90bcc`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.is_symlink.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].value.values[5].test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_stat_identity::root.body[17].body[1].value.values[5].body::Call

Source: `infra/agentinfra/context_cache.py:48`; AST `551c4b501723b32f24d138416ac1976c85bd096d61b5583cf31222ab1f181a68`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, str. Outputs/bindings: (none).
Calls/effect boundaries: path.readlink, str.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].value.values[5].body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_stat_identity::root.body[17].body[1].value.values[5].body.args[0]::Call

Source: `infra/agentinfra/context_cache.py:48`; AST `be12d503fd54bd779d75ccf612bcdbf41e065e05b938e9dfedb0ec2536ee3343`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.readlink.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].value.values[5].body.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18]::FunctionDef

Source: `infra/agentinfra/context_cache.py:52`; AST `7020f4a99d1434aa2ad4530a867b5b40b9410a1cc260051609d1bfbd3e9bfca5`.

Rust module: `infra::agentinfra::context_cache`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: RuntimeError, SCHEMA, all, data, dict, entry, field, int, isinstance, key, list, str. Outputs/bindings: entry, field, key.
Calls/effect boundaries: RuntimeError, all, data.get, data['sources'].items, entry.get, isinstance.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[18]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[0]::If

Source: `infra/agentinfra/context_cache.py:53`; AST `6ddc9fd64e52f68d6f406d98c9f29e939177eb682e8e88fd6135dfdffc69830d`.

Rust module: `infra::agentinfra::context_cache`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: RuntimeError, SCHEMA, data, dict, isinstance. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError, data.get, isinstance.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered If evaluation at root.body[18].body[0]; no call, error or mutation may be omitted. Condition: not isinstance(data, dict) or data.get('schema') != SCHEMA or (not isinstance(data.get('sources'), dict))
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[0].test.values[0].operand::Call

Source: `infra/agentinfra/context_cache.py:53`; AST `5f3dfa3b23b16e077ee85aed20c0cc9933e4cb3a08ae821ef38b1086b65c69f5`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data, dict, isinstance. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].test.values[0].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[0].test.values[1].left::Call

Source: `infra/agentinfra/context_cache.py:53`; AST `bb8b4355e9271bb1ebde178c434a6ea9e1de761a547a77e9ab1cdd68f407706a`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data. Outputs/bindings: (none).
Calls/effect boundaries: data.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[0].test.values[2].operand::Call

Source: `infra/agentinfra/context_cache.py:53`; AST `dfa05af1b4aa6b2679626c26cd24c9213185854b1b9a0a88024dcd394de78c7e`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data, dict, isinstance. Outputs/bindings: (none).
Calls/effect boundaries: data.get, isinstance.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].test.values[2].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[0].test.values[2].operand.args[0]::Call

Source: `infra/agentinfra/context_cache.py:53`; AST `f8506950030f15576c339cf4c36fc6ed3c5eeeb82a1d13e3405ea901649a1e6e`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data. Outputs/bindings: (none).
Calls/effect boundaries: data.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].test.values[2].operand.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[0].body[0]::Raise

Source: `infra/agentinfra/context_cache.py:54`; AST `c4ad5f2b746461c549ebfb8bb169c9b048c5c40acf95a73e5f1e3c3b803bb93a`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: RuntimeError. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Raise evaluation at root.body[18].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[0].body[0].exc::Call

Source: `infra/agentinfra/context_cache.py:54`; AST `58b142fbab37abb14bd0d26c4a205f259c25d025dd6fc5dbae6f7f65fc10919a`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: RuntimeError. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1]::For

Source: `infra/agentinfra/context_cache.py:55`; AST `0ffc4c7386f34e2540793ea090354d4c0b7d7a5389625a017fd49da64afae926`.

Rust module: `infra::agentinfra::context_cache`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: RuntimeError, all, data, dict, entry, field, int, isinstance, key, list, str. Outputs/bindings: entry, field, key.
Calls/effect boundaries: RuntimeError, all, data['sources'].items, entry.get, isinstance.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered For evaluation at root.body[18].body[1]; no call, error or mutation may be omitted. Iteration: (key, entry) in data['sources'].items()
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].iter::Call

Source: `infra/agentinfra/context_cache.py:55`; AST `67773a5766c84966847fc2c0f0ebee309b81af8c0b3cd78871ca7a6292ac2d4e`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data. Outputs/bindings: (none).
Calls/effect boundaries: data['sources'].items.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[0]::If

Source: `infra/agentinfra/context_cache.py:56`; AST `8b07caee9ebbf506f7ebcbaab5d87f94a60e14226ada37b442648d8684c82373`.

Rust module: `infra::agentinfra::context_cache`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: RuntimeError, dict, entry, isinstance, key, str. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError, entry.get, isinstance.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered If evaluation at root.body[18].body[1].body[0]; no call, error or mutation may be omitted. Condition: not isinstance(key, str) or not isinstance(entry, dict) or entry.get('kind') not in {'file', 'external', 'summary'}
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[0].test.values[0].operand::Call

Source: `infra/agentinfra/context_cache.py:56`; AST `cacffec277269334f4a9162e0d5a17654327f612395602c8646ed68079c5452c`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, key, str. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[0].test.values[0].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[0].test.values[1].operand::Call

Source: `infra/agentinfra/context_cache.py:56`; AST `b055d343abb678fdf97e8ceb35fe100b1cbd5539e45cc97fa3029e2ca0add4b8`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, entry, isinstance. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[0].test.values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[0].test.values[2].left::Call

Source: `infra/agentinfra/context_cache.py:56`; AST `013761e4100601a18af0bb9c33663a74f6139177faaa2711345f4e51870fe3cf`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry. Outputs/bindings: (none).
Calls/effect boundaries: entry.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[0].test.values[2].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[0].body[0]::Raise

Source: `infra/agentinfra/context_cache.py:57`; AST `8bfb82419849cc824128c2d6f63659fb817904faa60ab6689c6aa205ed3561df`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: RuntimeError. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Raise evaluation at root.body[18].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[0].body[0].exc::Call

Source: `infra/agentinfra/context_cache.py:57`; AST `a40d9086f907b47420bfc43f6e287ff08918b3c9233f85d1cb5237582e14afae`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: RuntimeError. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[1]::If

Source: `infra/agentinfra/context_cache.py:58`; AST `9f1dd240ca320f098ccbf1a24bf415a188f1a24e41e4ae8493e2f8105fa2cb3e`.

Rust module: `infra::agentinfra::context_cache`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: RuntimeError, all, dict, entry, field, isinstance, list, str. Outputs/bindings: field.
Calls/effect boundaries: RuntimeError, all, entry.get, isinstance.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered If evaluation at root.body[18].body[1].body[1]; no call, error or mutation may be omitted. Condition: entry['kind'] == 'file'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[1].body[0]::If

Source: `infra/agentinfra/context_cache.py:59`; AST `7e29bd4c45a91a4cd6f5dc9959b59aecbc990998b6af93944ed54a1806a8c839`.

Rust module: `infra::agentinfra::context_cache`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: RuntimeError, all, entry, field, isinstance, str. Outputs/bindings: field.
Calls/effect boundaries: RuntimeError, all, entry.get, isinstance.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered If evaluation at root.body[18].body[1].body[1].body[0]; no call, error or mutation may be omitted. Condition: not all((isinstance(entry.get(field), str) for field in ('path', 'sha256', 'recorded_at')))
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[1].body[0].test.operand::Call

Source: `infra/agentinfra/context_cache.py:59`; AST `c0a2c0e30be3f1116beb2eab7e20d75b29330c6cf4de4ad6b24468140fdbe8b2`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, entry, field, isinstance, str. Outputs/bindings: field.
Calls/effect boundaries: all, entry.get, isinstance.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[1].body[0].test.operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[1].body[0].test.operand.args[0]::GeneratorExp

Source: `infra/agentinfra/context_cache.py:59`; AST `6e2d413a42deed19eb5c609d1aaf5ccc687bfc5d709021a103cfd4395ee806cd`.

Rust module: `infra::agentinfra::context_cache`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: entry, field, isinstance, str. Outputs/bindings: field.
Calls/effect boundaries: entry.get, isinstance.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[18].body[1].body[1].body[0].test.operand.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[1].body[0].test.operand.args[0].elt::Call

Source: `infra/agentinfra/context_cache.py:59`; AST `2cc93ca8732dbf9a55b108b5d4d6e7eff3a90584b2c635e9949ac0a859559a36`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry, field, isinstance, str. Outputs/bindings: (none).
Calls/effect boundaries: entry.get, isinstance.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[1].body[0].test.operand.args[0].elt; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[1].body[0].test.operand.args[0].elt.args[0]::Call

Source: `infra/agentinfra/context_cache.py:59`; AST `e85f70e38f6e694765285dc6f4a389ab449ea747644cf584babee01565003154`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry, field. Outputs/bindings: (none).
Calls/effect boundaries: entry.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[1].body[0].test.operand.args[0].elt.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[1].body[0].body[0]::Raise

Source: `infra/agentinfra/context_cache.py:60`; AST `4d3f1792c2b77b99e85254306b2cc27b9315f7b84d92e48fadbdedce1fadf830`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: RuntimeError. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Raise evaluation at root.body[18].body[1].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[1].body[0].body[0].exc::Call

Source: `infra/agentinfra/context_cache.py:60`; AST `7ceab77ca55fa735c967dc1ab3bb1bdbc10197511fdc0bb95e7d716c51afb166`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: RuntimeError. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[1].body[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[1].body[1]::If

Source: `infra/agentinfra/context_cache.py:61`; AST `f1d60726065470588644c3b666c802aa24e9580c5fef876f5af236544cf86b57`.

Rust module: `infra::agentinfra::context_cache`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: RuntimeError, dict, entry, isinstance, list. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError, entry.get, isinstance.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered If evaluation at root.body[18].body[1].body[1].body[1]; no call, error or mutation may be omitted. Condition: not isinstance(entry.get('stat'), dict) or not isinstance(entry.get('dependencies', []), list)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[1].body[1].test.values[0].operand::Call

Source: `infra/agentinfra/context_cache.py:61`; AST `c81d911be7cde5c5ce079ce13c5461877d6bc548634643d65ebe37f2657afa00`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, entry, isinstance. Outputs/bindings: (none).
Calls/effect boundaries: entry.get, isinstance.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[1].body[1].test.values[0].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[1].body[1].test.values[0].operand.args[0]::Call

Source: `infra/agentinfra/context_cache.py:61`; AST `e14366185c7bcd0f2153a7652ad936c2791f4c0d86426598692b4c542b446534`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry. Outputs/bindings: (none).
Calls/effect boundaries: entry.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[1].body[1].test.values[0].operand.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[1].body[1].test.values[1].operand::Call

Source: `infra/agentinfra/context_cache.py:61`; AST `169fa616fdeb2b7dce33f31efa765b706787dbb92c04d016e6fd6713d2c792cb`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry, isinstance, list. Outputs/bindings: (none).
Calls/effect boundaries: entry.get, isinstance.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[1].body[1].test.values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[1].body[1].test.values[1].operand.args[0]::Call

Source: `infra/agentinfra/context_cache.py:61`; AST `ae8bc04b6f8c59c322c2722143046617535b209c47db802783dd0c299ccb72b9`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry. Outputs/bindings: (none).
Calls/effect boundaries: entry.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[1].body[1].test.values[1].operand.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[1].body[1].body[0]::Raise

Source: `infra/agentinfra/context_cache.py:62`; AST `97f47a34aaa5699084de90228c6f66317360b859bff879a20c0798ad00e1c22a`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: RuntimeError. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Raise evaluation at root.body[18].body[1].body[1].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[1].body[1].body[0].exc::Call

Source: `infra/agentinfra/context_cache.py:62`; AST `8988e47ade4e07be95082c8921722e437d4bfb2752cabd1a6410863ee6a0c49e`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: RuntimeError. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[1].body[1].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[2]::If

Source: `infra/agentinfra/context_cache.py:63`; AST `fb3c03f99654e1352293fca5fce0ac5fd917fbaf1e7fd187d924a9cfd27fcd93`.

Rust module: `infra::agentinfra::context_cache`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: RuntimeError, all, entry, field, isinstance, str. Outputs/bindings: field.
Calls/effect boundaries: RuntimeError, all, entry.get, isinstance.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered If evaluation at root.body[18].body[1].body[2]; no call, error or mutation may be omitted. Condition: entry['kind'] == 'external'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[2].body[0]::If

Source: `infra/agentinfra/context_cache.py:64`; AST `a7f2c0ada502b6e0fc8274e048ffb3384fa83238a88169ef3fdcf4bb8ec2be1f`.

Rust module: `infra::agentinfra::context_cache`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: RuntimeError, all, entry, field, isinstance, str. Outputs/bindings: field.
Calls/effect boundaries: RuntimeError, all, entry.get, isinstance.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered If evaluation at root.body[18].body[1].body[2].body[0]; no call, error or mutation may be omitted. Condition: not all((isinstance(entry.get(field), str) for field in ('source', 'fingerprint', 'recorded_at', 'provenance')))
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[2].body[0].test.operand::Call

Source: `infra/agentinfra/context_cache.py:64`; AST `4e0c35c30c7ef774d279f300bd86d7e638eee15af78d189568418b065f59a8d1`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, entry, field, isinstance, str. Outputs/bindings: field.
Calls/effect boundaries: all, entry.get, isinstance.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[2].body[0].test.operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[2].body[0].test.operand.args[0]::GeneratorExp

Source: `infra/agentinfra/context_cache.py:64`; AST `f049008dce4c40c49d2368e0fe344589c25dd93e5eabbfdaf16414a8432a226f`.

Rust module: `infra::agentinfra::context_cache`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: entry, field, isinstance, str. Outputs/bindings: field.
Calls/effect boundaries: entry.get, isinstance.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[18].body[1].body[2].body[0].test.operand.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[2].body[0].test.operand.args[0].elt::Call

Source: `infra/agentinfra/context_cache.py:64`; AST `2cc93ca8732dbf9a55b108b5d4d6e7eff3a90584b2c635e9949ac0a859559a36`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry, field, isinstance, str. Outputs/bindings: (none).
Calls/effect boundaries: entry.get, isinstance.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[2].body[0].test.operand.args[0].elt; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[2].body[0].test.operand.args[0].elt.args[0]::Call

Source: `infra/agentinfra/context_cache.py:64`; AST `e85f70e38f6e694765285dc6f4a389ab449ea747644cf584babee01565003154`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry, field. Outputs/bindings: (none).
Calls/effect boundaries: entry.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[2].body[0].test.operand.args[0].elt.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[2].body[0].body[0]::Raise

Source: `infra/agentinfra/context_cache.py:65`; AST `428ba98da33d2c94439eed53a135c72d9b5e27a247586c3df6fdd7277bc1e199`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: RuntimeError. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Raise evaluation at root.body[18].body[1].body[2].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[2].body[0].body[0].exc::Call

Source: `infra/agentinfra/context_cache.py:65`; AST `df7ac237917c63cbe7d1388083b3f8a6f1e698f50ca5033c80094775152d524b`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: RuntimeError. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[2].body[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[2].body[1]::If

Source: `infra/agentinfra/context_cache.py:66`; AST `18706128270aec9a3c98b969d8ca335320f08957ec89a00992a2b94289bc138e`.

Rust module: `infra::agentinfra::context_cache`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: RuntimeError, entry, isinstance, str. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError, entry.get, isinstance.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered If evaluation at root.body[18].body[1].body[2].body[1]; no call, error or mutation may be omitted. Condition: entry.get('valid_until') is not None and (not isinstance(entry.get('valid_until'), str))
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[2].body[1].test.values[0].left::Call

Source: `infra/agentinfra/context_cache.py:66`; AST `51e8dbed4991ffd33745bb3568d52214258b2d91d256850934013a0936468a16`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry. Outputs/bindings: (none).
Calls/effect boundaries: entry.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[2].body[1].test.values[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[2].body[1].test.values[1].operand::Call

Source: `infra/agentinfra/context_cache.py:66`; AST `905906aea1d011d1d7ed636f6e21a604ea30c9adb760e9ad00259ec0d91ca75d`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry, isinstance, str. Outputs/bindings: (none).
Calls/effect boundaries: entry.get, isinstance.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[2].body[1].test.values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[2].body[1].test.values[1].operand.args[0]::Call

Source: `infra/agentinfra/context_cache.py:66`; AST `51e8dbed4991ffd33745bb3568d52214258b2d91d256850934013a0936468a16`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry. Outputs/bindings: (none).
Calls/effect boundaries: entry.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[2].body[1].test.values[1].operand.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[2].body[1].body[0]::Raise

Source: `infra/agentinfra/context_cache.py:67`; AST `8f29edf849d514ae8769c03244deef9d2613d3b9e6528c4063699b519a0a77c7`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: RuntimeError. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Raise evaluation at root.body[18].body[1].body[2].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[2].body[1].body[0].exc::Call

Source: `infra/agentinfra/context_cache.py:67`; AST `9b6bf384b987582355c35d5099303bba5158aa618c25fdc063c1af60bcdb26c5`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: RuntimeError. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[2].body[1].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[3]::If

Source: `infra/agentinfra/context_cache.py:68`; AST `bdf64a2217446e170961c9d7db222e25f7e8097455d99a5789e5750d3cd04810`.

Rust module: `infra::agentinfra::context_cache`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: RuntimeError, entry, int, isinstance, str. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError, entry.get, isinstance.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered If evaluation at root.body[18].body[1].body[3]; no call, error or mutation may be omitted. Condition: entry['kind'] == 'summary'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[3].body[0]::If

Source: `infra/agentinfra/context_cache.py:69`; AST `60649e11eef39219626ef5840afe0b2a268b75776e7765b052a56584089c3b25`.

Rust module: `infra::agentinfra::context_cache`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: RuntimeError, entry, int, isinstance, str. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError, entry.get, isinstance.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered If evaluation at root.body[18].body[1].body[3].body[0]; no call, error or mutation may be omitted. Condition: not isinstance(entry.get('source'), str) or not isinstance(entry.get('sha256'), str) or (not isinstance(entry.get('bytes'), int))
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[3].body[0].test.values[0].operand::Call

Source: `infra/agentinfra/context_cache.py:69`; AST `74eddfd971f1af74a4a88a6cd1ce6719b0b12dd4c420b1cd8cc174afc80eaa61`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry, isinstance, str. Outputs/bindings: (none).
Calls/effect boundaries: entry.get, isinstance.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[3].body[0].test.values[0].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[3].body[0].test.values[0].operand.args[0]::Call

Source: `infra/agentinfra/context_cache.py:69`; AST `c2b0768106637869df27beee6f43af0d1863d28a0b92888ea1528c5f9d7fe319`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry. Outputs/bindings: (none).
Calls/effect boundaries: entry.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[3].body[0].test.values[0].operand.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[3].body[0].test.values[1].operand::Call

Source: `infra/agentinfra/context_cache.py:69`; AST `72f94d9aa654c23a34406ac3c5d9a9333c92b21232ed2356e3a0bca75f1a5708`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry, isinstance, str. Outputs/bindings: (none).
Calls/effect boundaries: entry.get, isinstance.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[3].body[0].test.values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[3].body[0].test.values[1].operand.args[0]::Call

Source: `infra/agentinfra/context_cache.py:69`; AST `7dbb6df6f6be78f4b4b766616b055cf385fda0148b4780fee3ab955e4b89b016`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry. Outputs/bindings: (none).
Calls/effect boundaries: entry.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[3].body[0].test.values[1].operand.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[3].body[0].test.values[2].operand::Call

Source: `infra/agentinfra/context_cache.py:69`; AST `46a966a6920c47d299d0fb333b22993c17bb0cfefc26d0cd79e71ed4709e09a3`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry, int, isinstance. Outputs/bindings: (none).
Calls/effect boundaries: entry.get, isinstance.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[3].body[0].test.values[2].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[3].body[0].test.values[2].operand.args[0]::Call

Source: `infra/agentinfra/context_cache.py:69`; AST `231c6e9900ee9c240f71c4200be0b670d9acb8de79da4efbd8568ede8dfa398b`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry. Outputs/bindings: (none).
Calls/effect boundaries: entry.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[3].body[0].test.values[2].operand.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[3].body[0].body[0]::Raise

Source: `infra/agentinfra/context_cache.py:70`; AST `55f6f27d32625760d5df7c1265982a915f25afe28fcf0d080a618d8d1b105d52`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: RuntimeError. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Raise evaluation at root.body[18].body[1].body[3].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::_validate::root.body[18].body[1].body[3].body[0].body[0].exc::Call

Source: `infra/agentinfra/context_cache.py:70`; AST `b39d193c904c61ec85d21ff62109907410def93a635c5fc322d78d4570b6e325`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: RuntimeError. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[3].body[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::root.body[19]::ClassDef

Source: `infra/agentinfra/context_cache.py:73`; AST `3eabd6b1a859bebbd254312836d7860af2d214d26e2fcc8f11bf00b68b35b221`.

Rust module: `infra::agentinfra::context_cache`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: Exception, FileLock, Iterable, Path, RuntimeError, SCHEMA, ValueError, _now, _parse, _source_key, _stat_identity, _validate, after, atomic_write_json, before, bool, bytes, cache_dir, commit_digest, commit_identity, conclusion, confined_path, confirm, current, current_digest, current_identity, current_stat, data, dep_path, dependencies, dependencies_fresh, dependency, dependency_path, dependency_records, dict, digest, exc, failure_region, fingerprint, fingerprint_fresh, float, fresh, hashlib, identity, int, isinstance, json, key, len, math, middle, old, path, provenance, range, raw, reason, redact_text, root, self, sha256_file, source, str, summary, timedelta, ttl_fresh, ttl_seconds, tuple, until, valid_until. Outputs/bindings: _, after, before, commit_digest, commit_identity, confirm, current, current_digest, current_identity, current_stat, data, dep_path, dependencies_fresh, dependency, dependency_path, dependency_records, digest, fingerprint_fresh, fresh, identity, key, middle, old, path, reason, summary, ttl_fresh, until, valid_until.
Calls/effect boundaries: (current + timedelta(seconds=ttl_seconds)).isoformat, FileLock, Path, RuntimeError, ValueError, _now, _now().isoformat, _parse, _source_key, _stat_identity, _validate, atomic_write_json, bool, cache_dir, confined_path, current.isoformat, data['sources'].get, dep_path.exists, dependency.get, dependency_records.append, fingerprint.strip, hashlib.sha256, hashlib.sha256(raw).hexdigest, hashlib.sha256(source.encode()).hexdigest, hashlib.sha256(str(path.readlink()).encode()).hexdigest, isinstance, json.loads, len, math.isfinite, old.get, path.exists, path.is_symlink, path.readlink, range, redact_text, root.resolve, self._confined, self._consistent_digest, self._save, self.load, self.load()['sources'].get, self.lock.acquire, self.lock.release, self.path.exists, self.path.read_text, sha256_file, source.encode, source.strip, str, str(path.readlink()).encode, timedelta.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered ClassDef evaluation at root.body[19]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::__init__::root.body[19].body[0]::FunctionDef

Source: `infra/agentinfra/context_cache.py:74`; AST `59e8d5d189a1b593f85a44ff546e0416a48c6ee0bb9cdf8970aa7fc619c32e38`.

Rust module: `infra::agentinfra::context_cache`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileLock, Path, cache_dir, root, self. Outputs/bindings: (none).
Calls/effect boundaries: FileLock, cache_dir, root.resolve.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[19].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::__init__::root.body[19].body[0].body[0]::Assign

Source: `infra/agentinfra/context_cache.py:75`; AST `2f05701fc8e1aa914cf88a3a35c9e5e178d0e3674a075174aa2f298cf310c32d`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root, self. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::__init__::root.body[19].body[0].body[0].value::Call

Source: `infra/agentinfra/context_cache.py:75`; AST `56ce091af63844ee93125714af2e994600b88740aa8b9bf3bb1ba7526dba15a7`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::__init__::root.body[19].body[0].body[1]::Assign

Source: `infra/agentinfra/context_cache.py:76`; AST `e2ec781dd07baa574b1786045eb1639d0ab647791d34e2904da4d7d47fac1bcc`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cache_dir, self. Outputs/bindings: (none).
Calls/effect boundaries: cache_dir.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::__init__::root.body[19].body[0].body[1].value.left::Call

Source: `infra/agentinfra/context_cache.py:76`; AST `5f30f1f3a6047e9345338ccaff092d1c8c5a7a3049d3d190cb8e5b63542c2c71`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cache_dir, self. Outputs/bindings: (none).
Calls/effect boundaries: cache_dir.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[0].body[1].value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::__init__::root.body[19].body[0].body[2]::Assign

Source: `infra/agentinfra/context_cache.py:77`; AST `015311fc10a677b3afa94f44f979892941e06e85133cc6798edd7d163506deb5`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileLock, cache_dir, self. Outputs/bindings: (none).
Calls/effect boundaries: FileLock, cache_dir.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::__init__::root.body[19].body[0].body[2].value::Call

Source: `infra/agentinfra/context_cache.py:77`; AST `8de6f69f59c73ed94c095c842f549afae4dc7cf30f9bf235459b9c5072a7596d`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileLock, cache_dir, self. Outputs/bindings: (none).
Calls/effect boundaries: FileLock, cache_dir.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::__init__::root.body[19].body[0].body[2].value.args[0].left::Call

Source: `infra/agentinfra/context_cache.py:77`; AST `5f30f1f3a6047e9345338ccaff092d1c8c5a7a3049d3d190cb8e5b63542c2c71`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cache_dir, self. Outputs/bindings: (none).
Calls/effect boundaries: cache_dir.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[0].body[2].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::load::root.body[19].body[1]::FunctionDef

Source: `infra/agentinfra/context_cache.py:79`; AST `4d37918476af8d60caee52dcaf1117b359e1c8ee8905cfebc53cd8ce21529c3b`.

Rust module: `infra::agentinfra::context_cache`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Exception, RuntimeError, SCHEMA, _validate, data, exc, json, self. Outputs/bindings: data.
Calls/effect boundaries: RuntimeError, _validate, json.loads, self.path.exists, self.path.read_text.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[19].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::load::root.body[19].body[1].body[0]::If

Source: `infra/agentinfra/context_cache.py:80`; AST `b53a00c31604a90d8382a23018d777e61fd529cbd944ad2bfa36795ffe5a8b07`.

Rust module: `infra::agentinfra::context_cache`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: SCHEMA, self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.exists.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered If evaluation at root.body[19].body[1].body[0]; no call, error or mutation may be omitted. Condition: not self.path.exists()
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::load::root.body[19].body[1].body[0].test.operand::Call

Source: `infra/agentinfra/context_cache.py:80`; AST `5a0ab509baad619ec2a1ec684d6882dd1595eead8f620b398322ae10eeaa6916`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.exists.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[1].body[0].test.operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::load::root.body[19].body[1].body[0].body[0]::Return

Source: `infra/agentinfra/context_cache.py:81`; AST `d51f6d79a97978eebe1ef54500f8df91c9f3ee968276e1c6e3de13a2718999f3`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SCHEMA. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Return evaluation at root.body[19].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::load::root.body[19].body[1].body[1]::Try

Source: `infra/agentinfra/context_cache.py:82`; AST `cd9f481ff71e3d88ab1051b6bc7ca01a810022c02dc2aea387bf021b4559b9b3`.

Rust module: `infra::agentinfra::context_cache`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: Exception, RuntimeError, exc, json, self. Outputs/bindings: data.
Calls/effect boundaries: RuntimeError, json.loads, self.path.read_text.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Try evaluation at root.body[19].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::load::root.body[19].body[1].body[1].body[0]::Assign

Source: `infra/agentinfra/context_cache.py:83`; AST `537866d8a69dce44662a10218817fcecfb6a1dafbf579a9f1fa675bb6453b84a`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, self. Outputs/bindings: data.
Calls/effect boundaries: json.loads, self.path.read_text.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[1].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::load::root.body[19].body[1].body[1].body[0].value::Call

Source: `infra/agentinfra/context_cache.py:83`; AST `0821249bc5d520456a58c8bd759d33bc2795100268ab823b399b37e6440024f2`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, self. Outputs/bindings: (none).
Calls/effect boundaries: json.loads, self.path.read_text.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[1].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::load::root.body[19].body[1].body[1].body[0].value.args[0]::Call

Source: `infra/agentinfra/context_cache.py:83`; AST `f9fe252e092d67f80149821fa317f11a8793887293ededd32e981c87c392711c`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.path.read_text.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[1].body[1].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::load::root.body[19].body[1].body[1].handlers[0]::ExceptHandler

Source: `infra/agentinfra/context_cache.py:84`; AST `a582109a6bb4acdc03787b88347badb325345b5e975692a6eba3296e998fcc15`.

Rust module: `infra::agentinfra::context_cache`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: Exception, RuntimeError, exc. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[19].body[1].body[1].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::load::root.body[19].body[1].body[1].handlers[0].body[0]::Raise

Source: `infra/agentinfra/context_cache.py:85`; AST `3e908f9b7eabf7b9d40030693706cb6eb6b42ed4d6502cae51989dc8ce8b754f`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: RuntimeError, exc. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Raise evaluation at root.body[19].body[1].body[1].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::load::root.body[19].body[1].body[1].handlers[0].body[0].exc::Call

Source: `infra/agentinfra/context_cache.py:85`; AST `631608a2b7eaa26c75aae6d9a796c6f3cb76dbd8d1800533a00c274ffd4b5bc5`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: RuntimeError, exc. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[1].body[1].handlers[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::load::root.body[19].body[1].body[2]::Expr

Source: `infra/agentinfra/context_cache.py:86`; AST `f4fa30586a61f21ceb4d6b0985b3775cb5c3cebaa40486117c9f8e011bfb2023`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _validate, data. Outputs/bindings: (none).
Calls/effect boundaries: _validate.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::load::root.body[19].body[1].body[2].value::Call

Source: `infra/agentinfra/context_cache.py:86`; AST `d5dcbad16d51d19bd67aa7abe721f68aa8ed76258b9ee24767f92046216e9e7e`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _validate, data. Outputs/bindings: (none).
Calls/effect boundaries: _validate.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[1].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::load::root.body[19].body[1].body[3]::Return

Source: `infra/agentinfra/context_cache.py:87`; AST `a12e64fa3a041e609d3a25dc46c10c675ec5ec937a53909e14dc1d95d37a3c33`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: data. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Return evaluation at root.body[19].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_save::root.body[19].body[2]::FunctionDef

Source: `infra/agentinfra/context_cache.py:89`; AST `cd501b80f024290c52f171f1d617af9814857fe092095fd3505abaeff053a905`.

Rust module: `infra::agentinfra::context_cache`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: _validate, atomic_write_json, data, self. Outputs/bindings: (none).
Calls/effect boundaries: _validate, atomic_write_json.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[19].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_save::root.body[19].body[2].body[0]::Expr

Source: `infra/agentinfra/context_cache.py:90`; AST `f4fa30586a61f21ceb4d6b0985b3775cb5c3cebaa40486117c9f8e011bfb2023`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _validate, data. Outputs/bindings: (none).
Calls/effect boundaries: _validate.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_save::root.body[19].body[2].body[0].value::Call

Source: `infra/agentinfra/context_cache.py:90`; AST `d5dcbad16d51d19bd67aa7abe721f68aa8ed76258b9ee24767f92046216e9e7e`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _validate, data. Outputs/bindings: (none).
Calls/effect boundaries: _validate.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_save::root.body[19].body[2].body[1]::Expr

Source: `infra/agentinfra/context_cache.py:91`; AST `fab4cfd40f093c331d5b7f6fc8a0fd4a9fa49bd7d40626fe42dfb5c7424447ed`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_json, data, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_save::root.body[19].body[2].body[1].value::Call

Source: `infra/agentinfra/context_cache.py:91`; AST `ee15e6ae45d7d2125fd104f5c494ce06cd1a2d3451ddad4aad247401492770cb`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_json, data, self. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_confined::root.body[19].body[3]::FunctionDef

Source: `infra/agentinfra/context_cache.py:93`; AST `9008b77df97a560cf22260a8606668775c3118f7fe3c7656db3c4caccd402c63`.

Rust module: `infra::agentinfra::context_cache`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, confined_path, path, self. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[19].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_confined::root.body[19].body[3].body[0]::Return

Source: `infra/agentinfra/context_cache.py:94`; AST `385e2f444b57f58415a52a64635f86dfe90be0646105675f2b23448cea35b06b`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, path, self. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Return evaluation at root.body[19].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_confined::root.body[19].body[3].body[0].value::Call

Source: `infra/agentinfra/context_cache.py:94`; AST `40c83c76d9564f1fcc2a0a97675034ea1e1b31e7cc894a016db6d345657e84a0`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, path, self. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_consistent_digest::root.body[19].body[4]::FunctionDef

Source: `infra/agentinfra/context_cache.py:96`; AST `531336305785ff3836fe987a12263784b9d22de81e47eb1337b2d7ea6a2eed81`.

Rust module: `infra::agentinfra::context_cache`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, RuntimeError, _stat_identity, after, before, confirm, dict, digest, hashlib, middle, path, range, sha256_file, str, tuple. Outputs/bindings: _, after, before, confirm, digest, middle.
Calls/effect boundaries: RuntimeError, _stat_identity, hashlib.sha256, hashlib.sha256(str(path.readlink()).encode()).hexdigest, path.is_symlink, path.readlink, range, sha256_file, str, str(path.readlink()).encode.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[19].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_consistent_digest::root.body[19].body[4].body[0]::For

Source: `infra/agentinfra/context_cache.py:97`; AST `7cc9f50105170808af52c69f24ad920c15e3532545a23b708e85c5c472f1d18b`.

Rust module: `infra::agentinfra::context_cache`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: _stat_identity, after, before, confirm, digest, hashlib, middle, path, range, sha256_file, str. Outputs/bindings: _, after, before, confirm, digest, middle.
Calls/effect boundaries: _stat_identity, hashlib.sha256, hashlib.sha256(str(path.readlink()).encode()).hexdigest, path.is_symlink, path.readlink, range, sha256_file, str, str(path.readlink()).encode.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered For evaluation at root.body[19].body[4].body[0]; no call, error or mutation may be omitted. Iteration: _ in range(3)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_consistent_digest::root.body[19].body[4].body[0].iter::Call

Source: `infra/agentinfra/context_cache.py:97`; AST `4b0bc5c55a9ee8588bf55ace54a54a6b18bf698be14d9f944347bc94108247bf`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: range. Outputs/bindings: (none).
Calls/effect boundaries: range.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[4].body[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_consistent_digest::root.body[19].body[4].body[0].body[0]::Assign

Source: `infra/agentinfra/context_cache.py:98`; AST `57cc91b717237f16561a4bf0d633509fde0e0d75f8ad7c28c47b0060b9d6b8cd`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _stat_identity, path. Outputs/bindings: before.
Calls/effect boundaries: _stat_identity.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[4].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_consistent_digest::root.body[19].body[4].body[0].body[0].value::Call

Source: `infra/agentinfra/context_cache.py:98`; AST `fbb8991cb345020e0440194f2f6918e3e6af513a0219b18ad3077d68ae44fa0d`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _stat_identity, path. Outputs/bindings: (none).
Calls/effect boundaries: _stat_identity.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[4].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_consistent_digest::root.body[19].body[4].body[0].body[1]::Assign

Source: `infra/agentinfra/context_cache.py:99`; AST `5e2854a4d7296c7576094c5445383619bef88b422bb584d2758af17bb6a61c65`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: hashlib, path, sha256_file, str. Outputs/bindings: digest.
Calls/effect boundaries: hashlib.sha256, hashlib.sha256(str(path.readlink()).encode()).hexdigest, path.is_symlink, path.readlink, sha256_file, str, str(path.readlink()).encode.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[4].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_consistent_digest::root.body[19].body[4].body[0].body[1].value.test.operand::Call

Source: `infra/agentinfra/context_cache.py:99`; AST `59b1c604985dcd3e66bb0b7ae49c367ee9372b6c297d22636b1ad06e54b90bcc`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.is_symlink.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[4].body[0].body[1].value.test.operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_consistent_digest::root.body[19].body[4].body[0].body[1].value.body::Call

Source: `infra/agentinfra/context_cache.py:99`; AST `a5c91ee3a3e2194edf29fb1e513a5ed89ca1afd112d67d6be4e4a5c4d59b570f`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, sha256_file. Outputs/bindings: (none).
Calls/effect boundaries: sha256_file.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[4].body[0].body[1].value.body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_consistent_digest::root.body[19].body[4].body[0].body[1].value.orelse::Call

Source: `infra/agentinfra/context_cache.py:99`; AST `e834fc86ccd90ad7d4fce323216c5311ceadec81ce2ece8d729b5b6ebcf4fe7b`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: hashlib, path, str. Outputs/bindings: (none).
Calls/effect boundaries: hashlib.sha256, hashlib.sha256(str(path.readlink()).encode()).hexdigest, path.readlink, str, str(path.readlink()).encode.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[4].body[0].body[1].value.orelse; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_consistent_digest::root.body[19].body[4].body[0].body[1].value.orelse.func.value::Call

Source: `infra/agentinfra/context_cache.py:99`; AST `46dc58f37579b01ff86788d6da1eba79c84f357d3b4420ff1b155c55271ce448`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: hashlib, path, str. Outputs/bindings: (none).
Calls/effect boundaries: hashlib.sha256, path.readlink, str, str(path.readlink()).encode.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[4].body[0].body[1].value.orelse.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_consistent_digest::root.body[19].body[4].body[0].body[1].value.orelse.func.value.args[0]::Call

Source: `infra/agentinfra/context_cache.py:99`; AST `014062c943405f805b1308191d0dad632f84e13d5112aab8d903b49ca6dd62c1`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, str. Outputs/bindings: (none).
Calls/effect boundaries: path.readlink, str, str(path.readlink()).encode.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[4].body[0].body[1].value.orelse.func.value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_consistent_digest::root.body[19].body[4].body[0].body[1].value.orelse.func.value.args[0].func.value::Call

Source: `infra/agentinfra/context_cache.py:99`; AST `551c4b501723b32f24d138416ac1976c85bd096d61b5583cf31222ab1f181a68`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, str. Outputs/bindings: (none).
Calls/effect boundaries: path.readlink, str.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[4].body[0].body[1].value.orelse.func.value.args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_consistent_digest::root.body[19].body[4].body[0].body[1].value.orelse.func.value.args[0].func.value.args[0]::Call

Source: `infra/agentinfra/context_cache.py:99`; AST `be12d503fd54bd779d75ccf612bcdbf41e065e05b938e9dfedb0ec2536ee3343`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.readlink.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[4].body[0].body[1].value.orelse.func.value.args[0].func.value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_consistent_digest::root.body[19].body[4].body[0].body[2]::Assign

Source: `infra/agentinfra/context_cache.py:100`; AST `e6ac7f293ecc520688925bb9be01d26eb60a46921bc87d8e685420933a810b88`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _stat_identity, path. Outputs/bindings: middle.
Calls/effect boundaries: _stat_identity.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[4].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_consistent_digest::root.body[19].body[4].body[0].body[2].value::Call

Source: `infra/agentinfra/context_cache.py:100`; AST `fbb8991cb345020e0440194f2f6918e3e6af513a0219b18ad3077d68ae44fa0d`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _stat_identity, path. Outputs/bindings: (none).
Calls/effect boundaries: _stat_identity.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[4].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_consistent_digest::root.body[19].body[4].body[0].body[3]::If

Source: `infra/agentinfra/context_cache.py:101`; AST `14cdf4eefc11671f4c6aad584fb2bc15019e3c1a3d60bb5f9974ce22f20efbbe`.

Rust module: `infra::agentinfra::context_cache`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: before, middle. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered If evaluation at root.body[19].body[4].body[0].body[3]; no call, error or mutation may be omitted. Condition: before != middle
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_consistent_digest::root.body[19].body[4].body[0].body[3].body[0]::Continue

Source: `infra/agentinfra/context_cache.py:102`; AST `3d1e0aaa463df3eefc9bd5be83f453adcd9621b2dc7f387c3eaff3ab42e91059`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Continue evaluation at root.body[19].body[4].body[0].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_consistent_digest::root.body[19].body[4].body[0].body[4]::Assign

Source: `infra/agentinfra/context_cache.py:103`; AST `65e45370f16a0eb52b1b6cf8e407e71fd61198185162e3edd2a8e5e0b3a1c71f`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: hashlib, path, sha256_file, str. Outputs/bindings: confirm.
Calls/effect boundaries: hashlib.sha256, hashlib.sha256(str(path.readlink()).encode()).hexdigest, path.is_symlink, path.readlink, sha256_file, str, str(path.readlink()).encode.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[4].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_consistent_digest::root.body[19].body[4].body[0].body[4].value.test.operand::Call

Source: `infra/agentinfra/context_cache.py:103`; AST `59b1c604985dcd3e66bb0b7ae49c367ee9372b6c297d22636b1ad06e54b90bcc`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.is_symlink.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[4].body[0].body[4].value.test.operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_consistent_digest::root.body[19].body[4].body[0].body[4].value.body::Call

Source: `infra/agentinfra/context_cache.py:103`; AST `a5c91ee3a3e2194edf29fb1e513a5ed89ca1afd112d67d6be4e4a5c4d59b570f`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, sha256_file. Outputs/bindings: (none).
Calls/effect boundaries: sha256_file.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[4].body[0].body[4].value.body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_consistent_digest::root.body[19].body[4].body[0].body[4].value.orelse::Call

Source: `infra/agentinfra/context_cache.py:103`; AST `e834fc86ccd90ad7d4fce323216c5311ceadec81ce2ece8d729b5b6ebcf4fe7b`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: hashlib, path, str. Outputs/bindings: (none).
Calls/effect boundaries: hashlib.sha256, hashlib.sha256(str(path.readlink()).encode()).hexdigest, path.readlink, str, str(path.readlink()).encode.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[4].body[0].body[4].value.orelse; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_consistent_digest::root.body[19].body[4].body[0].body[4].value.orelse.func.value::Call

Source: `infra/agentinfra/context_cache.py:103`; AST `46dc58f37579b01ff86788d6da1eba79c84f357d3b4420ff1b155c55271ce448`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: hashlib, path, str. Outputs/bindings: (none).
Calls/effect boundaries: hashlib.sha256, path.readlink, str, str(path.readlink()).encode.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[4].body[0].body[4].value.orelse.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_consistent_digest::root.body[19].body[4].body[0].body[4].value.orelse.func.value.args[0]::Call

Source: `infra/agentinfra/context_cache.py:103`; AST `014062c943405f805b1308191d0dad632f84e13d5112aab8d903b49ca6dd62c1`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, str. Outputs/bindings: (none).
Calls/effect boundaries: path.readlink, str, str(path.readlink()).encode.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[4].body[0].body[4].value.orelse.func.value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_consistent_digest::root.body[19].body[4].body[0].body[4].value.orelse.func.value.args[0].func.value::Call

Source: `infra/agentinfra/context_cache.py:103`; AST `551c4b501723b32f24d138416ac1976c85bd096d61b5583cf31222ab1f181a68`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, str. Outputs/bindings: (none).
Calls/effect boundaries: path.readlink, str.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[4].body[0].body[4].value.orelse.func.value.args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_consistent_digest::root.body[19].body[4].body[0].body[4].value.orelse.func.value.args[0].func.value.args[0]::Call

Source: `infra/agentinfra/context_cache.py:103`; AST `be12d503fd54bd779d75ccf612bcdbf41e065e05b938e9dfedb0ec2536ee3343`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.readlink.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[4].body[0].body[4].value.orelse.func.value.args[0].func.value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_consistent_digest::root.body[19].body[4].body[0].body[5]::Assign

Source: `infra/agentinfra/context_cache.py:104`; AST `e55ebb5e564019966783f683d9633d6786b1f98e50355455668d975c3804e61f`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _stat_identity, path. Outputs/bindings: after.
Calls/effect boundaries: _stat_identity.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[4].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_consistent_digest::root.body[19].body[4].body[0].body[5].value::Call

Source: `infra/agentinfra/context_cache.py:104`; AST `fbb8991cb345020e0440194f2f6918e3e6af513a0219b18ad3077d68ae44fa0d`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _stat_identity, path. Outputs/bindings: (none).
Calls/effect boundaries: _stat_identity.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[4].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_consistent_digest::root.body[19].body[4].body[0].body[6]::If

Source: `infra/agentinfra/context_cache.py:105`; AST `fbd4cf10a8d1101dad727e23cbcf62cf07aab8e8f62b91fccc16db70e244d743`.

Rust module: `infra::agentinfra::context_cache`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: after, confirm, digest, middle. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered If evaluation at root.body[19].body[4].body[0].body[6]; no call, error or mutation may be omitted. Condition: middle == after and digest == confirm
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_consistent_digest::root.body[19].body[4].body[0].body[6].body[0]::Return

Source: `infra/agentinfra/context_cache.py:106`; AST `1d357d9feb397cdce01dd1feabcfe695aabc64af5598f408c1f00d775d483e52`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: after, digest. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Return evaluation at root.body[19].body[4].body[0].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_consistent_digest::root.body[19].body[4].body[1]::Raise

Source: `infra/agentinfra/context_cache.py:107`; AST `c07619a6d446bce5e9cc7c37f626c185f993ac08755d8a3ae4b509063fb2845f`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: RuntimeError, path. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Raise evaluation at root.body[19].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::_consistent_digest::root.body[19].body[4].body[1].exc::Call

Source: `infra/agentinfra/context_cache.py:107`; AST `e973fa04c7024aa5f31471ea04ba7dc35b100e8ee16f00c6ab40985edc119d46`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: RuntimeError, path. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[4].body[1].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5]::FunctionDef

Source: `infra/agentinfra/context_cache.py:109`; AST `239a4e336cd07db1336c45c6d843b020da145cbcd671534cceab259cad1aa5e3`.

Rust module: `infra::agentinfra::context_cache`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Iterable, Path, RuntimeError, _now, commit_digest, commit_identity, conclusion, current_digest, current_identity, data, dependencies, dependency, dependency_path, dependency_records, digest, identity, key, path, redact_text, self, str. Outputs/bindings: commit_digest, commit_identity, current_digest, current_identity, data, dependency, dependency_path, dependency_records, digest, identity, key, path.
Calls/effect boundaries: Path, RuntimeError, _now, _now().isoformat, dependency_records.append, redact_text, self._confined, self._consistent_digest, self._save, self.load, self.lock.acquire, self.lock.release, str.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[19].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[0]::Assign

Source: `infra/agentinfra/context_cache.py:110`; AST `204905995e3757c8d83f28825f4e6d25a7b5ae8d84296d0274ed5ace7f90e263`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path, self. Outputs/bindings: path.
Calls/effect boundaries: self._confined.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[0].value::Call

Source: `infra/agentinfra/context_cache.py:110`; AST `925071545fb89cad9b8e1168d54c8d8ec4ab819abbfe408bd9294859ad5a8070`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, self. Outputs/bindings: (none).
Calls/effect boundaries: self._confined.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[1]::Assign

Source: `infra/agentinfra/context_cache.py:111`; AST `270c37444c7e3a00ab089f9da174b28dae22a64ffb56a04066f0294b24b61cc9`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: dependency_records.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[2]::For

Source: `infra/agentinfra/context_cache.py:112`; AST `064dc9f8bfcdf7d06028f68540a4e2bf8fe786eb153adc69f5d92abee371e714`.

Rust module: `infra::agentinfra::context_cache`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: dependencies, dependency, dependency_records, digest, identity, self, str. Outputs/bindings: dependency, digest, identity.
Calls/effect boundaries: dependency_records.append, self._confined, self._consistent_digest, str.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered For evaluation at root.body[19].body[5].body[2]; no call, error or mutation may be omitted. Iteration: dependency in dependencies
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[2].body[0]::Assign

Source: `infra/agentinfra/context_cache.py:113`; AST `9e23a3cd96a8ceadc68121f37f6b4b845d11a3007e06f836ae1110a2e84bfbbc`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dependency, self. Outputs/bindings: dependency.
Calls/effect boundaries: self._confined.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[5].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[2].body[0].value::Call

Source: `infra/agentinfra/context_cache.py:113`; AST `280a5bfb40c9003d50ee7e2e508e1d88a3f2d5c7f3ca8fc4082d82309782168d`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dependency, self. Outputs/bindings: (none).
Calls/effect boundaries: self._confined.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[2].body[1]::Assign

Source: `infra/agentinfra/context_cache.py:114`; AST `b7c3b363c65037706ccad1c31e0a0dfe357fc4003c386d5dc5598c2d17c45d2e`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dependency, self. Outputs/bindings: digest, identity.
Calls/effect boundaries: self._consistent_digest.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[5].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[2].body[1].value::Call

Source: `infra/agentinfra/context_cache.py:114`; AST `1b43b88bb0b08bc9035a92a33fd759ed5a9509d14443c9dd654cd1c89263f244`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dependency, self. Outputs/bindings: (none).
Calls/effect boundaries: self._consistent_digest.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[2].body[2]::Expr

Source: `infra/agentinfra/context_cache.py:115`; AST `158ddfb47e96eb9dfc3370af3fa50e2f9007adb9844b5710481b26a5fe7ab64f`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dependency, dependency_records, digest, identity, str. Outputs/bindings: (none).
Calls/effect boundaries: dependency_records.append, str.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[5].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[2].body[2].value::Call

Source: `infra/agentinfra/context_cache.py:115`; AST `0c9214c40b628fbb76d41b9f9d9b0fd34284d3df87bc538f949ecee821b831db`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dependency, dependency_records, digest, identity, str. Outputs/bindings: (none).
Calls/effect boundaries: dependency_records.append, str.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[2].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[2].body[2].value.args[0].values[0]::Call

Source: `infra/agentinfra/context_cache.py:115`; AST `e992f7f6502424c03279d2999449023d143ac98cb4f25549c76298a83d98d3a5`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dependency, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[2].body[2].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[3]::Assign

Source: `infra/agentinfra/context_cache.py:116`; AST `ab501ba01167458ca5c64d4d4a5e16ee0d0d0551f9672b64df8607a3f0c29891`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path, self. Outputs/bindings: digest, identity.
Calls/effect boundaries: self._consistent_digest.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[5].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[3].value::Call

Source: `infra/agentinfra/context_cache.py:116`; AST `4e95ee5049f4a1c2efdc65c66dc2aac9331a7e2f11b7d4dc3ab774e03ccaff0b`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, self. Outputs/bindings: (none).
Calls/effect boundaries: self._consistent_digest.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[4]::Expr

Source: `infra/agentinfra/context_cache.py:117`; AST `0e311ceac884a90dfdabd855c70d5b78193fef9fcb47613639d4c89049fa7b18`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.lock.acquire.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[5].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[4].value::Call

Source: `infra/agentinfra/context_cache.py:117`; AST `835ba501008cc8885bd889a8fad52e6a4b87965e27f757cf5d9b7c014ac190e9`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.lock.acquire.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[5]::Try

Source: `infra/agentinfra/context_cache.py:118`; AST `4b57afc4aab5c072e6063ed95d7a01d825addc2df8eb76f3539a90a6eae74354`.

Rust module: `infra::agentinfra::context_cache`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: Path, RuntimeError, _now, commit_digest, commit_identity, conclusion, current_digest, current_identity, data, dependency, dependency_path, dependency_records, digest, identity, key, path, redact_text, self, str. Outputs/bindings: commit_digest, commit_identity, current_digest, current_identity, data, dependency, dependency_path, key.
Calls/effect boundaries: Path, RuntimeError, _now, _now().isoformat, redact_text, self._consistent_digest, self._save, self.load, self.lock.release, str.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Try evaluation at root.body[19].body[5].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[5].body[0]::Assign

Source: `infra/agentinfra/context_cache.py:119`; AST `b5d1c1890e3a864cecf36d276763f8f314b86cd89224e46fb92ecb3b08653049`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path, self. Outputs/bindings: commit_digest, commit_identity.
Calls/effect boundaries: self._consistent_digest.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[5].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[5].body[0].value::Call

Source: `infra/agentinfra/context_cache.py:119`; AST `4e95ee5049f4a1c2efdc65c66dc2aac9331a7e2f11b7d4dc3ab774e03ccaff0b`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, self. Outputs/bindings: (none).
Calls/effect boundaries: self._consistent_digest.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[5].body[1]::If

Source: `infra/agentinfra/context_cache.py:120`; AST `f5531e3d202ccc8565281ea46671ad3a4dbc5784e3ccda2c39aeb98bbd1b82c3`.

Rust module: `infra::agentinfra::context_cache`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: RuntimeError, commit_digest, commit_identity, digest, identity, path. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered If evaluation at root.body[19].body[5].body[5].body[1]; no call, error or mutation may be omitted. Condition: commit_identity != identity or commit_digest != digest
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[5].body[1].body[0]::Raise

Source: `infra/agentinfra/context_cache.py:121`; AST `8566b0f01c262b50c35a62b0a3bae269e484448ab8a0f9cb546f7a65fea2d77f`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: RuntimeError, path. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Raise evaluation at root.body[19].body[5].body[5].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[5].body[1].body[0].exc::Call

Source: `infra/agentinfra/context_cache.py:121`; AST `3213ad9c84aa51c2230a481d76b1fa607176c3da5cdbe1cfaf323ce6d06f1a89`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: RuntimeError, path. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[5].body[1].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[5].body[2]::For

Source: `infra/agentinfra/context_cache.py:122`; AST `224d8fba454848d0e72912310272858a28ee4ac1522f9d5eda722bca4d4db0c9`.

Rust module: `infra::agentinfra::context_cache`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: Path, RuntimeError, current_digest, current_identity, dependency, dependency_path, dependency_records, self. Outputs/bindings: current_digest, current_identity, dependency, dependency_path.
Calls/effect boundaries: Path, RuntimeError, self._consistent_digest.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered For evaluation at root.body[19].body[5].body[5].body[2]; no call, error or mutation may be omitted. Iteration: dependency in dependency_records
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[5].body[2].body[0]::Assign

Source: `infra/agentinfra/context_cache.py:123`; AST `0da75eb5e24ebf61dc420fa974628b888ff3e04dc8cdc69ad6e75d7dc439015a`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, dependency. Outputs/bindings: dependency_path.
Calls/effect boundaries: Path.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[5].body[5].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[5].body[2].body[0].value::Call

Source: `infra/agentinfra/context_cache.py:123`; AST `ff81b7004a9a3f3599f2a8edac86e573da8bb1a82ae2ccfa977349bd1c78c362`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, dependency. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[5].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[5].body[2].body[1]::Assign

Source: `infra/agentinfra/context_cache.py:124`; AST `8cd655296d71f88866c8ac2fd248b32eea22a1d7ab61ed2d524fdf48313d03de`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dependency_path, self. Outputs/bindings: current_digest, current_identity.
Calls/effect boundaries: self._consistent_digest.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[5].body[5].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[5].body[2].body[1].value::Call

Source: `infra/agentinfra/context_cache.py:124`; AST `3583b8624645bd4976d667d18d077d3868657a0ecd46a5dfc0ee9e2e7be57f69`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dependency_path, self. Outputs/bindings: (none).
Calls/effect boundaries: self._consistent_digest.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[5].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[5].body[2].body[2]::If

Source: `infra/agentinfra/context_cache.py:125`; AST `1748050604daed93ffef426c940ebe0ed55d07269b5461c0b042cead3caec476`.

Rust module: `infra::agentinfra::context_cache`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: RuntimeError, current_digest, current_identity, dependency, dependency_path. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered If evaluation at root.body[19].body[5].body[5].body[2].body[2]; no call, error or mutation may be omitted. Condition: current_digest != dependency['sha256'] or current_identity != dependency['stat']
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[5].body[2].body[2].body[0]::Raise

Source: `infra/agentinfra/context_cache.py:126`; AST `62d5a248c334f47a34e759ffe03ae5e551db04814e0f1b5f1d9994167a5d52d5`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: RuntimeError, dependency_path. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Raise evaluation at root.body[19].body[5].body[5].body[2].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[5].body[2].body[2].body[0].exc::Call

Source: `infra/agentinfra/context_cache.py:126`; AST `27527a9d56e4c62eab031de7c7a5ab822fdebec06251c1e04cbdd20e4cd4404d`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: RuntimeError, dependency_path. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[5].body[2].body[2].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[5].body[3]::Assign

Source: `infra/agentinfra/context_cache.py:127`; AST `50b892d2585db987722e6aede6ac50be76f346921c72be68b99e3d5028a335af`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: data.
Calls/effect boundaries: self.load.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[5].body[5].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[5].body[3].value::Call

Source: `infra/agentinfra/context_cache.py:127`; AST `2f7b1542b904a22e99e3302fee96f8ab07261aa40c719345db0fafa2aed323fd`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.load.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[5].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[5].body[4]::Assign

Source: `infra/agentinfra/context_cache.py:128`; AST `7d72e9a041a8aec04ea6ef114f37b6f2f249013622e1438f0c9cf92b280aa570`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path, str. Outputs/bindings: key.
Calls/effect boundaries: str.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[5].body[5].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[5].body[4].value::Call

Source: `infra/agentinfra/context_cache.py:128`; AST `b69621d1d2cfab110acfa6b4ec39b44f2e36ecd25b7402532cc02261af94b6bf`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[5].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[5].body[5]::Assign

Source: `infra/agentinfra/context_cache.py:129`; AST `d3676c1b1cfa9d7d6376b5302f775a31d30c8fff4a854323a7a61b47e6b00678`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _now, conclusion, data, dependency_records, digest, identity, key, redact_text. Outputs/bindings: (none).
Calls/effect boundaries: _now, _now().isoformat, redact_text.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[5].body[5].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[5].body[5].value.values[5]::Call

Source: `infra/agentinfra/context_cache.py:135`; AST `8c39afb7de67447382726c270666bc2a6e3650639e72f1badecdb141996b4099`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: conclusion, redact_text. Outputs/bindings: (none).
Calls/effect boundaries: redact_text.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[5].body[5].value.values[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[5].body[5].value.values[6]::Call

Source: `infra/agentinfra/context_cache.py:136`; AST `d3f9e407bb5c13d6be1e67ea02303b2a5ab2eeb3ff1f26c7056d7250b26ab317`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _now. Outputs/bindings: (none).
Calls/effect boundaries: _now, _now().isoformat.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[5].body[5].value.values[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[5].body[5].value.values[6].func.value::Call

Source: `infra/agentinfra/context_cache.py:136`; AST `a45c2ac57befcf1212794e7c42a7aad7870de2198eba961b8d2f47b37f928f0f`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _now. Outputs/bindings: (none).
Calls/effect boundaries: _now.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[5].body[5].value.values[6].func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[5].body[6]::Expr

Source: `infra/agentinfra/context_cache.py:138`; AST `dab24004df007d3fab18fe8f8a3d672b270bc56729e3c5b36b4158bc20c37d0b`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: data, self. Outputs/bindings: (none).
Calls/effect boundaries: self._save.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[5].body[5].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[5].body[6].value::Call

Source: `infra/agentinfra/context_cache.py:138`; AST `8ebfa7986579ca006ae588c0cd261918f6965304c8eb2fb03ec2d47d54c0fd82`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data, self. Outputs/bindings: (none).
Calls/effect boundaries: self._save.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[5].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[5].body[7]::Return

Source: `infra/agentinfra/context_cache.py:139`; AST `92daa78d8f02e52fa6cadb21edea654a0d2b1afa9fd252e346f4959645323db5`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: data, key. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Return evaluation at root.body[19].body[5].body[5].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[5].finalbody[0]::Expr

Source: `infra/agentinfra/context_cache.py:141`; AST `50795522f731c697d7e2cab3a3003d5a9415cac791c6b4a635917bf2159ceac4`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.lock.release.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[5].body[5].finalbody[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_file::root.body[19].body[5].body[5].finalbody[0].value::Call

Source: `infra/agentinfra/context_cache.py:141`; AST `fda84b64bf236157e2f4744fc88aca42822337862c351b2c52b5e9a5ee54e621`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.lock.release.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[5].finalbody[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6]::FunctionDef

Source: `infra/agentinfra/context_cache.py:143`; AST `6d4281e1eb402054252a6e2fdafebe87ca9f493ff0cfc8a4cd002d02f7f16a1e`.

Rust module: `infra::agentinfra::context_cache`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, _stat_identity, confined_path, current_stat, data, dep_path, dependencies_fresh, dependency, digest, old, path, self, str. Outputs/bindings: _, current_stat, data, dep_path, dependencies_fresh, dependency, digest, old, path.
Calls/effect boundaries: _stat_identity, confined_path, data['sources'].get, dep_path.exists, dependency.get, old.get, path.exists, path.is_symlink, self._consistent_digest, self.load, str.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[19].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6].body[0]::Assign

Source: `infra/agentinfra/context_cache.py:144`; AST `ffc64513ddfc5d7f3092ba6816acaa2aa7239c7b342ecebb91a1ba2bbaf80889`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, path, self. Outputs/bindings: path.
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6].body[0].value::Call

Source: `infra/agentinfra/context_cache.py:144`; AST `14cbd93db90890673dc82f4d66f1c3376d533049952f4f237eeedd7f128cee64`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, path, self. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6].body[1]::Assign

Source: `infra/agentinfra/context_cache.py:145`; AST `50b892d2585db987722e6aede6ac50be76f346921c72be68b99e3d5028a335af`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: data.
Calls/effect boundaries: self.load.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6].body[1].value::Call

Source: `infra/agentinfra/context_cache.py:145`; AST `2f7b1542b904a22e99e3302fee96f8ab07261aa40c719345db0fafa2aed323fd`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.load.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[6].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6].body[2]::Assign

Source: `infra/agentinfra/context_cache.py:146`; AST `d687886c5b9b55bda0f4bae8f449266fb50c139656204aa0dcdca819160b77bc`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: data, path, str. Outputs/bindings: old.
Calls/effect boundaries: data['sources'].get, str.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[6].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6].body[2].value::Call

Source: `infra/agentinfra/context_cache.py:146`; AST `7e0c3a208836b70a847fd36b8e3f0752cda2a502a637c72634c53115bd8d460d`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data, path, str. Outputs/bindings: (none).
Calls/effect boundaries: data['sources'].get, str.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[6].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6].body[2].value.args[0]::Call

Source: `infra/agentinfra/context_cache.py:146`; AST `b69621d1d2cfab110acfa6b4ec39b44f2e36ecd25b7402532cc02261af94b6bf`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[6].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6].body[3]::If

Source: `infra/agentinfra/context_cache.py:147`; AST `d0fbe15b0bb77488cc5e76da3790dc32cbbe7b8498befb566cb428c70f2950ea`.

Rust module: `infra::agentinfra::context_cache`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: old. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered If evaluation at root.body[19].body[6].body[3]; no call, error or mutation may be omitted. Condition: not old
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6].body[3].body[0]::Return

Source: `infra/agentinfra/context_cache.py:148`; AST `a618bbff4813bc2cb08c56098a9653ee60d1ff28d7ae28c345192bff765d25c0`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Return evaluation at root.body[19].body[6].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6].body[4]::If

Source: `infra/agentinfra/context_cache.py:149`; AST `d44cf2b2dcc67ad94f45872e09c296474e44b30aff625cd594455d4de338d708`.

Rust module: `infra::agentinfra::context_cache`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.exists, path.is_symlink.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered If evaluation at root.body[19].body[6].body[4]; no call, error or mutation may be omitted. Condition: not path.exists() and (not path.is_symlink())
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6].body[4].test.values[0].operand::Call

Source: `infra/agentinfra/context_cache.py:149`; AST `2cac3ec82b344023c57b4bbfcae282698ef12842cbda26a14724eacbefb97016`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.exists.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[6].body[4].test.values[0].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6].body[4].test.values[1].operand::Call

Source: `infra/agentinfra/context_cache.py:149`; AST `59b1c604985dcd3e66bb0b7ae49c367ee9372b6c297d22636b1ad06e54b90bcc`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.is_symlink.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[6].body[4].test.values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6].body[4].body[0]::Return

Source: `infra/agentinfra/context_cache.py:150`; AST `9d1ce7145d03b4827a06594cb7882b1ad435c99bc95ae85a691374ed79157acb`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Return evaluation at root.body[19].body[6].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6].body[5]::Assign

Source: `infra/agentinfra/context_cache.py:151`; AST `e9ed63d614b8f3e0e1c4c745e06d8acde66a6276aae8c004044caf848b4ad3ae`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _stat_identity, path. Outputs/bindings: current_stat.
Calls/effect boundaries: _stat_identity.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[6].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6].body[5].value::Call

Source: `infra/agentinfra/context_cache.py:151`; AST `fbb8991cb345020e0440194f2f6918e3e6af513a0219b18ad3077d68ae44fa0d`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _stat_identity, path. Outputs/bindings: (none).
Calls/effect boundaries: _stat_identity.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[6].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6].body[6]::Assign

Source: `infra/agentinfra/context_cache.py:152`; AST `7aded2ec57c7a0324263944e88c13e967c6fb67ab4ba1aefb17d8912ce1c635f`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: dependencies_fresh.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[6].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6].body[7]::For

Source: `infra/agentinfra/context_cache.py:153`; AST `16b75ffaae8ea20caa947a0ffbc77e731d50355a8c3a90a75fb970c0305685e1`.

Rust module: `infra::agentinfra::context_cache`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: _stat_identity, confined_path, dep_path, dependency, old, self. Outputs/bindings: dep_path, dependencies_fresh, dependency.
Calls/effect boundaries: _stat_identity, confined_path, dep_path.exists, dependency.get, old.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered For evaluation at root.body[19].body[6].body[7]; no call, error or mutation may be omitted. Iteration: dependency in old.get('dependencies', [])
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6].body[7].iter::Call

Source: `infra/agentinfra/context_cache.py:153`; AST `e4f5a3e5bc3e40c6e606856f1c88e1a2b7111453771d9a730cf6c08b14df9d72`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old. Outputs/bindings: (none).
Calls/effect boundaries: old.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[6].body[7].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6].body[7].body[0]::Assign

Source: `infra/agentinfra/context_cache.py:154`; AST `8d3e2a5c188e0cd8ccc0196a504056070cdfa16eb6fd4fac8b674980faf2c2fd`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, dependency, self. Outputs/bindings: dep_path.
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[6].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6].body[7].body[0].value::Call

Source: `infra/agentinfra/context_cache.py:154`; AST `726017cc67abe323b913150f339f14e2011eab99adfd8f3ba48532096147dd6b`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, dependency, self. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[6].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6].body[7].body[1]::If

Source: `infra/agentinfra/context_cache.py:155`; AST `744e73741e2eaeb589454aee84f2275f1ffeac9baefeb88f1b217f365f4a1daf`.

Rust module: `infra::agentinfra::context_cache`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: _stat_identity, dep_path, dependency. Outputs/bindings: dependencies_fresh.
Calls/effect boundaries: _stat_identity, dep_path.exists, dependency.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered If evaluation at root.body[19].body[6].body[7].body[1]; no call, error or mutation may be omitted. Condition: not dep_path.exists() or _stat_identity(dep_path) != dependency.get('stat')
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6].body[7].body[1].test.values[0].operand::Call

Source: `infra/agentinfra/context_cache.py:155`; AST `32638d279486d0e64b926c1b776706dcf34da1f904cd066c976c39558c5729ec`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dep_path. Outputs/bindings: (none).
Calls/effect boundaries: dep_path.exists.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[6].body[7].body[1].test.values[0].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6].body[7].body[1].test.values[1].left::Call

Source: `infra/agentinfra/context_cache.py:155`; AST `9a317c566e7db3240fad067875f25e1761498142f71d12607168540390b46ae5`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _stat_identity, dep_path. Outputs/bindings: (none).
Calls/effect boundaries: _stat_identity.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[6].body[7].body[1].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6].body[7].body[1].test.values[1].comparators[0]::Call

Source: `infra/agentinfra/context_cache.py:155`; AST `297854b59ccc027bd5e9905f9312f0e6bdc6feeaa6c25efe645b730c0acbce8c`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dependency. Outputs/bindings: (none).
Calls/effect boundaries: dependency.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[6].body[7].body[1].test.values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6].body[7].body[1].body[0]::Assign

Source: `infra/agentinfra/context_cache.py:156`; AST `a954ce1f4dd058e4d4d3aa1d5570859a33a0831528bf444298bb9be4a12b0fc8`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: dependencies_fresh.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[6].body[7].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6].body[7].body[1].body[1]::Break

Source: `infra/agentinfra/context_cache.py:157`; AST `c0d25d96e6146e7b648417b86bf6bbfedd0a458099247cf2cd469124da4c9fec`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Break evaluation at root.body[19].body[6].body[7].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6].body[8]::If

Source: `infra/agentinfra/context_cache.py:158`; AST `918607848e80bd8862a139e085a2002fc9a95b89662646763def79e4cf29ea05`.

Rust module: `infra::agentinfra::context_cache`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: current_stat, dependencies_fresh, old. Outputs/bindings: (none).
Calls/effect boundaries: old.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered If evaluation at root.body[19].body[6].body[8]; no call, error or mutation may be omitted. Condition: current_stat == old.get('stat') and dependencies_fresh
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6].body[8].test.values[0].comparators[0]::Call

Source: `infra/agentinfra/context_cache.py:158`; AST `56957e39ba3d82030f5c3bb38bc4c90bad7e665401474ce5f43896ceebbac2d9`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old. Outputs/bindings: (none).
Calls/effect boundaries: old.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[6].body[8].test.values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6].body[8].body[0]::Return

Source: `infra/agentinfra/context_cache.py:159`; AST `cecd9a7f55faee1ece5069b538b64c75d856c11423addd1d1331d9ae42f3fea0`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: old. Outputs/bindings: (none).
Calls/effect boundaries: old.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Return evaluation at root.body[19].body[6].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6].body[8].body[0].value.values[4]::Call

Source: `infra/agentinfra/context_cache.py:164`; AST `4fb3a5911bd983b4ec9afe9ec799d6c80c7b45ca228668cf483ee40a2fa87fdd`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old. Outputs/bindings: (none).
Calls/effect boundaries: old.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[6].body[8].body[0].value.values[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6].body[9]::Assign

Source: `infra/agentinfra/context_cache.py:167`; AST `1bf217790ac368b5810c584609fa5417cde6b66d8a6e2aebaf2a6f38c3cb4008`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path, self. Outputs/bindings: _, digest.
Calls/effect boundaries: self._consistent_digest.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[6].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6].body[9].value::Call

Source: `infra/agentinfra/context_cache.py:167`; AST `4e95ee5049f4a1c2efdc65c66dc2aac9331a7e2f11b7d4dc3ab774e03ccaff0b`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, self. Outputs/bindings: (none).
Calls/effect boundaries: self._consistent_digest.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[6].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6].body[10]::Return

Source: `infra/agentinfra/context_cache.py:168`; AST `1c3e70e8312465372b71f9e225a80c42a4d501c688315e66e59f0aa30c679a67`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dependencies_fresh, digest, old. Outputs/bindings: (none).
Calls/effect boundaries: old.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Return evaluation at root.body[19].body[6].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6].body[10].value.values[1].values[0].comparators[0]::Call

Source: `infra/agentinfra/context_cache.py:170`; AST `e109a6b9ee3c1053d0e79aff8fe217f8057e64fdc2c9330701abdfcc88f838e0`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old. Outputs/bindings: (none).
Calls/effect boundaries: old.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[6].body[10].value.values[1].values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6].body[10].value.values[3]::Call

Source: `infra/agentinfra/context_cache.py:172`; AST `e109a6b9ee3c1053d0e79aff8fe217f8057e64fdc2c9330701abdfcc88f838e0`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old. Outputs/bindings: (none).
Calls/effect boundaries: old.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[6].body[10].value.values[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_file::root.body[19].body[6].body[10].value.values[5]::Call

Source: `infra/agentinfra/context_cache.py:174`; AST `4fb3a5911bd983b4ec9afe9ec799d6c80c7b45ca228668cf483ee40a2fa87fdd`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old. Outputs/bindings: (none).
Calls/effect boundaries: old.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[6].body[10].value.values[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7]::FunctionDef

Source: `infra/agentinfra/context_cache.py:178`; AST `1e697ebcd8fe9dd5083bd08b351d61d51e2c15504792311c3518db6656c28395`.

Rust module: `infra::agentinfra::context_cache`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ValueError, _now, _source_key, bool, conclusion, current, data, fingerprint, float, int, isinstance, key, math, provenance, redact_text, self, source, str, timedelta, ttl_seconds, valid_until. Outputs/bindings: current, data, key, valid_until.
Calls/effect boundaries: (current + timedelta(seconds=ttl_seconds)).isoformat, ValueError, _now, _source_key, current.isoformat, fingerprint.strip, isinstance, math.isfinite, redact_text, self._save, self.load, self.lock.acquire, self.lock.release, source.strip, timedelta.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[19].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7].body[0]::If

Source: `infra/agentinfra/context_cache.py:187`; AST `2f657bb8ee37a32b95235ba88be9dea3a84a5f097fc4476b6ff9c828536e4e73`.

Rust module: `infra::agentinfra::context_cache`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ValueError, fingerprint, isinstance, source, str. Outputs/bindings: (none).
Calls/effect boundaries: ValueError, fingerprint.strip, isinstance, source.strip.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered If evaluation at root.body[19].body[7].body[0]; no call, error or mutation may be omitted. Condition: not isinstance(source, str) or not source.strip() or (not isinstance(fingerprint, str)) or (not fingerprint.strip())
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7].body[0].test.values[0].operand::Call

Source: `infra/agentinfra/context_cache.py:187`; AST `3b86f2c1f450d24761975c1d54a80e1cee6372c27b85a463f1fb371cd3c3feb3`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, source, str. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[7].body[0].test.values[0].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7].body[0].test.values[1].operand::Call

Source: `infra/agentinfra/context_cache.py:187`; AST `8728e9ef3433c2e49e893585e309fdd95b34589962ef1409841298c55eb25db8`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: source. Outputs/bindings: (none).
Calls/effect boundaries: source.strip.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[7].body[0].test.values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7].body[0].test.values[2].operand::Call

Source: `infra/agentinfra/context_cache.py:187`; AST `46856f9f33ab3fcb2f1bdda328fcf76bc5b6c48ff0735b4227087025c431a94e`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fingerprint, isinstance, str. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[7].body[0].test.values[2].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7].body[0].test.values[3].operand::Call

Source: `infra/agentinfra/context_cache.py:187`; AST `d7f85fc8443d164f4dd8fed509bbb1954a664e81c6203bc30dbde3435e3d0c82`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fingerprint. Outputs/bindings: (none).
Calls/effect boundaries: fingerprint.strip.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[7].body[0].test.values[3].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7].body[0].body[0]::Raise

Source: `infra/agentinfra/context_cache.py:188`; AST `3904707e4493feed002e61d599e9aff7924504eba5212e8d96f46285b0dec852`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ValueError. Outputs/bindings: (none).
Calls/effect boundaries: ValueError.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Raise evaluation at root.body[19].body[7].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7].body[0].body[0].exc::Call

Source: `infra/agentinfra/context_cache.py:188`; AST `aa89e22240a14792f97d31b50d522ed62bf155f1ea4a828445528a41436902d6`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ValueError. Outputs/bindings: (none).
Calls/effect boundaries: ValueError.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[7].body[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7].body[1]::If

Source: `infra/agentinfra/context_cache.py:189`; AST `81c22eeeb554f222bc3eedd3cf17eb7eac807d82946c6405aebf895a4f89bb20`.

Rust module: `infra::agentinfra::context_cache`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ValueError, bool, float, int, isinstance, math, ttl_seconds. Outputs/bindings: (none).
Calls/effect boundaries: ValueError, isinstance, math.isfinite.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered If evaluation at root.body[19].body[7].body[1]; no call, error or mutation may be omitted. Condition: ttl_seconds is not None and (isinstance(ttl_seconds, bool) or not isinstance(ttl_seconds, (int, float)) or (not math.isfinite(ttl_seconds)) or (ttl_seconds < 0))
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7].body[1].test.values[1].values[0]::Call

Source: `infra/agentinfra/context_cache.py:190`; AST `bc9ec95dfc3655ed9c26a7aac2ffdbc3d4c09529dff02c137cc0782bc88cb95a`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, isinstance, ttl_seconds. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[7].body[1].test.values[1].values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7].body[1].test.values[1].values[1].operand::Call

Source: `infra/agentinfra/context_cache.py:191`; AST `0688dca24a4011b987249e98f4d5da237cfc8949a96c6fbcde756e7b11b4a6a5`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: float, int, isinstance, ttl_seconds. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[7].body[1].test.values[1].values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7].body[1].test.values[1].values[2].operand::Call

Source: `infra/agentinfra/context_cache.py:192`; AST `ff109fe3e66be5e423b8207a66d8ed930f5d9af1b4bda8adadd6276160ca12d9`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: math, ttl_seconds. Outputs/bindings: (none).
Calls/effect boundaries: math.isfinite.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[7].body[1].test.values[1].values[2].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7].body[1].body[0]::Raise

Source: `infra/agentinfra/context_cache.py:195`; AST `70a614cf5baab9c2de4000c9d3c9d6a2f6a1156d90a75a28896fa293451aad59`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ValueError. Outputs/bindings: (none).
Calls/effect boundaries: ValueError.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Raise evaluation at root.body[19].body[7].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7].body[1].body[0].exc::Call

Source: `infra/agentinfra/context_cache.py:195`; AST `30650b90f3ef138ad1e2f8ff31a42f35487830a292da059371f907fe56837a36`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ValueError. Outputs/bindings: (none).
Calls/effect boundaries: ValueError.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[7].body[1].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7].body[2]::If

Source: `infra/agentinfra/context_cache.py:196`; AST `944dc2d3210e8baa43042b9747d7ecd43d8d2ed9b457b0d755910d7fdba64dfe`.

Rust module: `infra::agentinfra::context_cache`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ValueError, provenance. Outputs/bindings: (none).
Calls/effect boundaries: ValueError.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered If evaluation at root.body[19].body[7].body[2]; no call, error or mutation may be omitted. Condition: provenance not in {'caller-asserted', 'http-etag', 'content-sha256', 'versioned-source'}
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7].body[2].body[0]::Raise

Source: `infra/agentinfra/context_cache.py:197`; AST `468c50b8c6ea5a36c012caa0f1ee4044332af564094b38dca82adae70f82bab1`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ValueError. Outputs/bindings: (none).
Calls/effect boundaries: ValueError.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Raise evaluation at root.body[19].body[7].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7].body[2].body[0].exc::Call

Source: `infra/agentinfra/context_cache.py:197`; AST `ba548e19862df9978a3548801c87908bda6f14eda6b66eff248f4929a70da377`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ValueError. Outputs/bindings: (none).
Calls/effect boundaries: ValueError.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[7].body[2].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7].body[3]::Assign

Source: `infra/agentinfra/context_cache.py:198`; AST `7d743ad94f856d6c1b9d7adb1a3cdeeebd50d16b3d5eacb98fca0516af7a9ec4`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _now. Outputs/bindings: current.
Calls/effect boundaries: _now.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[7].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7].body[3].value::Call

Source: `infra/agentinfra/context_cache.py:198`; AST `a45c2ac57befcf1212794e7c42a7aad7870de2198eba961b8d2f47b37f928f0f`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _now. Outputs/bindings: (none).
Calls/effect boundaries: _now.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[7].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7].body[4]::Assign

Source: `infra/agentinfra/context_cache.py:199`; AST `9210b6d85ffc8d2b8a2bfdb3d10f3212a5f67cbdff3e632a803823bd8d79d034`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current, timedelta, ttl_seconds. Outputs/bindings: valid_until.
Calls/effect boundaries: (current + timedelta(seconds=ttl_seconds)).isoformat, timedelta.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[7].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7].body[4].value.body::Call

Source: `infra/agentinfra/context_cache.py:199`; AST `a54d9bb2b424a6c416d1159b1b0e98d6d5cd6017680f1ebd5ce26c76665a91ec`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current, timedelta, ttl_seconds. Outputs/bindings: (none).
Calls/effect boundaries: (current + timedelta(seconds=ttl_seconds)).isoformat, timedelta.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[7].body[4].value.body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7].body[4].value.body.func.value.right::Call

Source: `infra/agentinfra/context_cache.py:199`; AST `c8ab7095682ca8e3ce0bb6ebe14e84f2ff40517e5aa6d063e76d4665787b9f0f`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: timedelta, ttl_seconds. Outputs/bindings: (none).
Calls/effect boundaries: timedelta.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[7].body[4].value.body.func.value.right; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7].body[5]::Assign

Source: `infra/agentinfra/context_cache.py:200`; AST `00c16cf6e4b5d77b383cae489ce3afd46f20a0c284d4603a87adcc818d95bb6f`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _source_key, source. Outputs/bindings: key.
Calls/effect boundaries: _source_key.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[7].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7].body[5].value::Call

Source: `infra/agentinfra/context_cache.py:200`; AST `c603d95385de37a575affb7fb7cd77da3c2585acc7debe83182eda0bc015e7c6`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _source_key, source. Outputs/bindings: (none).
Calls/effect boundaries: _source_key.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[7].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7].body[6]::Expr

Source: `infra/agentinfra/context_cache.py:201`; AST `0e311ceac884a90dfdabd855c70d5b78193fef9fcb47613639d4c89049fa7b18`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.lock.acquire.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[7].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7].body[6].value::Call

Source: `infra/agentinfra/context_cache.py:201`; AST `835ba501008cc8885bd889a8fad52e6a4b87965e27f757cf5d9b7c014ac190e9`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.lock.acquire.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[7].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7].body[7]::Try

Source: `infra/agentinfra/context_cache.py:202`; AST `24e7d93795fc0b58c980963532acc9f7fa5bdb53611adaa1a01107524c9e1860`.

Rust module: `infra::agentinfra::context_cache`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: conclusion, current, data, fingerprint, key, provenance, redact_text, self, source, valid_until. Outputs/bindings: data.
Calls/effect boundaries: current.isoformat, redact_text, self._save, self.load, self.lock.release.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Try evaluation at root.body[19].body[7].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7].body[7].body[0]::Assign

Source: `infra/agentinfra/context_cache.py:203`; AST `50b892d2585db987722e6aede6ac50be76f346921c72be68b99e3d5028a335af`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: data.
Calls/effect boundaries: self.load.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[7].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7].body[7].body[0].value::Call

Source: `infra/agentinfra/context_cache.py:203`; AST `2f7b1542b904a22e99e3302fee96f8ab07261aa40c719345db0fafa2aed323fd`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.load.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[7].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7].body[7].body[1]::Assign

Source: `infra/agentinfra/context_cache.py:204`; AST `fa6de57efa843b0f91155dc2ed79a1ad2418c75f494edf6e8b90b59dc7c0f012`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: conclusion, current, data, fingerprint, key, provenance, redact_text, source, valid_until. Outputs/bindings: (none).
Calls/effect boundaries: current.isoformat, redact_text.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[7].body[7].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7].body[7].body[1].value.values[5]::Call

Source: `infra/agentinfra/context_cache.py:210`; AST `8c39afb7de67447382726c270666bc2a6e3650639e72f1badecdb141996b4099`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: conclusion, redact_text. Outputs/bindings: (none).
Calls/effect boundaries: redact_text.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[7].body[7].body[1].value.values[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7].body[7].body[1].value.values[6]::Call

Source: `infra/agentinfra/context_cache.py:211`; AST `cf19bc4ef32dc88cdb40a8d123ee67468cf1c9f16ca3831c6c3f83ca79fee890`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: current. Outputs/bindings: (none).
Calls/effect boundaries: current.isoformat.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[7].body[7].body[1].value.values[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7].body[7].body[2]::Expr

Source: `infra/agentinfra/context_cache.py:214`; AST `dab24004df007d3fab18fe8f8a3d672b270bc56729e3c5b36b4158bc20c37d0b`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: data, self. Outputs/bindings: (none).
Calls/effect boundaries: self._save.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[7].body[7].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7].body[7].body[2].value::Call

Source: `infra/agentinfra/context_cache.py:214`; AST `8ebfa7986579ca006ae588c0cd261918f6965304c8eb2fb03ec2d47d54c0fd82`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data, self. Outputs/bindings: (none).
Calls/effect boundaries: self._save.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[7].body[7].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7].body[7].body[3]::Return

Source: `infra/agentinfra/context_cache.py:215`; AST `92daa78d8f02e52fa6cadb21edea654a0d2b1afa9fd252e346f4959645323db5`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: data, key. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Return evaluation at root.body[19].body[7].body[7].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7].body[7].finalbody[0]::Expr

Source: `infra/agentinfra/context_cache.py:217`; AST `50795522f731c697d7e2cab3a3003d5a9415cac791c6b4a635917bf2159ceac4`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.lock.release.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[7].body[7].finalbody[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_external::root.body[19].body[7].body[7].finalbody[0].value::Call

Source: `infra/agentinfra/context_cache.py:217`; AST `fda84b64bf236157e2f4744fc88aca42822337862c351b2c52b5e9a5ee54e621`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.lock.release.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[7].body[7].finalbody[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_external::root.body[19].body[8]::FunctionDef

Source: `infra/agentinfra/context_cache.py:219`; AST `24bfe951349eae9424df8da5b87c0daf643ef4cf6b97de69dbb9c55f1a1fa68e`.

Rust module: `infra::agentinfra::context_cache`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: _now, _parse, _source_key, bool, fingerprint, fingerprint_fresh, fresh, old, reason, self, source, str, ttl_fresh, until. Outputs/bindings: fingerprint_fresh, fresh, old, reason, ttl_fresh, until.
Calls/effect boundaries: _now, _parse, _source_key, bool, old.get, self.load, self.load()['sources'].get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[19].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_external::root.body[19].body[8].body[0]::Assign

Source: `infra/agentinfra/context_cache.py:220`; AST `d18d271041b93461cf2bc0050926df6d12f106e1b843ccb47f039b189be15cc8`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _source_key, self, source. Outputs/bindings: old.
Calls/effect boundaries: _source_key, self.load, self.load()['sources'].get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_external::root.body[19].body[8].body[0].value::Call

Source: `infra/agentinfra/context_cache.py:220`; AST `9fdc9f2dc138b16e5cb500107e25efc9d0d0c343b5f26f215ba998a92f8b1e68`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _source_key, self, source. Outputs/bindings: (none).
Calls/effect boundaries: _source_key, self.load, self.load()['sources'].get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[8].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_external::root.body[19].body[8].body[0].value.func.value.value::Call

Source: `infra/agentinfra/context_cache.py:220`; AST `2f7b1542b904a22e99e3302fee96f8ab07261aa40c719345db0fafa2aed323fd`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.load.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[8].body[0].value.func.value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_external::root.body[19].body[8].body[0].value.args[0]::Call

Source: `infra/agentinfra/context_cache.py:220`; AST `c603d95385de37a575affb7fb7cd77da3c2585acc7debe83182eda0bc015e7c6`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _source_key, source. Outputs/bindings: (none).
Calls/effect boundaries: _source_key.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[8].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_external::root.body[19].body[8].body[1]::If

Source: `infra/agentinfra/context_cache.py:221`; AST `d90876318e259eb8cfcb429fc7b3220c3f4ae16bce1e8eafda5773e696f7194a`.

Rust module: `infra::agentinfra::context_cache`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: old, source. Outputs/bindings: (none).
Calls/effect boundaries: old.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered If evaluation at root.body[19].body[8].body[1]; no call, error or mutation may be omitted. Condition: not old or old.get('source') != source
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_external::root.body[19].body[8].body[1].test.values[1].left::Call

Source: `infra/agentinfra/context_cache.py:221`; AST `776677d1d20c6b9cb86643d1b4caca5cbd233468bffb50cad4a479a4c8d6c4ab`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old. Outputs/bindings: (none).
Calls/effect boundaries: old.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[8].body[1].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_external::root.body[19].body[8].body[1].body[0]::Return

Source: `infra/agentinfra/context_cache.py:222`; AST `a618bbff4813bc2cb08c56098a9653ee60d1ff28d7ae28c345192bff765d25c0`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Return evaluation at root.body[19].body[8].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_external::root.body[19].body[8].body[2]::Assign

Source: `infra/agentinfra/context_cache.py:223`; AST `affb20e3417b4f2448ebbd734f00a29c0ac8797074005c647da289461f772d29`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _parse, old. Outputs/bindings: until.
Calls/effect boundaries: _parse, old.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[8].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_external::root.body[19].body[8].body[2].value::Call

Source: `infra/agentinfra/context_cache.py:223`; AST `2bddd5cfd60d8dae18ae5d232184db23eb872ac50922c47637df566f0931c6e7`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _parse, old. Outputs/bindings: (none).
Calls/effect boundaries: _parse, old.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[8].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_external::root.body[19].body[8].body[2].value.args[0]::Call

Source: `infra/agentinfra/context_cache.py:223`; AST `fe92875c18a1732cc8eb67fc589b65a38dd85b68154c6d80980b61a1185e29d2`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old. Outputs/bindings: (none).
Calls/effect boundaries: old.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[8].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_external::root.body[19].body[8].body[3]::Assign

Source: `infra/agentinfra/context_cache.py:224`; AST `9a484fcf836cad0b2ecbc016dc0fde8728f80875c2b868cb6f46b0fb39dcbfc8`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _now, until. Outputs/bindings: ttl_fresh.
Calls/effect boundaries: _now.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[8].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_external::root.body[19].body[8].body[3].value.values[1].left::Call

Source: `infra/agentinfra/context_cache.py:224`; AST `a45c2ac57befcf1212794e7c42a7aad7870de2198eba961b8d2f47b37f928f0f`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _now. Outputs/bindings: (none).
Calls/effect boundaries: _now.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[8].body[3].value.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_external::root.body[19].body[8].body[4]::Assign

Source: `infra/agentinfra/context_cache.py:225`; AST `36e7a6d51f6db52f03fe84227c102d86e9b183a4b25305982a804a0fc4f82fe3`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fingerprint, old. Outputs/bindings: fingerprint_fresh.
Calls/effect boundaries: old.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[8].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_external::root.body[19].body[8].body[4].value.values[1].comparators[0]::Call

Source: `infra/agentinfra/context_cache.py:225`; AST `98d600860cad981d3c0dd482541d338125074255dc6d7e8b7f4d0e024bbc7a06`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old. Outputs/bindings: (none).
Calls/effect boundaries: old.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[8].body[4].value.values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_external::root.body[19].body[8].body[5]::If

Source: `infra/agentinfra/context_cache.py:226`; AST `4410b47155313ea9da84daef56ad3ceb90cf86b9d7209e1af07337bbbf4b2ca9`.

Rust module: `infra::agentinfra::context_cache`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: bool, fingerprint, fingerprint_fresh, fresh, old, ttl_fresh, until. Outputs/bindings: fresh, reason.
Calls/effect boundaries: bool, old.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered If evaluation at root.body[19].body[8].body[5]; no call, error or mutation may be omitted. Condition: fingerprint is None
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_external::root.body[19].body[8].body[5].body[0]::Assign

Source: `infra/agentinfra/context_cache.py:227`; AST `3f962d1318a5a4be8ad3bea057462f2e0d3219b5f93fbd026fe493ba9636a561`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, old, ttl_fresh, until. Outputs/bindings: fresh.
Calls/effect boundaries: bool, old.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[8].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_external::root.body[19].body[8].body[5].body[0].value.values[2]::Call

Source: `infra/agentinfra/context_cache.py:227`; AST `a5d61f8b0b752d990fae9bc5b07673658d5105e473383bc78cd42ca3fe51eab4`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, old. Outputs/bindings: (none).
Calls/effect boundaries: bool, old.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[8].body[5].body[0].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_external::root.body[19].body[8].body[5].body[0].value.values[2].args[0]::Call

Source: `infra/agentinfra/context_cache.py:227`; AST `c8b54c689fc9706a00b186cd34324003b303ad3c2f8ba6f8c644c2d47ec9b73c`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old. Outputs/bindings: (none).
Calls/effect boundaries: old.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[8].body[5].body[0].value.values[2].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_external::root.body[19].body[8].body[5].body[1]::Assign

Source: `infra/agentinfra/context_cache.py:228`; AST `7684b87fd7e05723870bed52c9854e65ac120cc6c34bc85d3e8cb1f492c9133a`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fresh. Outputs/bindings: reason.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[8].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_external::root.body[19].body[8].body[5].orelse[0]::Assign

Source: `infra/agentinfra/context_cache.py:230`; AST `517ea876c252eac4906a67e0efdfb82a1cce8e282c2f63d91a9cfc64eda881bc`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fingerprint_fresh, ttl_fresh. Outputs/bindings: fresh.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[8].body[5].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_external::root.body[19].body[8].body[5].orelse[1]::Assign

Source: `infra/agentinfra/context_cache.py:231`; AST `b9cc837c062c068fa572258e85711cc5dcd329ee31ad32fca52ccdaa35376433`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fresh. Outputs/bindings: reason.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[8].body[5].orelse[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_external::root.body[19].body[8].body[6]::Return

Source: `infra/agentinfra/context_cache.py:232`; AST `bb511dc4f68c2639ca0149afd1a7b9859ae0d72ffc49bae3128cf616e4af3870`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bool, fresh, old, reason. Outputs/bindings: (none).
Calls/effect boundaries: bool, old.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Return evaluation at root.body[19].body[8].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_external::root.body[19].body[8].body[6].value.values[3]::Call

Source: `infra/agentinfra/context_cache.py:236`; AST `98d600860cad981d3c0dd482541d338125074255dc6d7e8b7f4d0e024bbc7a06`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old. Outputs/bindings: (none).
Calls/effect boundaries: old.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[8].body[6].value.values[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_external::root.body[19].body[8].body[6].value.values[4]::Call

Source: `infra/agentinfra/context_cache.py:237`; AST `fe92875c18a1732cc8eb67fc589b65a38dd85b68154c6d80980b61a1185e29d2`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old. Outputs/bindings: (none).
Calls/effect boundaries: old.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[8].body[6].value.values[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_external::root.body[19].body[8].body[6].value.values[5]::Call

Source: `infra/agentinfra/context_cache.py:238`; AST `a5d61f8b0b752d990fae9bc5b07673658d5105e473383bc78cd42ca3fe51eab4`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, old. Outputs/bindings: (none).
Calls/effect boundaries: bool, old.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[8].body[6].value.values[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_external::root.body[19].body[8].body[6].value.values[5].args[0]::Call

Source: `infra/agentinfra/context_cache.py:238`; AST `c8b54c689fc9706a00b186cd34324003b303ad3c2f8ba6f8c644c2d47ec9b73c`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old. Outputs/bindings: (none).
Calls/effect boundaries: old.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[8].body[6].value.values[5].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::check_external::root.body[19].body[8].body[6].value.values[6]::Call

Source: `infra/agentinfra/context_cache.py:239`; AST `4fb3a5911bd983b4ec9afe9ec799d6c80c7b45ca228668cf483ee40a2fa87fdd`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old. Outputs/bindings: (none).
Calls/effect boundaries: old.get.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[8].body[6].value.values[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_log_summary::root.body[19].body[9]::FunctionDef

Source: `infra/agentinfra/context_cache.py:242`; AST `920777f3d954bee95001ecc4f792cae3ddbc5b63354b319c885fc90280e1c6c1`.

Rust module: `infra::agentinfra::context_cache`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: _now, bytes, data, dict, digest, failure_region, hashlib, len, raw, redact_text, self, source, str, summary. Outputs/bindings: data, digest, summary.
Calls/effect boundaries: _now, _now().isoformat, hashlib.sha256, hashlib.sha256(raw).hexdigest, hashlib.sha256(source.encode()).hexdigest, len, redact_text, self._save, self.load, self.lock.acquire, self.lock.release, source.encode.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered FunctionDef evaluation at root.body[19].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_log_summary::root.body[19].body[9].body[0]::Assign

Source: `infra/agentinfra/context_cache.py:243`; AST `c92d648ecb277adc9e8d34b4417176989d414fa1412b988dae832d88d942e3b9`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: hashlib, raw. Outputs/bindings: digest.
Calls/effect boundaries: hashlib.sha256, hashlib.sha256(raw).hexdigest.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_log_summary::root.body[19].body[9].body[0].value::Call

Source: `infra/agentinfra/context_cache.py:243`; AST `b2be9b0451b94a2347162e04938f05c00da073ca3aaaae4aa70ead50cd8ba516`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: hashlib, raw. Outputs/bindings: (none).
Calls/effect boundaries: hashlib.sha256, hashlib.sha256(raw).hexdigest.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[9].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_log_summary::root.body[19].body[9].body[0].value.func.value::Call

Source: `infra/agentinfra/context_cache.py:243`; AST `12a456a8f0e7527180fbb5dcc3b4806f8d3efd8bed365b9c2a0b6d8c2c0a98ba`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: hashlib, raw. Outputs/bindings: (none).
Calls/effect boundaries: hashlib.sha256.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[9].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_log_summary::root.body[19].body[9].body[1]::Assign

Source: `infra/agentinfra/context_cache.py:244`; AST `ca5b2743e05ecd35967fdf961ce29885cc4e10f7353e81e9b4de7d7bd17f2312`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _now, digest, failure_region, len, raw, redact_text, source. Outputs/bindings: summary.
Calls/effect boundaries: _now, _now().isoformat, len, redact_text.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[9].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_log_summary::root.body[19].body[9].body[1].value.values[3]::Call

Source: `infra/agentinfra/context_cache.py:248`; AST `14381ee198b233fab86e0cefdac3169f8ede2b4f94479d019dcd9cc290015a66`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, raw. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[9].body[1].value.values[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_log_summary::root.body[19].body[9].body[1].value.values[4]::Call

Source: `infra/agentinfra/context_cache.py:249`; AST `a6b29600b0e839f46da2af5db065f25a70739514c8f748a24399843c37db3934`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: failure_region, redact_text. Outputs/bindings: (none).
Calls/effect boundaries: redact_text.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[9].body[1].value.values[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_log_summary::root.body[19].body[9].body[1].value.values[5]::Call

Source: `infra/agentinfra/context_cache.py:250`; AST `d3f9e407bb5c13d6be1e67ea02303b2a5ab2eeb3ff1f26c7056d7250b26ab317`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _now. Outputs/bindings: (none).
Calls/effect boundaries: _now, _now().isoformat.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[9].body[1].value.values[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_log_summary::root.body[19].body[9].body[1].value.values[5].func.value::Call

Source: `infra/agentinfra/context_cache.py:250`; AST `a45c2ac57befcf1212794e7c42a7aad7870de2198eba961b8d2f47b37f928f0f`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _now. Outputs/bindings: (none).
Calls/effect boundaries: _now.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[9].body[1].value.values[5].func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_log_summary::root.body[19].body[9].body[2]::Expr

Source: `infra/agentinfra/context_cache.py:252`; AST `0e311ceac884a90dfdabd855c70d5b78193fef9fcb47613639d4c89049fa7b18`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.lock.acquire.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[9].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_log_summary::root.body[19].body[9].body[2].value::Call

Source: `infra/agentinfra/context_cache.py:252`; AST `835ba501008cc8885bd889a8fad52e6a4b87965e27f757cf5d9b7c014ac190e9`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.lock.acquire.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[9].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_log_summary::root.body[19].body[9].body[3]::Try

Source: `infra/agentinfra/context_cache.py:253`; AST `e9dbb39734e77ff586207d965b9f074dc15c0bee4740a9c6cd9c0f7dbd80d080`.

Rust module: `infra::agentinfra::context_cache`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: data, hashlib, self, source, summary. Outputs/bindings: data.
Calls/effect boundaries: hashlib.sha256, hashlib.sha256(source.encode()).hexdigest, self._save, self.load, self.lock.release, source.encode.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Try evaluation at root.body[19].body[9].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_log_summary::root.body[19].body[9].body[3].body[0]::Assign

Source: `infra/agentinfra/context_cache.py:254`; AST `50b892d2585db987722e6aede6ac50be76f346921c72be68b99e3d5028a335af`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: data.
Calls/effect boundaries: self.load.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[9].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_log_summary::root.body[19].body[9].body[3].body[0].value::Call

Source: `infra/agentinfra/context_cache.py:254`; AST `2f7b1542b904a22e99e3302fee96f8ab07261aa40c719345db0fafa2aed323fd`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.load.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[9].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_log_summary::root.body[19].body[9].body[3].body[1]::Assign

Source: `infra/agentinfra/context_cache.py:255`; AST `8893123e5525f76869284bf56c3e549c4c6a36d17dc5da4d9df12169222ddb87`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: data, hashlib, source, summary. Outputs/bindings: (none).
Calls/effect boundaries: hashlib.sha256, hashlib.sha256(source.encode()).hexdigest, source.encode.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[9].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_log_summary::root.body[19].body[9].body[3].body[1].targets[0].slice.right::Call

Source: `infra/agentinfra/context_cache.py:255`; AST `e7853b030ced898aa7e88c4e62fb7c3159f2ce5efcb1e2839bd11b3fd473e256`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: hashlib, source. Outputs/bindings: (none).
Calls/effect boundaries: hashlib.sha256, hashlib.sha256(source.encode()).hexdigest, source.encode.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[9].body[3].body[1].targets[0].slice.right; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_log_summary::root.body[19].body[9].body[3].body[1].targets[0].slice.right.func.value::Call

Source: `infra/agentinfra/context_cache.py:255`; AST `08e1a90cf497463ad3ba3131a0de0335cdcedb7baa96d901fe955962cc9f5ed9`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: hashlib, source. Outputs/bindings: (none).
Calls/effect boundaries: hashlib.sha256, source.encode.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[9].body[3].body[1].targets[0].slice.right.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_log_summary::root.body[19].body[9].body[3].body[1].targets[0].slice.right.func.value.args[0]::Call

Source: `infra/agentinfra/context_cache.py:255`; AST `f3fa2d2638bdb55874d2c58f2328ea47d95274d3181a61c652d0f86827271c77`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: source. Outputs/bindings: (none).
Calls/effect boundaries: source.encode.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[9].body[3].body[1].targets[0].slice.right.func.value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_log_summary::root.body[19].body[9].body[3].body[2]::Expr

Source: `infra/agentinfra/context_cache.py:256`; AST `dab24004df007d3fab18fe8f8a3d672b270bc56729e3c5b36b4158bc20c37d0b`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: data, self. Outputs/bindings: (none).
Calls/effect boundaries: self._save.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[9].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_log_summary::root.body[19].body[9].body[3].body[2].value::Call

Source: `infra/agentinfra/context_cache.py:256`; AST `8ebfa7986579ca006ae588c0cd261918f6965304c8eb2fb03ec2d47d54c0fd82`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data, self. Outputs/bindings: (none).
Calls/effect boundaries: self._save.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[9].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_log_summary::root.body[19].body[9].body[3].body[3]::Return

Source: `infra/agentinfra/context_cache.py:257`; AST `4372a6c34fb998f6d8860fe4f7b81721c80d17d0bf1aa5380c6eb26f47db976f`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: summary. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Return evaluation at root.body[19].body[9].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_log_summary::root.body[19].body[9].body[3].finalbody[0]::Expr

Source: `infra/agentinfra/context_cache.py:259`; AST `50795522f731c697d7e2cab3a3003d5a9415cac791c6b4a635917bf2159ceac4`.

Rust module: `infra::agentinfra::context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.lock.release.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[9].body[3].finalbody[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/context_cache.py::module::ContextLedger::record_log_summary::root.body[19].body[9].body[3].finalbody[0].value::Call

Source: `infra/agentinfra/context_cache.py:259`; AST `fda84b64bf236157e2f4744fc88aca42822337862c351b2c52b5e9a5ee54e621`.

Rust module: `infra::agentinfra::context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.lock.release.
Dependencies: __future__, atomic, datetime, hashlib, json, locks, math, os, pathlib, paths, security, typing.

Invariants: Preserve ordered Call evaluation at root.body[19].body[9].body[3].finalbody[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
